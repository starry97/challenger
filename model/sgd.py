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
        point["label"] = r['res']

        features = []
        features.append(1.)
        features.append(float(r['anger']))
        features.append(float(r['contempt']))
        features.append(float(r['disgust']))
        features.append(float(r['fear']))
        features.append(float(r['happiness']))
        features.append(float(r['neutral']))
        features.append(float(r['sadness']))
        features.append(float(r['surprise']))
        
        point['features'] = features
        data.append(point)
    return data

def extract_features_single_point(r):
    point = {}
    # point["label"] = r['res']

    features = []
    features.append(1.) 
    features.append(float(r['anger']))
    features.append(float(r['contempt']))
    features.append(float(r['disgust']))
    features.append(float(r['fear']))
    features.append(float(r['happiness']))
    features.append(float(r['neutral']))
    features.append(float(r['sadness']))
    features.append(float(r['surprise']))
    
    point['features'] = features
    return point

# TODO: Tune your parameters for final submission
def submission(data):
    return train(data, 100, 0.001, 0.0001)
    
