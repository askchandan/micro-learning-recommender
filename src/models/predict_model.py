
def recommend_courses(model, user_features, available_courses, top_k=5):
    """Generate course recommendations"""
    # Placeholder recommendation logic
    predictions = model.predict(user_features)
    top_recommendations = sorted(zip(available_courses, predictions), key=lambda x: x[1], reverse=True)[:top_k]
    return top_recommendations
