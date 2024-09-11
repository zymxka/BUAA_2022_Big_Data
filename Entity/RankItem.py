class RankItem:
    contName = None
    rank = None
    studentId = None
    score = None
    penalty = None
    results = None

    def __init__(self, contName, rank, studentId, score, penalty, results):
        self.contName = contName
        self.rank = rank
        self.studentId = studentId
        self.score = score
        self.penalty = penalty
        self.results = results

    def toString(self):
        return self.contName + " " + str(self.rank) + " " + self.studentId + " " + self.score + " " + self.penalty + " " + str(self.results)