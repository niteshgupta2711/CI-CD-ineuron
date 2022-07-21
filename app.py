from housing.logger import logging
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/',methods=["GET"])
def main():
    return 'started machine learning project'
    

if __name__=='__main__':
    app.run(debug=True)
    logging.info('app has started')