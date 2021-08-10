## Pycaret(1)

> AutoML의 하나인 `PyCaret`에 대해서 다룬다.



* ### 소개

  *  신흥강자로 부상한 AutoML 도구이다.
  * 자동으로 하기 때문에 성능이 낮다고 생각하면 안된다.
  * https://pycaret.org/



* ### 데이터

  ```python
  import os
  
  BASE_DIR = './data' 
  
  train_path = os.path.join(BASE_DIR, 'train.csv')
  test_path = os.path.join(base_dir, 'test.csv')
  
  train = pd.read_csv(train_path)
  test = pd.read_csv(test_path)
  
  train.head()
  ```

  ![image-20210810153134615](markdown-images/image-20210810153134615.png)



* ### 설치 및 불러오기

  ```python
  !pip install pycaret
  from pycaret.classification import *
  ```

  * 많은 삶들이 `*`를 사용해 전체 패키지를 불러온다.



* ### 셋업

  > 전체적인 시스템을 준비한다. 기본세팅으로 `data`,`target`(target 컬럼명), `fold`를 입력해준다.

  ```python
  setup(data=train,
        target='credit',
        fold=5,
        silent=True)
  ```

  ![image-20210810153533047](markdown-images/image-20210810153533047.png)



* ### Metric 확인 및 추가

  * 확인 : 사용할 수 있는 metic 정보를 알 수 있다.

    ```python
    get_metrics()
    ```

    ![image-20210810154005033](markdown-images/image-20210810154005033.png)

  * `LogLoss` metric 추가

    ```python
    add_metric('logloss',  # id
               name='LogLoss', 
               score_func=log_loss, 
               greater_is_better=False, 
               target='pred_proba')
    ```

    * `greater_is_better` : 클수록 좋은 값으로 취급할지인데 `LogLoss`값은 낮을수록 좋으므로 `False`를 입력해 준다.
    * `target`의 `default`는 `pred`이다.

  * 다시 확인 : 추가 되었음을 알 수 있다.

    ```python
    get_metrics()
    ```

    ![image-20210810154413241](markdown-images/image-20210810154413241.png)





* ### 사용 가능 모델

  ```python
  models()
  ```

  ![image-20210810172526518](markdown-images/image-20210810172526518.png)



