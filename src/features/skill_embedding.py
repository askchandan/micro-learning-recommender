
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def create_skill_embeddings(skills_data):
    """Create skill embeddings"""
    vectorizer = TfidfVectorizer()
    skill_embeddings = vectorizer.fit_transform(skills_data['skill_name'])
    return skill_embeddings
