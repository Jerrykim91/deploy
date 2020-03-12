# -*- coding: utf-8 -*-
# import 
from flask import Flask, request, render_template
import datetime
import tensorflow as tf
import numpy as np

# instance creating
app = Flask(__name__)

# 플레이스 홀드 설정 =>  x,y 값을 정의
X = tf.placeholder( tf.float32, shape = [None, 4])
Y = tf.placeholder( tf.float32, shape = [None, 1])

# 가중치와 바이어스 값을 초기화 
W = tf.Variable( tf.random_normal( [4, 1] ), name = "weight" )
b = tf.Variable( tf.random_normal( [1] ), name = "bias" )

# 가설을 설정 => 선형회귀모델을 그대로 이용
hypothesis = tf.matmul( X, W ) + b

# 저장된 학습 모델을 불러오고 객체를 초기화 하는 식 역시 선언
saver = tf.train.Saver()
model = tf.global_variables_initializer()

# 세션 객체 설정 
sess = tf.Session()
sess.run( model )

# 저장된 모델을 세션에 적용 
save_path = "./model/saved.cpkt"
saver.restore(sess, save_path)

# Defining the home page of our web
@ app.route("/", methods=['GET', 'POST']) # page path setting 

def index(): 
    # GET => 
    if request.method == 'GET':
        return render_template('index.html')

    # POST
    if request.method == 'POST':

        # 파라미터를 전달 받음 => 사용자의 입력
        avg_temp  = float(request.form['avg_temp'])
        min_temp  = float(request.form['min_temp'])
        max_temp  = float(request.form['max_temp'])
        rain_fall = float(request.form['rain_fall'])
        
        # 배추가격 변수 선언 
        price = 0

        # 파라미터를 배열로 
        data  = ((avg_temp, min_temp, max_temp, rain_fall), (0, 0, 0, 0))
        arr   = np.array(data, dtype = np.float32)

        # 입력 값을 토대로 예측 
        x_data = arr[0:4]
        dict   = sess.run( hypothesis, feed_dict = {X : x_data})

        # 배추 결과 저장 
        price  = dict[0]
        
        # 사용자에게 입력받은데이터를 돌려 사용자에게 돌려줌
        return render_template('index.html', price = price)

if __name__ == "__main__":
    # 디버그 하면 자동으로 로그 확인 
    app.run( debug = True )

# It works(ok) 