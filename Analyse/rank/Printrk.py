import matplotlib.pyplot as plt
import openpyxl
import numpy as np
from scipy.ndimage import gaussian_filter1d


def getpic(mycolor):
    rkinfo = openpyxl.load_workbook("sturk.xlsx")['排名']
    test = [1, 3, 5, 7, 9, 11, 12]
    exe = [2, 4, 6, 8, 10, 13]
    v = [0 for _ in range(31)]
    for item in list(rkinfo.rows)[1:]:
        y = []
        for idx, cell in enumerate(item):
            if idx not in exe:
                continue
            # print(idx)
            y.append(cell.value)
        # print(y[0])
        vary = np.var(y)
        print(vary)
        idx = int(vary/10000)+1
        if idx > 30:
            idx = 30
        v[idx] += 1
    y_smoothed = gaussian_filter1d(v, sigma=1)
    y_smoothed[0]=0
    x = [10000*i for i in range(31)]
    plt.plot(x, y_smoothed, color=mycolor[0], linewidth=1, alpha=1)
    plt.show()


def getpersonpic(mycolor):
    rkinfo = openpyxl.load_workbook("sturk.xlsx")['排名']
    x = []
    for item in list(rkinfo.rows)[0][1:]:
        if item.value[0] == 'E':
            continue
        x.append(item.value)
    print(x)
    test = [1, 3, 5, 7, 9, 11, 12]
    for item in list(rkinfo.rows)[1:]:
        y = []
        darw = True
        for idx, cell in enumerate(item):
            if idx not in test:
                continue
            #print(idx)
            if cell.value == 1499:
                darw = False
                break
            y.append(cell.value)
        if not darw:
            continue
        #print(y[0])
        vary = np.mean(y)
        idx = int(vary // 300)
        if idx != 2:
            continue
        #idx = 1
        plt.plot(x, y, color=mycolor[idx], linewidth=0.5, alpha=0.6)
    plt.show()


if __name__ == "__main__":
    color = ['#F1948A', '#C39BD3', '#85C1E9', '#7DCEA0', '#F7DC6F', '#5499C7']
    getpic(color)
