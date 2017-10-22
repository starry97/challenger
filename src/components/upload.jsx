import React, { Component } from 'react';
import Dropzone from 'react-dropzone';
import './upload.css';
import Loading from 'react-loading-animation';

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
      isLoading: false
    }
  }

  async addPhoto(acceptedFiles) {
    document.getElementById("avg").innerHTML = '';
    document.getElementById("max").innerHTML = '';
    document.getElementById("min").innerHTML = '';
    let this_ = this;
    console.log(this.state.isLoading);
    this.setState({
      isLoading: true
    });
    await acceptedFiles.forEach(file => {
      var fileName = file.name;
      var key = username + '/' + fileName;
      s3.upload({
        Bucket: "dubhacks17",
        Key: key,
        Body: file,
      }, async function(err, data) {
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
        fetch("http://ec2-52-206-17-234.compute-1.amazonaws.com:8000", param)
        .then((response) => {
          if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
              response.status);
            return;
          }
          response.json().then((data) => {
            document.getElementById("avg").innerHTML = 'Average number of audience focused: ' + data.avg_focus;
            document.getElementById("max").innerHTML = 'Max number of audience focused: ' + data.max_focus;
            document.getElementById("min").innerHTML = 'Min number of audience focused: ' + data.min_focus;
          }).then(() => {
            this_.setState({
              isLoading: false
            })
          });
        }).catch(err => {
          console.log(err);
        });
      });  
    }); 
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

    const loading = <Loading isLoading={this.state.isLoading}></Loading>;
    const result = 
      <div className='result'>
        <div id='avg'></div>
        <div id='min'></div>
        <div id='max'></div>
      </div>
    
    return (
      <div className='upload' id='upload'>
        {loading}
        {result}
        {dropzone}
      </div>
    );
  }
}