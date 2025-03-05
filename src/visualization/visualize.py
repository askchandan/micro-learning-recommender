
import matplotlib.pyplot as plt
import seaborn as sns

def plot_skill_distribution(skills_data):
    """Visualize skill distribution"""
    plt.figure(figsize=(10, 6))
    skills_data['skill_category'].value_counts().plot(kind='bar')
    plt.title('Skill Distribution')
    plt.xlabel('Skill Category')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('skill_distribution.png')
