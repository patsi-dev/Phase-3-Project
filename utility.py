# This file contains functions for different stages in the modeling process.
# import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# function to plot distribution of categorical features
def plot_categorical_distribution(data, column, title='Distribution Plot'):
    """
    Plots the distribution of a categorical column using a count plot.

    Parameters:
    data : pandas.DataFrame
        The DataFrame containing the data.
    column : str
        The column name to plot.
    title : str, optional
        Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x=column)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()




# function to plot categorical features vs H1N1 for bivariate analysis
def categorical_h1n1(data, column, title='Bivariate Plot'):
    """
    This function plots the distribution of a categorical feature, with churn as a comparative variable

    Parameters:
        df(pd.DataFrame): The input dataframe
        column: The categorical column to plot
    """

    # plot the distribution
    plt.figure(figsize=(10, 5))
    h1n1_count = data.groupby(column)['h1n1_vaccine'].sum().sort_values(ascending=False)
    top_10_categories = h1n1_count.head(10).index.tolist()
    sns.countplot(x=column, hue='h1n1_vaccine', data=data, order=top_10_categories)
    plt.title(title)
    plt.xlabel(column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(loc='upper right')
    plt.show()
    


def plot_confusion_matrix(y_true, y_pred, labels, title='Confusion Matrix'):
    """
    Plots a confusion matrix.

    Parameters:
    y_true : array-like
        True labels.
    y_pred : array-like
        Predicted labels.
    labels : list
        List of class labels to display.
    title : str
        Title of the plot.
    """
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap=plt.cm.Blues)
    plt.title(title)
    figsize=(15, 5)
    plt.show()



