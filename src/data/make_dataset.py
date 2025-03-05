
import pandas as pd

def load_raw_data():
    """Load raw data from CSV files"""
    skills_df = pd.read_csv('data/raw/skills_data.csv')
    courses_df = pd.read_csv('data/raw/courses_data.csv')
    interactions_df = pd.read_csv('data/raw/user_interactions.csv')
    return skills_df, courses_df, interactions_df
