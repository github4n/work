'''
导入threading lock，线程安全
'''
import threading

'''
Statistics:统计
'''
class Statistics:

    __TotalNum = 0      # 总数
    __MatchNum = 0      # 匹配数
    __CorrectNum = 0    # 匹配正确数

    def __init__(self):
        self.__TotalNum = 0
        self.__MatchNum = 0
        self.__CorrectNum = 0
        self.__Lock = threading.Lock()
    def __del__(self):
        pass
    # 总数
    def TotalIncr(self):
        with self.__Lock:
            self.__TotalNum  += 1
    def GetTotalNum(self):
        with self.__Lock:
            return self.__TotalNum
    # 匹配数
    def MatchIncr(self):
        with self.__Lock:
            self.__MatchNum += 1
    def GetMatchNum(self):
        with self.__Lock:
            return self.__MatchNum
    # 匹配正确数
    def CorrectIncr(self):
        with self.__Lock:
            self.__CorrectNum += 1
    def GetCorrectNum(self):
        with self.__Lock:
            return self.__CorrectNum
    # 获取统计数:小数,匹配率\正确率\失败率\错误率
    def GetStat(self):
        with self.__Lock:
            __TotalNum, __MatchNum, __CorrectNum = self.__TotalNum,self.__MatchNum,self.__CorrectNum
        MatchRatio=CorrectRatio=FailedRatio=IncorrectRatio = 0.0
        if __TotalNum > 0:
            MatchRatio = __MatchNum  / __TotalNum     # 匹配率 = 匹配数/总数
            if __MatchNum > 0:
                CorrectRatio = __CorrectNum / __MatchNum  # 正确率 = 正确数/匹配数
            FailedRatio = 1 - MatchRatio              # 失败率
            IncorrectRatio = 1 - CorrectRatio         # 错误率
        return (MatchRatio, CorrectRatio, FailedRatio, IncorrectRatio)

    # 统计打印
    def __str__(self):
        with self.__Lock:
            __TotalNum, __MatchNum, __CorrectNum = self.__TotalNum,self.__MatchNum,self.__CorrectNum
        ratio = self.GetStat()
        MatchRatio,CorrectRatio,FailedRatio,IncorrectRatio = ratio[0],ratio[1],ratio[2],ratio[3]
        FailedNum = __TotalNum - __MatchNum
        IncrrectNum = __MatchNum - __CorrectNum
        strNum = "--TotalNum:%d,MatchNum:%d,CorrectNum:%d,FailedNum:%d,IncorrectNum:%d" % (__TotalNum,__MatchNum,__CorrectNum,FailedNum,IncrrectNum)
        strRatio = "--MatchRatio:%f,CorrectRatio:%f,FailedRatio:%f,IncorrectRatio:%f" % (MatchRatio,CorrectRatio,FailedRatio,IncorrectRatio)
        str = strNum + strRatio
        return str

    def __repr__ (self):
        with self.__Lock:
            __TotalNum, __MatchNum, __CorrectNum = self.__TotalNum,self.__MatchNum,self.__CorrectNum
        ratio = self.GetStat()
        MatchRatio,CorrectRatio,FailedRatio,IncorrectRatio = ratio[0],ratio[1],ratio[2],ratio[3]
        FailedNum = __TotalNum - __MatchNum
        IncrrectNum = __MatchNum - __CorrectNum
        strNum = "--TotalNum:%d,MatchNum:%d,CorrectNum:%d,FailedNum:%d,IncorrectNum:%d" % (__TotalNum,__MatchNum,__CorrectNum,FailedNum,IncrrectNum)
        strRatio = "--MatchRatio:%f,CorrectRatio:%f,FailedRatio:%f,IncorrectRatio:%f" % (MatchRatio,CorrectRatio,FailedRatio,IncorrectRatio)
        str = strNum + strRatio
        return str

# 单例,from stat import stat_singleton使用
StatHandler = Statistics()