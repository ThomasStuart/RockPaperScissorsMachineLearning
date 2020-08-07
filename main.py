import cv2
import numpy as np
import tensorflow as tf
CATEGORIES     = ['rock', 'paper', 'scissors']
IMG_SIZE       = 300 # must change in getData
def prepare(file):
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


def captureImage():
    cap = cv2.VideoCapture(0)
    # Set properties. Each returns === True on success (i.e. correct resolution)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Capture Mode',  frame[50:350, 100:450])
        # frame = cv2.resize(frame, (540, 380), fx=0, fy=100,
        #                    interpolation=cv2.INTER_CUBIC)
        # cv2.imshow('Capture Mode', frame)
        if cv2.waitKey(1) & 0xFF == ord(' '):
            print("PHOTO TAKEN")
            cv2.imwrite('/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg',  frame[50:350, 100:450])
            #cv2.imwrite('/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg', frame)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return

captureImage()

model = tf.keras.models.load_model("CNN.model")
#image = "/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/Test/scissors3.jpg" #your image path
imagePath = "/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg" #your image path
image = prepare(imagePath)
prediction = model.predict([image])
prediction = list(prediction[0])
print(CATEGORIES[prediction.index(max(prediction))])