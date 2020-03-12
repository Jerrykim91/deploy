'''
아파치: apache( or NGINX ) 서버(웹서버) 가 가장 먼저 찾는 파일 
wsgi기능은 서버기능을 제공하는 역활 

'''
import sys, os 

# 절대 경로 잡아줌 
cur_dir = os.getcwd()

# 접속 로그, 에러로그 존재 
# 로그의 위치를 조정 
sys.stdout = sys.stderr
sys.path.insert( 0, cur_dir ) 

# run.py 가지고 오기  
from run import app as application
