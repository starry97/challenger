from flask import Flask, request, jsonify
from flask_cors import CORS
from os import listdir
from os.path import isfile, join
import json
from sgd import logistic, dot, predict, accuracy, submission, extract_features, extract_features_single_point
from data import load_adult_train_data, load_adult_valid_data
from main import emotion_api, compute_for_username

app = Flask(__name__)
CORS(app)
model = None

@app.route('/', methods=['POST'])
def result():
    """
    Please call url "http://localhost/8000"
    """
    username = request.form['username']
    input_address = request.form['input_address']
    # get predictions for all pictures in the input_address
    predictions, max_num_faces = getPredictions(username, input_address)
    max_focus = 0
    min_focus = max_num_faces
    avg_focus = 0.0

    for prediction in predictions:
        num_not_focus = max_num_faces - len(prediction)
        for face in prediction:
            if face["result"] is 0:
                num_not_focus += 1
        max_focus = max(max_focus, max_num_faces - num_not_focus)
        min_focus = min(min_focus, max_num_faces - num_not_focus)
        avg_focus += max_num_faces - num_not_focus
        print "There are " + str(num_not_focus) + " out of " + str(max_num_faces) + " students are not focusing on the lecture."
    avg_focus /= len(predictions)
    response = {}
    response["avg_focus"] = avg_focus
    response["max_focus"] = max_focus
    response["min_focus"] = min_focus
    
    return jsonify(response) # response to your request.

def getPredictions(username, input_address):
    # read all filenames in the input folder
    data_list = compute_for_username(username)
    max_num_faces = 0
    # predictions for all pictures
    predictions_all = []
    
    # filename should be in format: <unique filename>_<number of faces in picture>
    for data in data_list:
        print(data)
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
    # prepare the model
    train_data = extract_features(load_adult_train_data())
    model = submission(train_data)
    print model
    predictions = [predict(model, p) for p in train_data]
    print
    print
    print "Training Accuracy:", accuracy(train_data, predictions)

    app.run(host='0.0.0.0', port=8000, threaded=True)
