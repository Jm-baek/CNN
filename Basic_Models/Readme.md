## 처음 공부하는 초심자의 상태에서 CNN을 이해하는 과정으로 작성 되었습니다.
  - 내용이 어수선할 수 있습니다.

먼저, Convolutionla Neural Network(CNN)를 공부했다면 strides, padding, pooling 등을 이해했을 것이다.<br/>
그렇다면 어떻게 CNN이 활용이 될까?<br/>

DNN(Deep Neural Network), RNN(Recursive Neural Network)에서도 마찬가지로 input data가 image라는 차이가 존재할뿐 input data에 대한 feature extraction을 **회귀(Regression)와 분류(Classification)** 중 어디로 사용되는지 구별한다.

CNN은 이미지 데이터에 대한 정보를 추출하는 구조를 이루고 있다.([Feature Extraction](#Feature-Extraction))<br/>

**그래서 이미지를 추출하고 난 다음 뭐를 해?**<br/>
이미지가 나타내고 있는 객체가 무엇인지 결정을 하게된다.([Classification](#Classification))<br/>


CNN 모델들의 변천 과정에서 생각해야될 부분!<br/>
1. 이미지 안의 객체(object)가 무엇(개, 사람, 자동차 등)인가?<br/>
  1.1 이미지 안의 객체가 한 개인가?<br/>
  1.2 이미지 안의 객체가 여러 개인가?<br/>

2. 이미지 안의 객체의 위치가 어디있나?<br/>
  2.1 위치를 찾는 방법의 알고리즘 <br/>
  

## Feature Extraction
이미지의 feature를 추출하는 과정<br/>
from tensorflow.keras.applications import VGG16, ResNet50, Xception 등 가능하다.<br/>




예시) VGG16 모델 구조<br/>
![image](https://user-images.githubusercontent.com/57121112/120911788-09c9a900-c6c5-11eb-897f-9f846cfd74fd.png)




## Classification
Flatten과 GlobalAveragepooling2D를 사용

Flatten의 경우, 많은 파라미터로 연산이 증가하게 된다.
![image](https://user-images.githubusercontent.com/57121112/120912755-f3bfe680-c6cc-11eb-81c7-42dc574dcd58.png)


GlobalAveragepooling2D 사용 파라미터 개수가 Flatten보다 줄어든 것을 확인 가능<br/>
단, 무조건 GlobalAveragepooling2D가 좋다고 할 수 없다.<br/>
![image](https://user-images.githubusercontent.com/57121112/120913034-0509f280-c6cf-11eb-9c57-1ef0cd083f95.png)



## Regional Proposal



## Two-Stage-Detection
Classification과 Regional Proposal이 순서대로 실행



## One-stage-Detection
Classification과 Regision Proposal이 한 번에 실행


