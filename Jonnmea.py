#!/usr/bin/env python3

# http://www.catb.org/gpsd/NMEA.html
# http://home.mira.net/~gnb/gps/nmea.html

import re

class Jonnmea:
    def __init__(self, sentence):
        self.sentence = sentence
        # $GPxxx
        self.sentenceType = self.sentence[3:6]
        self.nmeaStruct   = self.sentenceStruct(self.sentenceType)

        if not self.nmeaStruct:
            msg = "Sentence type '{0}' unknown"
            msg = msg.format(self.sentenceType)
            raise Exception(msg)

    def parseSentence(self):
        sentenceData     = re.split('[,*]', self.sentence)
        sentenceData_len = len(sentenceData)
        nmeaStruct_len   = len(self.nmeaStruct)

        if sentenceData_len != nmeaStruct_len:
            msg = "Field count does not match dictionary"
            msg = msg.format(self.sentenceType)
            raise Exception(msg)

        i = 0
        self.sentenceDataDict = {}
        for value in sentenceData:
            for key, nmeaValue in self.nmeaStruct.items():
                if key == i:
                    self.sentenceDataDict[nmeaValue] = value

            i = i+1

        return self.sentenceDataDict

    def validateChkSum(self):
        chksum = self.sentence.split('*',1)[1]

        # compare int
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
            return False

        return True

    def sentenceStruct(self, sType):
        sentenceTypes = {}

        sentenceTypes['GGA'] = {
                0  : 'sentence_type',
                1  : 'fix_timestamp',
                2  : 'latitude',
                3  : 'latitude_bearing',
                4  : 'longitude',
                5  : 'longitude_bearing',
                6  : 'fix_quality',
                7  : 'satellite_view_count',
                8  : 'hdop',
                9  : 'altitude',
                10 : 'altitude_unit',
                11 : 'geodial_separation',
                12 : 'geodial_separation_unit',
                13 : 'dgps_age',
                14 : 'diff_ref_station_id',
                15 : 'checksum'
        }

        sentenceTypes['RMC'] = {
                0  : 'sentence_type',
                1  : 'fix_timestamp',
                2  : 'status',
                3  : 'latitude',
                4  : 'latitude_bearing',
                5  : 'longitude',
                6  : 'longitude_bearing',
                7  : 'speed',
                8  : 'course',
                9  : 'date',
                10 : 'magnetic_variation',
                11 : 'magnetic_variation_bearing',
                12 : 'faa_mode', # NMEA 0183 version 3.00
                13 : 'checksum'
        }

        sentenceTypes['GSA'] = {
                0  : 'sentence_type',
                1  : 'selection_mode',
                2  : 'mode',
                3  : 'prn_1',
                4  : 'prn_2',
                5  : 'prn_3',
                6  : 'prn_4',
                7  : 'prn_5',
                8  : 'prn_6',
                9  : 'prn_7',
                10 : 'prn_8',
                11 : 'prn_9',
                12 : 'prn_10',
                13 : 'prn_11',
                14 : 'prn_12',
                15 : 'pdop',
                16 : 'hdop',
                17 : 'vdop',
                18 : 'checksum'
        }


        if not sentenceTypes.get(sType, False):
            return False

        return sentenceTypes[sType]
