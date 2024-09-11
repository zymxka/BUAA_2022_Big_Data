import json
import shlex
from collections import defaultdict
from bs4 import BeautifulSoup
import json as js

from selenium import webdriver

from Entity.SubmitItem import SubmitItem
from config import CrawlerConfig
from Entity.ProblemInfo import Probleminfo
import pandas as pd


class zymDriver:
    driver = None

    def __init__(self, location):
        self.driver = webdriver.Chrome(location)

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

    # 获取题目和ID的对应关系
    def getProSubmitSum(self, page):
        prosinfo = []
        for i in range(1, page + 1):
            self.driver.get("https://accoding.buaa.edu.cn:4000/problem/index?page=" + str(i))
            proitems = self.driver.find_elements_by_css_selector("tbody>tr")
            print(len(proitems))
            for j in range(3, len(proitems)):
                item = proitems[j]
                proinfo = item.find_elements_by_css_selector("td")
                proid = proinfo[1].text
                protitle = proinfo[2].text
                proauthor = proinfo[4].find_element_by_css_selector("a").get_attribute("href")[39:44]
                propeople = proinfo[6].text
                prosubmit = proinfo[7].text
                prosinfo.append(Probleminfo(proid, protitle, proauthor, propeople, prosubmit))
        self.driver.quit()
        return prosinfo

    # 获取某次比赛题目的所有提交信息
    def getProSubmit(self, proid):
        data = pd.read_excel('../Table/problem.xlsx', sheet_name='题目提交信息', usecols="A,F")
        df = defaultdict()
        # print(data)
        for idx, item in data.iterrows():
            df[item[0]] = item[-1]
        tol = df[proid]
        submitInfos = []
        for i in range(0, tol, 15):
            self.driver.get(CrawlerConfig.ojWebsite + "problem/" + str(proid) + "/submission?offset=" + str(i))
            proitems = self.driver.find_elements_by_css_selector("tbody>tr")
            # print(len(proitems))
            for j in range(1, len(proitems)):
                item = proitems[j]
                itemInfos = item.find_elements_by_css_selector("td")
                probId = itemInfos[0].text
                userName = itemInfos[1].find_element_by_css_selector("a").get_attribute("href")[39:44]
                result = itemInfos[2].text
                score = itemInfos[3].text
                codeLen = itemInfos[5].text
                runTime = itemInfos[6].text
                memory = itemInfos[7].text
                itemInfos[8].click()
                _time = itemInfos[8].find_element_by_css_selector("label").text
                while _time == "":
                    itemInfos[8].click()
                    _time = itemInfos[8].find_element_by_css_selector("label").text
                # print(_time)
                submitItem = SubmitItem(probId, userName, result, score, codeLen, runTime, memory, _time)
                submitInfos.append(submitItem)
        print(len(submitInfos))
        # print(submitInfos)
        return submitInfos

    def getProinfo(self, pros, proe):
        ans = []
        for pro in range(pros, proe + 1):
            self.driver.get("https://accoding.buaa.edu.cn:4000/problem/" + str(pro) + "/edit")
            tags = self.driver.find_elements_by_id("difficulty")
            if len(tags) == 0:
                continue
            bsObj = BeautifulSoup(self.driver.page_source, 'html.parser')
            bsElems = bsObj.find_all('script')
            d = "var my_pre_tags"
            for item in bsElems:
                # print(type(item.string))
                if str(item.string) is not None:
                    if str(item.string).find(d) != -1:
                        diff = tags[-1].get_attribute("_value")
                        content = [str(pro), str(diff)]
                        s = str(item.string)
                        idx = s.find("{\"id\"")
                        while idx != -1:
                            start = idx
                            end = s.find("}}", idx)
                            idx = s.find("{\"id\"", end+2)
                            tmpjs = json.loads(s[start:end+2])
                            content.append(tmpjs.get("content"))
                        ans.append(content)
                        print(content)
        print(len(ans))
        print(ans)
        return ans
