# Chatbot Developed with Flask and JavaScript

Chatbot is used to answer the question, It works as a support team to and help to resolve the queries for your customer.

## Initial Setup:

Clone repo and create a virtual environment
```
$ git clone https://github.com/Adtya09/Chat-Bot.git
$ cd chatbot-deployment
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install  -r requirements.txt

```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot as the behaviour you required.

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```
To Run as a web app use the below commands.

```
$ (venv) python app.py
```

Now the ChatBot will be available at http://localhost:5001

