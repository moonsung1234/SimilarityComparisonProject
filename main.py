
from selenium import webdriver
from urllib import parse
import requests
import time
import os

# 대상
search_target = input("대상을 입력해주세요 : ")

# 크롬 창 띄우고 접속하기
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" + parse.quote(search_target))

time.sleep(3)

# 모든 사진을 로딩하기 위해 순차적으로 스크롤
scroll_count = int(input("스크롤 횟수를 입력해주세요 : "))

for i in range(scroll_count) :
    driver.execute_script("scrollBy(0, 10000);")
    time.sleep(1)

time.sleep(3)

# 사진 링크들을 모으기 
images = driver.execute_script("return document.querySelectorAll(\"._image._listImage\")")
images = list(map(lambda e : e.get_attribute("src"), images))
images = list(filter(lambda img : "https://" in img, images))

print(images)

# 창 닫기
driver.quit()

# 사진 링크를 통해 사진들을 다운받기
image_path = "C:\\Users\\muns3\\OneDrive\\Desktop\\python-project\\유사도 측정 프로그램\\image"

for i in range(len(images)) :
    folder = image_path + "\\" + search_target
    file =  search_target + str(i) + ".jpg"

    res = requests.get(images[i])
    
    with open(os.path.join(folder, file), "wb") as f :
        f.write(res.content)
