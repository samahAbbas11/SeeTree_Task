from flask import Flask, render_template, request, abort
import requests
from PIL import Image,ImageOps
import functions
import numpy as np
from flask_caching import Cache  # Import Cache from flask_caching module

app = Flask(__name__)

app.config.from_object('config.BaseConfig')  # Set the configuration variables to the flask application
cache = Cache(app)  # Initialize Cache


prange=[]
for i in range(101):
    prange.append("p"+str(i))


# stats route (img statistics) --> supports only GET requests
@app.route('/stats/<img_file_name>/<func_name>', methods = ['GET'])

@cache.cached(timeout=300, query_string=True)
def stats(img_file_name , func_name):

    url= "https://storage.googleapis.com/seetree-demo-open/"+img_file_name

    #check if an image does not exist or the function is not supported
    if not functions.validate_img(url):
        abort(404)

    #check if the function is not supported
    if not functions.func_IsSupported(func_name):
        abort(404)


    img = Image.open(requests.get(url, stream=True).raw) #open image from url

    # convert the image to grayscale with PIL ImageOps.grayscale \
    gray_img = ImageOps.grayscale(img)

    # then pass grayscale image it to np.asarray(),
    # it returns 2D ndarray whose shape is (row (height), column (width)).
    arr_img = np.asarray(gray_img)

    # handle calculations --> call methods in functions class
    if not functions.check_p_func(func_name):
        method_to_call = getattr(functions, func_name)
        result = method_to_call(arr_img)
    else : # in case that the entered func is pXXX
        method_to_call  = getattr(functions, "percentile")
        result = method_to_call(arr_img,int(func_name[1:]))


    return render_template('stats.html',img_file_name=img_file_name,func_name=func_name,res=result,prange=prange)


# health route --> supports only GET requests
@app.route('/health', methods = ['GET'])
def health():
    return render_template('health.html')

# root route (the main page) --> supports only GET requests
@app.route('/', methods = ['GET'])
def root_route():
    return render_template('root.html')

# In case of choosing images from gallery page and choosing function
@app.route('/stats', methods = ['GET'])
def images():
    return render_template('images.html')

@app.route("/stats/<img_file_name>")
def choose_Func(img_file_name):
    return render_template("choose_Func.html",img_file_name=img_file_name,prange=prange)


@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181)