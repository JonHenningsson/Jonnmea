# Jonnmea

Jonnmea is a python class for parsing NMEA sentences. 

## Current status
GPGGA and GPRMC supported. Probably wont be any support for other types anytime soon.

## How to use
Create the object:

<pre><code>
from Jonnmea.Jonnmea import Jonnmea
nmeaObj = Jonnmea("$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47")
</code></pre>

Validate checksum, returns True upon success:
<pre><code>
nmeaObj.validateChkSum()
</code></pre>

Import the sentence to a dictionary:
<pre><code>
gpsData = nmeaObj.parseSentence()
print(gpsData)
</code></pre>

Result:
<pre><code>
{'sentenceType': '$GPGGA', 'bearingLong': 'E', 'altitudeEllipsoidUnit': 'M', 'latitude': '4807.038', 'checkSum': '47', 'fixTimestamp': '123519', 'altitudeSeaLevel': '545.4', 'altitudeSeaLevelUnit': 'M', 'bearingLat': 'N', 'fixQuality': '1', 'nrSatellitesTracked': '08', 'hzDilution': '0.9', 'longitude': '01131.000', 'altitudeEllipsoid': '46.9'}
</pre></code>
