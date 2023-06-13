# Library imports
from flask import Flask, request, render_template
import string
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import regex as re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Create the app object
app = Flask(__name__)

with open("./sentiment_analysis_model.pickle",'rb') as f:
    model = pickle.load(f)
f.close()

with open("./sentiment_analysis_tokenizer.pickle",'rb') as f:
    tokenizer = pickle.load(f)
f.close()

max_len = 200 

def clean_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^A-Za-zÀ-ú ]+', '', text)
    # Analyzing the most used words below, i chose to exclude these because there are too many and are unnecessary
    text = re.sub('movi', '', text)
    # Convert to lower case
    text = text.lower()
    # remove scores
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(texto):
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(texto.lower())
    return " ".join([token for token in tokens if token not in stop_words])

def normalize_text(text):
    lemmatizer = WordNetLemmatizer()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

def predict_custom_text(input_text):
    input_text = clean_text(input_text)
    input_text = remove_stopwords(input_text)
    cleaned_text = normalize_text(input_text)
    
    input_sequences = tokenizer.texts_to_sequences([cleaned_text]) 
    padded_input = pad_sequences(input_sequences, maxlen = max_len)
    prediction = model.predict(padded_input)[0]
    sentiment = "Positive" if prediction > 0.5 else "Negative"
    return sentiment

# Define predict function
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    new_review = [str(x) for x in request.form.values()]

    sentiment = predict_custom_text(new_review[0])
    return render_template('index.html', prediction_text=sentiment)


if __name__ == "__main__":
    app.run(debug=True)
