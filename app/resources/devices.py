import time
import bluetooth

from lib.mindwave.MindwaveDataPoints import *
from lib.mindwave.MindwaveDataPointReader import MindwaveDataPointReader

from datetime import datetime
from os import path
from lib.oximon.cms50 import CMS50
from lib.queue import RedisQueue
import var

q_mindwave = RedisQueue('mindwave')
q_oxymeter = RedisQueue('oxymeter')

seriesLength=12

# init series
EEG_series = {}
waves=["delta","theta","lowAlpha","highAlpha","lowBeta","highBeta","lowGamma","midGamma"]

for wave in waves:
    EEG_series[wave]={}
    EEG_series[wave]["data"]=[{"x":int(time.time()),"y":0}]*12
    EEG_series[wave]["name"]=wave

brain_values=["attention","meditation"]

att_med_series={}
for val in brain_values:
    att_med_series[val]={}
    att_med_series[val]["name"]=val
    att_med_series[val]["data"]=[{"x":int(time.time()),"y":0}]*12

def get_data_from_eeg_headset():
    point={}
    point["EEG"]={}
    print "starting headset"
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    while(var.headset_on):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()

        # poor signal
        if (dataPoint.__class__ is PoorSignalLevelDataPoint):
            if (not dataPoint.headSetHasContactToSkin()):
                point["poorSignal"] = 0
            else:
                point["poorSignal"] = dataPoint.amountOfNoise

        # meditation
        if (dataPoint.__class__ is MeditationDataPoint):
            point["meditation"] = dataPoint.meditationValue

        # attention
        if (dataPoint.__class__ is AttentionDataPoint):
            point["attention"] = dataPoint.attentionValue

        # blink
        if (dataPoint.__class__ is BlinkDataPoint):
            point["blink"] = dataPoint.blinkValue

        # EEG
        if (dataPoint.__class__ is EEGPowersDataPoint):
            print dataPoint.delta
            point["EEG"] = {
                "delta": dataPoint.delta,
                "theta": dataPoint.theta,
                "lowAlpha": dataPoint.lowAlpha,
                "highAlpha": dataPoint.highAlpha,
                "lowBeta": dataPoint.lowBeta,
                "highBeta": dataPoint.highBeta,
                "lowGamma": dataPoint.lowGamma,
                "midGamma": dataPoint.midGamma
                }

        try:
            point["EEG"],point["attention"],point["attention"],point["meditation"],point["poorSignal"]
            print "point added to queue"

            # parse EEG
            for key in EEG_series:
                EEG_series[key]["data"].pop(0)
                EEG_series[key]["data"].append({ "x" : int(time.time()), "y" : point["EEG"][key] })

            for key in att_med_series:
                att_med_series[key]["data"].pop(0)
                att_med_series[key]["data"].append({ "x" : int(time.time()), "y" : point[key] })


            q_mindwave.put({
                    "point" :point,
                    "series":[ EEG_series[x] for x in EEG_series],
                    "values":[ att_med_series[x] for x in att_med_series]
                  })

            # print "point ok !"
            point={}
            time.sleep(1)
        except KeyError:
            pass

def get_data_from_oxymon():
    port = '/dev/ttyUSB0'
    if not path.exists(port):
        exit("oximon: could not open '%s': no such file or directory" % port)

    oximeter = CMS50(port)
    print('Oxymeter Device : #date\theart rate\toxygen saturation')

    while var.oxymeter_on:
        try:
            if oximeter.update():
                # print dir(oximeter)
                output = { "heart_rate" : oximeter.hr, "oxygen_saturation" : oximeter.sat, "x":oximeter.x,"y":oximeter.y }
                print output
                q_oxymeter.put(output)
        except SerialException as e: 
            exit('oximon: %s' % e)
    oximeter.close()
