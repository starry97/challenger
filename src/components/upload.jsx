import React, { Component } from 'react';
import Dropzone from 'react-dropzone';
const AWS = require('aws-sdk');

AWS.config.update({
  accessKeyId: "AKIAJFOVQUF3EYLXWPHA",
  secretAccessKey: "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",
  region: "us-west-2"
});

const s3 = new AWS.S3();
const username = "temp-user";

export class Uploader extends Component {
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
      <div>
        <Dropzone
          multiple={true}
          accept="image/*"
          onDrop={this.addPhoto.bind(this)}
        />
      </div>
    );
  }
}