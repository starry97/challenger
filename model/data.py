import csv
import json

# def load_csv(filename):
#     jsonstring = json.dumps(filename)
#     print jsonstring
#
#     json_data = json.loads(filename)
#     csv_file_name = "face.scv"
#     csv_data = open(csv_file_name, 'w')
#     csvwriter = csv.writer(csv_data)
#     count = 0
#     for face in json_data:
#         if count == 0:
#             header = face['scores'].keys()
#             csvwriter.writerow(header)
#             count += 1
#         csvwriter.writerow(face['scores'].values())
#     lines = []
#     with open(json.loads(filename)) as csvfile:
#         reader = csv.DictReader(csvfile)
#         for line in reader:
#             lines.append(line)
#     return lines

def load_adult_data():
    with open("face.json") as json_data:
        data = json.load(json_data)
        json_data.close()
        list = []
        for face in data:

            list.append(face['scores'])
        print list
        return list
    # return load_csv("face.data")

# Note: Possibly use different data for training and validation to get a more accurate result, 
# but remember that in the last part your model will be trained on the full training data
# load_adult_data() and be tested on a test dataset you don't have access to.
def load_adult_train_data():
    return load_adult_data()

def load_adult_valid_data():
    return load_adult_data()

