from Observer import Observer

class WeatherStation():

    def __init__(self):
        self.observer = []
        self.temp = None

    def addObserber(self, observer: Observer):
        self.observer.append(observer)

    def removeObserber(self, observer: Observer):
        self.observer.remove(observer) 

    def setTemp(self, temp: int):
        self.temp = temp
        self.notify()     

    def notify(self):
        for observer in self.observer:
            observer.update(self.temp)

################### Run Code ###################


phoneApp1 = Observer()
phoneApp2 = Observer()

wStation = WeatherStation()
wStation.addObserber(phoneApp1)
wStation.addObserber(phoneApp2)

wStation.setTemp(20)
wStation.removeObserber(phoneApp2)
wStation.setTemp(10)






