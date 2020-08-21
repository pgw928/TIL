# branch

## 기본 명령어 

* 브랜치 목록

  ```bash
  $ git branch
  ```

* 브랜치 생성

  ```bash
  $ git branch {브랜치이름}
  ```

* 브랜치 이동

  ```bash
  $ git checkout {브랜치이름}
  ```

  ```bash
  # 브랜치 생성 및 이동
  $ git checkout -b {브랜치이름}
  ```

* 브랜치 병합

  ```bash
  (master) $ git merge {브랜치이름}
  ```

  {브랜치이름}을 (master)로 병합

* 브랜치 삭제

  ```bash
  $ git branch -d {브랜치이름}
  ```

  

### 상황 1. fast-foward

> fast-foward는 feature 브랜치 생성된 이후 master 브랜치에 변경 사항이 없는 상황

1. feature/blog branch 생성 및 이동

   ```bash
   (master) $ git checkout -b feature/blog
   Switched to a new branch 'feature/blog'
   (feature/blog) $
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch blog.html
   $ git add blog.html
   $ git commit -m 'Complete blog app'
   [feature/blog 1aa1e05] Complete blog app
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 blog.html
   
   $ git log --oneline
   1aa1e05 (HEAD -> feature/blog) Complete blog app
   5315196 (master) Hellobranch
   7bcaf91 Init
   
   ```


3. master 이동

   ```bash
   $ git checkout master
   Switched to branch 'master'
   (master) $ git log --oneline
   5315196 (HEAD -> master) Hellobranch
   7bcaf91 Init
   ```


4. master에 병합

   ```bash
   $ git merge feature/blog
   Updating 5315196..1aa1e05
   Fast-forward
    blog.html | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 blog.html
   ```


5. 결과 -> fast-foward (단순히 HEAD를 이동)

   ```bash
   $ git log --oneline
   1aa1e05 (HEAD -> master, feature/blog) Complete blog app
   5315196 Hellobranch
   7bcaf91 Init
   ```

6. branch 삭제

   ```bash
   $ git branch -d feature/blog
   Deleted branch feature/blog (was 1aa1e05).
   ```

   

   

---

### 상황 2. merge commit

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 다른 파일이 수정되어 있는 상황
>
> git이 auto merging을 진행하고, commit이 발생된다.

1. feature/poll branch 생성 및 이동

   ```bash
   (master)
   $ git checkout -b feature/poll
   Switched to a new branch 'feature/poll'
   (feature/poll) $
   ```

2. 작업 완료 후 commit

   ```bash
   $ touch poll.html
   $ git add poll.html
   $ git commit -m 'Complete poll app'
   [feature/poll 7e2990c] Complete poll app
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 poll.html
   
   $ git log --oneline
   7e2990c (HEAD -> feature/poll) Complete poll app
   1aa1e05 Complete blog app
   5315196 Hellobranch
   7bcaf91 Init
   
   ```

3. master 이동

   ```bash
   $ git checkout master
   ```

4. *master에 추가 commit 이 발생시키기!!*

   * **다른 파일을 수정 혹은 생성하세요!**

   ```bash
   $ touch hotfix.css
   $ git add .
   $ git commit -m 'hofix in master'
   [master b25f8ab] hofix in master
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 hotfix.css
   $ git log --oneline
   b25f8ab (HEAD -> master) hofix in master
   1aa1e05 Complete blog app
   5315196 Hellobranch
   7bcaf91 Init
   
   ```

5. master에 병합

   ```bash
   (master) $ git merge feature/poll
   hint: Waiting for your editor to close the file...Merge made by the 'recursive' strategy.
    poll.html | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 poll.html
   ```

6. 결과 -> 자동으로 *merge commit 발생*

   * vim 편집기 화면이 나타납니다.

   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
      
   * 커밋이  확인 해봅시다.

