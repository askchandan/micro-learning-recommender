
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_recommendation_model(features, target):
    """Train recommendation model"""
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    return model, X_test, y_test
