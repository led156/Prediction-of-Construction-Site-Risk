import streamlit as st
from lightgbm import LGBMClassifier
import joblib
import numpy as np


def add_sum(a, b):
    return a+b


class ourModel():
    def __init__(self, path='lgb12.pkl'):
        self.model = joblib.load(path) #TODO: 모델 로드


    def scaler(self, input):
        # TODO: scaler 적용
        pass


    def predict(self, input):
        y_hat = 2 #TODO: 모델 predict
        y_hat = self.model.predict(np.array(input).reshape(1, -1)).item()
        return y_hat