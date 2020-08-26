# Automobile-Pricing-Model
This is a Linear Regression Model based on the following dataset from Kaggle:
https://www.kaggle.com/vipashakaul/predicting-the-price-of-an-automobile

The given dataset has 26 feature columns, 1 target column and over 200 observations, the main objective was to create a model to accurately predict the price of cars.
In order to achieve that goal first it was necessary to preprocess the data.

In the preprocessing step, I had to face missing values, dummies generation, outliers and turning apparently categorical variables into numerical. After that it was time to start
start thinking in building the model, but there were some steps left before getting to fit the model, I had to check the PDFs in order to identify problematic outliers, and also 
verify the OLS assumptions and relax the if necesary; to achieve linearity we had to apply somo logarithmic transformations and also an absolute value transformation to one
feature, then I used VIF to check if there was multicolinearity in the features. After that everything was set for Machine Learning, I standardized the inputs and fitted the model.

The final outcome was a Linear Model with a train accuracy of 93%, a test accuracy of 85.3%, and a mean percentage of deviation of 12%.
