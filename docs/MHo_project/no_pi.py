"""The following code is used to provide an alternative to students who do not have a Raspberry Pi.
If you have a Raspberry Pi, or a SenseHAT emulator under Debian, you do not need to use this code.

You need to split the classes here into two files, one for the CarParkDisplay and one for the CarDetector.
Attend to the TODOs in each class to complete the implementation."""
#from interfaces import CarparkSensorListener
#from interfaces import CarparkDataProvider
import carpark
from CarParkDisplayM import CarParkDisplay 
from CarDetectorM import CarDetectorWindow
import threading
import tkinter as tk

# -----------------------------------------#
# TODO: STUDENT IMPLEMENTATION STARTS HERE #
# -----------------------------------------#





if __name__ == '__main__':
    root = tk.Tk()

    #TODO: This is my dodgy mockup. Replace it with a good one!
    my_new_carpark=carpark.CarparkManager(5)

    display=CarParkDisplay(root)
    #TODO: Set the display to use your data source
    display.data_provider=my_new_carpark

    #pass reference of CarParkDisplay to CarparkManager
    my_new_carpark.C_M_display = display
    
    detector=CarDetectorWindow(root)
    #TODO: Attach your event listener
    detector.add_listener(my_new_carpark)

    root.mainloop()
