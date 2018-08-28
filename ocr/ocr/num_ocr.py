import os
import time

from ocr_stat import StatHandler
from ocr_config import OCRConf
from ocr_loger import OCRLoger
from ocr_thread import OcrThread
import ocr_http

'''
NumOCR:识别
'''
class NumOCR:

    def __init__(self):
        pass

    def StartOCR(self):
        # scheduler = BackgroundScheduler()
        # scheduler.add_job(fun1, 'interval', seconds=2)
        # scheduler.start()

        # scheduler = BlockingScheduler()
        # scheduler.add_job(self.get_pics, 'interval', seconds=2)
        # scheduler.start()

        # while True:
        self.DoTask()
            # time.sleep(OCRConf.Tick)
        # pass

    # 一次任务
    def DoTask(self):
        # 时间戳,秒
        ts = int(time.time())
        # 获取吃鸡房间在线列表
        roomlist = ocr_http.get_room_info()
        print(roomlist)
        # 遍历列表,生成任务列表
        taskList = []
        for room in roomlist:
            roomInfo = {
                "id": room["id"],                   # 房间id
                "room_number": room["room_number"], # 房间number
                "stream": room["stream"],           # 房间流名
                "survivors": -1,                    # 生存人数，-1表示失败，不上报
                "ts":ts                             # 时间戳
            }
            taskList.append(roomInfo)
        # 开启线程执行任务
        num = len(taskList)
        start = 0
        while num > 0:
            th_num = num                     # 线程数
            if th_num > OCRConf.MaxThreads:  # 如果线程数大于最大线程数
                th_num = OCRConf.MaxThreads

            # 启动线程，加入线程列表
            threads = []
            for ind in range(start,start+th_num): # 启动线程，传入对应房间信息
                th_name = "OcrThread-"+str(ind)      # 线程名
                th =  OcrThread(ind,th_name,taskList[ind])
                threads.append(th)
                th.start()

            # 等待线程结束任务
            for th in threads:
                #th.join()
                th.join(OCRConf.DownTimeout) # 线程超时时间为最大下载时间+5秒
                if th.isAlive():
                    OCRLoger.warn("%s: isAlive",th.name)

            # 计算剩余任务
            start += th_num
            num -= th_num

        # 任务执行完毕，上报结果信息
        ocr_http.report_room_info(taskList)
        # 记录统计
        OCRLoger.info("statics:%s", StatHandler)

    # 遍历指定目录，返回png图片列表
    def __eachFile(self,filepath):
        pngList = []
        pathDir = os.listdir(filepath)
        for allDir in pathDir:
            child = os.path.join('%s%s' % (filepath, allDir))
            if ".png" in child:
                pngList.append(child)
        return pngList


def PrintInfo():
    OCRLoger.info('Version:%s' % OCRConf.Version)
    OCRLoger.info('ConfPath:%s' % OCRConf.ConfPath)
    OCRLoger.info('LogPath:%s' % OCRConf.LogPath)
    OCRLoger.info('RoomInfoAddr:%s' % OCRConf.RoomInfoAddr)
    OCRLoger.info('ReportStatAddr:%s' % OCRConf.ReportStatAddr)
    OCRLoger.info('MaxThreads:%d' % OCRConf.MaxThreads)
    OCRLoger.info('SavePic:%d' % OCRConf.SavePic)
    OCRLoger.info('PicPath:%s' % OCRConf.PicPath)
    OCRLoger.info('Tick:%d' % OCRConf.Tick)
    OCRLoger.info('FFmpegPath:%s' % OCRConf.FFmpegPath)
    OCRLoger.info('DownTimeout:%d' % OCRConf.DownTimeout)

if __name__ == '__main__':
    # 初始化配置文件
    OCRConf.ParseCmdLines()
    PrintInfo()
    # 启动OCR识别
    numOCR = NumOCR()
    numOCR.StartOCR()

