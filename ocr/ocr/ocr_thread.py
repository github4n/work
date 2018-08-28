import threading
import os
import subprocess
import sys
import time

from PIL import Image
import cv2
import pytesseract

from ocr_stat import StatHandler
from ocr_config import OCRConf
from ocr_loger import OCRLoger

PIC_EXT = ".jpg"

class OcrThread (threading.Thread):
    def __init__(self, threadID, name,rInfo):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.info = rInfo
    def run(self):
        # 下载(ffmpeg截图)
        pic = self.GetPic()
        # 裁剪
        print(len(pic), os.path,os.path.isfile(pic))
        if len(pic) > 0 and os.path.isfile(pic): # 如果文件存在
            img = self.ClipPicture(pic)
            if img is not None:
                # 识别
                res = self.cv_gray_2(pic, img)
                retNum, matched = res[0], res[1]

                # 是否匹配成功
                if matched:
                    # 判断识别数字是否正确
                    if retNum > 0 and retNum <= 100:
                        StatHandler.CorrectIncr()   # 统计：正确数+1
                        # 记录识别结果到info
                        self.info["survivors"] = retNum
                        # 删除原图, 识别出来的图，删除原图
                        #os.remove(pic)
                    else:
                        # 识别错误
                        pass

                # 保存裁剪的图片，保留用于验证
                room_number = self.info["room_number"]
                ts = self.info["ts"]
                survs = self.info["survivors"]
                pic_name = str(ts) + "_room" + room_number + "(" + str(survs) + ")" + PIC_EXT  # 例：1524537754_room_100.png
                pic_path = os.path.join(OCRConf.PicPath, pic_name)
                #cv2.imwrite(pic_path, img)
                if OCRConf.SavePic != 0:
                    # 保存
                    cv2.imwrite(pic_path, img)
                else:
                    # 删除原图
                    pass
                    # os.remove(pic)
            else:
                # 裁剪失败,已记录日志
                pass
        else:
            # 下载失败，超时,已记录日志
            pass


    # 调用ffmpeg 截图并保存
    def GetPic(self):
        pic = ""
        # try:
        #     stream_name = self.info["stream"]
        #     room_number = self.info["room_number"]
        #     ts = self.info["ts"]
        #
        #     pic_name = str(ts) + "_room" + room_number + PIC_EXT # 例：1524537754_room_100.jpg
        #     pic_path = os.path.join(OCRConf.PicPath,pic_name)
        #     #ffmpeg = OCRConf.FFmpegPath + ''' -analyzeduration 0 -i http://live-tx-hdl.huomaotv.cn/live/''' + stream_name + '''.flv -f image2 -vframes 1 -s 1920x1080 -y ''' + pic_path
        #     ffmpeg = [OCRConf.FFmpegPath, '-analyzeduration', '0', '-i', 'http://live-tx-hdl.huomaotv.cn/live/' + stream_name + '.flv', '-f', 'image2', '-vframes','1', '-s', '1920x1080', '-y', pic_path]
        #     OCRLoger.debug("%s.GetPic ffmpeg:%s",self.name,ffmpeg)
        #     # 下载并等待结束
        #     #result = self.command(cmd=ffmpeg, timeout=OCRConf.DownTimeout)
        #     self.commandWithTimeout(cmd=ffmpeg, timeout=OCRConf.DownTimeout)
        #
        #     if os.path.isfile(pic_path):
        #         pic = pic_path
        #     else:
        #         OCRLoger.warn("%s.GetPic %s  is not exist (download failed)", self.name, pic_name)
        # except:
        #     OCRLoger.error("%s.GetPic exception:type: %s,msg:%s",self.name, sys.exc_info()[0],sys.exc_info()[1])
        # return r'Z:/share/ocr/ocr/pics/ocrpics/12345.jpg'
        return r'Z:\share\ocr\ocr\pics\ocrpics\1532511101_room130957.jpg'

    # 裁剪指定图片
    def ClipPicture(self,fname):
        try:
            img = cv2.imread(fname)
            size = img.shape
            hei, wid = size[0],size[1]
            if wid == 1920 and hei == 1080:
                # 1920*1080 固定裁剪区域:box = (1784, 30, 1820, 66)
                left, top, right, bottom= 1784, 30, 1820, 66
                # 裁剪
                crop_img = img[top:bottom, left:right]
                #cv2.imwrite(fname + ".cv2corp.png", crop_img)
                return crop_img
            else:
                OCRLoger.error("%s.ClipPicture fname:%s, wid:%d,hei:%d", self.name, fname,wid,hei)
                return None
        except:
            OCRLoger.error("%s.ClipPicture exception:type: %s,msg:%s", self.name, sys.exc_info()[0], sys.exc_info()[1])

    # opencv转灰度图，降噪，然后二值化
    '''
    返回：(retNum,matched)
    retNum:整型
    matched:bool型
    '''
    def cv_gray_2(self,pic_name,img):
        retNum,matched = 0,False
        StatHandler.TotalIncr() # 统计：总数+1
        # opencv转灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        # 降噪
        dst = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
        # 二值化
        retval, im_th = cv2.threshold(dst, 200, 255, cv2.THRESH_BINARY)
        dstRGB = cv2.cvtColor(im_th, cv2.COLOR_GRAY2RGB)
        # 识别
        im2 = Image.fromarray(dstRGB, "RGB")
        code = pytesseract.image_to_string(im2,lang='num_my',config="--psm 7 digits")
        print(code)
        im2.close()
        if code.isnumeric():

            # 匹配成功
            StatHandler.MatchIncr() # 统计，匹配数+1
            if code == "00":
                code = "100" # 只裁剪了2位数，识别为00的，设置为100
            retNum = int(code)
            matched = True
            OCRLoger.debug("%s.cv_gray_2 %s num_my:%s", self.name, pic_name, code)
        else:
            OCRLoger.debug("%s.cv_gray_2 %s num_my:%s (match failed)", self.name, pic_name,code)
            # 匹配失败不用统计
            pass
        return (retNum,matched)

    # 执行命令行
    def command(self,cmd, timeout=60):
        chp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        t_beginning = time.time()
        seconds_passed = 0
        while True:
            if chp.poll() is not None:
                break
            seconds_passed = time.time() - t_beginning
            if timeout and seconds_passed > timeout:
                chp.kill()
                return None
            time.sleep(0.1)
        return chp.stdout.read()

    # 执行命令， 使用communicate()及时读取管道内容
    def commandWithTimeout(self,cmd,timeout=60):
        proc = subprocess.Popen(cmd,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, shell=False)
        try:
            outs, errs = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            try:
                OCRLoger.warn("%s.commandWithTimeout2 timeout, kill", self.name)
                proc.kill()
                outs, errs = proc.communicate()
            except:
                OCRLoger.error("%s.commandWithTimeout kill exception:type: %s,msg:%s", self.name, sys.exc_info()[0],sys.exc_info()[1])
        except:
            OCRLoger.error("%s.commandWithTimeout exception:type: %s,msg:%s", self.name, sys.exc_info()[0], sys.exc_info()[1])


    # 执行命令,使用run
    def commandWithTimeout2(self,cmd,timeout=60):
        try:
            ret = subprocess.run(cmd,stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL,shell=True, timeout=timeout)
            return ret.stdout
        except subprocess.TimeoutExpired:
            OCRLoger.warn("%s.commandWithTimeout timeout", self.name)
