import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from collections import Counter

from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
from keras import layers, regularizers
from keras.layers import Embedding, LSTM, Dense, SpatialDropout1D, Dropout

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()
stop = stopwords.words('english')
stop.extend(['@', '.', '#', 'user'])

# Loading Data and Sanity Checks
train_data_add = "./Data/dataset.csv"
train_data = pd.read_csv(train_data_add)

## Checking Data
print("Training Data")
print(train_data.head(3))
print("Length of Test data = ", len(train_data))
train_data.head(5)

# Pre-Procesing
"""
Pre-processing of data
    0) Making Every tweet to lowercase
    1) Tokenization
    2) Stop Word 
    3) Lemmatization
"""

## Converting to Lower Case
count = 0
for i in range(len(train_data)):
    try:
        train_data.iloc[i, 0] = train_data.iloc[i, 0].lower()
    except:
        train_data.iloc[i, 0] = str(train_data.iloc[i, 0]).lower()
        pass
print(" Training Data            : ", train_data.iloc[0, 0])

## Tokenization
tokens = []
for i in range(len(train_data)):
    tokens.append(nltk.word_tokenize(train_data.iloc[i, 0]))
print("After Tokenizing          : ", tokens[0])

## Stop Word Removal
filtered_tokens = []
for i in range(len(tokens)):
    filtered_tokens.append([word for word in tokens[i] if word not in stop])
print("After Removing Stop Words : ", filtered_tokens[0])

## Lemmatization
lemmatizers = []
for i in range(len(filtered_tokens)):
    lemmatizers.append([lemmatizer.lemmatize(word) for word in filtered_tokens[i]])
print("After Lemmatization       : ", lemmatizers[0])

total_words = []
for i in range(len(lemmatizers)):
    total_words.extend(lemmatizers[i])

## Extra Tokenizer

tokenizer = Tokenizer(
    num_words=len(total_words),
    filters= '"#$%&()*+-/:,;<=>@[\]^_`{|}~'
)
tokenizer.fit_on_texts(lemmatizers)

# Pictorial Analysis of Word Lengths

"""
 The next step currently is converting these words into numbers based on occurances and padding with zeros for length  
"""
word_lengths = []
for i in range(len(lemmatizers)):
    word_lengths.append(len(lemmatizers[i]))
mean = sum(word_lengths) / len(word_lengths)
plt.hist(word_lengths)
plt.show()
# Over here The max_length represents the max length of phrase taken inro consideration
max_len = int(mean)
print(" Mean Length of twitter tweets = ", max_len)

# One Hot Encoding of the Data
pos = []
mid = []
neg = []
for l in range(len(train_data.iloc[:, 1])):
    if train_data.iloc[l, 1] == 0:
        pos.append(0)
        mid.append(0)
        neg.append(1)
    elif train_data.iloc[l, 1] == 1:
        pos.append(0)
        mid.append(1)
        neg.append(0)
    else:
        pos.append(1)
        mid.append(0)
        neg.append(0)
train_data['Pos'] = pos
train_data['Mid'] = mid
train_data["Neg"] = neg
print("\n Training Data")
print(train_data.head(2))

# Finding Highest frequency of words and creating the int dict
lemmatizers_to_int = Counter(total_words)
total_word_count = len(total_words)
print("\n\nTotal Word Count          : ", total_word_count)

sorted_order = lemmatizers_to_int.most_common(total_word_count)
print("Most Repeated Word        : ", sorted_order[0][0])

vocab_to_index = {w: i + 1 for i, (w, c) in enumerate(sorted_order)}

## Encoding to numbers
num_encoded_reviews = []
for i in range(len(lemmatizers)):
    num_encoded_reviews.append([vocab_to_index[word] for word in lemmatizers[i]])
print("Num Encoded First Tweet   : ", num_encoded_reviews[0])

## Padding and truncating
padded_reviews = pad_sequences(num_encoded_reviews, maxlen=max_len)
print("Padded First Tweet        : ",padded_reviews[0])

# Modelling and Training
## X_train and Y_train
X_train = np.array(padded_reviews[0:int(len(padded_reviews) * 0.8)])
Y_train = train_data.loc[0:int(len(padded_reviews) * 0.8), ["Pos", "Mid", "Neg"]]

## X_test and Y_test
X_test = np.array(padded_reviews[int(len(padded_reviews) * 0.8):])
Y_test = train_data.loc[int(len(padded_reviews) * 0.8):len(padded_reviews), ["Pos", "Mid", "Neg"]]

checkpoint1_Model1 = ModelCheckpoint(".ipynb_checkpoints/best_mode1_15-02-2021.hdf5", monitor='accuracy', save_best_only=True,
                                     save_weights_only=False)
checkpoint1_Model2 = ModelCheckpoint(".ipynb_checkpoints/best_mode2_15-02-2021.hdf5", monitor='accuracy', save_best_only=True,
                                     save_weights_only=False)

## Model 1
# Now we are ready to train our model through LSTM network
model = Sequential()
model.add(layers.Embedding(len(vocab_to_index) + 1, output_dim=45, input_length=max_len))
model.add(SpatialDropout1D(0.3))
model.add(layers.LSTM(45))
model.add(layers.Dense(10, activation='relu', input_shape=(45,)))
model.add(layers.Dense(3, activation='softmax', input_shape=(10,)))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print("Model 1 : ")
print(model.summary())

# Our vectorized labels
model.fit(X_train, Y_train, validation_split=0.2, epochs=16, callbacks=[checkpoint1_Model1], verbose=1)

## Model 2
model_lstm = Sequential()
model_lstm.add(Embedding(input_dim=len(vocab_to_index) + 1, output_dim=256, input_length=max_len))
model_lstm.add(SpatialDropout1D(0.3))
model_lstm.add(LSTM(256, dropout=0.3, recurrent_dropout=0.3))
model_lstm.add(Dense(256, activation='relu'))
model_lstm.add(Dropout(0.3))
model_lstm.add(Dense(3, activation='softmax'))
model_lstm.compile(
    loss='categorical_crossentropy',
    optimizer='Adam',
    metrics=['accuracy']
)
print("Model 2 : ")
print(model_lstm.summary())

history = model_lstm.fit(
    X_train,
    Y_train,
    validation_split=0.1,
    epochs=16,
    batch_size=512,
    callbacks=[checkpoint1_Model2]
)

# Evaluation
## Model 1
# Evaluate the model on the test data using `evaluate`
print("Evaluate on test data")
results = model.evaluate(X_test, Y_test, batch_size=128)
print("test loss, test acc:", results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print("Generate predictions for 3 samples")
predictions = model.predict(X_test[:1])
print("predictions shape:", predictions.shape)

print(np.around(predictions, 2), np.array(Y_test[:1]))

# Evaluate the model on the test data using `evaluate`
print("Evaluate on test data")
results = model_lstm.evaluate(X_test, Y_test, batch_size=128)
print("test loss, test acc:", results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print("Generate predictions for 3 samples")
predictions = model_lstm.predict(X_test[:5])
print("predictions shape:", predictions.shape)

print(np.around(predictions, 2), np.array(Y_test[:5]))
