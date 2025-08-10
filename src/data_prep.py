from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split


def load_data():
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame
    return df


def preprocess_data(df):
    X = df.drop("MedHouseVal", axis=1)
    y = df["MedHouseVal"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


def save_datasets(X_train, X_test, y_train, y_test):
    X_train.to_csv("data/processed/X_train.csv", index=False)
    X_test.to_csv("data/processed/X_test.csv", index=False)
    y_train.to_csv("data/processed/y_train.csv", index=False)
    y_test.to_csv("data/processed/y_test.csv", index=False)


df = load_data()
df.to_csv("data/raw/california_housing.csv", index=False)

X_train, X_test, y_train, y_test = preprocess_data(df)
save_datasets(X_train, X_test, y_train, y_test)
