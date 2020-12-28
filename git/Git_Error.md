# Git Error

> Git error와 해결 방법에 대해서 다룬다.

1. 위에서 commit 명령을 통해서 remote repo에 반영하기 전에 HEAD에 먼저 반영을 한다고 하였다. 하지만 가끔 실수로 commit을 하던가 아니면 commit 단계에서의 어떤 문제로 인하여 push가 안되는 경우가 생길 수 있다. 이 경우에는 commit을 취소하여 문제를 해결하는 방법이 있을 수 있다.

```bash
>>> git push origin master
Username for 'https://github.com': hcnoh
Password for 'https://hcnoh@github.com':
Counting objects: 15, done.
Delta compression using up to 12 threads.
Compressing objects: 100% (14/14), done.
Writing objects: 100% (15/15), 203.79 MiB | 10.41 MiB/s, done.
Total 15 (delta 6), reused 0 (delta 0)
remote: Resolving deltas: 100% (6/6), completed with 3 local objects.
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.gitub.com.
remote: error: Trace: 08f3b36675dd671be3f4b76f255740a4
remote: error: File models/model.ckpt.data-00000-of-00001 is 217.98 MB; this exceeds GitHub's file size limit of 100.00 MB
To https:// github.com/hcnoh/wavenet-tensorflow
 ! [remote rejected] master -> master (pre-receive hook declined)
 error: failed to push some refs to 'https://github.com/hcnoh/wavenet-tensorflow'
```

push를 한 경우 다음과 같은 에러가 발생하였다. 어떤 파일의 용량이 219MB의 크기를 가지고있고 이것은 제한 용량을 초과하기 때문에 push가 되지 않는 것이다. 이 경우 저 파일을 지우고 다시 commit을 하더라도 이전에 commit한 것들이 여전히 push에 반영되기 때문에 같은 에러가 발생할 것이다. 이 경우에는 이전에 해놓은 commit들을 삭제해야 한다.

commit을 취소하는 명령들은 다음과 같다.

- 최종 commit을 취소하되 파일은 복구/삭제하지 않는 명령

```
>>> git reset HEAD^
```

- 최종 commit을 취소하고 파일도 복구/삭제

```
>>> git reset --hard HEAD^
```

- 최종 commit을 n개 취소하되 파일은 복구/삭제하지 않는 명령

```
>>> git reset HEAD~n
```

- 최종 commit을 n개 취소하고 파일도 복구/삭제

```
>>> git reset --hard HEAD~n
```