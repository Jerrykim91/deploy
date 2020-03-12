# deploy
deploy

# 세팅절차 
- 1. git 새로운 저장소 생성 
- https://github.com/유저어아디/deploy.git

- 2. 로컬 PC에서 aws폴더를 vscode 에서 오픈 
- 3. 터미널 오픈
- 4. `$ git clone https://github.com/유저어아디/deploy.git`
- 5. 터미널에서  `cd deploy `

# 파일 세팅 (~/aws/deploy)
- 1. deploy.json, fabfile.py 두 파일을 deploy에 옮긴다 
- 2. 서버파일 생성  
- 3. run.py, wsgi.py 생성
- 4. 코드작성 
- 5. 배포관련 환경 변수 파일 수정(deploy.json) 