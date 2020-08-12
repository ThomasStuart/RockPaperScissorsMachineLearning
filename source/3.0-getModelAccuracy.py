import Constants
import os
import cv2
import tensorflow as tf

# DIR               = Constants.DATA_DIR
# PICS_PER_CATEGORY = 200

DIR               = Constants.TEST_DIR
PICS_PER_CATEGORY = 10

SET_SIZE = PICS_PER_CATEGORY * Constants.CLASS_SIZE
model = tf.keras.models.load_model("/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/CNN.model")
cr = cp = cs = 0

def prepare(file):
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (Constants.IMG_SIZE, Constants.IMG_SIZE))
    return new_array.reshape(-1, Constants.IMG_SIZE, Constants.IMG_SIZE, 1)

def predict(image):
    prediction = model.predict([image])
    prediction = list(prediction[0])
    return Constants.CATEGORIES[prediction.index(max(prediction))]



for category in Constants.CATEGORIES:
    path = os.path.join(DIR, category)
    class_num = Constants.CATEGORIES.index(category)
    for img in os.listdir(path):
        try :
            imagePath = os.path.join(path, img)
            image     = prepare(imagePath)
            guess     = predict(image)
            print('category->', category , '<-guess->', guess, '<-')
            if   category == 'rock' and guess == category:
                cr += 1
            elif category == 'paper' and guess == category:
                cp += 1
            elif category == 'scissors' and guess == category:
                cs += 1

        except Exception as e:
            pass




print("Rock     correct: ", cr)
print("Paper    correct: ", cp)
print("Scissors correct: ", cs)
print("total:  " , (cr+cp+cs)/SET_SIZE * 100)