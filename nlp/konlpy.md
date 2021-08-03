## 자연어 토크나이징 도구(2)

> 자연어 처리를 위한 위한 텍스트를 단위별로 나누는 라이브러리에 대해서 알아본다.



### KoNLPy

> 한글 자연어 처리를 쉽고 간결하게 처리할 수 잇도록 만들어진 오픈소스 라이브러리이다.



* 일반적인 어절 단위에 대한 토크나이징은 NLTK로 해결할 수 있다.
* 형태소 분석으로 형태소 단위의 토크나이징이 가능하다.
* 형태보 분석기 목록
  * Hannanum
  * Khma
  * Komoran
  * Mecab(윈도우 사용 불가)
  * Okt(Twitter)

* Okt 객체는 4개의 함수를 제공한다.

  * `Okt().morphs()` : 텍스트를 형태소 단위로 나눈다.

    *  `norm` 은 `True/False` 값을 받으면 정규화를 뜻한다.
    * `stem`은 `True/False`값을 받으며 각 단어에서 어간을 추출하는 기능이다.

    ```python
    from konlpy.tag import Okt
    
    text = '한글 자연어 처리는 재밌어 이제부터 열심히 해야지ㅎㅎㅎ'
    
    okt = Okt()
    
    print(okt.morphs(text))
    # ['한글', '자연어', '처리', '는', '재밌어', '이제', '부터', '열심히', '해야지', 'ㅎㅎㅎ']
    
    print(okt.morphs(text, stem=True))
    # ['한글', '자연어', '처리', '는', '재밌다', '이제', '부터', '열심히', '하다', 'ㅎㅎㅎ']
    ```

    * `stem=True`를 설정하면 `재밌어` →`재밌다`, `해야지`→`하다` 와 같이 변경됨을 알 수 있다.

    

  * Okt().nouns() : 텍스트에서 명사를 추출한다.

    ```python
    print(okt.nouns(text))
    # ['한글', '자연어', '처리', '이제']
    ```

    * 명사만 추출한다.

    

  * Okt().phrases() : 텍스트에서 어절을 추출한다.

    ```python
    print(okt.phrases(text))
    # ['한글', '한글 자연어', '한글 자연어 처리', '이제', '자연어', '처리']
    ```

    * 어절들을 추출한다.

    

  * Okt().pos() : 품사 태깅한다.

    ```python
    print(okt.pos(text))
    # [('한글', 'Noun'), ('자연어', 'Noun'), ('처리', 'Noun'), ('는', 'Josa'), ('재밌어', 'Adjective'), ('이제', 'Noun'), ('부터', 'Josa'), ('열심히', 'Adverb'), ('해야지', 'Verb'), ('ㅎㅎㅎ', 'KoreanParticle')]
    
    print(okt.pos(text, join=True))
    # ['한글/Noun', '자연어/Noun', '처리/Noun', '는/Josa', '재밌어/Adjective', '이제/Noun', '부터/Josa', '열심히/Adverb', '해야지/Verb', 'ㅎㅎㅎ/KoreanParticle']
    ```

    

