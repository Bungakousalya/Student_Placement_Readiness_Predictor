
import numpy as np
class FeatureEngineering:

    def __init__(self, df):
        self.df = df

    def apply(self):

        self.df["consistency_score"] = (
            0.4 * (self.df["study_hours_per_day"] / 8) +
            0.3 * (self.df["dsa_problems_solved"] / 300).clip(upper=1) +
            0.3 * (self.df["attendance_percentage"] / 100)
        )

        self.df["effort_score"] = (
            self.df["study_hours_per_day"] * self.df["consistency_score"]
        )

        self.df["stress_sleep_ratio"] = (
            self.df["stress_level"] / self.df["sleep_hours"].replace(0, np.nan)
        ).fillna(self.df["stress_level"].median())

        self.df["burnout_score"] = (
            0.5 * self.df["stress_level"] +
            0.3 * (8 - self.df["sleep_hours"]) +
            0.2 * (1 - self.df["consistency_score"]) * 10
        )

        self.df["practice_growth_rate"] = (
            self.df["dsa_problems_solved"] /
            (self.df["study_hours_per_day"].replace(0, np.nan) * 30)
        ).fillna(0)

        self.df["prep_index"] = (
            0.25 * (self.df["cgpa"] / 10) +
            0.20 * (self.df["mock_test_score"] / 100) +
            0.15 * (self.df["projects_count"].clip(upper=5) / 5) +
            0.15 * (self.df["resume_score"] / 100) +
            0.15 * self.df["consistency_score"] +
            0.10 * (self.df["core_subjects_confidence"] / 5)
        )

        # Flags
        self.df["low_cgpa_flag"] = (self.df["cgpa"] < 6.5).astype(int)
        self.df["high_stress_flag"] = (self.df["stress_level"] > 7).astype(int)
        self.df["low_dsa_flag"] = (self.df["dsa_problems_solved"] < 150).astype(int)
        self.df["low_sleep_flag"] = (self.df["sleep_hours"] < 5).astype(int)

        return self.df