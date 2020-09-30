import numpy as np
import pandas as pd
import pickle

class Automobile_Model():
    
    def __init__(self, model_file, scaler_file):
        with open(model_file, 'rb') as model_file, open(scaler_file, 'rb') as \
        scaler_file:
            self.reg = pickle.load(model_file)
            self.scaler = pickle.load(scaler_file)
            self.data = None
                   
    def load_and_clean_data(self, data_file):
        
        df = pd.read_csv(data_file)
        self.df_with_predictions = df.copy()
        
        if 'Unnamed: 0' in df.columns:
            df = df.drop(['Unnamed: 0'], axis=1)
        df = df.replace('?', np.nan)
        
        df['fuel-type'] = df['fuel-type'].map({'gas':0, 'diesel':1})
        df['aspiration'] = df['aspiration'].map({'std':0, 'turbo':1})
        
        make_dummies = pd.get_dummies(df['make'], drop_first=True)
        df = df.drop(['make'], axis=1)
        df = pd.concat([df, make_dummies], axis=1)
        
        body_style_dummies = pd.get_dummies(df['body-style'], drop_first=True)
        df = df.drop(['body-style'], axis=1)
        df = pd.concat([df, body_style_dummies], axis=1)
        
        drive_wheels_dummies = pd.get_dummies(df['drive-wheels'],
                                              drop_first=True)
        df = df.drop(['drive-wheels'], axis=1)
        df = pd.concat([df, drive_wheels_dummies], axis=1)
        
        df = df.drop(['engine-location'], axis=1)
        
        engine_type_dummies = pd.get_dummies(df['engine-type'],
                                            drop_first=True)
        df = df.drop(['engine-type'], axis=1)
        df = pd.concat([df, engine_type_dummies], axis=1)
        
        df['num-of-cylinders'] = df['num-of-cylinders'].map(
            {'four':4, 'five':5, 'six':6, 'three':3, 'two':2, 'eight':8})
        
        fuel_system_dummies = pd.get_dummies(df['fuel-system'],
                                              drop_first=True)
        df = df.drop(['fuel-system'], axis=1)
        df = pd.concat([df, fuel_system_dummies], axis=1)
        
        preprocessed_data = pd.read_csv('Car_price_preprocessed.csv')
        for col in preprocessed_data.columns:
            if col not in df.columns:
                df[col] = 0
        
        new_columns = ['symboling', 'normalized-losses', 'bmw', 'chevrolet', 'dodge',
       'honda', 'jaguar', 'mazda', 'mercedes-benz', 'mitsubishi',
       'nissan', 'peugot', 'plymouth', 'porsche', 'saab', 'subaru',
       'toyota', 'volkswagen', 'volvo', 'fuel-type', 'aspiration',
       'two-doors', 'hardtop', 'hatchback', 'sedan', 'wagon', 'fwd',
       'rwd', 'wheel-base', 'length', 'width', 'height', 'curb-weight',
        'l', 'ohc', 'ohcf', 'ohcv', 'rotor',
       'num-of-cylinders', 'engine-size', '2bbl', '4bbl', 'idi', 'mfi', 'mpfi',
       'spdi', 'bore', 'stroke',
       'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
       'highway-mpg']
        df = df[new_columns]
        
        df.drop(['compression-ratio'], axis=1, inplace=True)
        df.drop(['stroke'], axis=1, inplace=True)
        df.drop(['peak-rpm'], axis=1, inplace=True)
        
        df['num-of-cylinders'] = df['num-of-cylinders'].map({4:0, 5:1, 6:1})
        df = df.rename(columns={'num-of-cylinders':'+4 cylinders'})
        
        df.drop(['city-mpg'], axis=1, inplace=True)
        df['highway-mpg'] = np.log(df['highway-mpg'])
        df.rename(columns={'highway-mpg':'Log highway-mpg'}, inplace=True)
        
        df['symboling'] = abs(df['symboling'] - 1)
        df.rename(columns={'symboling':'abs(symb-1)'}, inplace=True)
        
        for i in ['wheel-base', 'length', 'width', 'height', 'curb-weight',
       'engine-size', 'bore', 'horsepower', 'Log highway-mpg']:
            df.drop([i], axis=1, inplace=True)
                        
        self.preprocessed_data = df.copy()
        self.data = self.scaler.transform(df)
           
    def predicted_output(self):
        if (self.data is not None):
            self.df_with_predictions['Predicted Price'] = \
            np.exp(self.reg.predict(self.data))
            return self.df_with_predictions