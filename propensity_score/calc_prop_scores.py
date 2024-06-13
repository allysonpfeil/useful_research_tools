import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

excel_file_path = 'Your_Path_Here'
sheet_name = 'Your_Sheet_Name_Here'
data = pd.read_excel(excel_file_path, sheet_name=sheet_name)
continuous_features = ['Feature_1', 'Feature_2'] # continuous variables for normalization
scaler = StandardScaler()
data[continuous_features] = scaler.fit_transform(data[continuous_features])
X = data[['Feature_1', 'Feature_2', 'Feature_3']]  # Covariates (independent variables)
y = data['Your_Outcome_Variable']  # Dependent variable (binary outcome group)
model = LogisticRegression()
model.fit(X, y)
propensity_scores = model.predict_proba(X)[:, 1]
for score in propensity_scores:
    print(score)
