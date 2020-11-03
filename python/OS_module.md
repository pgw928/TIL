# OS 모듈 (+ shutil 모듈)

> 수많은 Image 파일과 같은 데이터를 손쉽게 다루기 위해 파일 경로등을 다룬다. 코드부분에서 `import os`와 `import shuitl` 부분은 언급하지 않는다. 또한 기본적으로 알아야 할것은 `/`로 시작하면 무조건 절대경로이고 아니면 상대 경로를 나타낸다. 또한 `.`으로 시작하면 현재 directory를 의미한다.



* #### os.getcwd() : 현재 작업 폴더의 절대 경로를 출력한다.

```python
print(os.getcwd)

# C:\notebook_dir
```



* #### os.listdir('경로') : 경로 폴더 안에 있는 파일/서브 디렉토리 리스트를 모두 가져온다.

```python
print(os.listdir(os.getcwd()))

['.ipynb_checkpoints', '01.numpy.ipynb', '01.numpy_teacher.ipynb', '02.pandas.ipynb', '03.Machine_Learning.ipynb', '03.머신러닝.ipynb', '03.머신러닝_teacher.ipynb', '04.Machine_Learning(2).ipynb', '1013.ipynb', '1013_tensorflow2_teacher.ipynb', '1015_tensorflow2.ipynb', '1016_TF1.15_teacher.ipynb', '1019_TF2.1_teacher.ipynb', '10_22부터_10_26까지_cnn_1.15.ipynb', 'cache', 'data', 'DNN_mnist_1.15(16~19).ipynb', 'Elice.ipynb', 'exercise_teacher.ipynb', 'image', 'mnist.ipynb', 'multi-Linear_regression_review.ipynb', 'os 다루기.ipynb', 'Pandas_Exercise_teacher.ipynb', 'plant.ipynb', 'tf2_dnn(mnist)_svm_DT.ipynb', 'titanic.ipynb', 'titanic_exercise_tf1.15.ipynb', '수행평가', '오존 문제.ipynb']
```



* #### os.path.abspath('경로') : 경로의 절대경로를 출력한다.

```python
print(os.path.abspath('.'))

# C:\notebook_dir
```



* #### os.path.exists('경로') : 경로의 유효성을 True/False로 출력한다.

```python
print(os.path.exists('01.numpy.ipynb'))
# True

print(os.path.exists('02.numpy.ipynb'))
# False
```



* #### os.mkdir('경로') : 새 폴더를 만든다.

```python
base_dir = './data/try_out'
if not os.path.exists(base_dir):
    os.mkdir(base_dir)       
# 폴더가 생성된다. 이미 존재할 시 error가 발생하므로 os.path.exists로 유효성을 검증해준다

```



* #### os.path.join('경로','file명')  : 경로에 파일명을 연결해준다.

```python
base_dir = './data/try_out'
train_dir = os.path.join(base_dir, 'train')
print(train_dir)
# './data/try_out\train'
```



* #### os.walk('경로') : path, directory, file 명들을 담고 있는 객체이다.

```python
for path, directory, file in os.walk('./data'):
    print(path)
    print(directory)
    print(file)


./data
['json', 'Koweps', 'mnist', 'titanic', 'try_out', '공모전']
['admission.csv', 'bmi.csv', 'daegu.csv', 'Koweps_hpc10_2015_beta1.sav', 'movies.csv', 'mpg.txt', 'ozone.csv', 'ratings.csv', 'seoul.csv', 'student.csv']
./data\json
[]
['books_columns.json', 'books_records.json']
./data\Koweps
[]
['Koweps_Codebook.xlsx', 'Koweps_hpc10_2015_beta1.sav']
./data\mnist
[]
['submission.csv', 'test.csv', 'train.csv']
./data\titanic
[]
['submission.csv', 'submission1.csv', 'test.csv', 'train.csv']
./data\try_out
['train', 'validataion']
[]
./data\try_out\train
['0', '1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '3', '4', '5', '6', '7', '8', '9']
[]
```



* ####  shutil.move(src, dst) : 파일 이동

```python
src ='/home/workspace/PKU_black_out.ipynb'
dst = '/home/workspace/user-workspace/pku/PKU_black_out.ipynb'
shutil.move(src,dst) # source에서 destination으로 이동시켜준다.
```



* #### shutil.rmtree('경로') : 경로에 있는 모든 파일을 삭제한다. 신중히 실행한다.

```python
shutil.rmtree(base_dir)
```



* #### shutil.copyfile(src, dst) : 파일 복사





## train, validation 나누는 예제

> train 하나의 폴더를 train/validation 폴더로 나누어 category 별로 나눠주는 코드를 작성한다. 여기서 `shutil.copyfile` 을 사용해 원본이 아닌 복사본 파일을 이용한다.

```python
import os
import shutil

original_dataset_dir = './data/공모전/train'

base_dir = './data/try_out'
if not os.path.exists(base_dir):
    os.mkdir(base_dir)        

train_dir = os.path.join(base_dir, 'train')
if not os.path.exists(train_dir):
    os.mkdir(train_dir)

validation_dir = os.path.join(base_dir, 'validataion')
if not os.path.exists(validation_dir):
    os.mkdir(validation_dir)

for i in range(20):
    train_class_dir = os.path.join(train_dir,'{}'.format(i)) 
    if not os.path.exists(train_class_dir):
        os.mkdir(train_class_dir)

for i in range(20):
    validation_class_dir = os.path.join(validation_dir,'{}'.format(i)) 
    if not os.path.exists(validation_class_dir):
        os.mkdir(validation_class_dir)

# 20개의 category가 있기 때문에 train/validation 폴더를 생성해 각각 20개의 폴더를 만들어준다.
```

```python
train_size = 0.7    

# file 형식 : '3_5_1123.jpg' , 3: plant_label, 5:disease_label
plant_label  = ['3','3','4','4','4','5','7','7','8','8','10','11','13','13','13','13','13','13','13','13']
disease_label = ['5','20','2','7','11','8','1','20','6','9','20','14','1','6','9','15','16','17','18','20']

for path, direct, files in os.walk(original_dataset_dir):
    for i in range(20):
        temp_list = [ file for file in files if file.split('_')[0]==plant_label[i] and file.split('_')[1]==disease_label[i]]
        num_of_train = int(len(temp_list)* train_size)    
        train_list      = temp_list[:num_of_train]
        validation_list = temp_list[num_of_train:]
        for train_file in train_list:
            src = os.path.join(original_dataset_dir, train_file)
            dst = os.path.join(os.path.join(train_dir, '{}'.format(i)), train_file)
            shutil.copyfile(src, dst)
        for validation_file in validation_list:
            src = os.path.join(original_dataset_dir, validation_file)
            dst = os.path.join(os.path.join(validation_dir, '{}'.format(i)), validation_file)
            shutil.copyfile(src, dst)

```



 