import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv2. cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.05, 4, minSize=(200, 200))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Video', frame)

        print('number of people =', enumerate(faces))
        
        if cv2.waitkey(25) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
