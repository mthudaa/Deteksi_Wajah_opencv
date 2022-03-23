import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 648)
cam.set(4, 448)
wajah = cv2.CascadeClassifier('wajah.xml')
while True:
    retV, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = wajah.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 2)
    cv2.imshow("Wajah", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cam.release()
cv2.destroyWindow()