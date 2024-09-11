import time

from selenium import webdriver
from config import CrawlerConfig
from Entity.CResult import CResult
from Entity.RankItem import RankItem
from Entity.RankTitle import RankTitle
from Entity.SubmitItem import SubmitItem
from Entity.StudentInfo import StudentInfo

class MyDriver:

    driver = None

    def __init__(self, location):
        self.driver = webdriver.Chrome(location)

    # 滑动滚动条至最下
    def scroll(self):
        js = "return action=document.body.scrollHeight"

        height = 0
        new_height = self.driver.execute_script(js)

        while height < new_height:
            for i in range(height, new_height, 800):
                self.driver.execute_script('window.scrollTo(0, {})'.format(i))
                time.sleep(0.5)
            height = new_height
            time.sleep(1)
            new_height = self.driver.execute_script(js)

    # 打开网址
    def openPage(self):
        self.driver.get(CrawlerConfig.ojWebsite)

    # 登录
    def login(self):
        loginBtn = self.driver.find_element_by_id("loginpage")
        loginBtn.click()

        emailInp = self.driver.find_element_by_id("email")
        emailInp.send_keys(CrawlerConfig.email)

        passwdInp = self.driver.find_element_by_id("password")
        passwdInp.send_keys(CrawlerConfig.passwd)

        submitBtn = self.driver.find_element_by_class_name("loginbtn")
        submitBtn.click()

    # 进入比赛
    def openContestPage(self):
        contextBtn = self.driver.find_element_by_id("contestpage")
        contextBtn.click()

        pageIndexBtn = self.driver.find_element_by_id("button"+str(CrawlerConfig.contestPageIndex))
        pageIndexBtn.click()

        linkBtn = self.driver.find_element_by_link_text(CrawlerConfig.contestName)
        linkBtn.click()

    # 获取排名
    def getContestRank(self):
        rankBtn = self.driver.find_element_by_link_text("排名")
        rankBtn.click()

        time.sleep(10)

        resultTitles = []
        titleBar = self.driver.find_element_by_css_selector("thead tr")
        titles = titleBar.find_elements_by_css_selector("td")
        titlelen = len(titles)
        for i in range(0, titlelen - 6):
            resultTitles.append(chr(ord('A') + i))

        rankTitle = RankTitle(CrawlerConfig.contestName, resultTitles)

        rankInfos = []

        for i in range(1, CrawlerConfig.contextRankPageNum + 1):
            pagelink = self.driver.find_element_by_link_text(str(i))
            pagelink.click()

            # time.sleep(10)
            self.scroll()

            rankItems = self.driver.find_elements_by_css_selector("tbody tr")
            length = len(rankItems)
            for i in range(length):
                item = rankItems[i]
                try:
                    itemInfos = item.find_elements_by_css_selector("td")
                    length = len(itemInfos)

                    rank = int(itemInfos[0].text)
                    try:
                        studentId = itemInfos[1].find_element_by_css_selector("a").get_attribute("href")[39:]
                    except Exception:
                        rankItems = self.driver.find_elements_by_css_selector("tbody tr")
                        item = rankItems[i]
                        itemInfos = item.find_elements_by_css_selector("td")
                        studentId = itemInfos[1].find_element_by_css_selector("a").get_attribute("href")[39:]

                    score = itemInfos[4].text
                    penalty = itemInfos[5].text

                    results = []

                    for i in range(6, length):
                        classes = itemInfos[i].get_attribute("class")
                        success = ("success" in classes)
                        results.append(success)

                    rankItem = RankItem(CrawlerConfig.contestName, rank, studentId, score, penalty, results)
                    rankInfos.append(rankItem)
                except Exception:
                    rankItems = self.driver.find_elements_by_css_selector("tbody tr")
                    item = rankItems[i]
                    itemInfos = item.find_elements_by_css_selector("td")
                    length = len(itemInfos)

                    rank = int(itemInfos[0].text)
                    try:
                        studentId = itemInfos[1].find_element_by_css_selector("a").get_attribute("href")[39:]
                    except Exception:
                        rankItems = self.driver.find_elements_by_css_selector("tbody tr")
                        item = rankItems[i]
                        itemInfos = item.find_elements_by_css_selector("td")
                        studentId = itemInfos[1].find_element_by_css_selector("a").get_attribute("href")[39:]
                    score = itemInfos[4].text
                    penalty = itemInfos[5].text

                    results = []

                    for i in range(6, length):
                        classes = itemInfos[i].get_attribute("class")
                        success = ("success" in classes)
                        results.append(success)

                    rankItem = RankItem(CrawlerConfig.contestName, rank, studentId, score, penalty, results)
                    rankInfos.append(rankItem)

        return rankTitle, rankInfos

    # 进入题目
    def openProblemPage(self):
        problemBtn = self.driver.find_element_by_id("problempage")
        problemBtn.click()

        pageIndexBtn = self.driver.find_element_by_id("button"+str(CrawlerConfig.problemPageIndex))
        pageIndexBtn.click()

        linkBtn = self.driver.find_element_by_link_text(str(CrawlerConfig.problemId))
        linkBtn.click()

    # 获取比赛提交记录
    def getSubmits(self):
        submitBtn = self.driver.find_element_by_link_text("提交")
        submitBtn.click()

        time.sleep(5)

        submitInfos = []

        for i in range(1, CrawlerConfig.contextSubmitPageNum + 1):
            pagelink = self.driver.find_element_by_link_text(str(i))
            pagelink.click()

            submitItems = self.driver.find_elements_by_css_selector("tbody tr")
            length = len(submitItems)

            for i in range(length):
                item = submitItems[i]
                itemInfos = item.find_elements_by_css_selector("td")
                probId = itemInfos[1].text
                userName = itemInfos[2].find_element_by_css_selector("a").get_attribute("href")[39:]
                result = itemInfos[3].text
                score = itemInfos[4].text
                codeLen = itemInfos[6].text
                runTime = itemInfos[7].text
                memory = itemInfos[8].text
                _time = itemInfos[9].text

                submitItem = SubmitItem(probId, userName, result, score, codeLen, runTime, memory, _time)

                submitInfos.append(submitItem)

        return submitInfos

    # 获取学生信息列表
    def getStudentInfo(self):
        groupBtn = self.driver.find_element_by_id("grouppage")
        groupBtn.click()

        groupInBtn = self.driver.find_element_by_link_text("2021级-航空航天大类-C语言程序设计")
        groupInBtn.click()

        memberBtn = self.driver.find_element_by_id("group-memberPage")
        memberBtn.click()

        studentInfos = []
        studentItems = self.driver.find_elements_by_css_selector("tbody tr")
        studentItems = studentItems[1:]

        for studentItem in studentItems:
            infos = studentItem.find_elements_by_css_selector("td")
            id = infos[0].find_element_by_css_selector("a").get_attribute("href")[39:-6]
            name = infos[0].text
            sid = infos[1].text
            identity = infos[2].text

            studentInfo = StudentInfo(id, name, sid, identity)
            studentInfos.append(studentInfo)

        return studentInfos