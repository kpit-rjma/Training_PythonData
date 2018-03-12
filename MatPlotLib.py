# This is a basic overview of dealing with numpy and matplotlib in Python
# The enviornment is the problem to set up, used Anaconda and the Conda commands to set up
# Data taken from a phone using AndroSensor
import numpy
import matplotlib.pyplot as plt
import csv
import sys
import traceback

# Change this to point to your specific AndroSensor CSV file
filelocation = "C:\\Users\\rachela\\Documents\\phonedata.csv"

# These are variables I want easily accessible to edit, so I'm storing them at the top
optionsstring = "1 - Run Test Plot\n2 - Exit"
exitoption = "2"

# Get the data
# Data is as follows:
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
nameslist = ["AccelX", "AccelY", "AccelZ", "GravX", "GravY", "GravZ", "LAccelX", "LAccelY", "LAccelZ", "GyroX", "GyroY", "GyroZ", "Light", "MagX", "MagY", "MagZ", "OrienX", "OrienY", "OrienZ", "Proximity", "Pressure", "Sound", "Latitude", "Longitude", "Altitude", "GoogleAlt", "GoogleATM", "Speed", "Accuracy", "Orientation", "SatelliteCount", "Duration", "Date"]
data = numpy.genfromtxt(filelocation, delimiter=',', names=nameslist, skip_header=1)
# print(data) # Comment out when NOT testing data grabbing

# The following block of code (commented out) prints a test plot for you to check.
# If this does not plot per expectations, then there might be an issue with your Numpy or MatPlotLib installations
# If you run into issues, uncommenting this block out and attempting to use it is worthwhile.
def runtestplot():
    try:
        n = 20
        x = numpy.linspace(0, numpy.pi, n)
        y = numpy.sin(x)
        plt.plot(x, y)
        plt.show()
    except:
        print("Something went wrong with printing the test plot...")
        print("Please exit and check your Numpy and MatPlotLib installations.")
        print("To install either from the command line (using pip), run the following:")
        print("pip install numpy")
        print("pip install matplotlib")
        # The next line is for debugging only, leave commented out for delivery
        #print(traceback.format_exc())
    print("Test plot attempt complete.")

# Print Light values over Time
#subpl1 = plt.subplot()
#subpl1.plot((data["Duration"]/1000), data["Light"])
#subpl1.set_xlabel("Duration (Seconds)")
#subpl1.set_ylabel("Lumens")

# The following block of code ensures the user is able to navigate commands and controls the
# movement from call to call of various subroutines.
selection = ""
while (selection.lower() != "exit" or selection.lower() != "e" or selection != exitoption):
    print("Please type a command from the below list:")
    print("(Remember to exit graphs before returning to the console window!)")
    print(optionsstring)
    selection = input("Type command: ")

    if (selection == "1" or selection.lower() == "run test plot" or selection.lower() == "run test"):
        runtestplot()
    elif (selection.lower() != "exit" or selection.lower() != "e" or selection != exitoption):
        break
    else:
        selection = input("\nCommand not recognized! Please try again...\n")