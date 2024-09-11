class SubmitItem:
    probId = None
    userName = None
    result = None
    score = None
    codeLen = None
    runTime = None
    memory = None
    time = None

    def __init__(self, probId, userName, result, score, codeLen, runTime, memory, time):
        self.probId = probId
        self.userName = userName
        self.result = result
        self.score = score
        self.codeLen = codeLen
        self.runTime = runTime
        self.memory = memory
        self.time = time

    def toString(self):
        return str(self.probId) + " " + self.userName + " " + self.result + " " + self.score + " " + self.codeLen + " " + self.runTime + " " + self.memory + " " + self.time