import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

def test_linear_regression_fit_predict():
    X_train = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    y_train = np.array([7, 8, 9])
    X_test = pd.DataFrame({'a': [4, 5], 'b': [7, 8]})

    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    assert len(preds) == len(X_test)

def test_decision_tree_fit_predict():
    X_train = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    y_train = np.array([7, 8, 9])
    X_test = pd.DataFrame({'a': [4, 5], 'b': [7, 8]})

    model = DecisionTreeRegressor(max_depth=2)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    assert len(preds) ==