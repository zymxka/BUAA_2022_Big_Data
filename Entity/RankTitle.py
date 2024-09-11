class RankTitle:
    contName = None
    rankTitle = "排名"
    studentIdTitle = "学号"
    scoreTitle = "得分"
    penaltyTitle = "罚时"
    resultTitles = None

    def __init__(self, contName, resultTitles):
        self.contName = contName
        self.resultTitles = resultTitles