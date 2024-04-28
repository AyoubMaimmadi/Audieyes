from flask import Flask, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, LSTM, Embedding, Input, Concatenate, Activation, RepeatVector, TimeDistributed
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask_cors import CORS

# Load ResNet50 pre-trained model
resnet_model = ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3), pooling='avg')

# Load vocabulary
vocab = np.load('vocab.npy', allow_pickle=True)
vocab = vocab.item()
inv_vocab = {v: k for k, v in vocab.items()}

# Constants
embedding_size = 128
max_len = 40
vocab_size = len(vocab)

# Input layers for both image and text
image_input = Input(shape=(2048,))
text_input = Input(shape=(max_len,))

# Image feature extraction model
image_dense = Dense(embedding_size, activation='relu')(image_input)
image_repeat = RepeatVector(max_len)(image_dense)

# Language model
text_embedding = Embedding(input_dim=vocab_size, output_dim=embedding_size)(text_input)
text_lstm = LSTM(256, return_sequences=True)(text_embedding)
text_time_dist = TimeDistributed(Dense(embedding_size))(text_lstm)

# Concatenate the outputs of both models
concatenated = Concatenate()([image_repeat, text_time_dist])
x = LSTM(128, return_sequences=True)(concatenated)
x = LSTM(512, return_sequences=False)(x)
outputs = Dense(vocab_size, activation='softmax')(x)

# Create the model
model = Model(inputs=[image_input, text_input], outputs=outputs)
model.compile(loss='categorical_crossentropy', optimizer='RMSprop', metrics=['accuracy'])

print("=" * 50)
print("Model loaded")

app = Flask(__name__)
CORS(app)

@app.route('/after', methods=['POST'])
def after():
    file = request.files['file']
    file.save('static/file.jpg')
    img = cv2.imread('static/file.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.reshape(img, (1, 224, 224, 3))
    
    features = resnet_model.predict(img).reshape(1, 2048)
    text_in = ['startofseq']
    final = ''

    for _ in range(20):
        encoded = [vocab[word] for word in text_in]
        padded = pad_sequences([encoded], maxlen=max_len, padding='post').reshape(1, max_len)
        sampled_index = np.argmax(model.predict([features, padded]))
        sampled_word = inv_vocab[sampled_index]
        
        if sampled_word == 'endofseq':
            break
        final += ' ' + sampled_word
        text_in.append(sampled_word)

    return jsonify({'caption': final})

if __name__ == "__main__":
    app.run(debug=True)
