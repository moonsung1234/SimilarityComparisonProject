
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model   
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import cv2
import os

# 감스트
path = os.path.relpath("C:\\Users\\dit67\\Desktop\\python\\GAMST\\SimilarityComparisonProject\\image\\감스트_face")

# for i, img in enumerate(os.listdir(path)) :
#     image = cv2.imdecode(np.fromfile(os.path.join(path, img), dtype=np.uint8), cv2.IMREAD_GRAYSCALE)

#     print(image.shape)
#     cv2.imshow("image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# 괴물쥐
path = os.path.relpath("C:\\Users\\dit67\\Desktop\\python\\GAMST\\SimilarityComparisonProject\\image\\괴물쥐_face")

# 안유진
path = os.path.relpath("C:\\Users\\dit67\\Desktop\\python\\GAMST\\SimilarityComparisonProject\\image\\안유진_face")

# 정찬성
path = os.path.relpath("C:\\Users\\dit67\\Desktop\\python\\GAMST\\SimilarityComparisonProject\\image\\정찬성_face")

# 침착맨
path = os.path.relpath("C:\\Users\\dit67\\Desktop\\python\\GAMST\\SimilarityComparisonProject\\image\\침착맨_face")

# transfer_input = Input(shape=(200, 200, 1))
transfer_model = tf.keras.applications.vgg16.VGG16(
    # include_top = False,
    weights = "imagenet",
    # input_tensor = transfer_input,
)

transfer_model.summary()