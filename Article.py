import datetime
class Article:
    def __init__(self, url, publishedAt, readability, realFake):
        self.url = url
        self.publishedAt = publishedAt
        self.readabilityScore = readability
        self.realProbability = realFake
        now = datetime.datetime.now()
        publishDateTime = datetime() #2020-10-17T20:40:13Z
        self.timeSincePublished =
