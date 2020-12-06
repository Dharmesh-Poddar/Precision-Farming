import os
import sys
import numpy as np
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from PIL import Image, ImageFile
from io import BytesIO
import matplotlib.pyplot as plt
import base64


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route('/Prediction', methods=['GET','POST'])
def pred():
    if request.method=='POST':
         file = request.files['file']
         # file: cantains all uploaded itmes 
         # conduct all the relevant operations HERE



    return render_template('Pred3.html')






if __name__=='__main__':
    app.run()
