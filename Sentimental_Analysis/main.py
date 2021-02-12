# Header Files
import pandas as pd
import numpy as np

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from collections import Counter

from keras.preprocessing.sequence import pad_sequences

from keras.models import Sequential
from keras.callbacks import ModelCheckpoint
from keras import layers, regularizers

lemmatizer = WordNetLemmatizer()
stop = stopwords.words('english')
stop.extend(['@', '.', '#', 'user'])

# Loading Train and Test Data
train_data_add = "./Data/train.csv"
test_data_add = "./Data/test.csv"
train_data = pd.read_csv(train_data_add)
test_data = pd.read_csv(test_data_add)

train_data = train_data[0:10]
test_data  = test_data[0:10]

# Checking Data
print("Training Data")
print(train_data.head(3))
print("Length of Test data = ", len(train_data))
print("\nTest Data")
print(test_data.head(3))
print("Length of Test data = ", len(test_data))

"""
            Pre-processing of data
    0) Making Every tweet to lowercase
    1) Tokenization
    2) Stop Word 
    3) Lemmatization
"""

# Converting to Lower Case
for i in range(len(train_data)):
    train_data.iloc[i, 2] = train_data.iloc[i, 2].lower()
print(train_data.head(5))

# Tokenization
tokens = []
for i in range(len(train_data)):
    tokens.append(nltk.word_tokenize(train_data.iloc[i, 2]))
print("After Tokenizing          : ", tokens[0])

# Stop Word Removal
filtered_tokens = []
for i in range(len(tokens)):
    filtered_tokens.append([word for word in tokens[i] if word not in stop])
print("After Removing Stop Words : ", filtered_tokens[0])

# Lemmatization
lemmatizers = []
for i in range(len(filtered_tokens)):
    lemmatizers.append([lemmatizer.lemmatize(word) for word in filtered_tokens[i]])
print("After Lemmatization       : ", lemmatizers[0])

"""
 The next step currently is converting these words into numbers based on occurances and padding with zeros for length  
"""
total_words=[]
for i in range(len(lemmatizers)):
    total_words.extend(lemmatizers[i])

# Finding Highest frequency of words and creating the int dict
lemmatizers_to_int = Counter(total_words)
total_word_count = len(total_words)
sorted_order = lemmatizers_to_int.most_common(total_word_count)
print(lemmatizers_to_int)

vocab_to_index = {w: i+1 for i, (w, c) in enumerate(sorted_order)}
print(vocab_to_index)

# Encoding to numbers
num_encoded_reviews = []
for i in range(len(lemmatizers)):
    num_encoded_reviews.append([vocab_to_index[word] for word in lemmatizers[i]])
print(num_encoded_reviews)

# Padding and truncating
padded_reviews = pad_sequences(num_encoded_reviews, maxlen=50)
print(padded_reviews)

# Now we are ready to train our model through LSTM network

model = Sequential()
model.add(layers.Embedding(1000, 64))
model.add(layers.LSTM(15, dropout=0.5))
model.add(layers.Dense(1,activation='softmax', input_shape=(50,)))

model.compile(optimizer='rmsprop',loss='binary_crossentropy', metrics=['accuracy'])

checkpoint1 = ModelCheckpoint("best_mode1_11-02-2021.hdf5",monitor='val-accuracy',save_best_only = True, save_weights_only= False)

# Our vectorized labels
y_train = np.asarray(np.array(train_data.iloc[:,1])).astype('float32').reshape((-1,1))

history = model.fit(np.array(padded_reviews), y_train , validation_split=0.2, epochs=50, callbacks=[checkpoint1], verbose=2 )


print(history)