import cv2
import dlib

# read the image
img = cv2.imread("dtcs.png")

# convert img to grayscale: 3D (RGB) -> 2D (Black & White)
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

# dlib: cung cấp các mô hình trí tuệ nhân tạo như nhận diện khuôn mặt (Face Recognition Detector)
face_detector = dlib.get_frontal_face_detector()

# load the predictor:
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") # this model will return 68 points in the face

# use face detector to find face landmarks
faces = face_detector(gray)
print('Face detected: ', len(faces))

# vẽ bounding box xung quanh face
for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    # draw rectangle
    cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=3)

    # face feature detector
    face_features = predictor(image=gray, box=face)
    print(face_features)
    for n in range(0, 68):
        x = face_features.part(n).x
        y = face_features.part(n).y
        # draw a circle to img
        cv2.circle(img=img, center=(x, y), radius=2, color=(0, 0, 255), thickness=1)
        #break

# show the image
cv2.imshow(winname='Face Recognition App', mat=img)

# wait for a key press to exit
cv2.waitKey(delay=0)

# Closed All windows
cv2.destroyAllWindows()