from datetime import timezone, date, datetime
from astral import Astral

class LedChanger():
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.city_name = 'Sofia'
        a = Astral()
        a.solar_depression = 'civil'
        self.city = a[self.city_name]
        self.timezone = self.city.timezone
        self.sun_info = self.city.sun(date=date.today(), local=True)

    def print_info(self):
        print('Information for %s/%s\n' % (self.city_name, self.city.region))
        print('Timezone: %s' % self.timezone)
        print('Latitude: %.02f; Longitude: %.02f\n' % \
            (self.city.latitude, self.city.longitude))
        print('Dawn:    %s' % str(self.sun_info['dawn']))
        print('Sunrise: %s' % str(self.sun_info['sunrise']))
        print('Noon:    %s' % str(self.sun_info['noon']))
        print('Sunset:  %s' % str(self.sun_info['sunset']))
        print('Dusk:    %s' % str(self.sun_info['dusk']))
        print
        print("The time now is: {}".format(datetime.now()))

    def daylight(self):
        now = datetime.now(timezone.utc)
        sunrise = self.sun_info['sunrise']
        print(now < sunrise)



if __name__ == '__main__':
    lc = LedChanger()
    # lc.print_info()
    lc.daylight()