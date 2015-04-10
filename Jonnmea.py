#!/usr/bin/env python3

class Jonnmea:
    def __init__(self, sentence):
        self.sentence = sentence
        self.validTypes = ['GGA', 'RMC']

    def parseSentence(self):
        # $GPxxx
        self.sentenceType = self.sentence[3:6]

        if self.sentenceType not in self.validTypes:
            msg = "Sentence type '{0}' invalid"
            msg = msg.format(self.sentenceType)
            raise ValueError(msg)

        self.nmeaData = self.sentenceStruct(self.sentenceType)
        sentenceData = self.sentence.split(',')

        i = 0;
        for value in sentenceData:
            for key in self.nmeaData:
                if self.nmeaData[key] == i:
                    self.nmeaData[key] = value
            i = i+1


        if self.nmeaData['checkSum']:
            self.nmeaData['checkSum'] = self.sentence.split('*', 1)[1]

        if self.sentenceType == 'RMC':
            self.nmeaData['receiverType'] = self.sentence.split('*', 1)[0].split(',')[-1]

        return self.nmeaData

    def validateChkSum(self):
        chksum = self.sentence.split('*',1)[1]

        # compare int instead
        chksum = int(chksum, 16)

        calc_chksum = 0;
        for i in self.sentence:
            if i == '$':
                calc_chksum = 0
            elif i == '*':
                break
            else:
                calc_chksum ^= ord(i)
        
        calc_chksum = calc_chksum
        if chksum != calc_chksum:
            msg = "Incorrect checksum. Received: {0}, Calculated: {1}"
            msg = msg.format(chksum, calc_chksum)
            print(msg)
            return False

        return True

    def sentenceStruct(self, sType):
        structTypes = {}

        structTypes['GGA'] = {
            'sentenceType'          : 0,
            'fixTimestamp'          : 1,
            'latitude'              : 2,
            'bearingLat'            : 3,
            'longitude'             : 4,
            'bearingLong'           : 5,
            'fixQuality'            : 6,
            'nrSatellitesTracked'   : 7,
            'hzDilution'            : 8,
            'altitudeSeaLevel'      : 9,
            'altitudeSeaLevelUnit'  : 10,
            'altitudeEllipsoid'     : 11,
            'altitudeEllipsoidUnit' : 12,
            'checkSum'              : 14,
        }

        structTypes['RMC'] = {
            'sentenceType'          : 0,
            'fixTimestamp'          : 1,
            'status'                : 2,
            'latitude'              : 3,
            'bearingLat'            : 4,
            'longitude'             : 5,
            'bearingLong'           : 6,
            'speedGroundKnots'      : 7,
            'trackAngleDeg'         : 8,
            'date'                  : 9,
            'magDeviation'          : 10,
            'magDeviationBearing'   : 11,
            'checkSum'              : 12,
        }


        return structTypes[sType]

