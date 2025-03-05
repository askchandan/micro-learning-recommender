
import pytest
import pandas as pd
from src.features.skill_embedding import create_skill_embeddings

def test_skill_embeddings():
    # Mock skills data for testing
    mock_skills_data = pd.DataFrame({'skill_name': ['Python', 'Machine Learning', 'Data Science']})
    embeddings = create_skill_embeddings(mock_skills_data)
    assert embeddings is not None
