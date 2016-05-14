# Jonnmea

Jonnmea is a python class for parsing NMEA sentences. 

## Current status
GPGGA, GPRMC and GPGSA supported.

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
</code></pre>
