import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        print("PHOTO TAKEN")
        cv2.imwrite('/temp.jpg', frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()