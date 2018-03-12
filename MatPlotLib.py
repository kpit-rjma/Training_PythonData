# This is a basic overview of dealing with numpy and matplotlib in Python
# The enviornment is the problem to set up, used Anaconda and the Conda commands to set up
# Data taken from a phone using AndroSensor
import numpy
import matplotlib.pyplot as mpl
import csv
import sys

filelocation = "C:\\Users\\rachela\\Documents\\phonedata.csv"

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
# print(data) # Comment out when testing

print("When working with MatPlotLib, you'll want to ensure you're printing all the graphics you want to show.");
print("In this case, we're going to want to display multiple plots in the console in succession based on the data gathered from the phone")
print("Be aware that in the code, subplot() is called to create a single plot with the specified style and parameters.")

# Print Light values over Time
subpl1 = mpl.subplot()
subpl1.plot((data["Duration"]/1000), data["Light"])
subpl1.set_xlabel("Duration (Seconds)")
subpl1.set_ylabel("Lumens")