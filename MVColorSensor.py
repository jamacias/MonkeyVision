from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor

class MVColorSensor:
    def __init__(self, port=None):
        self.colorSensor = ColorSensor(port)

    def getColor(self):
        self.colorSensor.mode='COL-COLOR'
        colorValue = self.colorSensor.value()
        colors=('unknown','black','blue','green','yellow','red','white','brown')
        return colors[colorValue]
    
    def getRefectionLight(self):
        self.colorSensor.mode = 'COL-REFLECT'
        return self.colorSensor.value()

    def getAmbientLight(self):
        self.colorSensor.mode = 'COL-AMBIENT'
        return self.colorSensor.value()

    def getRGB(self):
        self.colorSensor.mode = 'RGB-RAW'
        red = self.colorSensor.value(0)
        green = self.colorSensor.value(1)
        blue = self.colorSensor.value(2)
        return (red, green, blue)