

import pandas as pd

df = pd.read_parquet("heart_failure_clinical_records_dataset.parqet", engine="pyarrow")

#df = df.drop(columns=["Unnamed: 0"])

(print(df))

df.to_parquet("heart_failure_clinical_records_dataset.parqet", engine="pyarrow", index=False)