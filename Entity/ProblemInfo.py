class Probleminfo:
    def __init__(self, proid, title, author, propeople, prosubmit):
        self.proid = str(proid)
        self.title = str(title)
        self.author = str(author)
        psplit = propeople.split("/")
        self.peoplepass = str(psplit[0])
        self.peoplesum = str(psplit[1])
        ssplit = prosubmit.split("/")
        self.submitpass = str(psplit[0])
        self.submitsum = str(ssplit[1])

    def printpro(self):
        return self.proid+" "+self.title+" "+self.author+" "+self.peoplepass+" "+self.peoplesum+" "+self.submitpass+" "+self.submitsum