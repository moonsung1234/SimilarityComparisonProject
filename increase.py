
import tensorflow as tf
import numpy as np
import cv2
import os

def save_image(path, image) :
    extension = os.path.splitext(path)[1]
    result, encoded_img = cv2.imencode(extension, image)

    if result :
        with open(path, "wb") as f :
            encoded_img.tofile(f)

# 대상 입력
target = input("대상을 입력하세요 : ")

# 사진 폴더 경로 설정
image_path = "./image/" + target + "_face"

# 폴더 내의 사진들 탐색
for i, img in enumerate(os.listdir(image_path)) :
    # 사진 읽기
    image = cv2.imdecode(np.fromfile(os.path.join(image_path, img), dtype=np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 사진 좌우 뒤집기
    flipped = tf.image.flip_left_right(gray)
    path = "./image/" + target + "_face/flipped" + img

    save_image(path, np.array(flipped))

    # 사진 그레이스케일 만들기
    grayscaled = tf.image.rgb_to_grayscale(gray)
    path = "./image/" + target + "_face/grayscaled" + img

    save_image(path, np.array(flipped))

    # 사진 포화시키기
    for sf in range(1, 6) :
        saturated = tf.image.adjust_saturation(gray, sf)
        path = "./image/" + target + "_face/saturated" + str(sf) + img

        save_image(path, np.array(saturated))

    # 시진 밝기 변경하기
    for delta in range(1, 6) :
        bright = tf.image.adjust_brightness(gray, delta * 0.1)
        path = "./image/" + target + "_face/bright" + str(delta) + img

        save_image(path, np.array(bright))

    print(i)

