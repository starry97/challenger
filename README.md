# Challenger :+1:

## This is the repo for team *Challenger* @ Dubhacks 2017!

## Team member:
* Xukai (Antony) Liu
* Dawei (David) Shen
* Bowen Sun
* Lingyue (Cynthia) Zhang

## Project description:
Our project focuses on the 3rd challenge of Dubhacks2017:
> Craft sustainable experiences 
> that break down barriers for 
> your local communities.

Specifically, we use *Microsoft EmotionAPI* and *machine learning* algorithm
to assess the level of focus for lecture audience. 

For most of the times, audience/students and lecturers/professors are blocked by some 
barriers, where lecturers don't know how are the audience feeling during the time period.
Our project can analyze photos taken during the lecture and give feedback to the lecturer about
whether the audience is focused on the content or not throughout the entire time period.
We can also find the highest and lowest point of focusing level to help improving the 
lecture/presentation based on those data.

## Project architecture:
### Interface:
Our web app lets users upload some images of the audience for analyzing, then we show users 
our report about the audience.

### Structure:
We store user uploaded images into our *AWS S3* buckets, and then calls the *Microsoft EmotionAPI* 
for each image that user uploaded to get the emotion scores for each person in the image. Then we pass
those scores into a *machine learning* model we trained to get a level of focusing for each audience.
We show the focusing level to the user and also report which point has the highest/lowest level of focus.

```
|front end|     ->  |AWS S3|    ->  |MS EmotionAPI|     ->  |Logistic Regression model|     ->  |front end|
image upload    ->  storage     ->  Analyze emotions    ->  convert to focusing level       ->  report result
```
