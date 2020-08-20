# Git 기초

> Git은 분산형 버전관리시스템(DVCS)이다.

Git을 윈도우에서 활용하기 위해서는 [git bash](https://gitforwindows.org/)를 설치해야 한다.

## 1. 저장소 초기화

``` bash
$ git init
Initialized empty Git repository in C:/Users/i/Desktop/TIL/.git/

(master) $
```

* 로컬 저장소를 만들고 나면, `.git/` 폴더가 생성되고, bash에 `(master)`  라고 표기 된다.
* 반드시 저장소를 만들기 전에 원하는 디렉토리인지 확인하는 습관을 가지고, 저장소 내부에 저장소를 만들지 말자.
  * 예)Desktop->git저장소, TIL->다른 git 저장소  (X)

## 2. `add`

작업한 내용을 커밋 대상 목록에 추가한다.

```bash
$ git status
On branch master

No commits yet
# Untracked files => Git으로 관리된 적 없는 파일
Untracked files:
# 커밋 될 것들에 포함시키기 위해서는 add 명령어를 써라
  (use "git add <file>..." to include in what will be committed)
        markdown-images/
        markdown.md
# 총평
# 커밋될 곳에 없다(nothing)
# 하지만, 새로 생성한 파일(untracked files)은 존재한다.
nothing added to commit but untracked files present (use "git add" to track)

```

```bash
$ git add .				# 현재 디렉토리(하위 디렉토리 포함)
$ git add a.html		# 특정 파일
$ git add b.html c.html # 특정 다수 파일
$ git add blog/			# 특정 폴더


```

```bash
# add 명령어 후 상태
$ git status
On branch master

No commits yet
# 커밋이 될 변경 사항들
# working directory X
# Staging area O
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   "markdown-images/\354\272\241\354\262\230.JPG"
        new file:   markdown.md

```

작업 공간 : working directory

커밋 대상 목록 : staging area

```bash
$ git commit -m 'Add markdown.md'
[master (root-commit) 15a5468] Add markdown.md
 2 files changed, 80 insertions(+)
 create mode 100644 "markdown-images/\354\272\241\354\262\230.JPG"
 create mode 100644 markdown.md

```

* 커밋은 버전(이력)을 기록하는 명령어이다.
* 커밋메세지는 해당하는 이력을 나타낼 수 있도록 작성 하여야 한다.
* 커밋 이력을 확인하기 위해서는 아래의 명령어를 사용한다.

```bash
$ git log
commit 15a54685f23c77ec4fb944648efeebf79d2e633f (HEAD -> master)
Author: KeunungPark <pku928@naver.com>
Date:   Thu Aug 20 14:58:14 2020 +0900

    Add markdown.md
$ git log -1
$ git log --oneline
$ git log --oneline
15a5468 (HEAD -> master) Add markdown.md
$ git log --online -1
```



``` bash
$ git status
On branch master
# WD X
# Staging area X
nothing to commit, working tree clean
```

