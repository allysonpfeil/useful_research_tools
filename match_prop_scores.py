import pandas as pd
from sklearn.neighbors import NearestNeighbors

excel_file_path = 'Your_Path_Here'
sheet_name = 'Your_Sheet_Name_Here'
data = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# separate the data into control and experimental groups
control_data = data[data['Your_Outcome_Variable'] == 0] # assuming one-hot encoded label
experimental_data = data[data['Your_Outcome_Variable'] == 1]

# fit a k-NN model to find the closest control patients for each experimental patient
knn = NearestNeighbors(n_neighbors=1)
knn.fit(control_data['PropScore'].values.reshape(-1, 1))
# prop score can be calculated from calc_prop_scores.py and needs to be a column in the xlsx

# find the closest control patients for each experimental patient
distances, indices = knn.kneighbors(experimental_data['PropScore'].values.reshape(-1, 1))

matched_pairs = []
used_control_patients = set()  # keep track of control patients used for logic to not repeat control patients

for index, row in experimental_data.iterrows():
    experimental_propensity_score = row['PropScore']

    # find control patients with similar propensity scores
    potential_matches = control_data[
        (abs(control_data['PropScore'] - experimental_propensity_score) < 0.02) &
        (~control_data['Your_Instance_Identifier'].isin(used_control_patients))  # exclude used control patients
    ]

    if not potential_matches.empty:
        # select the closest control patient
        matched_control_patient = potential_matches.iloc[0]

        # add the matched pair to the list
        matched_pairs.append((row, matched_control_patient))

        # mark the control patient as used
        used_control_patients.add(matched_control_patient['Your_Instance_Identifier'])

# print the matched pairs with 'Your_Outcome_Variable' and 'Your_Instance_Identifier' columns
for experimental, control in matched_pairs:
    print("Experimental Instance - Outcome:", experimental['Your_Outcome_Variable'], "Your_Instance_Identifier:", experimental['Your_Instance_Identifier'])
    print("Matched Control Instance - Outcome:", control['Your_Outcome_Variable'], "Your_Instance_Identifier:", control['Your_Instance_Identifier'])
    print()
# END
