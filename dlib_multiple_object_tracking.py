#necessary imports
import numpy as np
import cv2
import dlib
import time
import psutil
import os

def fps(inference_time):
    fps = 1/fps
    return fps

def track_single_object():
    cap = cv2.VideoCapture('test/video_sample4.mp4')
    ret,frame = cap.read()
    #initiate Tracker
    tracker = dlib.correlation_tracker()
    #select the object to be tracked
    cv2.imshow('frame',frame)
    bb = cv2.selectROI('frame',frame)
    x,y,w,h = bb
    xmin = x
    ymin = y
    xmax = x+w
    ymax = y+h
    #create dlib ractangle from the region selected
    dlib_rect = dlib.rectangle(xmin,ymin,xmax,ymax)
    tracker.start_track(frame,dlib_rect)

    while True:
        ret,frame = cap.read()
        inference_start = time.time()
        tracker.update(frame)
        track_rect = tracker.get_position()
        xmin  = int(track_rect.left())
        ymin  = int(track_rect.top())
        xmax = int(track_rect.right())
        ymax = int(track_rect.bottom())
        cv2.rectangle(frame,(xmin,ymin),(xmax,ymax),(0,0,255),2)
        inference_end = time.time()
        inference_time = inference_end - inference_start
        frameps =round(1/inference_time,2)
        cv2.putText(frame, str(frameps), (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
            #observing memory usage
    process = psutil.Process(os.getpid())
    print('memory usage is',process.memory_info().rss)
    cv2.destroyAllWindows()
# track_single_object()

def track_multiple_objects(num_objects):
    def update_positions(tracker):
        tracker.update(frame)
        track_rect = tracker.get_position()
        return track_rect

    cap = cv2.VideoCapture('test/video_sample4.mp4')
    ret,frame = cap.read()
    k = num_objects
    tracker = []
    dlib_rect = []

    for i in range(k):
        trackeri = dlib.correlation_tracker()
        tracker.append(trackeri)
        cv2.imshow('frame',frame)
        bbi = cv2.selectROI('frame',frame)
        x,y,w,h = bbi
        xmin = x
        ymin = y
        xmax = x+w
        ymax = y+h
        dlib_recti = dlib.rectangle(xmin,ymin,xmax,ymax)
        dlib_rect.append(dlib_recti)
        tracker[i].start_track(frame,dlib_rect[i])
    while True:
        ret,frame = cap.read()
        inference_start = time.time()
        # track_rect = map(update_positions,tracker)
        # track_rect = tuple(track_rect)
        for i in range(k):
            tracker[i].update(frame)
            track_rect = tracker[i].get_position()
            xmin  = int(track_rect.left())
            ymin  = int(track_rect.top())
            xmax = int(track_rect.right())
            ymax = int(track_rect.bottom())
            cv2.rectangle(frame,(xmin,ymin),(xmax,ymax),(0,0,255),2)
        inference_end = time.time()
        inference_time = inference_end - inference_start
        frameps =round(1/inference_time,2)
        cv2.putText(frame, str(frameps), (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
            #observing memory usage
    process = psutil.Process(os.getpid())
    print('memory usage is',process.memory_info().rss)
    cv2.destroyAllWindows()
