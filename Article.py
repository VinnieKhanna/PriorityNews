import datetime
import numpy
import math

class Article:
    def __init__(self, url, publishedAt, readability):
        self.url = url
        self.publishedAt = publishedAt

        if readability <= 55:
            self.readabilityScore = 15 - (55 - readability)
        elif readability > 55 and readability <= 75:
            self.readabilityScore = 15
        elif readability > 75:
            self.readabilityScore = 15 - (readability - 75)

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
        self.rankScore = 0

    def setRealProb(self, realProbability):
        self.realProb = realProbability

    def equateRank(self):
        real = self.realProb
        readability = self.readabilityScore
        time = self.timeSincePublished
        self.rankScore = real * real * readability * 3 * ((numpy.arctan(-1.2 * (time/24 - 3))) + 3 * math.pi/2)
