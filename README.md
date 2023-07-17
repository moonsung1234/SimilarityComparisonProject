# Similarity Comparison Project (인물 유사도 측정 프로젝트)

장유고등학교 **SMART 진로학습 공동체** 공학 계열 실습 프로젝트
> 공학 계열 친구들과 학급 친구들 모두가 쉽고 재미있게 사용할 수 있는 프로그램을 만들자는 취지로 계획되었다.
<br>

## Target

|감스트|괴물쥐|안유진|정찬성|침착맨|
|---|---|---|---|---|
|![00](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/c429fd70-d896-4142-a96f-55529c0bf195)|![00](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/d4c6e156-2827-4586-83fd-c04073c052ef)|![10](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/ed804762-e32e-42f5-a0ed-53af8b422d00)|![10](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/0773f9a7-f282-4777-8b8a-d302cc8d304b)|![10](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/ef97be6a-2001-4427-af46-ccff51f0e5d5)|

곻학 계열 친구들과 비교할 기준이 되는 대상을 취합하여 위와 같이 5명을 선정하였다.

<br>

## Data

```
image
├──── 감스트
├──── 감스트_face
├──── 괴물쥐
├──── 괴물쥐_face
├──── 안유진
├──── 안유진_face
├──── 정찬성
├──── 정찬성_face
├──── 침착맨
├──── 침착맨_face
```
<br>

## structure

![vgg16readme](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/2ca318dc-117a-4f01-ae50-21c12eeccd47)

imagenet 으로 학습된 **VGG-16** model 을 transfer learning 하였다.

<br>

## Result

![민기강_모자이크](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/1ca419ce-2258-4a1a-91aa-116d41f039f2) <br>
![김동규_모자이크](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/66a11ec1-4b36-45b1-a27b-d327375868fc) <br>
![조우철_모자이크](https://github.com/moonsung1234/SimilarityComparisonProject/assets/71556009/df0e40b2-b083-4e2d-a3a4-4de845b92d0c)

학급 친구들을 대상으로 실행한 결과이며, 예상과 비슷하게 잘 나왔다.
<br>
