import Constants
import cv2
import tensorflow as tf
from random import choice

def prepare(file):
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (Constants.IMG_SIZE, Constants.IMG_SIZE))
    return new_array.reshape(-1, Constants.IMG_SIZE, Constants.IMG_SIZE, 1)

def calculate_winner(move1, move2):
    if move1 == move2:
        return "Tie"

    if move1 == "rock":
        if move2 == "scissors":
            return "User"
        if move2 == "paper":
            return "Computer"

    if move1 == "paper":
        if move2 == "rock":
            return "User"
        if move2 == "scissors":
            return "Computer"

    if move1 == "scissors":
        if move2 == "paper":
            return "User"
        if move2 == "rock":
            return "Computer"


model = tf.keras.models.load_model("/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/CNN.model")

cap = cv2.VideoCapture(0)

prev_move = None

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # rectangle for user to play
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    # rectangle for computer to play
    cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 2)

    # extract the region of image within the user rectangle
    roi = frame[100:500, 100:500]
    #img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    #img = cv2.resize(img, (Constants.IMG_SIZE, Constants.IMG_SIZE))
    cv2.imwrite('/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg', roi)

    # predict the move made
    image = prepare("/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg")
    prediction = model.predict([image])
    prediction = list(prediction[0])
    user_move_name = Constants.CATEGORIES[prediction.index(max(prediction))]

    # predict the winner (human vs computer)
    if prev_move != user_move_name:
        if user_move_name != "none":
            computer_move_name = choice(['rock', 'paper', 'scissors'])
            winner = calculate_winner(user_move_name, computer_move_name)
        else:
            computer_move_name = "none"
            winner = "Waiting..."
    prev_move = user_move_name

    # display the information
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Your Move: " + user_move_name,
                (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Computer's Move: " + computer_move_name,
                (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Winner: " + winner,
                (400, 600), font, 2, (0, 0, 255), 4, cv2.LINE_AA)

    if computer_move_name != "none":
        icon = cv2.imread("/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/images/{}.png".format(computer_move_name))
        icon = cv2.resize(icon, (400, 400))
        frame[100:500, 800:1200] = icon

    cv2.imshow("Rock Paper Scissors", frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()