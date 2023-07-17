
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, BatchNormalization
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import plot_model
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.model_selection import train_test_split
from PIL import Image 
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import os

img_width, img_height = 200, 200
batch_size = 32
epochs = 10
label = 5

def get_data(target) :
    path = ".\\image\\" + target + "_face"
    data = []

    for i, img in enumerate(os.listdir(path)) :
        image = np.asarray(Image.open(os.path.join(path, img)).resize((img_width, img_height)).convert("L"))
        image = np.repeat(image[..., np.newaxis], 3, -1)
        
        data.append(image)

        if i >= 200 :
            break

    return data

def one_hot_encode(label, index) :
    return_label = [ 0 for _ in range(label) ]
    return_label[index] = 1

    return return_label

# 감스트
train_gst_x = get_data("감스트")
train_gst_t = [ one_hot_encode(label, 0) for i in range(len(train_gst_x)) ]

print(len(train_gst_x))

# 괴물쥐
train_mm_x = get_data("괴물쥐")
train_mm_t = [ one_hot_encode(label, 1) for i in range(len(train_mm_x)) ]

print(len(train_mm_x))

# 안유진
train_an_x = get_data("안유진")
train_an_t = [ one_hot_encode(label, 2) for i in range(len(train_an_x)) ]

print(len(train_an_x))

# 정찬성
train_jung_x = get_data("정찬성")
train_jung_t = [ one_hot_encode(label, 3) for i in range(len(train_jung_x)) ]

print(len(train_jung_x))

# 침착맨
train_relx_x = get_data("침착맨")
train_relx_t = [ one_hot_encode(label, 4) for i in range(len(train_relx_x)) ]

print(len(train_relx_x))

train_x_data = np.array(train_gst_x + train_mm_x + train_an_x + train_jung_x + train_relx_x) / 255
train_t_data = np.array(train_gst_t + train_mm_t + train_an_t + train_jung_t + train_relx_t)

random_index = np.arange(train_x_data.shape[0])
np.random.shuffle(random_index)

train_x_data = train_x_data[random_index]
train_t_data = train_t_data[random_index]

train_x, test_x, train_t, test_t = train_test_split(train_x_data, train_t_data, test_size=0.1, random_state=2023)

print(train_x.shape, train_t.shape)

train_data = tf.data.Dataset.from_tensor_slices((train_x, train_t)).batch(batch_size)
test_data = tf.data.Dataset.from_tensor_slices((test_x, test_t)).batch(batch_size)

transfer_input = Input(shape=(img_width, img_height, 3))
transfer_model = tf.keras.applications.vgg16.VGG16(
    include_top = False,
    weights = "imagenet",
    input_tensor = transfer_input
)
transfer_model.trainable = False
transfer_model.summary()

model = Sequential([
    transfer_model,
    Flatten(),
    Dense(4096, activation="relu"),
    Dropout(0.5),
    Dense(5, activation="softmax")
])
checkpoint = ModelCheckpoint("model4.h5",
    monitor = "val_loss",
    verbose = 1,
    save_best_only = True,
    mode = "auto"
)

model.summary()
model.compile(
    optimizer = "adam", 
    loss = "categorical_crossentropy", 
    metrics = ["accuracy"]
)
model.fit(
    train_data,
    validation_data = test_data,
    epochs = epochs,
    verbose = 1,
    batch_size = batch_size,
    callbacks = [checkpoint]
)
