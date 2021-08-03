## 자연어 토크나이징 도구(1)

> 자연어 처리를 위한 위한 텍스트를 단위별로 나누는 라이브러리에 대해서 알아본다.



### NLTK(Natural Language Toolkit)

> 영어 토크나이징 작업을 수행할 수 있는 라이브러리, 영어 텍스트에 대해 전처리 및 분석을 위한 도구이다.



* 50여 개가 넘는 말뭉치 리소스를 활용해 영어 텍스트를 분석할 수 있게 제공한다.

  

* 함수를 쉽게 사용할 수 있게 구성돼 있어 빠르게 텍스트를 전처리 할 수 있다.



* 다운로드 : NLTK는 `conda install ntk` 뿐만 아니라 말뭉치(corpus)를 내려받아야 연동할 수 있다.

  * library 설치

    ```python
    !conda install ntk # 설치되어 있다면 skip
    ```

  * corpus 다운로드

    ```python
    import nltk
    nltk.download('punkt')
    # [nltk_data] Downloading package punkt to /root/nltk_data...
    # [nltk_data]   Unzipping tokenizers/punkt.zip.
    # True
    ```

    *  `Punkt Tokenizer Models` 라는 녀석을 설치해준다.

  

* 토크나이징 : 텍스트에 대해 특정 기준 단위로 문장을 나누는 것을 의마한다.

  * 단어 단위 토크나이징(1) : `word_tokenize`

    * 불용어 미제거

      ```python
      from nltk.tokenize import word_tokenize
      
      sample_text = "One of the first things that we ask ourselves is what are the pros and cons of any task we perform."
      word_tokens = word_tokenize(sample_text)
      print(word_tokens)
      # ['One', 'of', 'the', 'first', 'things', 'that', 'we', 'ask', 'ourselves', 'is', 'what', 'are', 'the', 'pros', 'and', 'cons', 'of', 'any', 'task', 'we', 'perform', '.']
      ```

    * 불용어 제거

      ```python
      nltk.download('stopwords')
      # [nltk_data] Downloading package stopwords to /root/nltk_data...
      # [nltk_data]   Unzipping corpora/stopwords.zip.
      # True
      ```

      ```python
      from nltk.corpus import stopwords
      word_tokens_wt_sw = [word for word in word_tokens if word not in stopwords.words('english')]
      print(word_tokens_wt_sw)
      # ['One', 'first', 'things', 'ask', 'pros', 'cons', 'task', 'perform', '.']
      ```

  * 단어 단위 토크나이징(2) : `WordPunctTokenizer`

    ```python
    sentence = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."
    
    tokenizer = WordPunctTokenizer()
    word_tokens = tokenizer.tokenize(sentence)
    
    print(word_tokens)
    # ['Don', "'", 't', 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', ',', 'Mr', '.', 'Jone', "'", 's', 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop', '.']
    
    print(word_tokenize(sentence))
    # ['Do', "n't", 'be', 'fooled', 'by', 'the', 'dark', 'sounding', 'name', ',', 'Mr.', 'Jone', "'s", 'Orphanage', 'is', 'as', 'cheery', 'as', 'cheery', 'goes', 'for', 'a', 'pastry', 'shop', '.']
    
    ```

    * `'`를 어떻게 처리하는지 다르다.

  * 문장 단위 토크나이징

     ```python
     from nltk.tokenize import sent_tokenize
     
     paragraph = 'We start from the very basic, we call it our pre-lit level, where students have not had experience with education in their own countries. They may have never learned to read or write, or even use a pencil sometimes. Our highest level, we call it level five, are often university students, they go to Utah State University, they might be graduate instructors or the spouses of professors, and they will be here to practice more English during the evening while they are at the university during the day. Also, some of our students that are from our community will finish level five and then move on to Bridgerline classes,'
     
     print(sent_tokenize(paragraph))
     ## 결과
     ['We start from the very basic, we call it our pre-lit level, where students have not had experience with education in their own countries.',
      'They may have never learned to read or write, or even use a pencil sometimes.',
      'Our highest level, we call it level five, are often university students, they go to Utah State University, they might be graduate instructors or the spouses of professors, and they will be here to practice more English during the evening while they are at the university during the day.',
      'Also, some of our students that are from our community will finish level five and then move on to Bridgerline classes,']
     ```

  

* 어간(Stem) 추출 : 형태학적 분석을 단순화한 버전이라고 볼 수 이고, 어간 추출 결과가 사전에 없을 수 있다.

  ```python
  from nltk.stem import PorterStemmer
  
  stemmer = PorterStemmer()
  
  print(stemmer.stem('obesses'), stemmer.stem('obessed')) #obess obess
  print(stemmer.stem('standardizes'), stemmer.stem('standardization')) # standard standard
  print(stemmer.stem('national'), stemmer.stem('nation')) # nation nation
  print(stemmer.stem('tribalical'), stemmer.stem('tribalicalized')) # tribal tribalic
  ```

* 표제어(Lemma) 추출 : 표제어는 `기본 사전형 단어` 정도의 의미를 갖는다. 문장에 있는 단어의 뿌리 단어를 찾아 단어 개수를 줄일 수 있는지 판단한다.

  * 어간(stem) : 단어의 의미를 담고 있는 `핵심` 부분
  * 접사(affix) : 단어에 `추가`적인 의미를 주는 부분
    * (ex) cats : cat(어간) + s(접사)

  * 다운로드

    ```python
    import nltk
    nltk.download('wordnet')
    ```

  * 품사 없이 표제어 추출

    ```python
    from nltk.stem import WordNetLemmatizer
    lemma = WordNetLemmatizer()
    
    words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
    print([lemma.lemmatize(w) for w in words])
    # ['policy', 'doing', 'organization', 'have', 'going', 'love', 'life', 'fly', 'dy', 'watched', 'ha', 'starting']
    ```

    * dies → dy, has → ha : 의미를 알 수 없는 단어로 추출했다. 따라서 품사 정보를 추가 입력해 정확한 결과를 얻을 수 있다.

  * 품사 포함해 표제어 추출

    ```python
    print(lemma.lemmatize('dies', 'v'))    # die
    print(lemma.lemmatize('has', 'v'))     # have
    print(lemma.lemmatize('watched', 'v')) # watch
    ```

    * 동사 원형으로 잘 나온다.

* 토큰화 및 품사 태깅

  * 다운로드

    ```python
    nltk.download('averaged_perceptron_tagger')
    ```

  * 품사 태깅

    ```python
    from nltk.tag import pos_tag
    from nltk.tokenize import word_tokenize
    
    text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."
    print(pos_tag(word_tokenize(text)))
    
    # [('I', 'PRP'), ('am', 'VBP'), ('actively', 'RB'), ('looking', 'VBG'), ('for', 'IN'), ('Ph.D.', 'NNP'), ('students', 'NNS'), ('.', '.'), ('and', 'CC'), ('you', 'PRP'), ('are', 'VBP'), ('a', 'DT'), ('Ph.D.', 'NNP'), ('student', 'NN'), ('.', '.')]
    
    ```

    * VBZ : 동사, 동명사, 현재분사
    * PRP : 인칭 대명사
    * JJ : 형용사
    * VBG : 동사, 동명사, 현재분사
    * NNS :명사, 복수형
    * CC : 등위 접속사
  
  
  
  