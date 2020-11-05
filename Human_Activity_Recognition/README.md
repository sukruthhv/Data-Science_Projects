
The Human Activity Recognition database was built from the recordings of 30 study participants performing activities of daily living (ADL) while carrying a waist-mounted smartphone with embedded inertial sensors.  _The objective is to classify activities into one of the six activities performed_.

![Human Activity Recognition](https://images.squarespace-cdn.com/content/v1/597d2753be6594cef6a34840/1501425209549-H2H9AZNAC3LMBKRZCHIL/ke17ZwdGBToddI8pDm48kITcJBvE1wk9BMTjuPn_gmB7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0le00SKh50FmsJr_9wQ9VAETQd4wUIeRmkKjdrZnmw1b3k-WGA6oYaXcSK6cHKpzNQ/micromachines-06-01100-g002.png?format=1000w)

## Description of experiment

The experiments have been carried out with a group of 30 volunteers within an age bracket of 19-48 years. Each person performed six activities (WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING) wearing a smartphone (Samsung Galaxy S II) on the waist. Using its embedded accelerometer and gyroscope, we captured 3-axial linear acceleration and 3-axial angular velocity at a constant rate of 50Hz. The experiments have been video-recorded to label the data manually. The obtained dataset has been randomly partitioned into two sets, where 70% of the volunteers was selected for generating the training data and 30% the test data.

The sensor signals (accelerometer and gyroscope) were pre-processed by applying noise filters and then sampled in fixed-width sliding windows of 2.56 sec and 50% overlap (128 readings/window). The sensor acceleration signal, which has gravitational and body motion components, was separated using a Butterworth low-pass filter into body acceleration and gravity. The gravitational force is assumed to have only low frequency components, therefore a filter with 0.3 Hz cutoff frequency was used. From each window, a vector of features was obtained by calculating variables from the time and frequency domain.

## Attribute information

For each record in the dataset the following is provided:

-   Triaxial acceleration from the accelerometer (total acceleration) and the estimated body acceleration.
    
-   Triaxial Angular velocity from the gyroscope.
    
-   A 561-feature vector with time and frequency domain variables.
    
-   Its activity label.
    
-   An identifier of the subject who carried out the experiment.
