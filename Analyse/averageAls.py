"""
对每次比赛平均分的分析
"""

import openpyxl
from config import AnalyseConfig
from sqlbox import SqlBox

def calculateAvg():
    workbook1 = openpyxl.load_workbook(AnalyseConfig.rankXlsx)
    workbook2 = openpyxl.load_workbook(AnalyseConfig.studentXlsx)
    sheet0 = workbook2["学生信息"]
    sqlbox0 = SqlBox(sheet0)

    for sheet in workbook1:
        sqlbox = SqlBox(sheet)
        bk = sqlbox0.LinkWith(sqlbox.filter({"得分": "95"}, 2), "成员id", "学号").orderBy(["right.排名"]).choose(["left.学号", "left.昵称", "right.得分", "right.罚时"]).ModifyHead({"left.学号": "学号", "left.昵称": "姓名", "right.得分": "得分", "right.罚时": "罚时"}).value
        # bk = sqlbox.filter({"得分": "101"}).value
        for value in bk:
            print(value)
        break