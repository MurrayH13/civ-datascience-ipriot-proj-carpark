from interfaces import CarparkSensorListener
from interfaces import CarparkDataProvider
from CarParkDisplayM import CarParkDisplay
import time

class CarparkManager(CarparkSensorListener,CarparkDataProvider,):
    
    def __init__(self, number_of_bays):
    
        self.available_bays = number_of_bays
        self._temp = 0
        self.C_M_display = None


    @property   
    def available_spaces(self):
        return max(self.available_bays,0)


    
    # getter
    #@property
    def temperature(self):
        return self._temp
    
    # setter
    #@temperature.setter
    def set_temperature(self,value):
        self._temp = value


    @property
    def current_time(self):
        return time.localtime()

    def incoming_car(self,license_plate):
        print('Car in! ' + license_plate)
        self.available_bays = self.available_bays - 1
        print('Available bays ' , self.available_spaces)
        self.logging_information("car in, licence plate", license_plate)
        self.update()

    def outgoing_car(self,license_plate):
        print('Car out! ' + license_plate)
        self.available_bays = self.available_bays + 1
        print('Available bays ' , self.available_spaces)
        self.logging_information("car out, licence plate", license_plate) 
        self.update()

    def temperature_reading(self,reading):
        print(f'temperature is {reading}')
        self.set_temperature(reading)
        self.logging_information("temperature", reading)
        self.update()

    def logging_information(self, message, value):
        with open("samples_and_snippets\\log.txt", "a") as file:
                file.write(time.strftime("%d:%b:%Y:%H:%M:%S",self.current_time) + str(message) + ": " + str(value) + '\n')
                file.close()

    def update(self):
        self.C_M_display.update_display()

    



