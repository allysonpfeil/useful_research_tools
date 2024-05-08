import pandas as pd
import statsmodels.formula.api as smf
from sklearn.preprocessing import StandardScaler
import numpy as np

data = pd.read_excel("C://dev//ABOS2013.xlsx")
data = data[["Fellowship Abbreviation", "Patient Age", "Patient Gender", "Medical Binary", "Surgical Binary", "CPT Codes", 
             "Reoperation", "Readmission"
             ]]
scaler = StandardScaler()
data["Patient Age"] = scaler.fit_transform(data[["Patient Age"]])

log_reg = smf.logit("Q('Readmission') ~ Q('Fellowship Abbreviation') + Q('Patient Age') + Q('Patient Gender') + Q('CPT Codes') + Q('Surgical Binary') + Q('Reoperation') + Q('Medical Binary')", data=data).fit()

print(log_reg.summary())

results_summary = log_reg.summary()
results_as_html = results_summary.tables[1].as_html()
summary_df = pd.read_html(results_as_html, header=0, index_col=0)[0]

coefs = summary_df['coef']
std_errs = summary_df['std err']

risk_ratios = np.exp(coefs)
conf_ints = np.exp(coefs - 1.96 * std_errs), np.exp(coefs + 1.96 * std_errs)

print("Risk Ratios:")
print(risk_ratios)
print("\nConfidence Intervals:")
print(conf_ints)
