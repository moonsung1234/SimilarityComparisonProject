
from selenium import webdriver
from urllib import parse
import time

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

# 사진 갯수 가져오기
images = driver.execute_script("return document.querySelectorAll(\"._image._listImage\")")
images = list(map(lambda e : e.get_attribute("src"), images))

print(len(images))

images = list(filter(lambda img : "https://" not in img, images))

print(len(images))
