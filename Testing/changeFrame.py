import cv2


def captureImage():
    cap = cv2.VideoCapture(0)
    # Set properties. Each returns === True on success (i.e. correct resolution)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        frame = cv2.resize(frame, (540, 380), fx=0, fy=100,
                           interpolation=cv2.INTER_CUBIC)
        cv2.imshow('Capture Mode', frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            print("PHOTO TAKEN")
            cv2.imwrite('/Users/Thomas_Stuart/PycharmProjects/ClassifyImage/temp.jpg', frame)
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return