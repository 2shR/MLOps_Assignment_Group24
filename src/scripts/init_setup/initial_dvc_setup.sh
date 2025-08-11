pip install dvc pandas scikit-learn matplotlib jupyter
#For the first time, initialize DVC
dvc init -f
# Add the data directory to DVC
dvc add data/raw/california_housing.csv
dvc add data/processed/X_train.csv
dvc add data/processed/X_test.csv
dvc add data/processed/y_train.csv
dvc add data/processed/y_test.csv
git add data/*.dvc
git commit -m "Initial commit with DVC"
