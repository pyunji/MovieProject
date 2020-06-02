### :mag_right:git 사용법

```
git clone <url>
    : git repo를 현재 폴더에 클론함
git remote add <name: ex.origin> <url>
    : git repo를 원격으로 등록
git remote -v
    : 현재 원격으로 등록되어있는 git 저장소 확인
git remote rm <name>
    : 원격 접속 해제
git pull origin master
    : 해당 폴더의 변경 사항을 포함해 모든 파일을 로컬에 복제
git add .
    : 모든 로컬 파일의 변경 사항을 git 저장소에 할당
git commit -m "<message>"
    : message와 함께 변경 사항 커밋
git push origin master
    : git 저장소에 push
```