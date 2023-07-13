
from tensorflow.keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os

model = load_model("./model4.h5")
label = np.array(["감스트", "괴물쥐", "정찬성", "침착맨"])
path = "./image/학급_face"

matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["axes.unicode_minus"] = False

for i, img in enumerate(os.listdir(path)) :
    image = Image.open(os.path.join(path, img))
    image_resize = image.convert("L").resize((200, 200))

    pre_image = np.asarray(image_resize)
    pre_image = np.repeat(pre_image[..., np.newaxis], 3, -1)
    pre_image = pre_image / 255
    pre_image = np.reshape(pre_image, (1, 200, 200, 3))

    result = model.predict(pre_image)[0]
    index = np.argsort(result)[::-1]

    print(img, list(map(lambda x : round(x, 2), result)))

    plt.figure(figsize=(10, 20))
    plt.subplot(1, 5, 1)
    plt.title(img)
    plt.imshow(np.asarray(image.resize((200, 200))))

    for i, target in enumerate(label[index]) :
        target_path = "./image/" + target + "_face"
        target_img = Image.open(os.path.join(target_path, os.listdir(target_path)[0]))
        target_img = np.asarray(target_img)
        
        plt.subplot(1, 5, i + 2)
        plt.title(target + " : " + str(round(result[index[i]] * 100, 2)) + "%")
        plt.imshow(target_img)

    plt.show()

