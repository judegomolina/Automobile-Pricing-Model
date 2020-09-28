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
        
        df = df.drop(['Unnamed: 0'], axis=1)
        df = df.replace('?', np.nan)
        
        make_dummies = pd.get_dummies(df['make'], drop_first=True)
        df = df.drop(['make'], axis=1)
        df = pd.concat([df, make_dummies], axis=1)
        
        df.dropna(subset=['num-of-doors'], axis=0, inplace=True)
        
        body_style_dummies = pd.get_dummies(df['body-style'], drop_first=True)
        df = df.drop(['body-style'], axis=1)
        df = pd.concat([df, body_style_dummies], axis=1)
        
        drive_wheels_dummies = pd.get_dummies(df['drive-wheels'],
                                              drop_first=True)
        df = df.drop(['drive-wheels'], axis=1)
        df = pd.concat([df, drive_wheels_dummies])
        
        df = df.drop(['engine-location'], axis=1)
        
        engine_type_dummies = pd.get_dummies(df['engine-type'],
                                            drop_first=True)
        df = df.drop(['engine-type'], axis=1)
        df = pd.concat([df, engine_type_dummies], axis=1)
        
        df['num-of-cylinders'] = df['num-of-cilinders'].map(
            {'four':4, 'five':5, 'six':6, 'three':3, 'two':2, 'eight':8})
        
        fuel_system_dummies = pd.get_dummies(df['drive-wheels'],
                                              drop_first=True)
        df = df.drop(['fuel-system'], axis=1)
        df = pd.concat([df, fuel_system_dummies])
        