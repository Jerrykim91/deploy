# deploy
deploy

# 세팅절차 
1. git 새로운 저장소 생성 
    - https://github.com/jsrrykim91/deploy.git

2. 로컬 PC에서 aws폴더를 vscode 에서 오픈 
3. 터미널 오픈
4. `$ git clone https://github.com/유저아이디/deploy.git`
5. 터미널에서 경로 이동  `cd deploy`

# 파일 세팅 (~/aws/deploy)
1. deploy.json, fabfile.py 두 파일을 deploy에 옮긴다 
2. 서버파일 생성  
3. run.py, wsgi.py 생성
4. 코드작성 
5. 배포관련 환경 변수 파일 수정(deploy.json) 

```json
// deploy.json
{
// 깃허브 경로 
    "REPO_URL":"https://github.com/유저아이디/deploy",
// 이름 
    "PROJECT_NAME":"이름",
//  IPv4 :아마존 퍼플릭 도메인 - 만약 도매인 구매하면 : 아이피를 집어 넣으면 됨 
    "REMOTE_HOST":" 주소 ",
//  IPv4 퍼블릭 IP
    "REMOTE_HOST_SSH":"IP",
    "REMOTE_USER":"ubuntu"
  }
```
6. requirements.txt 
    - 본서비스를 구동하기 위해 필요 
```txt
# 버전정보입력

flask ==  1.0.2  
```
---

# 구동 
- python3 버전 기반으로 수행 
- 운영 체계 및 서버 세팅 및 배포, 업데이트 관리등을 자동화 하는 모듈 => fabric3

1. fabric3 패키지 설치 
    - `$ pip3 install fabric3`
2. git에 최종 소스 반영 

```py
#  fabfile.py 수정 
# line 24
env.use_ssh_config = True
env.key_filename = '../내파일이름.pem' # 변경
project_folder = '/home/{}/{}'.format(env.user, PROJECT_NAME)
apt_requirements = [
    'curl',
    'git',
    'python3-dev',
    'python3-pip',
    'build-essential',
    'apache2',
    'libapache2-mod-wsgi-py3',
    'python3-setuptools',
    'libssl-dev', 
    'libffi-dev',
]
```
---

```bash

PS C:\Users\admin\Desktop\aws\deploy> fab new_server
[13.209.97.183] Executing task 'new_server'

Warning: Unable to load SSH config file 'C:\Users\admin\.ssh\config'

would you update?: [y/n]y

```

3. 브라우저 가동 : http://13.209.97.183/
    - 브라우저 접속 

4. 접속 로그 확인 (리눅스에서 진행 )
    - $ tail -f /var/log/apache2/access.log
    - 모니터링하다가 
    - 종료 : ctrl +c 

5. 에러 로그 
    - $ tail -f /var/log/apache2/error.log
    - 종료 : ctrl +c 

``` bash
# 디렉토리 확인 
ubuntu@ip-***:~$ ls
deploy
ubuntu@ip-***:~$ cd deploy
ubuntu@ip-***:~/deploy$ ls
README.md  deploy.json  fabfile.py  reguirements.txt  run.py  wsgi.py
ubuntu@ip-***:~/deploy$

# 로그 확인 
ubuntu@ip-***:~/deploy$ tail -f /var/log/apache2/access.log
tail: cannot open '/var/log/apache2/access.log' for reading: No such file or directory
tail: no files remaining
ubuntu@ip-***:~/deploy$ # 동작 안함 - 서버 요청이 막힘 

```
- 인바운드 룰 
- 새로 생성 
    - http -> anywhere
---
## 이후 과정 
- 업데이트 
    - `$ fab deploy`
---
## 잘 안될때 
- 소스 코드상에 , 파일 명, 설정 값등 오타가 없어야 한다. 
- git에 최종 소스코드가 올라 가있어야 한다 
- 리눅스에서 기존의 흔적을 모드 삭제 해야한다 
```
$ls -a 
$ rm -r -f .virtualenvs
- 로컬 PC
$ fab new_server
```
---

## 가상호스트가 설정된 부분 
- deploy 프로젝트 명 - json에 정의 되어 있음 
    - $ cat /etc/apache2/sites-available/deploy.conf

    ```bash
    <VirtualHost *:80>
    ServerName 13.209.97.183
    <Directory /home/ubuntu/deploy>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>
    WSGIDaemonProcess deploy python-home=/home/ubuntu/.virtualenvs/deploy python-path=/home/ubuntu/deploy
    WSGIProcessGroup deploy
    WSGIScriptAlias / /home/ubuntu/deploy/wsgi.py

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    </VirtualHost>
    ```
- 서버 주소 변경 
    - git 업로드

- 변경후 
    - 업데이트 
        - `$ fab deploy`

- 변경 됨 

#### 여기까지 배포 운영 
-- 