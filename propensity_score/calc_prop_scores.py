# import libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# load your data from Excel
excel_file_path = 'Your_Path_Here'
sheet_name = 'Your_Sheet_Name_Here'
data = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# standardize continuous variables
continuous_features = ['Feature_1', 'Feature_2'] # continuous variables for normalization
scaler = StandardScaler()
data[continuous_features] = scaler.fit_transform(data[continuous_features])

# note: Feature_3 has already been one-hot encoded
# define the dependent variable (treatment) and independent variables (covariates)
X = data[['Feature_1', 'Feature_2', 'Feature_3']]  # Covariates (independent variables)
y = data['Your_Outcome_Variable']  # Dependent variable (binary outcome group)

# define and fit the logistic regression model
model = LogisticRegression()
model.fit(X, y)

# fet propensity scores
propensity_scores = model.predict_proba(X)[:, 1]

# print propensity scores to the console
for score in propensity_scores:
    print(score)
# END
