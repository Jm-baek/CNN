Tensorflow Obeject detection tutorial은 현재 tf.2* 에 맞춰져있다.
만약, tf1.1* 버전을 사용하면 Error가 발생한다.
두 버전을 사용되게 해야하는데

모듈? 라이브러리를 다 호출 후 바로 아래에 아래 코드를 하나 더 작성해줘야한다.
tf.compat.v1.enable_eager_execution()

그리고 
tf.compat.v2 or tf.compat.v1을 사용해서 버전을 맞춰줘야한다.
model = tf.saved_model.load_v2(str(model_dir)) -->  model = tf.compat.v2.saved_model.load(str(model_dir))

아래 Issue 참고 해결 방법이다.
https://github.com/tensorflow/models/pull/8556
