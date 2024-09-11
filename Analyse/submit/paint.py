import sys
import pickle
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import numpy as np

sys.path.append("../")


def paint(title: str, name: str = '', height=(1400, 10)):
    data = pickle.load(open(f'{title}{name}_ac.pkl', 'rb'))
    tot, ac, cnta, cntw = data['tot'], data['ac'], data['cnta'], data['cntw']
    while data['pid'][0].startswith('Sh'):
        data['pid'].pop(0)
        tot.pop(0)
        ac.pop(0)
        cnta.pop(0)
        cntw.pop(0)
    tot, ac, cnta, cntw = np.array(tot), np.array(ac), np.array(cnta), np.array(cntw)
    # print(data)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    x = np.arange(len(data['pid'])) * 4
    dx = 0.9

    ax1.set_xlabel('pid')
    ax1.set_ylabel('pass/fail')
    ax1.bar(x, height[0], width=dx, color=(0, 0, 0, 0))
    ax1.bar(x - dx * 1.1, tot, width=dx, label='failed', color='brown')
    ax1.bar(x - dx * 1.1, ac, width=dx, label='passed', color='darkgreen')
    ax1.legend(loc='upper center')

    ax2 = ax1.twinx()
    ax2.set_ylabel('average attempts needed')
    ax2.bar(x, height[1], width=dx, color=(0, 0, 0, 0))
    ax2.bar(x + dx * 1.1, cntw / (tot - ac + 1e-8), width=dx, label='attempts till fail', color='rosybrown')
    ax2.bar(x, cnta / (ac + 1e-8), width=dx, tick_label=data['pid'], label='attempts to pass', color='cadetblue')

    plt.legend()
    plt.savefig(f"../../Output/ac/{name}/overview{title}.png")
    plt.show()


cls = '2118'
for t in ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6']:
    paint(t, cls, (30, 10))
