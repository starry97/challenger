from math import exp
import random

# TODO: Calculate logistic
def logistic(x):
    return 1.0 / (1 + exp(-x))

# TODO: Calculate dot product of two lists
def dot(x, y):
    assert len(x) == len(y)
    s = 0
    for i in range(len(x)):
        s += x[i] * y[i]
    return s

# TODO: Calculate prediction based on model
def predict(model, point):
    return logistic(dot(model, point['features']))

# TODO: Calculate accuracy of predictions on data
def accuracy(data, predictions):
    assert len(data) == len(predictions)
    correct = 0
    for i in range(len(data)):
        point = data[i]
        if (predictions[i] >= 0.5 and point['label'] == 1) or (predictions[i] < 0.5 and point['label'] ==0):
            correct += 1
    return float(correct)/len(data)


# TODO: Update model using learning rate and L2 regularization
def update(model, point, delta, rate, lam):
    prediction = predict(model, point)
    features = point['features']
    actual = point['label']
    for i in range(len(model)):
        model[i] -= rate * (- lam * model[i] + features[i] * (prediction - actual))

def initialize_model(k):
    return [random.gauss(0, 1) for x in range(k)]

# TODO: Train model using training data
def train(data, epochs, rate, lam):
    used = []
    model = initialize_model(len(data[0]['features']))
    for i in range(epochs):
        for n in range(len(data)):
            point = random.choice(data)
            update(model, point, 0, rate, lam)
    return model
        
def extract_features(raw):
    data = []
    for r in raw:
        point = {}
        point["label"] = (r['income'] == '>50K')

        features = []
        features.append(1.) 
        features.append(float(r['age'])/100)
        features.append(float(r['education_num'])/20)
        features.append(r['marital'] == 'Married-civ-spouse')
        #TODO: Add more feature extraction rules here!
        features.append(r['education'] in ['Doctorate'])
        
        features.append(float(r['hr_per_week'])/50)
        #features.append(r['race'] == 'White')
        #features.append(r['occupation'] == 'Exec-managerial')
        #features.append(int(r['capital_loss']) > 10)
        features.append(r['relationship'] == 'Husband' and r['race'] == 'White' 
                        and r['type_employer'] == 'Self-emp-inc')
        filter_marital = ['Divorced', 'Widowed' 'Separated', 'Never-married']
        features.append(r['marital'] in filter_marital)
        filter_countries = ['Dominican-Republic', 'El-Salvador', 'Greece', 
                            'Guatemala', 'Haiti', 'Honduras', 'Hungary', 'Mexico', 'Nicaragua',
                            'Vietnam']
        features.append(r['country'] in filter_countries)
        
        features.append(float(r['fnlwgt'])/600000)
        
        features.append(int(r['capital_gain'])-int(r['capital_loss']) > 0)
        
        point['features'] = features
        data.append(point)
    return data

# TODO: Tune your parameters for final submission
def submission(data):
    return train(data, 100, 0.001, 0.0001)
    