* ### 모델 한가지로 학습

  > lightgbm을 사용해 모델을 생성하고 학습 및 결과를 살펴본다.

  * 모델 생성 : 생성과 동시에 결과를 알려준다.

    ```python
    lightgbm = create_model(estimator='lightgbm')
    ```

    ![image-20210810172603774](markdown-images/image-20210810172603774.png)

  * 모델 튜닝 : 여러가지 library로 hyperparameter 튜닝이 가능하다.

    * default : `'scikit-learn'`

      ```python
      tuned_lightgbm = tune_model(lightgbm)
      ```

      ![image-20210810172838787](markdown-images/image-20210810172838787.png)

    * `'optuna'` : `!pip install optuna` 로 다운받아 가능하다.

      ```python
      tuned_lightgbm_optuna = tune_model(lightgbm, search_library='optuna')
      ```

      ![image-20210810172942097](markdown-images/image-20210810172942097.png)

    * 그 밖에, `'tune-sklearn'`, `'scikit-optimize'`를 활용할 수 있다.

  * 시각화 : `plot_model`을 사용해 모델에 관해 편하게 시각화가 가능하다.

    * Validataion Curve

      ```python
      plot_model(tuned_lightgbm_optuna, plot='vc')
      ```

      ![image-20210810173706878](markdown-images/image-20210810173706878.png)

    * confusion_matrix

      ```python
      plot_model(tuned_lightgbm_optuna, plot='confusion_matrix')
      ```

      ![image-20210810173737397](markdown-images/image-20210810173737397.png)

    * ROC curve

      ```python
      plot_model(tuned_lightgbm_optuna, plot='auc')
      ```

      ![image-20210810173845484](markdown-images/image-20210810173845484.png)

    * Feature Importance

      ```python
      plot_model(tuned_lightgbm_optuna, plot='feature_all')
      ```

      ![image-20210810173928086](markdown-images/image-20210810173928086.png)

    * 참고 : `evaluate_model`을 통해 선택을 통해 모델 그래프나 정보를 볼 수 있다.

      ```python
      evaluate_model(tuned_lightgbm_optuna)
      ```

      ![image-20210810183046794](markdown-images/image-20210810183046794.png)

  * test set 예측(1) : 결과인 `class`와 `raw_score=True`를 설정시 확률까지 기존 `test`에 컬럼ㅇ로 추가되어  `DataFrame`을 생성해준다.

    ```python
    final_lgbm = finalize_model(tuned_lightgbm_optuna)
    res = predict_model(final_lgbm, test, raw_score=True)
    res.iloc[:,-4:]
    ```

    ![image-20210810222456816](markdown-images/image-20210810222456816.png)
    
  * test set예측(2) :`sklearn`의  `pipeline`형식으로 바꾸어 `predict_proba` 메소드를 사용할 수 있다.
  
    * 파이프라인 불러오기
  
      ```python
      prep_pipe = get_config('prep_pipe')
      type(prep_pipe) # sklearn.pipeline.Pipeline
      ```
  
      ```python
      prep_pipe
      ## 결과
      Pipeline(memory=None,
               steps=[('dtypes',
                       DataTypes_Auto_infer(categorical_features=[],
                                            display_types=False, features_todrop=[],
                                            id_columns=['index'],
                                            ml_usecase='classification',
                                            numerical_features=[], target='credit',
                                            time_features=[])),
                      ('imputer',
                       Simple_Imputer(categorical_strategy='not_available',
                                      fill_value_categorical=None,
                                      fill_value_numerical=None,
                                      numer...
                      ('scaling', 'passthrough'), ('P_transform', 'passthrough'),
                      ('binn', 'passthrough'), ('rem_outliers', 'passthrough'),
                      ('cluster_all', 'passthrough'),
                      ('dummy', Dummify(target='credit')),
                      ('fix_perfect', Remove_100(target='credit')),
                      ('clean_names', Clean_Colum_Names()),
                      ('feature_select', 'passthrough'), ('fix_multi', 'passthrough'),
                      ('dfs', 'passthrough'), ('pca', 'passthrough')],
               verbose=False)
      ```
  
    * 파이프라인에 위에서 만들어진 모델 추가
  
      ```python
      prep_pipe.steps.append(['trained_model', voting_tune_optuna])
      prep_pipe
      ## 결과
      Pipeline(memory=None,
               steps=[('dtypes',
                       DataTypes_Auto_infer(categorical_features=[],
                                            display_types=False, features_todrop=[],
                                            id_columns=['index'],
                                            ml_usecase='classification',
                                            numerical_features=[], target='credit',
                                            time_features=[])),
                      ('imputer',
                       Simple_Imputer(categorical_strategy='not_available',
                                      fill_value_categorical=None,
                                      fill_value_numerical=None,
                                      numer...
                                                                var_smoothing=1e-09)),
                                                    ('lda',
                                                     LinearDiscriminantAnalysis(n_components=None,
                                                                                priors=None,
                                                                                shrinkage=None,
                                                                                solver='svd',
                                                                                store_covariance=False,
                                                                                tol=0.0001))],
                                        flatten_transform=True, n_jobs=-1,
                                        verbose=False, voting='soft',
                                        weights=[0.8935957404176336,
                                                 0.2966272856190533,
                                                 0.5839363934433777,
                                                 0.6254688659302372,
                                                 0.12890313666331554,
                                                 0.09569782255345581])]],
               verbose=False)
      ```
  
    * test set 예측
  
      ```python
      prep_pipe.predict_proba(test)
      ## 결과
      array([[0.08422577, 0.10594238, 0.80983186],
             [0.12410099, 0.15575107, 0.72014793],
             [0.10716005, 0.20692658, 0.68591336],
             ...,
             [0.08977594, 0.19165872, 0.71856534],
             [0.11115337, 0.16746082, 0.72138581],
             [0.05171066, 0.23571267, 0.71257667]])
      ```
  
      
  
    

