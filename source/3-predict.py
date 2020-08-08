import Constants
import cv2
import tensorflow as tf

def prepare(file):
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (Constants.IMG_SIZE, Constants.IMG_SIZE))
    return new_array.reshape(-1, Constants.IMG_SIZE, Constants.IMG_SIZE, 1)


def captureImage():
    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Capture Mode',  frame[50:350, 100:450])
        if cv2.waitKey(1) & 0xFF == ord(' '):
            print("PHOTO TAKEN")
            cv2.imwrite('/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg', frame[50:350, 100:450])
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return

captureImage()
model = tf.keras.models.load_model("CNN.model")

#Train answer
#imagePath = "/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/Train/scissors/scissors0.jpg" #your image path

#Test answer
#imagePath = "/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/Test/scissors3.jpg" #your image path

# Take photo answer
imagePath = "/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg"        #your image path


image = prepare(imagePath)
prediction = model.predict([image])
prediction = list(prediction[0])

print(Constants.CATEGORIES[prediction.index(max(prediction))])