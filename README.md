# Study

소프트웨어 엔지니어가 되기위한 흔적들

## 목차
- [Java Web](#java-web)
  - [Homepage_Kurly](#homepage_kurly)
- [Python Web](#python-web)
  - [Django](#django)
- [Data Analysis](#data-analysis)
  - [ML/DL](#ml-dl)
    - [tensorflow](#tensorflow)
      - [RNN](#rnn)
      - [CNN](#cnn)
  

## Java Web
### Homepage_Kurly

----

>사용된 스펙
- MariaDB 10.5.8
- Spring 5.0.0
- Java 1.8.261
- MyBatis 3.2.3
 
<br>

> 구현된 기능
   - 스프링 MVC 구조로 설계   
   - CSS, Html 등은 마켓컬리 홈페이지를 참고
   - index 페이지의 슬라이더 기능.   
   - 연관 검색어 기능, db 상품목록 가져오기(ajax)
   - 로그인 AOP, 세션기능
   - 회원가입, 장바구니 담기, 상품 선택 및 해 로직(결제금액 자동 변경)
   - 게시판 기본기능, 좋아요 기능, 비밀글 기능
   - 상품 이미지 업로드 기능  
   - MyBatis 로 JDBC(mariadb) 연동

<br>

**db 데이터 테이블**<br><br>
<img src="https://raw.githubusercontent.com/jangjungkeon/Study/main/Data/image/kurly_db.png" width="450px" height="300px" title="kurly_db_img" alt="kurly_db_img"></img><br/>


---

## Python Web

------

### python 으로 mariadb 연동(기본)
> test35db.py <br>
> db에 있는 데이터를 select 해오기

소스코드 설명
- pymysql 모듈을 활용해서 connection 객체 생성
- cursor 메서드로 Sql문 직접 넣고 select

------

### 로컬에서 돌아가는 간단한 멀티 채팅서버 만들기
> simpleChatServer.py, simpleChatClient.py<br>
> 쓰레드*를 활용

소스코드 설명
- 서버 -> 클라이언트 순 실행
- 소켓 인스턴스를 생성 후 메타데이터(ip, port) 바인드. 
- 쓰레드 인스턴스 생성

**파이썬 멀티쓰레드**<br>
파이썬(Cpython)은 메모리 관리방법이 thread-safe하지 않기 때문에 gil이 필요하다. 그래서 비효율적으로 메모리를 사용한다. 
이런 문제로 인해 파이썬 개발자들은 멀티프로세싱 모듈을 지원하여 사용을 권장. 

----
## Django

----

### 장고 활용하여 mariadb 연동 후 Ajax 활용
> django_test11ajaxdb_ex
> 장고를 활용하여 db의 데이터를 ajax를 통해 실시간으로 불러오기.

소스코드 설명
- main.html에서 결과보기 버튼을 누르면 아래 함수가 실행
- 장고 orm으로 db에서 데이터를 가져와서 출력.
- json 파일로 main.html에 넘기기

```
def jikwonFunc(request):
    sdata = Jikwon.objects.filter(jikwon_jik=request.GET.get('jik'))
    datas = []
    for i in sdata:
        dic = {'jikwon_no': i.jikwon_no, 'jikwon_name': i.jikwon_name, 'buser_num': i.buser_num}
        datas.append(dic)
    # print(datas)
    return HttpResponse(json.dumps(datas), content_type="application/json")
```

---

## Data Analysis
python을 이용한 데이터 분석

## ML/DL

----

### 나이브 베이즈 분류모델로 텍스트 분류하기.
> bayes3_text.py

소스코드 설명
```
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
```
로 모델 생성 후 작업.

------

### iris 데이터를 활용하여 PCA 분석(주성분 분석) 
> pca_test.py<br>
> 주성분 분석이라고도 한다. 

**PCA 주성분 분이란**<br>
분포된 데이터들 중 주성분을 분석해내는 기법. 

-----

### RandomForest, DecisionTree 활용해보기
> rf_regressor.py <br>
> boston 집값 데이터셋을 활용하여 RandomForest*, DecisionTree* 모델을 활용해보자

소스코드 설명
- DecisionTreeRegressor, RandomForestRegressor 클래스활용

**DecisionTree**<br>
분류와 회귀가 가능한 지도학습 모델 중 하나<br> 
일련의 분류 규칙을 설정한 뒤 데이터를 분류 예측하는 알고리즘. 트리모양으로 되어있음.
오버피팅 될 가능성이 높다는 약점이 있음.

**RandomForest**<br> 
결정트리가 오버피팅될 가능성이 있어 좀더 일반화된 트리로 만들어진 것이 RandomForest.<br>
결정트리를 여러개 만든 후 합치는 병렬처리 ensemble 기법이 활용된다. 
-----

### xgboost 모델을 활용(feat. iris)
> xgb1.py <br>
> xgboost*는 Randomforest와 더불어 대표적인 ensemble 기법이다.  


**xgboost**<br>
Randomforest와 같이 ensemble 기법이나 직렬처리이며, 고성능이나 과적합이 우려될 수 있다. 

----

### BMI 데이터셋에 SVM 모델을 활용.
> svm3_bmi.py<br>
> svm* 모델을 활용해서 데이터셋 분석 및 예측

**SVM**<br>
분류를 위한 최적의 기준 선을 정의하는 모델. 

----

### 숫자 이미지 데이터에 K-평균 알고리즘 사용하기
> clu4.py<br>
> 숫자 이미지 데이터에 K-평균* 알고리즘 사용하기

**KMean 알고리즘**<br>
사용자가 정한 클러스터의 숫자만큼 군집을 만들어주는 알고리즘. 각 데이터사이의 거리를 유클리드 거리법으로 측정하여 군집화한 것이다.  
kmean는 특이한 모양의 군집은 찾지 못하는 경향이 있다.
----

### 밀도 기반 클러스터링 dbscan 활용해보기
> clu6_dbscan.py <br>
> DBSCAN*는 Kmeans와 달리 K를 지정하지 않음.

**DBSCAN**<br>
kmean 알고리즘에서 할 수 없던 다양한 모양의 군집도 군집화 시킬 수 있다.

----

## Tensorflow
데이터 양이 많아서 colab 에서 GPU버전으로 주로 실행.

-----

### fashion_mnist 데이터로 이미지 분류
> ke20fashion.py<br>
> 구두, 신발 등 많은 이미지 데이터를 바탕으로 이미지 분류

소스코드 설명
- 텐서플로 데이터셋의 fashion_mnist를 활용
- cnn, rnn 등의 기술을 활용하지 않고 오직 Dense Layer를 바탕으로 학습
- 모델을 저장하고 불러오기

-----

### 내가 그린 숫자를 컴퓨터가 맞춰보기
> ke19mnist.py <br> 
> 이미지 분류의 바이블 데이터셋인 mnist를 활용해서 기본기 다지기

소스코드 설명
1. 데이터 로드
2. 데이터 전처리
   - one-hot 처리
   - 0 ~ 1 사이 값으로 정규화
3. 학습
   - 가중치를 규제하는 kernel_regularizer* 활용
4. 결과
   - 그림판에서 숫자를 그린 후 예측 데이터에 넣어보기

<br>
**kernel_regularizer**<br>
오버 피팅 방지를 위해 사용됨

--------

### tensorflow를 활용하여 iris 모델을 분류하고 성능 측정하기
> ke18.py<br><br>
> layer의 갯수를 다르게 조정하여 모델을 여러개 만들고, roc 커브로 성능 측정하기

소스코드 설명
iris 데이터를 가져와서 
- one-hot 인코딩, 
- 표준화*를 진행. (StandardScaler)
- layer 갯수에 따른 모델을 여러개 생성.
- k-fold* 교차 검증(sklearn의 cross_val_score)
- roc_curve* 로 성능 측정. 


**k-fold**<br>
데이터가 적을 때 오버피팅을 방지하기 위한 목적으로 사용.<br> 
k번 접는다(train과 validation을 나눠서 k번 학습)는 개념으로 생각하면 된다. 
train, test, validation 3개로 쪼개서 검증하다보면 데이터가 많이 필요해서 나온 개념이다. 

**표준화를 하는 이유**<br>
표준화를 한다고 정확도가 오르진 않지만 그래프로 표현하거나 값을 비교할 때 
사용자가 알아보기 쉽게할 수 있다. 가독성이 더 뛰어나진다고 생각하면될듯.

**roc_curve**
모델의 성능을 평가하기 위해 사용하는 방법. x축으론 FPR, y축으론 TPR인 그래프(roc curve)에서
커브의 밑면적 넓이(AUC)가 넓을수록 모델은 더 정확하게 예측한다고 볼 수 있다. 

-----

### zoo 데이터셋을 학습시킨 후 다항분류해보기
> ke17zoo.py
-----


### 당뇨병환자 데이터셋을 학습시킨 후 당뇨병 예측하기(feat. k-fold 교차검증)
> ke14k_fold.py

소스코드 설명
- 이항분류이기에 sigmoid함수를 활용해보았다.
- k-fold 교차검증

-----

### 자동차 데이터셋을 학습시킨 후 연비 예측하기 (회귀분석)
> ke11cars.py

소스코드 설명
- 회귀분석이기에 Dense layer의 활성화 함수에 'linear' 를 사용.

-----

### boston 데이터셋을 학습시킨 후 주택 가격 예측하기(다중회귀분석)
> ke10boston.py<br>
> 결정계수*를 활용해서 해당 회귀모델이 주택 가격을 얼마나 설명할 수 있는지 파악

소스코드 설명
- 결정계수(r2_score)를 통해 회귀모델의 성능을 측정
         


**결정계수**<br>
회귀분석모델의 성능을 측정하는 하나의 값으로, 0~1사이값을 갖는다. 값이 클수록 
독립변수들이 종속변수를 잘 설명하고 있다고(유의하다) 볼 수 있다. 정확도와는 차이가 있어 설명력이라고 부른다. 
-----

### 텐서보드를 활용하여 모델의 구조 및 학습 과정을 시각화하기(feat. 다중선형모델)
> ke_tensorboard.py
> 임의의 숫자 데이터(5행 3열)를 만들어 학습시키고 과정을 텐서보드로 시각화.

소스코드 설명
- tensorflow.keras.callbacks.TensorBoard 클래스를 활용
```
tb = TensorBoard(log_dir='my',
                 histogram_freq=True,
                 write_graph=True,
                 write_images=False)
```
<br>
log_dir : 저장하는 파일 위치<br>
histogram_freq : 히스토그램 시각화를 얼마나 자주 보여줄건지<br>
write_graph : 그래프를 보여줄 건지<br>
write_images : 가중치(gradient)를 보여줄 건지<br>

----

## RNN
----

### 네이버 영화 리뷰 감성분석 (feat. RNN, konlpy)
> tf_rnn_navermovie.ipynb<br>
> train, test = 150000, 50000 개 네이버 영화 리뷰 데이터셋 <br>
> 전처리 과정 중 konlpy 를 바탕으로 한글 형태소 분석 추가.

소스코드 설명
전처리과정
- 앞서 토지 데이터셋에서는 단어, 글자, 자모 단위로 쪼개서 단어사전에 넣었다.
- 이번에는 형태소 분석이 가능한 라이브러리인 konlpy* 를 활용하여 전처리 진행
- 불용어 사전을 통해 의미없는 단어 필터링
- 정규표현식으로 구두점등 제거
- OOV 문제를 해결하기 위해 vocab_size 에 + 2, Tokenizer 함수에 oov_token='OOV'추가


### 영화 리뷰 감성분석 (feat. CNN, RNN)
> tf_rnn_imdb.ipynb
> imdb 데이터셋을 CNN, RNN 버전으로 나눠 학습시킨 후 비교. 

소스코드 설명
- CNN으로 텍스트 분류를 하려면 1차원 배열로 해야되기에 Conv1D를 사용.

결과
- 정확도가 CNN : 0.86, RNN(LSTM) : 0.89가 나와서 RNN이 근소하게 좋다는 것을 알 수 있었다.  


### 로이터 통신 기사의 카테고리 분류하기
> tf_rnn_reuters_classification.ipynb <br><br>
> LSTM을 활용하여 기사 카테고리 분류해보기

데이터셋 : tensorflow.keras.datasets.reuters
- train : (8982, ),  test : (2246, ) 
- 이미 토큰화 되어있음.
- 총 45개의 카테고리

소스코드 설명
- 제공된 reuters 데이터를 불러와 LSTM 모델을 구성하여 시각화를 해보았다.
- epochs 를 50정도 주어서 돌려보았다. 

결과 
- epochs가 10이 넘어갈 때 validation 데이터와 차이가 벌어져 오버피팅이 발생한 것을 확인할 수 있었다. 

오버피팅을 방지하는 방법
- 가장 좋은 방법은 더 많은 데이터를 모으는 것
- 차선책은 모델이 수용할 수 있는 정보의 양을 조절
- 저장할 수 있는 정보에 패널티를 가하는 것(kernel_regularizer)
- 모델의 파라미터수를 줄이는 것. (dropout)

----

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
대표적으로 텍스트 감성분석이 있을 수 있다. 
**many-to-many**      
input 여러개, output 여러개 
RNN 각 layer마다 output 을 생성
RNN layer에 return_sequences=True 항목을 추가.
대표적으로 번역활동이 있을 수 있따.


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

### MNIST 로 CNN 연습(이미지 분류)
> ke21cnn.py
> mnist* 데이터로 cnn 연습. 

소스코드 설명
- 학습이 완료된 모델을 저장하고 load
- pickle 을 통해 history 객체를 그대로 저장
- 시각화는 역시 matplotlib!

**mnist 데이터**<br>
수기로 숫자가 적힌 데이터. 흑백이여서 각 픽셀의 색정도에 따라 벡터로 표현 가능.  

----








