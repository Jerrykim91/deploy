# run.py 
# 실제 서비스 
from flask import Flask

app = Flask(__name__)

# 라우트 
@app.route('/')
def home():
    return 'aws 홈페이지- 수정 '


# 실행 

if __name__ == '__main__':
    app.run(debug=True)