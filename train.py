import pandas as pd
import pickle

from src.preprocessing import Preprocessing
from src.feature_engineering import FeatureEngineering
from src.model import ModelTrainer
from src.evaluate import evaluate

df = pd.read_csv("data/raw/students_dataset.csv")

# Preprocessing
prep = Preprocessing(df)
df = prep.clean()
df, le = prep.encode_target()

# Save label encoder
pickle.dump(le, open("models/label_encoder.pkl", "wb"))

# Feature Engineering
fe = FeatureEngineering(df)
df = fe.apply()

# Train
trainer = ModelTrainer(df)
model, X_test, y_test = trainer.train()

# Evaluate
evaluate(model, X_test, y_test)

# -------------------------------
# ✅ Train vs Test Accuracy
# -------------------------------
train_acc = model.score(trainer.X_train, trainer.y_train)
test_acc = model.score(X_test, y_test)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)

# -------------------------------
# ✅ Cross Validation
# -------------------------------
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, trainer.X, trainer.y, cv=5)

print("Cross Validation Scores:", scores)
print("Average CV Score:", scores.mean())