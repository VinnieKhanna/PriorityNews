import datetime
class Article:
    def __init__(self, url, publishedAt, readability):
        self.url = url
        self.publishedAt = publishedAt
        self.readabilityScore = readability
        now = datetime.datetime.now()
        # publishDateTime = datetime() #2020-10-17T20:40:13Z
        # self.timeSincePublished =
        self.realProb = 0

    def setRealProb(self, realProbability):
        self.realProb = realProbability
