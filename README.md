# Hand Gesture Recogination

This project is a result of the Assignment in IIP subject taught in UG 4 year at LNMIIT where the main aim is to create a robust model which can solve a important problem using computer vision

## Motivation
* Humans interact with each other on many levels. Communication is one of the key feature which separates humans from other species.
* Some disabled people are not able to interact using the common way, i.e, through words. Dumb people are not able to speak and deaf people are not able to understand us.

* To bridge this gap in communication, humans have developed gestures to interact with such disabled people.


* For such people to use computer-operated devices to help them communicate in a better way with rest, we have come up with an idea for training the system to understand gestures. This can also be used by us in other areas to improve user experience.

## Application 
The application of such a tool can be endless. Some of such applications are:


* Communication ease for the physically challenged.

* Improved user experience for computers.

* New technologies in the field of televisions and other electronic devices.

## Proposed System

* We initialised with a self-made dataset of images which contained six classes. These classes represented the six numbers, from zero to five. The dataset contains binary images of hand gestures for these numbers.

* We tried some basic machine learning algorithms like Logistic Regression, Decision Trees and SVM for prediction but upon testing , the accuracy count was not as good as expected.

* As this could be termed as a computer vision task, we thought of trying out deep learning, using a basic CNN model. This gave us some pretty good results and we thought of continuing with this model.

![abc](https://user-images.githubusercontent.com/5564730/51240024-e17c6b00-19a0-11e9-9a8b-12dbbb8de206.jpg)

## Getting Started

Following are the instruction to you need to follow to get this project up and running into your local machine for testing and development purporse.

Following are the steps to create Python virtual environment for this project. This is recommended so that this project and other project can have its own dependencies, regardless of what dependencies every other project has.


### Installing

Following are the step by step to get a development env running

    1. Visit the Anaconda homepage.
    2. Click “Anaconda” from the menu and click “Download” to go to the download page.
    3. Choose the download suitable for your platform (Windows, OSX, or Linux):
    4. Follow the Installation wizard.
    5. Open the Anaconda Prompt and enter the following to create a python env
```
conda create -n myenv python=3.5
```
    6. Then enter the following commands to install the required dependencies for this project. 
```
conda install -n myenv scikit-learn
conda install -n myenv pandas
conda install -n myenv keras
```

## Running the Code 

1. Download/Clone this repository.
2. Go the location and open Anaconda Prompt/Termial and start the environment by 
```
activate myenv
```
3. After this you can run the program by executing the following line.
```
python predict.py
```

## Built With

* [scikit-learn](http://scikit-learn.org/) - Python Machine Learning Framework
* [Pandas](https://pandas.pydata.org/) - Python Data Analysis Library


## Authors

* **Dhruvraj Singh Rawat** - [LinkedIn](https://www.linkedin.com/in/dhruvrajrawat/)




