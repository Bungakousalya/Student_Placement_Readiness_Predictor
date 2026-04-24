import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Preprocessing:

    def __init__(self, df):
        self.df = df

    # -----------------------
    # 1. CLEAN + MISSING VALUES
    # -----------------------
    def clean(self):

        # missing indicators
        self.df["resume_missing"] = self.df["resume_score"].isna().astype(int)
        self.df["mock_missing"] = self.df["mock_test_score"].isna().astype(int)

        # fill missing values
        self.df["resume_score"] = self.df["resume_score"].fillna(self.df["resume_score"].median())
        self.df["mock_test_score"] = self.df["mock_test_score"].fillna(self.df["mock_test_score"].median())

        # remove duplicates only (DON'T blindly dropna)
        self.df = self.df.drop_duplicates()

        return self.df

    # -----------------------
    # 2. ENCODE TARGET
    # -----------------------
    def encode_target(self):

        le = LabelEncoder()
        self.df["placement_status"] = le.fit_transform(self.df["placement_status"])

        return self.df, le

    # -----------------------
    # 3. SPLIT
    # -----------------------
    def split_xy(self):

        X = self.df.drop("placement_status", axis=1)
        y = self.df["placement_status"]

        return X, y