# Automobile Pricing Model

This project was dedicated to the development of a predictive model for the estimation of car prices, for which a Linear Regression Model was chosen. The Model generated has a test accuracy of 84.4% and an average error of 12.6% thus, based in the simplicity of the chosen model, it was considered as succesful.

The project can be divided in three main steps:
* Preprocessing.
* Modeling.
* Deployment.


The model was built based on the following dataset from Kaggle: https://www.kaggle.com/vipashakaul/predicting-the-price-of-an-automobile , the dataset has 26 feature columns, 1 target column and over 200 observations.

## Getting Started

The following steps will let you obtain a functional version of this project in your own machine.

### Requirements

The main requirement for running this project in your computer is having Python and Jupyter Notebook installed, you'll also require to install the following Python Libraries:
* Numpy.
* Pandas.
* Matplotlib.
* Seaborn.
* StatsModels.
* Sklearn.

### Installation

After verifying that you meet all the above mentioned requirements you have two different options to install this project in your local machine depending on if you want to review every step of the analysis or just being able to use the model to make predictions on new data.

#### Review Every Step of the Analysis

In the first case, you'll need to clone the entire repository in your machine and everything we'll be set for you to start running the project. 

This option is strongly recommended as you will get all the information about the model and also won't have to deal with choosing specific files that could lead to some issues.

#### Just Use the Model for Predictions

In this case, you won't need the whole repository and instead you just require to download the following files:
* Automobile Pricing Deployment.ipynb
* Automobile_pricing_module.py
* Car_price_preprocessed.csv
* model
* scaler
* new_data.csv

## Running the Project

At this point everything is ready for you to start running the project, so we'll now go through some things you can do.

### Reviewing Preprocessing and Modelling Steps

You can start by opening the notebooks with the preprocessing and modelling steps and check everything we went through to achive our final result. You may need to run all cells again if the outpots are not displayed.

Also if you have some issues with the files required for the deployment (Car_price_preprocessed.csv, model and scaler) running these notebooks again will generate those files.

### Making Predictions on New Data

Finally, we'll see how to use the model for making predictions on new data, it is important to mention that the data must be in the same format that the training data for the model, you can check out that format in the New_Data.xlsx file, you could even use a copy of that file to input your new data and then make the predictions, but make sure to convert it to csv in the deployment notebook.

#### Testing that the Module is working Properly

We have prepared a simple test that is inside the Automobile Pricing Deployment.ipynb file, it just takes the New_Data.csv file and check if there is no problem making predictions on this data prior moving forward to predict the outputs of the new data you are giving to the model.

#### Making the Predictions

In order to make predictions on your new data you just need to follow the steps mentioned in the Automobile Pricing Deployment.ipynb file, which just require you to input the path of your new file and uncomment the lines of code you require to run. The above mentioned file also allows you to save your predictions as csv or excel files.

