import tensorflow as tf
from keras import models, layers

import matplotlib.pyplot as plt


# reference: https://www.tensorflow.org/tutorials/quickstart/beginner?hl=ko


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(f"x train shape    : {x_train.shape}")
print(f"x train[0] shape : {x_train[0].shape}")

model = models.Sequential([layers.Flatten(input_shape=(28, 28)),
                           layers.Dense(128, activation='relu'),
                           layers.Dropout(0.2),
                           layers.Dense(10, activation='softmax')])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test, verbose=2)

folder_path = "Chapter03/2022/project_sudoku/"
model_path = folder_path + 'mnist_tensorflow.h5'
model.save(model_path)
