from interfaces import CarparkSensorListener
from interfaces import CarparkDataProvider
from Windows import WindowedDisplay
import carpark
import threading
import time


class CarParkDisplay:
    """Provides a simple display of the car park status. This is a skeleton only. The class is designed to be customizable without requiring and understanding of tkinter or threading."""
    # determines what fields appear in the UI
    fields = ['Available bays', 'Temperature', 'At']


    def __init__(self,root):
        self.window = WindowedDisplay(root,
            'Moondalup', CarParkDisplay.fields)
        
        # The following commented-out code was needed when just using a timer to update the display
        # updater = threading.Thread(target=self.check_updates)
        # updater.daemon = True
        # updater.start()
        
        self.window.show()
        self._provider=None
    
    @property
    def data_provider(self):
        return self._provider
    @data_provider.setter
    def data_provider(self,provider):
        if isinstance(provider,CarparkDataProvider):
            self._provider=provider

    
    def update_display(self):
        field_values = dict(zip(CarParkDisplay.fields, [
            f'{self._provider.available_spaces:03d}',
            f'{self._provider.temperature():02}℃',
            time.strftime("%H:%M:%S",self._provider.current_time)
        ]))
        self.window.update(field_values)

    #   No longer needed as only use update_display 
    # def check_updates(self):
    #     while True:
    #         # TODO: This timer is pretty janky! Can you provide some kind of signal from your code
    #         # to update the display?
    #         time.sleep(1)
    #         # When you get an update, refresh the display.
    #         if self._provider is not None:

    #             self.update_display()

