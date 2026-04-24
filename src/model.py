import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression

class ModelTrainer:

    def __init__(self, df):
        self.df = df

    def train(self):

        # -------------------------------
        # Split features and target
        # -------------------------------
        X = self.df.drop("placement_status", axis=1)
        y = self.df["placement_status"]

         # -------------------------------
        # Encoding
        # -------------------------------
        X = pd.get_dummies(X, drop_first=True)

        # Save full data (for cross validation)
        self.X = X
        self.y = y

       

        # -------------------------------
        # Train-Test Split
        # -------------------------------
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        # -------------------------------
        # SMOTE (only on training)
        # -------------------------------
        smote = SMOTE(random_state=42)
        self.X_train, self.y_train = smote.fit_resample(self.X_train, self.y_train)

        # -------------------------------
        # Scaling
        # -------------------------------
        self.scaler = StandardScaler()
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)

        # -------------------------------
        # Model
        # -------------------------------
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(self.X_train, self.y_train)

        # -------------------------------
        # Save artifacts
        # -------------------------------
        pickle.dump(self.model, open("models/model.pkl", "wb"))
        pickle.dump(self.scaler, open("models/scaler.pkl", "wb"))
        pickle.dump(X.columns, open("models/columns.pkl", "wb"))

        return self.model, self.X_test, self.y_test