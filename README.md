# Object_tracking
track objects of your choice from a live video feed

install dependencies:

!pip install numpy

!pip install opencv-python

!pip install psutils

!pip install os-sys

!python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf

# RUN FILE
clone this directory, then from this directory:
1. run dlib_multiple_object_tracking.py
2. type the number of objects you want to detect and PRESS ENTER!
3. draw a box around the object you want to detect and press enter or spacebar key.
4. enjoy

P.S: by default a feed from "test" folder will run. to change the feed as per your preference just change:

cap = cv2.VideoCapture('test/video_sample4.mp4')----------in run dlib_multiple_object_tracking.py to :


cap = cv2.VideoCapture(<video file path>)
 
or

cap = cv2.VideoCapture(0)-------- to feed video from webcam
