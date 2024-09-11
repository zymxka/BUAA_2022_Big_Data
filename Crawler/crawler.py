from selenium import webdriver
from config import CrawlerConfig
from MyDriver import MyDriver
from zymDriver import zymDriver
from DataSave.savexls import saveRankXls, saveSubmitXls, SaveProinfo, SaveProsubmit, SaveProdetail, saveStudentXls


def crawlerRank(myDriver):
    myDriver.openContestPage()
    rankTitle, rankInfos = myDriver.getContestRank()
    saveRankXls(rankTitle, rankInfos)


def crawlerSubmit(myDriver):
    myDriver.openContestPage()
    submitInfos = myDriver.getSubmits()
    saveSubmitXls(submitInfos, CrawlerConfig.contestName)

def crawlerStudent(myDriver):
    studentInfos = myDriver.getStudentInfo()
    saveStudentXls(studentInfos)


def crawlerProinfo(myDriver):
    prosinfo = myDriver.getProSubmitSum(15)
    SaveProinfo(prosinfo)


def crawlerProSub(myDriver):
    # 把这些修改成对应比赛的所有题目的编号
    proset = [5470, 5457, 5450, 5428, 5449, 5440, 5391, 5415, 5473, 5425, 5476]
    for item in proset:
        prosubmits = myDriver.getProSubmit(item)
        # 下面的地址修改成需要保存的文件（需要事先在table文件夹创建同名文件）
        SaveProsubmit(prosubmits, str(item), "../Table/C3.xlsx")


def crawlerProdetail(myDriver):
    ans = myDriver.getProinfo(5359, 5742)
    SaveProdetail(ans, "../Table/Proinfo.xlsx", "题目信息")


if __name__ == '__main__':

    myDriver = MyDriver(CrawlerConfig.driverPath)

    myDriver.openPage()
    myDriver.login()

    # crawlerRank(myDriver)
    crawlerSubmit(myDriver)
    # crawlerStudent(myDriver)

    '''
    myDriver = zymDriver(CrawlerConfig.zympath)
    myDriver.openPage()
    myDriver.login()
    crawlerProdetail(myDriver)
    '''
