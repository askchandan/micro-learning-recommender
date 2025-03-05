
import pytest
from src.data.make_dataset import load_raw_data

def test_load_raw_data():
    skills_df, courses_df, interactions_df = load_raw_data()
    assert not skills_df.empty
    assert not courses_df.empty
    assert not interactions_df.empty
