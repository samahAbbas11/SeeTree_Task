# SeeTree Task

### Requirements: 
Write a python web server using Flask framework:
The web server will support the following routes, both will support only GET requests :
- /health : will respond with “OK” to any request
- /stats/IMAGE_FILE_NAME/FUNC_NAME : will calculate FUNC_NAME on the pixels of given IMAGE_FILE_NAME and    return the result. 
    Supported FUNC_NAMES should be:
    i. min
    ii. max
    iii. mean
    iv. median
    v. pXXX where XXX is a percentile between 0...100. For example p10 is the  10th percentile of the image, p99 is the 99th percentile
______________________________________________
### Run the app  :
 In order to run the app:
 1. install pyhton3.10
 2. install the requiremnets (run ```pip install -r requirements.txt```)
 3. run the app
```
git clone https://github.com/samahAbbas11/SeeTree_Task.git
python ./img_Stats.py
```

You can then access the app here: http://localhost:8181


