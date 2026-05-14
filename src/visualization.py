import matplotlib.pyplot as plt
import seaborn as sns


def plot_reason_distribution(df):
    """
    Plot distribution of emergency call reasons.
    """
    
    plt.figure(figsize=(8,5))
    
    sns.countplot(x='Reason', data=df)
    
    plt.title('Distribution of Emergency Call Reasons')
    
    plt.xlabel('Emergency Type')
    
    plt.ylabel('Number of Calls')
    
    plt.tight_layout()