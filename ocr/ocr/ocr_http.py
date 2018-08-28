import sys
import time
from hashlib import md5
from ocr_loger import OCRLoger
from ocr_config import OCRConf
import requests
import json

# 密钥
KeyStr = "EU*T*)*(#23ssdfd"


# 下载文件
def http_get(url):
    fname = "test.png"
    path = os.path.join('%s%s' % (OCRConf.PicPath, fname))
    r = requests.get(url, stream=True)
    with open(path, "wb") as savefile:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                savefile.write(chunk)
    pass

# 生成url
def GenUrl(httpAddr,payload):
    # 取keys，降序
    keys = []
    for (key, val) in payload.items():
        keys.append(key)
    keys.sort(reverse=True)
    # 根据降序keys生成vals
    vals = ""
    for key in keys:
        vals += payload[key]
    vals += KeyStr
    # MD5生成token
    m = md5()
    m.update(vals.encode("utf-8"))
    payload["token"] = m.hexdigest()
    # 生成URL
    args = ""
    for (key,val) in payload.items():
        if len(args) > 0:
            args += "&" + key + "=" + val
        else:
            args += "?" + key + "=" + val
    http_url = httpAddr + args

    return http_url

# 生成token
def GetToken(payload):
    # 取keys，降序
    keys = []
    for (key, val) in payload.items():
        keys.append(key)
    keys.sort(reverse=True)
    # 根据降序keys生成vals
    vals = ""
    for key in keys:
        vals += payload[key]
    vals += KeyStr
    # MD5生成token
    m = md5()
    m.update(vals.encode("utf-8"))
    payload["token"] = m.hexdigest()

# 获取当前在播房间信息
def get_room_info():
    # 参数
    ts = time.time()            # 参数：time 时间戳
    get_type = "battlegrounds"  # 参数：type 类型
    payloads = {
        "time":str(int(ts)),
        "type":get_type
    }

    # 请求
    roomList = []
    try:
        # 生成请求url
        #http_url = GenUrl(OCRConf.RoomInfoAddr, payloads)
        #OCRLoger.debug("get_room_info:http_url:%s", http_url)
        #resp = requests.get(http_url,params=payloads, verify=False)

        # 生成token
        GetToken(payloads)
        OCRLoger.debug("get_room_info:%s,payloads:%s", OCRConf.RoomInfoAddr,payloads)
        resp = requests.get(OCRConf.RoomInfoAddr,params=payloads,verify=False)

        # 解析
        try:
            Geted = False
            resJson = resp.json()
            if "code" in resJson.keys():
                code = resJson["code"]
                if code == "200":
                    if "data" in resJson.keys():
                        roomList = resJson["data"]
                        Geted = True
            # 未获取到信息，记录日志
            if not Geted:
                OCRLoger.error("get_room_info failed,res:%s", resJson)
        except:
            OCRLoger.error("get_room_info exception:type:%s,msg:%s,resp.text:%s", sys.exc_info()[0],sys.exc_info()[1],resp.text)
    except:
        OCRLoger.error("get_room_info exception:type:%s,msg:%s",sys.exc_info()[0],sys.exc_info()[1])

    OCRLoger.debug("roomList:%s", roomList)
    return roomList

def report_room_info(infoList):
    OCRLoger.debug("report_room_info infoList:%s",str(infoList))
    rInfoList = []
    # 遍历信息列表，生成上报列表
    for info in infoList:
        # if info["survivors"] < 0:
        #     # 小于0 为失败的任务，剔除
        #     pass
        # else:
        #     pass
        rInfo = {
            "id": info["id"],                   # 房间id
            "room_number": info["room_number"], # 房间number
            "survivors": info["survivors"]      # 生存人数，-1：表示失败，前端不展示
        }
        rInfoList.append(rInfo)

    # 如果上报列表有元素，则上报
    if len(rInfoList) > 0:
        # GET参数
        ts = time.time()  # 参数：time 时间戳
        get_type = "battlegrounds"  # 参数：type 类型
        payloads = {
            "time": str(int(ts)),
            "type": get_type
        }
        # 生成token
        GetToken(payloads)

        # POST内容
        reportInfo = {
            "info":rInfoList
        }
        # 生成json string
        content = json.dumps(reportInfo)
        post_data = {
            "report":content
        }
        # POST 上报
        try:
            resp = requests.post(OCRConf.ReportStatAddr, params=payloads, data=post_data,verify=False)
            OCRLoger.debug("report_room_info:%s,params:%s,post_data:%s", OCRConf.ReportStatAddr, str(payloads), str(post_data))
            # 解析
            try:
                Reported = False
                resJson = resp.json()
                if "code" in resJson.keys():
                    code = resJson["code"]
                    if code == "200":
                        # 上报成功
                        Reported = True
                # 上报失败，记录日志
                if  not Reported:
                    OCRLoger.error("report_room_info report failed,resJson:%s", resJson)
            except:
                OCRLoger.error("report_room_info exception:type:%s,msg:%s,resp.text:%s", sys.exc_info()[0], sys.exc_info()[1], resp.text)
        except:
            OCRLoger.error("report_room_info exception:type:%s,msg:%s", sys.exc_info()[0],sys.exc_info()[1])
    else:
        OCRLoger.debug("report_room_info rInfoList is null")