7. 그래프 확인하기

   ```bash
   $ git log --oneline --graph
   *   fb9c33d (HEAD -> master) Merge branch 'feature/poll' into master
   |\
   | * 7e2990c (feature/poll) Complete poll app
   * | b25f8ab hofix in master
   |/
   * 1aa1e05 Complete blog app
   * 5315196 Hellobranch
   * 7bcaf91 Init
   ```

8. branch 삭제

   ```bash
   $ git branch -d feature/poll
   ```

---

### 상황 3. merge commit 충돌

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 동일 파일이 수정되어 있는 상황
>
> git이 auto merging을 하지 못하고, 해당 파일의 위치에 라벨링을 해준다.
>
> 원하는 형태의 코드로 직접 수정을 하고 merge commit을 발생 시켜야 한다.

1. feature/board branch 생성 및 이동

   ```bash
   $ git checkout -b feature/board
   ```

2. 작업 완료 후 commit

   * readme  파일 수정 후 아래 명령어

   ```bash
   $ touch board.html
   $ git status
   On branch feature/board
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
     # 추후에 마스터에서도 README를 고쳐서 충돌 발생시킬 예정
           modified:   README.md
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           board.html
   
   no changes added to commit (use "git add" and/or "git commit -a")
   $ git add .
   $ git commit -m 'Complate board and update README'
   [feature/board deff7fe] Complate board and update README
    2 files changed, 1 insertion(+)
    create mode 100644 board.html
    
   $ git log --oneline
   deff7fe (HEAD -> feature/board) Complate board and update README
   fb9c33d (master) Merge branch 'feature/poll' into master
   b25f8ab hofix in master
   7e2990c Complete poll app
   1aa1e05 Complete blog app
   5315196 Hellobranch
   7bcaf91 Init
   ```


3. master 이동

   ```bash
   $ git checkout master
   ```


4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**
   

```bash
   # README 수정 후 commit
   $ git add README.md
   $ git commit -m 'Update README'
   $ git log --oneline
   a6530b3 (HEAD -> master) Update README
   fb9c33d Merge branch 'feature/poll' into master
   b25f8ab hofix in master
   7e2990c Complete poll app
   1aa1e05 Complete blog app
   5315196 Hellobranch
   7bcaf91 Init

   ```
   
5. master에 병합

   ```bash
   $ git merge feature/board
   Auto-merging README.md
   # 내용 충돌 
   # README.md에서 충돌
   CONFLICT (content): Merge conflict in README.md
   # 자동 병합 실패;
   # 충돌을 고치고 다시 커밋해라!
   Automatic merge failed; fix conflicts and then commit the result.
   
   (master|MERGING) $ git status
   On branch master
   You have unmerged paths.
   # 충돌 고치고 commit!
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   # 커밋될 변경사항
   Changes to be committed:
           new file:   board.html
   
   # 병합 되지 않은 파일들
   Unmerged paths:
   # 해결하고 add해!
     (use "git add <file>..." to mark resolution)
           both modified:   README.md
   ```

   


6. 결과 -> *merge conflict발생*

   


7. 충돌 확인 및 해결

   ```
   <<<<<<< HEAD
   def index(request):
   	return 
   =======
   def create(request):
   	return 
   >>>>>>> feature/board
   ```

   ```
   # master에서 수정함
   ```

   * 수정 후에는 반드시 해당 파일 `add` 

     ```bash
     $ git add .
     ```


8. merge commit 진행

    ```bash
    $ git commit
    ```

   * vim 편집기 화면이 나타납니다.
   
   * 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
      * `w` : write
      * `q` : quit
      
   * 커밋이  확인 해봅시다.
   
9. 그래프 확인하기

    ```bash
   $ git log --oneline --graph
   *   ba913f9 (HEAD -> master) Merge branch 'feature/board' into master
   |\
   | * deff7fe (feature/board) Complate board and update README
   * | a6530b3 Update README
   |/
   *   fb9c33d Merge branch 'feature/poll' into master
   ```


10. branch 삭제

    ```bash
    $ git branch -d feature/board
    ```
    
    
```

```