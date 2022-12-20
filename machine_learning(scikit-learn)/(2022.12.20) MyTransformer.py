from sklearn.base import BaseEstimator, TransformerMixin

class MyTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, first_param =  1, second_param = 2):
        self.first_param = first_param
        self.second_param = second_param
    
    def fit(self, X, y = None):
        pass
    
    # 분류나 회귀 : TransformerMixin 대신 ClassifierMixin, RegressorMixin 상속
    #               transform 대신 predict 구현
    
    def transform(self, X):
        X_transformed = X + 1
        return X_transformed