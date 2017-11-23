#!/bin/bash

~/Development/opencv/opencv-3.2.0/build/bin/opencv_traincascade -data ~/Development/PycharmProjects/analyze-x/src/haar_learning/haarcascade -vec samples.vec -bg ~/Development/PycharmProjects/analyze-x/data/my_collection/Bad.dat -numStages 16 -minhitrate 0.999 -maxFalseAlarmRate 0.4 -numPos 200 -numNeg 975 -w 20 -h 20 -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024
