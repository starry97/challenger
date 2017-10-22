from flask import Flask, request
from os import listdir
from os.path import isfile, join
import json
from sgd import logistic, dot, predict, accuracy, submission, extract_features
from data import load_adult_train_data, load_adult_valid_data
from main import emotion_api

app = Flask(__name__)
model = None

@app.route('/', methods=['POST'])
def result():
    """
    Please call url "http://localhost/8000"
    """
    username = request.form['username']
    input_address = request.form['input_address']
    predictions, max_num_faces = getPredictions(username, input_address)
    
    
    return 'Received !' # response to your request.

def getPredictions(username, input_address):
    # read all filenames in the input folder
    filename_list = [f for f in listdir(input_address) if isfile(join(input_address, f))]
    max_num_faces = 0
    # predictions for all pictures
    predictions_all = []
    
    # filename should be in format: <unique filename>_<number of faces in picture>
    for filename in filename_list:
        print(filename)
        data = emotionAPI(filename)
        item_dict = json.loads(data)
        max_num_faces = max(max_num_faces, len(item_dict))
        
        # predict for result of one picture
        predictions = []
        for i in range(0, len(item_dict)):
            face = {}
            face["faceRectangle"] = item_dict[i]["faceRectangle"]
            face["result"] = (predict(model, extract_features_single_point(item_dict[i]["scores"])) >= 0.5)
            predictions.append(face)
        predictions_all.append(predictions)
        
    print max_num_faces
    return predictions_all, max_num_faces

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=8000)
     # prepare the model
     train_data = extract_features(load_adult_train_data())
     model = submission(train_data)