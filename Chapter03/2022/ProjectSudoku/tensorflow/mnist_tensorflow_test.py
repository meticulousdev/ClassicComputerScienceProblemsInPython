from keras import models, layers
import tensorflow as tf
import cv2
import numpy as np
import matplotlib.pyplot as plt


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print(f"x train shape    : {x_train.shape}")
print(f"x train[0] shape : {x_train[0].shape}")


folder_path = "Chapter03/2022/project_sudoku/tensorflow/"
model_path = folder_path + 'mnist_tensorflow.h5'
# model_path = 'mnist_tensorflow.h5'
mnist_model = models.load_model(model_path)

folder_path = "Chapter03/2022/project_sudoku/tensorflow/"
file_path = folder_path + 'image_part.png'
# file_path = 'image_part.png'
image_src = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
image_src = cv2.resize(image_src, dsize=(28, 28), interpolation=cv2.INTER_LINEAR)
image_src = tf.convert_to_tensor(image_src, dtype=tf.float32)
image_src = tf.expand_dims(image_src, 0)
image_src = 1 - image_src / 255.

num_prob = mnist_model.predict(image_src)
plt.imshow(image_src[0])
plt.title(str(np.argmax(num_prob[0])))
plt.show()

# num_prob = mnist_model.predict(x_train[0])
# plt.imshow(x_train[0])
# plt.title(str(np.argmax(num_prob[0])))
# plt.show()