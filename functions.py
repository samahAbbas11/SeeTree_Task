import requests
import numpy as np


## Supported functions are :
# min
def min(img):
    return np.min(img)
# max
def max(img):
    return np.max(img)
# mean
def mean(img):
    return np.mean(img)
# median
def median(img):
    return np.median(img)
# pXXX
def percentile(img,p):
    return np.percentile(img, p) # Compute the p-th percentile of the data along the specified axis



######### ERROR handing helper functions #################

# checks if func is supported
def func_IsSupported(func):
    funcs =['min','max','mean','median']

    if func in funcs or check_p_func(func):
        return True

# checks that pXXX function is valid -> (p0 - p100)
def check_p_func(pFunc):
    if pFunc.startswith('p') and pFunc[1:].isdigit:
        print(pFunc)
        if int(pFunc[1:]) in range(0,101):
            return True
    return False

# validate image URL
def validate_img(url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(url)
   if r.headers["content-type"] in image_formats:
      return True
   return False


