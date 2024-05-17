import cv2
import mediapipe as mp
import math



def dist(x1, y1, x2, y2):
    # 두 점 사이의 거리 계산
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))



mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
my_hands = mp_hands.Hands()

img_path = '/Users/geonhyung/faceimage/finger_3.jpeg'

# 이미지 입력을 하기 위함
img = cv2.imread(img_path)

h, w, c = img.shape
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = my_hands.process(imgRGB)
if results.multi_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
        # 들린 손가락 개수를 저장할 변수
        lifted_fingers = -1
        # 나머지 손가락들에 대한 판단
        for i in range(1, 6): # 엄지 제외, 인덱스 1부터 시작
            tip_y = handLms.landmark[i*4].y
            pip_y = handLms.landmark[i*4 - 2].y
            if tip_y < pip_y:
                lifted_fingers += 1
        # 들린 손가락의 개수에 따라 번호를 할당
        number = lifted_fingers  # 들린 손가락의 수에 따라 직접 숫자를 할당
        # 번호를 화면에 표시
        print(number)