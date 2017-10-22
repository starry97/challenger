from math import exp
import random

# TODO: Calculate logistic
def logistic(x):
    if x < 0:
        return 1 - 1 / (1 + exp(x))
    else:
        return 1 / (1 + exp(-x))

# TODO: Calculate dot product of two lists
def dot(x, y):
    s = sum([i * j for (i, j) in zip(x, y)])
    return s

# TODO: Calculate prediction based on model
def predict(model, point):
    return logistic(dot(model, point['features']))

# TODO: Calculate accuracy of predictions on data
def accuracy(data, predictions):
    correct = 0
    for i in range(len(data)):
        if data[i]['label'] == 1 and predictions[i] > 0.5:
            correct += 1
        if data[i]['label'] == 0 and predictions[i] <= 0.5:
            correct += 1
    return float(correct)/len(data)

# TODO: Update model using learning rate and L2 regularization
def update(model, point, delta, rate, lam):
    for i in range(len(point['features'])):
        gradient = point['features'][i] * delta - lam * model[i]
        model[i] += rate * gradient

def initialize_model(k):
    return [random.gauss(0, 1) for x in range(k)]

# TODO: Train model using training data
def train(data, epochs, rate, lam):
    model = initialize_model(len(data[0]['features']))
    for i in range(epochs):
        random.shuffle(data)
        for j in range(len(data)):
            point = data[j]
            prediction = predict(model, point)
            delta = point['label'] - prediction
            # decrease learning rate over time
            r = float(rate) / (i + 1)
            update(model, point, delta, r, lam)
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
        #TODO: Add more feature extraction rules here!

        # capital gain / loss
        features.append(float(r['capital_loss']) / 1000)
        features.append(float(r['capital_gain']) / 10000)

        # hr_per_week
        features.append(float(r['hr_per_week']) / 100)

        # education
        features.append(r['education'] == 'Masters')
        features.append(r['education'] == 'Prof-school')
        features.append(r['education'] == 'Doctorate')
        features.append(r['education'] == 'Masters')
        features.append(r['education'] == 'Bachelors')
        features.append(r['education'] == 'Assoc-voc')
        features.append(r['education'] == 'Assoc-acdm')
        features.append(r['education'] == 'Some-college')
        features.append(r['education'] == 'HS-grad')
        features.append(r['education'] == '11th')
        features.append(r['education'] == '10th')
        features.append(r['education'] == '9th')
        features.append(r['education'] == '7th-8th')
        features.append(r['education'] == '5th-6th')
        features.append(r['education'] == '1st-4th')
        features.append(r['education'] == 'Preschool')

        # type_employer
        features.append(r['type_employer'] == 'Federal-gov')
        features.append(r['type_employer'] == 'Local-gov')
        features.append(r['type_employer'] == 'Self-emp-not-inc')
        features.append(r['type_employer'] == 'State-gov')
        features.append(r['type_employer'] == 'Private')
        features.append(r['type_employer'] == 'Self-emp-inc')
        features.append(r['type_employer'] == 'Without-pay')

        # sex
        features.append(r['sex'] == 'Female')
        features.append(r['sex'] == 'Male')

        # race
        features.append(r['race'] == 'White')
        features.append(r['race'] == 'Black')
        features.append(r['race'] == 'Asian-Pac-Islander')
        features.append(r['race'] == 'Amer-Indian-Eskimo')
        features.append(r['race'] == 'Other')

        # relationship
        features.append(r['relationship'] == 'Own-child')
        features.append(r['relationship'] == 'Unmarried')
        features.append(r['relationship'] == 'Not-in-family')
        features.append(r['relationship'] == 'Husband')
        features.append(r['relationship'] == 'Wife')
        features.append(r['relationship'] == 'Other-relative')

        # marital
        features.append(r['marital'] == 'Married-civ-spouse')
        features.append(r['marital'] == 'Never-married')
        features.append(r['marital'] == 'Divorced')
        features.append(r['marital'] == 'Widowed')
        features.append(r['marital'] == 'Separated')
        features.append(r['marital'] == 'Married-spouse-absent')

        # occupation
        features.append(r['occupation'] == 'Exec-managerial')
        features.append(r['occupation'] == 'Craft-repair')
        features.append(r['occupation'] == 'Other-service')
        features.append(r['occupation'] == 'Adm-clerical')
        features.append(r['occupation'] == 'Sales')
        features.append(r['occupation'] == 'Machine-op-inspct')
        features.append(r['occupation'] == 'Handlers-cleaners')
        features.append(r['occupation'] == 'Transport-moving')
        features.append(r['occupation'] == 'Prof-specialty')
        features.append(r['occupation'] == 'Farming-fishing')
        features.append(r['occupation'] == 'Protective-serv')
        features.append(r['occupation'] == 'Tech-support')
        features.append(r['occupation'] == 'Armed-Forces')
        features.append(r['occupation'] == 'Priv-house-serv')

        # country
        features.append(r['country'] == 'United-States')
        features.append(r['country'] == 'Mexico')
        features.append(r['country'] == 'Puerto-Rico')
        features.append(r['country'] == 'Vietnam')
        features.append(r['country'] == 'Columbia')
        features.append(r['country'] == 'Ireland')
        features.append(r['country'] == 'Italy')
        features.append(r['country'] == 'Poland')
        features.append(r['country'] == 'Canada')
        features.append(r['country'] == 'Peru')
        features.append(r['country'] == 'Thailand')
        features.append(r['country'] == 'Hong')
        features.append(r['country'] == 'Germany')
        features.append(r['country'] == 'Ecuador')
        features.append(r['country'] == 'El-Salvador')
        features.append(r['country'] == 'Philippines')
        features.append(r['country'] == 'Portugal')
        features.append(r['country'] == 'Japan')
        features.append(r['country'] == 'England')
        features.append(r['country'] == 'South')
        features.append(r['country'] == 'Taiwan')
        features.append(r['country'] == 'Trinadad&Tobago')
        features.append(r['country'] == 'Dominican-Republic')
        features.append(r['country'] == 'Cuba')
        features.append(r['country'] == 'Jamaica')
        features.append(r['country'] == 'Yugoslavia')
        features.append(r['country'] == 'Greece')
        features.append(r['country'] == 'Scotland')
        features.append(r['country'] == 'China')
        features.append(r['country'] == 'Hungary')
        features.append(r['country'] == 'Iran')
        features.append(r['country'] == 'France')
        features.append(r['country'] == 'Nicaragua')
        features.append(r['country'] == 'Guatemala')
        features.append(r['country'] == 'Haiti')
        features.append(r['country'] == 'Honduras')
        features.append(r['country'] == 'Outlying-US(Guam-USVI-etc)')
        features.append(r['country'] == 'Cambodia')
        features.append(r['country'] == 'Laos')
        features.append(r['country'] == 'Holand-Netherlands')

        point['features'] = features
        data.append(point)
    return data



