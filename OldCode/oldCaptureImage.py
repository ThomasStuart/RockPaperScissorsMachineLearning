import cv2

def captureImage():
    cap = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Capture Mode',  frame[50:350, 100:450])
        if cv2.waitKey(1) & 0xFF == ord(' '):
            print("PHOTO TAKEN")
            cv2.imwrite('/Test/rock/temp.jpg', frame[50:350, 100:450])
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    return