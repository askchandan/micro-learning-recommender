
import pytest
from src.models.train_model import train_recommendation_model

def test_model_training():
    # Mock features and target for testing
    features = [[1, 2], [3, 4], [5, 6]]
    target = [10, 20, 30]
    model, X_test, y_test = train_recommendation_model(features, target)
    assert model is not None