# return a dictionary of all possible features in the data
# and count how many of them in each label respectively
def analyse_data(raw):
    manu = {}
    for r in raw:
        for category in r.keys():
            if len(manu) < len(r):
                if r['income'] == '>50K':
                    manu[category] = [(r[category], 1, 0)]
                else:
                    manu[category] = [(r[category], 0, 1)]
            else:
                added = False
                for i in range(len(manu[category])):
                    f, c1, c2 = manu[category][i]
                    if f == r[category]:
                        manu[category].remove((f, c1, c2))
                        if r['income'] == '>50K':
                            manu[category].append((r[category], c1+1, c2))
                        else:
                            manu[category].append((r[category], c1, c2+1))
                        added = True
                        break
                if not added:
                    if r['income'] == '>50K':
                        manu[category].append((r[category], 1, 0))
                    else:
                        manu[category].append((r[category], 0, 1))


    for c in manu.keys():
        print c, " ", manu[c]
        print

    for c in manu.keys():
        print c, " ", len(manu[c])



# TODO: Tune your parameters for final submission
def submission(data):
    epochs = 40
    rate = 0.14
    lam = 0.000001
    n = 5
    # check the accuracy on the train data set to avoid bad models
    # return the model with the median accuracy on train data set
    models = {}
    random.shuffle(data)
    valid = random.sample(data, int(0.3 * len(data)))
    for i in range(n):
        model = train(data, epochs, rate, lam)
        predictions = [predict(model, p) for p in valid]
        acc = accuracy(valid, predictions)
        models.update({acc: model})
    return models[median(models.keys())]

# find the median in a list of numbers
def median(list):
    l = sorted(list)
    if len(l) == 1:
        return l[0]
    else:
        return l[(len(l)+1)/2-1]

