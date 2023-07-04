
import numpy as np 
import cv2
import os

# 사진 폴더 경로 설정
image_path = "C:\\Users\\muns3\\OneDrive\\Desktop\\python-project\\유사도 측정 프로그램\\image\\감스트"

# haar cascades 모델 가져오기
haar = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

# 폴더 내의 사진들 탐색
for i, img in enumerate(os.listdir(image_path)) :
    # 사진 읽기
    image = cv2.imdecode(np.fromfile(os.path.join(image_path, img), dtype=np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (1000, 1000))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # haar cascades 모델을 이용하여 얼굴 탐색
    results = haar.detectMultiScale(
        gray,             # 입력 이미지
        scaleFactor = 1.5, # 이미지 피라미드 스케일 factor                            
        minNeighbors = 5,  # 인접 객체 최소 거리 픽셀
        minSize = (20, 20) # 탐지 객체 최소 크기
    )

    # 찾은 얼굴들을 탐색
    for j, box in enumerate(results) :
        try :
            # 얼굴 사진들을 저장
            x, y, w, h = box
            cropped_image = image[y:y + h, x:x + w]
            cropped_image = cv2.resize(cropped_image, (200, 200))

            print(i, j)

            result, encoded_img = cv2.imencode(".jpg", cropped_image)
            face_image = "./image/감스트_face/" + str(i) + str(j) + ".jpg"

            if result :
                with open(face_image, "wb") as f :
                    encoded_img.tofile(f)

        except Exception as e:
            print(e)
            