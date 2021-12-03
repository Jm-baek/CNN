Tensorflow Obeject detection tutorial은 현재 tf.2* 에 맞춰져있다.  
만약, tf1.1* 버전을 사용하면 Error가 발생한다.  

### 방법1.
 두 버전을 사용되게 해야하는데  

 모듈? 라이브러리를 다 호출 후 바로 아래에 아래 코드를 하나 더 작성해줘야한다.  
 tf.compat.v1.enable_eager_execution()  

 그리고  
 tf.compat.v2 or tf.compat.v1을 사용해서 버전을 맞춰줘야한다.  
 model = tf.saved_model.load_v2(str(model_dir)) -->  model = tf.compat.v2.saved_model.load(str(model_dir))  

 아래 Issue 참고 해결 방법이다.   
 https://github.com/tensorflow/models/pull/8556  
 
 
### 방법2
Tensorflow Obeject detection tutoria의 release 버전을 tf1.13으로 맞추고 실행해야한다.  
아래 tf1.13의 주소이다.  
https://github.com/tensorflow/models/blob/57e075203f8fba8d85e6b74f17f63d0a07da233a/research/object_detection/object_detection_tutorial.ipynb  



코드는 최대한 깔끔하게 정리해서 다시 올리겠따~!!  
현재 코드의 재생산성을 높이기 위해..FLAGS를 통해 작성하고 있다.    
단순히 되게끔만 하면 쉽기는 하지만 추후 계속 사용을 고려해야한다.  
python progressbar을 사용해서 진행 상황 표시바도 만들어야된다!!  


### how to make tfrecord!?
convert_tfrecrod.py  
#### 방법


크게 두 가지로 나눈다.
1. tf.train.Example 만드는 함수
  - example을 만들면서 생기는 궁금증
    1. bounding box의 format은 어떤 형태로 저장?
       - pascal VOC or COCO ?!
    2. image는 어떤 형태로 저장?
       - bytes_feature? 
    3. train은 되는데 val도 자동으로 저장을 어떻게?

2. 이미지를 지정한 개수만큼 나눠서(shard) tfrecord 파일에 저장한다.
   - 

참고사이트
 - https://juhyung.kr/t/practical-tf-2-0-tfrecords/50/1
 - https://medium.com/@rodrigobrechard/tfrecords-how-to-use-sharding-94059e2b2c6b
 - https://www.tensorflow.org/tutorials/load_data/tfrecord#creating_a_tftrainexample_message
