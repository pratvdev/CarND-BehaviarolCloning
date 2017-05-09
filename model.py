#model.py for training the data collected from simulator 

import csv
import cv2
import numpy as np

# Reading the .csv file generated after collecting the data in the simulator using csv package in python
lines = []
with open('Driving_Data/driving_log.csv') as csvfile:
	reader = csv.reader(csvfile)
	for line in reader:
		lines.append(line)

images = []
measurements = []

# Correction is the variable we add/subtract from steering wheel angle value calculated during data collection
# This value is appended to the measurements array for training

correction = 0.2

# This loop reads the csv files and extracts the image name from the paths. These image names are appended to the Images array
for line in lines:
	for i in range(3):
		source_path = line[i]
		filename = source_path.split('\\')[-1]
		current_path = 'Driving_Data/IMG/' + filename
		image = cv2.imread(current_path)
		images.append(image)
		
		if i==0:
			measurement = float(line[3])
		elif i==1:
			measurement = float(line[3]) + correction
		else:
			measurement = float(line[3]) - correction
		
		measurements.append(measurement)
	
#Creating training data
X_train = np.array(images)
y_train = np.array(measurements)

#Importing keras packages to create a model
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout
from keras.layers import Convolution2D

model = Sequential()

#Using lambda layer to convert pixel values
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape = (160,320,3)))

#Cropping the unwated top and bottom portions of an image
model.add(Cropping2D(cropping=((70,25),(0,0))))

#Using model from Nvidia discussed in the course to train
model.add(Convolution2D(24,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(36,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(48,5,5,subsample=(2,2),activation="relu"))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Convolution2D(64,3,3,activation="relu"))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

#This model uses mean squared error and adam optimizer
model.compile(loss='mse', optimizer = 'adam')

#Splitting data into 70% for training and 30% for validation
model.fit(X_train, y_train, validation_split=0.3, shuffle=True, nb_epoch=5)

#Saving model
model.save('model.h5')

#Printing model summary
print(model.summary())
