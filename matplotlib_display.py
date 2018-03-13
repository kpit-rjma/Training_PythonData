"""
# This is a basic overview of dealing with numpy and matplotlib in Python
# The enviornment is the problem to set up, used Anaconda and the Conda commands to set up
# DATA taken from a phone using AndroSensor
"""
# import csv
# import sys
import traceback
import numpy
import matplotlib.pyplot as plt

# Change this to point to your specific AndroSensor CSV file
FILE_LOCATION = ".\\defaultDATA.csv"

# These are variables I want easily accessible to edit, so I'm storing them at the top
OPTIONS_STRING = "1 - Run Test Plot\n2 - Light over Time\n3 - Sound over Time\n4 - Exit"
SELECTION = ""
EXIT_OPTION = "4"

# Get the DATA
# DATA is as follows:
# -------------------
# Acceleration: AccelX, AccelY, AccelZ
# Gravity: GravX, GravY, GravZ
# Linear Acceleration: LAccelX, LAccelY, LAccelZ
# Gyroscope: GyroX, GyroY, GyroZ
# Light: Light
# Magnetic Field: MagX, MagY, MagZ
# Orientation: OrienX, OrienY, OrienZ
# Proximity: Proximity
# Pressure: Pressure
# Sound: Sound
# Location: Latitude, Longitude, Altitude (EMPTY when Location is OFF)
# Google Specifics: GoogleAlt, GoogleATM (EMPTY when Location is OFF)
# Speed: Speed
# Accuracy: Accuracy
# Orientation: Orientation
# Satellites in Range: SatelliteCount
# Time Passed: Duration
# Date: Date
# Also see: https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
try:
    NAMES_LIST = ["AccelX", "AccelY", "AccelZ", "GravX", "GravY", "GravZ", "LAccelX", "LAccelY", "LAccelZ", "GyroX", "GyroY", "GyroZ", "Light", "MagX", "MagY", "MagZ", "OrienX", "OrienY", "OrienZ", "Proximity", "Pressure", "Sound", "Latitude", "Longitude", "Altitude", "GoogleAlt", "GoogleATM", "Speed", "Accuracy", "Orientation", "SatelliteCount", "Duration", "Date"]
    DATA = numpy.genfromtxt(FILE_LOCATION, delimiter=',', names=NAMES_LIST, skip_header=1)
    # print(DATA) # Comment out when NOT testing DATA grabbing
except:
    print("There was an issue with reading in your DATA...")
    print("Please check that your CSV file is available, or that the default has not moved location.")
    SELECTION = "2"

"""
# The following block of code prints a test plot for you to check.
# If this does not plot per expectations, then there might be an issue with your Numpy or MatPlotLib installations
# If you run into issues, uncommenting this block out and attempting to use it is worthwhile.
"""
def runtestplot():
    try:
        n_value = 20
        x_value = numpy.linspace(0, numpy.pi, n_value)
        y_value = numpy.sin(x_value)
        plt.plot(x_value, y_value)
        plt.show()
    except:
        print("Something went wrong with printing the test plot...")
        print("Please exit and check your Numpy and MatPlotLib installations.")
        print("To install either from the command line (using pip), run the following:")
        print("pip install numpy")
        print("pip install matplotlib")
        # The next line is for debugging only, leave commented out for delivery
        print(traceback.format_exc())
    print("Test plot attempt complete.\n")
    plt.gcf().clear()

"""
# The following block of code prints light over time in a line graph.
"""
def runlightovertime():
    try:
        plt.plot((DATA["Duration"]/1000), DATA["Light"])
        plt.xlabel("Duration (Seconds)")
        plt.ylabel("Light Sensed")
        plt.show()
    except:
        print("Something went wrong with printing this graph...")
        print("Please test plotting first with the Test Plot option.")
        print("If the test works, this may be due to a problem obtaining DATA.")
        # The next line is for debugging only, leave commented out for delivery
        print(traceback.format_exc())
    print("Light over Time plot attempt complete.\n")
    plt.gcf().clear()

"""
# The following block of code prints sound over time in a line graph.
"""
def runsoundovertime():
    try:
        plt.plot((DATA["Duration"]/1000), DATA["Sound"])
        plt.xlabel("Duration (Seconds)")
        plt.ylabel("Sound Sensed")
        plt.show()
    except:
        print("Something went wrong with printing this graph...")
        print("Please test plotting first with the Test Plot option.")
        print("If the test works, this may be due to a problem obtaining DATA.")
        # The next line is for debugging only, leave commented out for delivery
        print(traceback.format_exc())
    print("Sound over Time plot attempt complete.\n")
    plt.gcf().clear()

# The following block of code ensures the user is able to navigate commands and controls the
# movement from call to call of various subroutines.
while (SELECTION.lower() != "exit" or SELECTION.lower() != "e" or SELECTION != EXIT_OPTION):
    print("Please type a command from the below list:")
    print("(Remember to exit graphs before returning to the console window!)")
    print(OPTIONS_STRING)
    SELECTION = input("Type command: ")

    if (SELECTION == "1" or SELECTION.lower() == "run test plot" or SELECTION.lower() == "run test"):
        runtestplot()
    elif (SELECTION.lower() == "2" or SELECTION.lower() == "light over time" or SELECTION == "light"):
        runlightovertime()
    elif (SELECTION.lower() == "3" or SELECTION.lower() == "sound over time" or SELECTION == "sound"):
        runsoundovertime()
    elif (SELECTION.lower() == "exit" or SELECTION.lower() == "e" or SELECTION == EXIT_OPTION):
        print("Exiting...")
        break
    else:
        SELECTION = input("\nCommand not recognized! Please try again...\n")
