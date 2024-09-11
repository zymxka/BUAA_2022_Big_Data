# -*- coding: utf-8 -*-

import openpyxl
import matplotlib.pyplot as plt
from result import problems1, problems2, problems3, problems4, problems5, problems6, problem
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
color = ['#F1948A', '#C39BD3', '#AED6F1', '#A3E4D7', '#F9E79F', '#EDBB99', '#ABB2B9']


def pie_chart():
    a1 = []
    b1 = []
    for key in problems3[1]:
        a1.append(key)
        b1.append(problems2[1][key])
    a1.pop()
    a1.pop()
    b1.pop()
    b1.pop()
    plt.figure(figsize=(6, 6))
    explode = (0, 0, 0, 0, 0, 0, 0)
    plt.pie(b1, colors=color,
            explode=explode,
            labels=a1,
            shadow=False,
            autopct="%1.1f%%",
            labeldistance=1,
            startangle=90,
            pctdistance=0.6)
    plt.axis('equal')
    plt.legend()
    plt.savefig("pie_chart/思维型题目")


def pass_():
    a1 = ["简单题", "含有数据范围等易错点的题目", "简单算法类题目", "思维型题目", "难题", "防AK题"]
    b1 = [0.968, 0.748, 0.780, 0.121, 0.742, 0]
    b2 = [0.972, 0.788, 0.914, 0.205, 0.833, 0]
    b3 = [0.875, 0.540, 0.540, 0.192, 0.643, 0]

    # 绘图（在一个刻度的两边分别绘制两条柱状图）
    width = 0.18  # 设置一个固定宽度
    p1 = [i - 0.2 for i in range(len(a1))]
    p2 = [i for i in range(len(a1))]
    p3 = [i + 0.2 for i in range(len(a1))]

    plt.bar(p1, b1, width=width, label='1', color=color[0])
    plt.bar(p2, b2, width=width, label='2', color=color[1])
    plt.bar(p3, b3, width=width, label='3', color=color[2])

    # 设置刻度
    plt.xticks(range(len(a1)), a1)

    # 设置坐标标签
    plt.xlabel('题目种类')
    plt.ylabel('通过率')

    for i in range(0,6):
        plt.text(p1[i]-0.08, b1[i]+0.01, str(b1[i]))
    for i in range(0,6):
        plt.text(p2[i]-0.08, b2[i]+0.01, str(b2[i]))
    for i in range(0,6):
        plt.text(p3[i]-0.08, b3[i]+0.01, str(b3[i]))

    # 设置图例
    plt.legend()
    # 展示
    plt.show()


def accuracy():
    a1 = ["简单题", "含有数据范围等易错点的题目", "简单算法类题目", "思维型题目", "难题", "防AK题"]
    b1 = [0.623, 0.253, 0.266, 0.049, 0.215, 0]
    b2 = [0.483, 0.355, 0.355, 0.094, 0.444, 0]
    b3 = [0.606, 0.216, 0.216, 0.062, 0.175, 0]

    # 绘图（在一个刻度的两边分别绘制两条柱状图）
    width = 0.18  # 设置一个固定宽度
    p1 = [i - 0.2 for i in range(len(a1))]
    p2 = [i for i in range(len(a1))]
    p3 = [i + 0.2 for i in range(len(a1))]

    plt.bar(p1, b1, width=width, label='1', color=color[0])
    plt.bar(p2, b2, width=width, label='2', color=color[1])
    plt.bar(p3, b3, width=width, label='3', color=color[2])

    # 设置刻度
    plt.xticks(range(len(a1)), a1)

    # 设置坐标标签
    plt.xlabel('题目种类')
    plt.ylabel('正确率')

    for i in range(0,6):
        plt.text(p1[i]-0.08, b1[i]+0.01, str(b1[i]))
    for i in range(0,6):
        plt.text(p2[i]-0.08, b2[i]+0.01, str(b2[i]))
    for i in range(0,6):
        plt.text(p3[i]-0.08, b3[i]+0.01, str(b3[i]))


    # 设置图例
    plt.legend()
    # 展示
    plt.show()


def duiji():
    a1 = ["简单题", "含有数据范围等易错点的题目", "简单算法类题目", "思维型题目", "难题", "防AK题"]
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    for pro in problem:
        b1.append(pro["AC"])
        b2.append(pro["CE"])
        b3.append(pro["OE"])
        b4.append(pro["PE"])
        b5.append(pro["RE"])
        b6.append(pro["TLE"])
        b7.append(pro["WA"])
    # 堆积柱状图
    b1 = np.array(b1)
    b2 = np.array(b2)
    b3 = np.array(b3)
    b4 = np.array(b4)
    b5 = np.array(b5)
    b6 = np.array(b6)
    b7 = np.array(b7)

    plt.bar(a1, b1, color=color[0], label='AC')
    plt.bar(a1, b2, bottom=b1, color=color[1], label='CE')
    plt.bar(a1, b3, bottom=b1 + b2, color=color[2], label='OE')
    plt.bar(a1, b4, bottom=b1 + b2 + b3, color=color[3], label='PE')
    plt.bar(a1, b5, bottom=b1 + b2 + b3 + b4, color=color[4], label='RE')
    plt.bar(a1, b6, bottom=b1 + b2 + b3 + b4 + b5, color=color[5], label='TLE')
    plt.bar(a1, b7, bottom=b1 + b2 + b3 + b4 + b5 + b6, color=color[6], label='WA')
    # 添加图例
    plt.legend(loc='upper right')
    plt.grid(axis='y', color='gray', linestyle=':', linewidth=2)
    plt.savefig("各种结果数量堆积图")
    plt.show()


if __name__ == "__main__":
    pass_()
