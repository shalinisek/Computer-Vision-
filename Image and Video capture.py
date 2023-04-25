######################## READ IMAGE ############################
# import cv2
# # LOAD AN IMAGE USING 'IMREAD'
# img = cv2.imread("flower.jpg")
# # DISPLAY
# cv2.imshow("flower",img)
# cv2.waitKey(0)

######################### READ VIDEO #############################
# import cv2
# frameWidth = 640
# #frameHeight = 480
# frameHeight = 100 # reduced video Frame testing use above height for normal size
# cap = cv2.VideoCapture("butterfly-12060.mp4")
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
######################### READ WEBCAM  ############################
import cv2
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break