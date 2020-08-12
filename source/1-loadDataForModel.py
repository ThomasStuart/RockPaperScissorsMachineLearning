import Constants
import numpy as np
import os
import cv2
import random
import pickle

training_data = []
X = [] #features
y = [] #labels

def create_training_data():
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


create_training_data()
random.shuffle(training_data)

for features, label in training_data:
	X.append(features)
	y.append(label)

X = np.array(X).reshape(-1, Constants.IMG_SIZE, Constants.IMG_SIZE, 1)
y = np.array(y)


print("X.shape: ", X.shape)
print("y.shape: ", y.shape)
# # Creating the files containing all the information about your model
# pickle_out = open("X.pickle", "wb")
# pickle.dump(X, pickle_out)
# pickle_out.close()
#
# pickle_out = open("y.pickle", "wb")
# pickle.dump(y, pickle_out)
# pickle_out.close()
#
# pickle_in = open("X.pickle", "rb")
# X = pickle.load(pickle_in)