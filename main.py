import cv2
from mtcnn import MTCNN

detector = MTCNN()

image = cv2.cvtColor(cv2.imread("ManyPeople.jpg"), cv2.COLOR_BGR2RGB)
result = detector.detect_faces(image)

# Result is an array with all the bounding boxes detected.

# keypoints = result[0]['keypoints']

# Rendering all the bounding boxes.
for i in range(len(result)):
    cv2.rectangle(image,
                  (result[i]['box'][0], result[i]['box'][1]),
                  (result[i]['box'][0] + result[i]['box'][2], result[i]['box'][1] + result[i]['box'][3]),
                  (0, 155, 255),
                  2)


'''
cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)
'''

cv2.imwrite("ManyPeople_draw.jpg", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

print(result)
