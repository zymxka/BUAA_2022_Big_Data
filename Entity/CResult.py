class CResult:
    """
    表单上单题结果
    """
    # 作答类型
    """
    0:未作答
    1:完全错误
    2:部分错误
    3:正确
    """
    rType = None
    # 作答时间
    rTime = None
    # 错误次数
    rWrong = None

    def __init__(self, rtype, rtime, rwrong):
        self.rType = rtype
        self.rTime = rtime
        self.rWrong = rwrong