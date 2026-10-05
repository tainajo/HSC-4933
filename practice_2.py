# Practice 1 # Taina Joseph
# 9/22/26

#import libraries
import pandas as pd

#import the .csv
df = pd.read_csv("heart_failure_clinical_records_dataset.csv")


df.to_json("heart_failure_clinical_records_dataset.json" , orient="records", indent=2 )
