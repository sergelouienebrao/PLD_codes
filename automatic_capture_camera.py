import cv2
cap = cv2.VideoCapture(0)
while True:
<<<<<<< HEAD
    _, frame = cap.read()
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 255), 2) 
        face_roi = frame[y: y + h, x: x + w]
        gray_roi = gray[y: y + h, x: x + w]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
        for x1, y1, w1, h1 in smile:
            cv2.rectangle(face_roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 2)
            time_stamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            file_name = f"selfie-{time_stamp}.png"
            cv2.imwrite(file_name, original_frame)
    cv2.imshow("automatic camera", frame)
    if cv2.waitKey(10) == ord("q"): 
        break

#modify tayo dito perd 

=======
     _, frame = cap.read()
     cv2.imshow("automatic capture camera", frame)
     if cv2.waitKey(10) == ord("q"): 
      break
>>>>>>> ba1600df90257affd464baf6b394ad8077110d71
