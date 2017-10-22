import csv

def load_csv(filename):
    lines = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            lines.append(line)
    return lines

def load_adult_data():
    return load_csv("adult.data")

# Note: Possibly use different data for training and validation to get a more accurate result, 
# but remember that in the last part your model will be trained on the full training data
# load_adult_data() and be tested on a test dataset you don't have access to.
def load_adult_train_data():
    return load_adult_data()

def load_adult_valid_data():
    return load_adult_data()

