import logging
import logging.handlers
import logging.config
import yaml
from ocr_config import OCRConf

'''
OCRLoger:日志对象
'''
# 读取yaml日志配置
with open(OCRConf.LogPath, 'r') as log_conf:
    dict_conf = yaml.load(log_conf)

# dictConfig
logging.config.dictConfig(dict_conf)

# 日志对象
OCRLoger = logging.getLogger("OCRLog")