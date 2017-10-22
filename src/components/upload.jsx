import React, { Component } from 'react';
import Dropzone from 'react-dropzone';
import './upload.css';

const AWS = require('aws-sdk');

AWS.config.update({
  accessKeyId: "AKIAJFOVQUF3EYLXWPHA",
  secretAccessKey: "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",
  region: "us-west-2"
});

const s3 = new AWS.S3();
const username = "temp-user";

export class Uploader extends Component {

  componentDidMount() {
    const formData = new FormData();
    formData.append("username", "temp-user");
    formData.append("input_address", "http://s3.amazonaws.com/dubhacks17/temp-user");
    var param = {
      method: 'POST',
      mode: 'cors',
      body: formData
    };
    fetch("http://localhost:8000", param)
    .then((response) => {
      console.log(response);
      // perform setState here
    }).catch(err => {
      console.log(err);
    });
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
      });  
    });
  }

  render() {
    return (
      <div className='upload' id='upload'>
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
          
          
        </Dropzone>
      </div>
    );
  }
}