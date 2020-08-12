import Constants
import cv2
import tensorflow as tf

def prepare(file):
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (Constants.IMG_SIZE, Constants.IMG_SIZE))
    return new_array.reshape(-1, Constants.IMG_SIZE, Constants.IMG_SIZE, 1)

def captureImage():
    cap   = cv2.VideoCapture(0)
    count = 1
    while True:
        ret, frame = cap.read()
        cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Collecting {}".format(count), (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Collecting images", frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            print("PHOTO TAKEN")
            roi = frame[100:500, 100:500]
            cv2.imwrite('/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg', roi)
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