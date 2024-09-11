#-*- coding: utf-8 -*-

import openpyxl
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def passTimeChange2():
    workbook = openpyxl.load_workbook("../../Table/rank.xlsx")
    color = ['#F1948A', '#ABB2B9']
    index1 = 0
    d = {}
    for sheet in workbook:
        for row in sheet.iter_rows(min_row=2, max_row=1450, min_col=1, max_col=15):
            p = d.setdefault(row[1].value, 0)
            for i in row:
                if i.value == True:
                    p += 1
            d[row[1].value] = p
    a = []
    for key in d:
        a.append(d.get(key))
    n=plt.hist(x=a,  # 指定绘图数据
             bins=7,  # 指定直方图中条块的个数
             color=color[index1],  # 指定直方图的填充色
             edgecolor='black'  # 指定直方图的边框色
             )
    print(n)
    plt.xlabel("通过题目数量")
    plt.ylabel("人数")
    y=[165,294,512,332,125,32,3]
    plt.text(8, 166,str(165))
    plt.text(29, 295,str(294))
    plt.text(47, 513,str(512))
    plt.text(65, 333,str(332))
    plt.text(85, 126,str(125))
    plt.text(105, 33,str(32))
    plt.text(126,4,str(3))
    plt.title("通过题目数量分布")
    plt.savefig("通过数量分布")
    plt.show()

if __name__ == "__main__":
    passTimeChange2()
