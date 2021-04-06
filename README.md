# Study

소프트웨어 엔지니어가 되기위한 흔적들

## 목차
- [Java Web](#java-web)
  - [Homepage_Kurly](#homepage_kurly)
- [Python Web](#python-web)
- [Data Analysis](#data-analysis)
  - [ML/DL](#ml-dl)
    - [tensorflow](#tensorflow)
      - [RNN](#rnn)
      - [CNN](#cnn)
  

## Java Web
### Homepage_Kurly

---

## Python Web
## ChatService

---

## Data Analysis
python을 이용한 데이터 분석
## ML/DL

------

## Tensorflow
데이터 양이 많아서 colab 에서 GPU버전으로 주로 실행.

-----

## RNN

### LSTM을 활용하여 스펨메일 분류해보기(영어 메일)
> tf_rnn_spamClassification.ipynb <br><br>
tensorflow + RNN*(NLP)을 이용하여 스팸메일 분류 모델.  
Dense 앞부분은 LSTM을 활용하였고 loss, acc 변화에 대한 시각화 작업도 추가하였다.

소스코드 설명
1. data 로딩
2. 데이터 전처리 작업
    - 기본작업(매핑, 불필요한 컬럼제거, 결측치확인, 중복 데이터확인 등)
    - token 처리*
    - padding 및 one-hot 작업
    - train / test 분리(8:2)
3. 데이터 정보 확인 
    - 단어들의 빈도수 및 메일 길이 시각화(matplotlib)
4. 학습
    - LSTM*을 활용하여 DL 모델 학습
5. 결과
    - loss, acc 변화에 대한 시각화(matplotlib)
    
<br>

**RNN** <br>
주로 텍스트 데이터같은 순차적으로 등장하는 데이터에 좋은 성능을 보이는 Neural Networks 모델 중 하나.<br>
한 층에서 학습한 데이터의 파라미터를 다음 층으로 넘겨주어 학습시킨다. 즉, 이전 학습내용을 반영하여 학습한다.  
  

**LSTM**<br>
RNN의 진화된 형태로 vanishing gradient problem을 해결하기 위해 나왔다. 
히든 레이어에 cell-state 하나를 추가해서 가중치(gradient)가 최대한 오랫동안 남아 있도록한다.  


**token 처리란?** <br>
문장을 가장 의미있는 단위로 쪼개어(토큰화) 단어사전을 만들고 문자열을 숫자로 매핑 시키는 작업.
이때 단어사전은 단어별, 문장별, 형태소별로 세분화될 수 있다.


---

### 기본적인 text generation 해보기
> tf_rnn_text_gen.ipynb <br><br>
tensorflow + RNN(NLP)을 이용하여 다음 단어를 예측해보는(text generation) 모델.
> 데이터는 기사에 있는 내용으로 가져왔다. 데이터가 많지 않아 성능이 좋게 나오지는 않는다. 

소스코드 설명
1. 데이터 전처리 작업
    - token 처리
    - 문장 슬라이싱.
    - padding* 및 one-hot* 작업
2. 학습
    - LSTM*을 활용하여 DL 모델 학습
3. 결과
    - 단어를 입력값으로 넣어 문장을 자동 생성.
  
<br>
LSTM Layer 전에 **Embedding** 작업이 선행된다.

**padding 작업이란?**  <br>
병렬연산을 위해 여러 문장의 길이를 임의로 동일하게 맞춰주는 작업. 
벡터 길이가 동일할 때 효율적인 학습이 가능하다.

**one-hot 작업이란?**    <br>
숫자(or 데이터)를 0, 1로 이루어진 벡터로 표현하여(보통 단위벡터) 병렬연산을 쉽게 할 수 있도록 하는 작업. 
      
      
------

### RNN 모형의 2가지 핵심 구조 공부하기
> tf_rnn_many_to.ipynb  <br><br>
> RNN 모형의 input-output 데이터 흐름 2가지 공부 (many-to-many, many-to-one)
> function API 활용


소스코드 설명

1. many-to-one*
2. many-to-many*
3. stacked many-to-many : 2번에서 layer를 추가한 것.
 
공통 : 단순 데이터셋 활용, function API 사용
<br>

**many-to-one**
input 여러개, output 1개
RNN의 각 layer를 거치면서 하나의 output이 생성
 
**many-to-many**      
input 여러개, output 여러개 
RNN 각 layer마다 output 을 생성
RNN layer에 return_sequences=True 항목을 추가.  


-------
### LSTM을 활용하여 초간단 영화 리뷰 감성분류 해보기
> tf_rnn_token.ipynb  <br><br>
> 문자열 토큰화, LSTM 활용 초간단 영화 리뷰 텍스트 감성분류

소스코드 설명                                
                                       
1. 데이터 전처리
   - token 처리
   - padding, one-hot 처리
2. 학습                       
3. 결과

<br>                                           
**주의**
embedding의 단어 사전 사이즈는 word_size + 1을 해야한다. 
이유는 1번부터 시작하기 때문.

---

### 뉴욕타임즈 기사 일부로 학습한 후 기사 만들어보기
> tf_rnn_newyork_article.ipynb  <br><br>  
> 뉴욕타임즈 기사의 일부 자료로 RNN 학습 모델을 만들어 기사 생성(text generation)

소스코드 설명
1. 데이터 로드
2. 데이터 전처리
    - 불필요 데이터 제거
    - punctuation(encode, decode) 제거
    - 단어 갯수별로 sequence 다시 생성. 
    - padding, one-hot 처리
3. 학습
    - Embedding, LSTM, 학습
4. 결과
    - 특정 단어를 넣고 텍스트 만들어내기

--------

### 한글을 글자 단위로 토큰화 하여 문장 생성해보기(feat. 소설 토지)
> tf_rnn_togi.ipynb  <br><br>
> 저작권이 없는 토지 소설을 바탕으로 학습시킨 후 text generation* 수행
> 전처리시 **글자**를 기준으로 토큰화시킨 후 학습


소스코드 설명

1. 데이터 로드
2. 데이터 전처리
    - 데이터의 모든 문자(중복없이)를 단어 사전에 넣음
    - maxlen 길이의 문자열을 기준으로 sentences list를 생성
    - one-hot 처리(False, True)
3. 학습
    - Dense layer를 2개로 하여 학습
4. 결과
   - 임의의 idx로 input text 선별
   - text 다음에 올 문자열 예측(모델)
   - 무작위로 샘플링하기 위해 sample_func 함수를 활용하여 그 다음 idx를 설정 


**text generation 이란**
주어진 text 데이터 다음에 어떤 text가 올 것인지 예측하는 것.


------

### 한글을 단어 단위로 토큰화 하여 문장 생성해보기(feat. 소설 토지) 
> tf_rnn_togi_word.ipynb <br>       
> tf_rnn_togi.ipynb 와 유사하나 <br>
> 전처리시 글자가 아닌 단어를 기준으로 토큰화 

소스코드 설명
1. 데이터 로드
2. 데이터 전처리
   - 정규표현식(re)을 이용해서 불필요한 문자 제거. 
   - 글자가 아닌 단어를 기준으로 sentence 생성
   - text 안에 존재하지 않는 토큰을 UNK로 설정(코드 안정성을 위해)
   - 25개의 단어가 주어지고, 다음 단어를 예측하도록 설정
3. 학습
   - LSTM을 활용.
   - Dropout* 활용
4. 결과
   - LambdaCallback 함수를 활용해서 모델이 생성한 결과물 확인   
   

**dropout(0~1값)**<br>
오버 피팅을 방지하기 위한 대표적인 방법으로 학습시 레이어의 노드 일부를 0으로 변경.
물론 테스트 단계에서는 dropout이 되지 않으므로 이때는 층의 출력을 드롭아웃에 비례해서 줄여준다.
       
    
-----

### 한글을 자음모음 단위로 토큰화 하여 문장 생성해보기(feat. 소설 토지)
> tf_rnn_togi_jamo.ipynb <br>             
> tf_rnn_togi.ipynb 와 유사하나
> 전처리시 글자가 아닌 자모(자음, 모음)를 기준으로 토큰화

소스코드 설명
1. 데이터 로드
2. 데이터 전처리
   - jamotools 라이브러리를 활용하여 자모기준으로 토큰화 진행
   - padding 처리 
3. 결과
   - 주어진 문장에 next_chars 만큼의 자모를 예측(예시에서는 5000개니깐 한 문장이 형성)

-----

## CNN  

### MobileNet V2를 베이스모델로 해서 전이학습해보기(feat. 고양이개 이미지 데이터)

> tn_cnn_transferLearning.ipynb <br><br>
> 이미지 분류에 좋은 CNN*, 전이학습*에서 사용할 모델은 구글에서 개발한 MobileNet V2(베이스모델)을 사용
> <br> 베이스 모델을 학습에 포함하지 않는 버전 과 포함하는 버전으로 나눠서 진행. 

소스코드 설명
1. 데이터 로드 (tensorflow_datasets(라이브러리)에서 가져오기)
   - cats_vs_dogs 이미지로, shape는 (160,160,3) 이다 
2. 데이터 전처리
   - 이미지 셔플링, 배치 크기*로 정하여 나눔.
3. 학습
   - GlobalAveragePooling2D() 를 통해 feature의 수를 줄여줌.
   - optimizer 는 RMSprop를 사용
4. 결과
   - MobileNetV2 모델은 학습 정지된 상태로 먼저 학습하고 시각화
   - 학습 정지를 풀고 다시 학습후 시각화


**전이학습**
미리 학습된 모델에 데이터를 추가적으로 넣어 튜닝하는 학습. 

**BATCH_SIZE**<br>
한번에 네트워크로 넘겨주는 데이터 수를 의미. 
클수록 학습량이 많아져 train 과정이 빨라진다. 


**CNN**<br>
주로 이미지 데이터에 좋은 성능을 보이는 Neural Networks 모델 중 하나.<br>
필터링 기법을 활용하여 데이터의 특징을 추출하고, shape을 낮춰서 FC Layer 형태로 만든다. 

----

### ImageDataGenerator 를 활용해서 이미지 데이터 만들기. 
> tf_cnn_imageGenerator.ipynb <br><br>
> ImageDataGenerator를 활용해서 좌우대칭, 회전 기울기, 이동 등을 통해 이미지 양 늘리기.

소스코드 설명
- mnist 이미지 데이터 셋을 활용.
- ImageDataGenerator 클래스를 이용해서 이미지 추가보강 후 학습진행
- CNN 을 활용. (Conv2D -> MaxPooling2D -> Dropout) x 2

-----

### CIFAR-10 데이터셋 이미지 분류 해보기(일반 vs CNN) 
> tf_cnn_cifar.ipynb <br><br>
> 10개의 레이블, 6만장의 칼라 이미지(train 5만, test 1만) 분류. CNN을 썼을때와 안썼을때 비교


소스코드 설명
- model 을 생성하는 2가지 방법(Sequential, Function API 활용)

-----

### Mnist 데이터셋으로 CNN 연습하기. (feat. subclassing) 
> tf_cnn_mnist_subclassing.ipynb  <br><br>
> 모델을 만드는 방법 중 가장 까다로운 subclassing 방법 맛보기.<br>
> GradientTape을 활용해서 모델 학습시켜보기
                                
소스코드 설명
1. 초간단 subclassing 
   - Model을 상속받는 Class를 만든다
   - 초기화 시켜줄 때 layer 객체 만들기. 
   - call 함수로 객체끼리 호출임   
2. 모델 학습방법 GradientTape 사용
   - 고급 tensorflow에서 활용되며 유연한 코딩이 가능.
   - 원래 텐서 1.x 버전에서는 그래프를 만들어서 돌렸다가 2.x 이후 keras를 품으면서 안으로 들어갔는데
   이를 끄집어 낸것이라 볼 수 있다.
   - 즉, 복잡하지만 세부적인 조작이 가능.(low 한 코드)
   - 그래프를 만드는 함수에 @tf.function를 붙임
   

-----

### MNIST 로 CNN 연습
> ke21cnn.py
> mnist* 데이터로 cnn 연습. 

소스코드 설명
- 학습이 완료된 모델을 저장하고 load
- pickle 을 통해 history 객체를 그대로 저장
- 시각화는 역시 matplotlib!

**mnist 데이터**<br>
수기로 숫자가 적힌 데이터. 흑백이여서 각 픽셀의 색정도에 따라 벡터로 표현 가능.  

----

### fashion_mnist 데이터로 이미지 분류
> ke20fashion.py     <br><br>
> 구두, 신발 등 많은 이미지 데이터를 바탕으로 이미지 분류 

소스코드 설명
- 텐서플로의 fashion_mnist 을 활용.
- cnn, rnn 등의 기술은 활용하지 않고 오직 Dense layer를 바탕으로 학습 
- 모델을 저장하고 불러오기

------










