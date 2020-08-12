import Constants
import numpy as np
import os
import cv2
import random
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

training_data = []
X = [] #features
y = [] #labels

for category in Constants.CATEGORIES:
    path = os.path.join(Constants.DATA_DIR, category)
    class_num = Constants.CATEGORIES.index(category)
    for img in os.listdir(path):
        try :
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (Constants.IMG_SIZE, Constants.IMG_SIZE))
            training_data.append([new_array, class_num])
        except Exception as e:
            pass

random.shuffle(training_data)

for i in range(len(training_data)):
    features = training_data[i][0]
    label    = training_data[i][1]
    X.append(features)
    y.append(label)

X = np.array(X)
y = np.array(y)
X = X/255.0
print("X.shape: ", X.shape)
print("y.shape: ", y.shape)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(Constants.IMG_SIZE, Constants.IMG_SIZE)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(Constants.CLASS_SIZE)
])

# # Building the model
# model = Sequential()
# # 2 hidden layers
# model.add(Flatten())
# model.add(Dense(128))
# model.add(Activation("relu"))
#
# model.add(Dense(128))
# model.add(Activation("relu"))
#
# # The output layer with 13 neurons, for 13 classes
# keras.layers.Dense(Constants.CLASS_SIZE)


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


model.fit(X, y, epochs=25)

test_data   = []
test_images = []
test_labels = []

for category in Constants.CATEGORIES:
    path = os.path.join(Constants.TEST_DIR, category)
    class_num = Constants.CATEGORIES.index(category)
    for img in os.listdir(path):
        try :
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (Constants.IMG_SIZE, Constants.IMG_SIZE))
            test_data.append([new_array, class_num])
        except Exception as e:
            pass

for i in range(len(test_data)):
    features = test_data[i][0]
    label    = test_data[i][1]
    test_images.append(features)
    test_labels.append(label)

test_images = np.array(test_images)
test_images = test_images/255.0
test_labels = np.array(test_labels)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

# Saving the model
model_json = model.to_json()
with open("/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/model.json", "w") as json_file :
	json_file.write(model_json)

model.save_weights("/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/model.h5")
print("Saved model to disk")

model.save('/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/CNN.model')