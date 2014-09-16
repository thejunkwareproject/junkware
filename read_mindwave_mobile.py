import time
import bluetooth
from lib.mindwave.MindwaveDataPoints import *
from lib.mindwave.MindwaveDataPointReader import MindwaveDataPointReader

from lib.queue import RedisQueue

# data
point= {}
q = RedisQueue('mindwave')

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()

    while(True):
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
            q.put(point)
            point={}
            time.sleep(1)
        except KeyError:
            pass
