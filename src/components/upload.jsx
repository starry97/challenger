import React, { Component } from 'react';
import Dropzone from 'react-dropzone';
import './upload.css';
import Loading from './loading.jsx';

const AWS = require('aws-sdk');

AWS.config.update({
  accessKeyId: "AKIAJFOVQUF3EYLXWPHA",
  secretAccessKey: "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",
  region: "us-west-2"
});

const s3 = new AWS.S3();
const username = "temp-user";

export class Uploader extends Component {
  constructor() {
    super();
    this.state = {
      isLoading: true,
      result: ""
    }
  }

  addPhoto(acceptedFiles) {
    acceptedFiles.forEach(file => {
      var fileName = file.name;
      var key = username + '/' + fileName;
      s3.upload({
        Bucket: "dubhacks17",
        Key: key,
        Body: file,
      }, function(err, data) {
        if (err) {
          return alert('There was an error uploading your photo: ', err.message);
        }
        console.log('Successfully uploaded photo.');
        const formData = new FormData();
        formData.append("username", username);
        formData.append("input_address", username);
        var param = {
          method: 'POST',
          mode: 'cors',
          body: formData
        };
        fetch("http://localhost:8000", param)
        .then((response) => {
          if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
              response.status);
            return;
          }
          response.json().then((data) => {
            document.getElementById("result").innerHTML = JSON.stringify(data);
          });
        }).catch(err => {
          console.log(err);
        });
      });  
    });    
  }

  renderDataVis() {

  }
  
  render() {
    const dropzone =  
      <Dropzone
        multiple={true}
        accept="image/*"
        onDrop={this.addPhoto.bind(this)}
        className={'upload-area'}
        activeClassName='active'
        acceptClassName='accepted'
        rejectClassName='rejected'
      >
        <p>Drop your pictures here</p>
      </Dropzone>;

    const loading = <Loading />;
    const result = 
      <div id='result'>
      </div>
    

    return (
      <div className='upload' id='upload'>
        {this.isLoading ? loading : result}
        {dropzone}
      </div>
    );
  }
}