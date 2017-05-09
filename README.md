# Behaviarol Cloning -Udacity Self Driving Car Nano Degree Project3

#### Files Submitted

1. model.py
2. drive.py
3. model.h5
4. Writeup-Project3.md
5. video.mp4

## Data Collection

To train the model developed in model.py, the car was driven on track 1 in simultor for 2 laps in anti-clockwise direction and 3 laps in clockwise direction.
This resulted in generation of total 19506 images and driving_log.csv file which contains the image paths and driving data. Images are of the resolution 160 by 320 and are color images. Steering angle is the only driving data being used in this project to train the model.


## Data Preprocessing

Firstly, the data generated is read. For this the csv package available in python is used to read the driving_log.csv file to extract the image names from the paths stored in this file. The center, left and right side images of the car appended to an array and corresponding steering wheel angle values are appended in another array. For the steering wheel angle values for left and right side images a small correction factor is added/subtracted from the steering wheel value recorded during data collection. The correction factor for the model is chosed to be **0.2**.

Secondly, after creating arrays of image names and corresponding steering wheel angle values, these are converted into numpy arrays and are stored in training variables.

![](https://github.com/pratvdev/CarND-BehaviarolCloning/blob/master/Driving_Data/Example%20Images/center_2017_04_26_21_00_42_738.jpg?style=center "Center Image Before Cropping")

![](https://github.com/pratvdev/CarND-BehaviarolCloning/blob/master/Driving_Data/Example%20Images/left_2017_04_26_21_00_42_738.jpg?style=center "Left Image Before Cropping")

![](https://github.com/pratvdev/CarND-BehaviarolCloning/blob/master/Driving_Data/Example%20Images/right_2017_04_26_21_00_42_738.jpg?style=center "Right Image Before Cropping")

**These examples images and the driving_log.csv file used are available in the folder Driving_Data**

The training data is split into two parts. **70%** of the data is used for training and **30%** of the data is used for validation.

Lambda feature in keras is used to furthur preprocess the data. The RGB pixel values are converted to values between 0 and 1 and later 0.5 is subtracted from these values.
The top portion of the imaged contains data which is not related to the road and the bottom part of the image contains the hood of the car. The top 70 and bottom 20 layers of the image are cropped for training the data effectively. For cropping the image, Cropping2D from keras is used.

## Model Architecture

For training the model the architecture chosen was the Nvidia Autonomous model discussed in the course.
The same exact model is used to train color images of input size 160x320.
This model used 9 layers in which first 5 are convolutional layers.

#### Layer 1: Convolutional Layer

Uses 24 filters and a 5x5 kernel with a 2x2 sub sampling.
Activation used is Relu.

#### Layer 2: Convolutional Layer

Uses 36 filters and a 5x5 kernel with a 2x2 sub sampling.
Activation used is Relu.

#### Layer 3: Convolutional Layer

Uses 48 filters and a 5x5 kernel with a 2x2 sub sampling.
Activation used is Relu.

#### Layer 4: Convolutional Layer

Uses 64 filters and a 3x3 kernel.
Activation used is Relu.

#### Layer 5: Convolutional Layer

Uses 64 filters and a 3x3 kernel.
Activation used is Relu.

After this layer we flatten the data.

#### Layer 6: Dense Layer

This layer uses dense of 100.

#### Layer 7: Dense Layer

This layer uses dense of 50.

#### Layer 8: Dense Layer

This layer uses dense of 10.

#### Layer 9: Dense Layer

This layer uses dense of 1.


This model uses mean squared error for loss and an adam optimizer.

Number of Epochs: **5**

Saved model file: **model.h5**

Model Summary information: **Model_Summary.png**

**The model was tested by adding a dropout layer between Layers 8 and 9 with values for dropout ranging from '0.1 - 0.5'. This resulted in a bad models. The car was unable to stay on the road and it was failing to turn properly at curves. The training model summary for The model with the use of dropout layer is given below. The model without the use of any dropout layers is chosen to be the final model to test drive the car on the simulator track. Generators were also not necessary to load the data.**

![](https://github.com/pratvdev/CarND-BehaviarolCloning/blob/master/Model_Summary_With_Dropout.png?raw=true "Model Summary With Dropout Layer")

![](https://github.com/pratvdev/CarND-BehaviarolCloning/blob/master/Model_Summary_without_Dropout.png?raw=true "Model Summary Without Dropout Layer")

## Running the saved model on the simulator

A model.h5 is generated after training. This file is given as an argument to drive.py, which helps to run the simulator in autonomous mode and record the driving images.

**drive.py file is edited to change the speed of the car. Initially the speed was set to 9 miles per hour and is changed to 14 miles per hour.**

The car drives inside the road and goes on to the yellow lines twice during the testing. This can be further improved by training the model with more data.

The images for autonomous driving on the test track are saved and a **video.mp4** file is generated. This file shows the test drive of the car.





