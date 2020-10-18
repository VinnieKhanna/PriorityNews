import datetime
import numpy
class Article:
    def __init__(self, url, publishedAt, readability):
        self.url = url
        self.publishedAt = publishedAt
        if readability <= 55:
            self.readabilityScore = 15 - (55 - readability)
        elif readability > 55 and readability <= 75:
            self.readabilityScore = 0

        self.readabilityScore = readability
        now = datetime.datetime.utcnow()
        year = int(publishedAt[0:4])
        month = int(publishedAt[5:7])
        day = int(publishedAt[8:10])
        hour = int(publishedAt[11:13])
        minute = int(publishedAt[14:16])
        second = int(publishedAt[17:19])
        publishDateTime = datetime.datetime(year, month, day, hour, minute, second) #2020-10-17T20:40:13Z
        self.timeSincePublished = (now - publishDateTime).total_seconds() / 3600
        self.realProb = 0

    def setRealProb(self, realProbability):
        self.realProb = realProbability

    def equateRank(self):
        real = self.realProb
        readability = self.readabilityScore
        # real * real * readability * 3 * numpy.arctan()
