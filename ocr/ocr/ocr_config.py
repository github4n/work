import argparse
import configparser
import os

'''
OCRConfig:配置
'''
class OCRConfig:

    Version = "num_ocr[1.0.0.0]"    # 版本号
    ConfPath = './num_ocr.conf'     # config配置文件路径
    LogPath = './num_ocr.yml'       # log yaml配置文件路径

    RoomInfoAddr = ""               # 获取吃鸡所有在线房间信息地址
    ReportStatAddr = ""             # 上报吃鸡状态信息地址

    Tick = 30                       # 任务间隔时间
    MaxThreads = 10                 # 最大线程数
    SavePic = 0                     # 是否保存截图
    PicPath = ""                    # 截图存放路径
    FFmpegPath = ""                 # ffmpeg路径
    DownTimeout = 10                # ffmpeg 下载超时时间

    def __init__(self):
        pass
    def __del__(self):
        pass
    # 解析命令行
    def ParseCmdLines(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-c","--conf",nargs=1,default=self.ConfPath,required=False)
        parser.add_argument("-log","--log", nargs=1, default=self.LogPath, required=False)
        args = parser.parse_args()
        self.ConfPath = args.conf
        self.ParseConfig()
        self.LogPath = args.log
    # 解析配置文件
    def ParseConfig(self):
        cfg = configparser.ConfigParser()
        cfg.read(self.ConfPath,encoding="utf-8")

        self.RoomInfoAddr = cfg.get("base","room_info_addr",fallback="http://127.0.0.1")
        self.ReportStatAddr = cfg.get("base","report_stat_addr",fallback="http://127.0.0.1")
        self.FFmpegPath = cfg.get("base","ffmpeg_path",fallback="D:/tools/ffmpeg/bin/ffmpeg")
        self.DownTimeout = cfg.getint("base","down_timeout",fallback=10)

        self.MaxThreads = cfg.getint("base","max_threads",fallback=10)
        self.SavePic = cfg.getint("base","save_pic",fallback=0)
        self.PicPath = cfg.get("base","pic_path",fallback="E:/OCR/pics/ocrpics/")
        self.Tick = cfg.getint("base","tick",fallback=25)

        self.MakeDir()
    # 创建图片目录(如果目录不存在)
    def MakeDir(self):
        if len(self.PicPath) > 0:
            if os.path.exists(self.PicPath) is not True:
                os.makedirs(self.PicPath)
# 单例,from config import OCRConf
OCRConf = OCRConfig()