from flask import *
import os

app = Flask(__name__,static_folder='static')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/file',methods=['GET'])
def get_file():
   filename = request.args.get('file')
   file=open('/home/thiru_krish/Desktop/hackin/chall-1/templates/'+filename,'rb')

   return file.read()
   


if __name__ == '__main__':
   app.run('127.1',9090,debug=True)