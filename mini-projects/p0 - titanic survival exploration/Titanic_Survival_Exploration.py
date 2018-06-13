import numpy as np
import pandas as pd
from pprintpp import pprint

# RMS Titanic data visualization code
from titanic_visualizations import survival_stats
from IPython.display import display

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Store the 'Survived' feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """

    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)

    else:
        return "Number of predictions does not match number of outcomes!"

#survival_stats(data, outcomes, 'Age', ["Sex == 'male'", "Pclass <= 3", "SibSp == 0"])
#survival_stats(data, outcomes, 'Age', ["Sex == 'male'", "Pclass <= 3", "SibSp == 1"])
#survival_stats(data, outcomes, 'Age', ["Sex == 'male'", "Pclass < 2", "SibSp == 0"])
#survival_stats(data, outcomes, 'Age', ["Sex == 'male'", "Pclass < 2", "SibSp == 1"])
survival_stats(data, outcomes, 'Pclass', ["Sex == 'female'", "SibSp == 0"])
survival_stats(data, outcomes, 'Pclass', ["Sex == 'female'", "SibSp > 0"])

def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """

    predictions = []
    for _, passenger in data.iterrows():
        #print passenger

        # Remove the 'pass' statement below
        # and write your prediction conditions here
        if passenger['Sex'] == 'male':
            if passenger['Age'] < 10:
                predictions.append(1)
                print "%d" %(passenger['PassengerId'])
            else:
                if passenger['Pclass'] == 1:
                    if passenger['SibSp'] == 0:
                        if passenger['Age'] >= 10 and passenger['Age'] <= 40:
                            predictions.append(1)
                            print "%d" %(passenger['PassengerId'])
                        else:
                            predictions.append(0)
                            print "%d" %(passenger['PassengerId'])
                    elif passenger['SibSp'] > 0:
                        if passenger['Age'] >= 20 and passenger['Age'] <= 50:
                            predictions.append(1)
                            print "%d" %(passenger['PassengerId'])
                        else:
                            predictions.append(0)
                            print "%d" %(passenger['PassengerId'])
                else:
                    predictions.append(0)
                    print "%d" %(passenger['PassengerId'])
        elif passenger['Sex'] == 'female':
        	if passenger['Pclass'] == 3:
        		if passenger['SibSp'] > 0:
        			predictions.append(0)
        			print "%d" %(passenger['PassengerId'])
        		else:
        			predictions.append(1)
        			print "%d" %(passenger['PassengerId'])
        	else:
        		predictions.append(1)
        		print "%d" %(passenger['PassengerId'])

    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_3(data)

print accuracy_score(outcomes, predictions)
