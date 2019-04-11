# -*- coding: utf-8 -*-
# @Time    : 2018/05/08
# @Author  : WangRong
import cv2

import dlib
import json
import os
import requests
import numpy as np

# from core.youtuUtil import getFaceDataFromYoutu
COLOUR_CORRECT_BLUR_FRAC = 0.6
PREDICTOR_PATH = "/home/hadoop/Desktop/dlib-19.17/shape_predictor_68_face_landmarks.dat"

FACE_POINTS = list(range(0, 68))
MOUTH_POINTS = list(range(48, 61))
RIGHT_BROW_POINTS = list(range(17, 21))
LEFT_BROW_POINTS = list(range(22, 26))
RIGHT_EYE_POINTS = list(range(36, 41))
LEFT_EYE_POINTS = list(range(42, 47))
NOSE_POINTS = list(range(27, 35))
JAW_POINTS = list(range(0, 16))

JAW_END = 17
FACE_START = 0
FACE_END = 67

OVERLAY_POINTS = [
    LEFT_BROW_POINTS + LEFT_EYE_POINTS,
    RIGHT_BROW_POINTS + RIGHT_EYE_POINTS,
    JAW_POINTS,
]


def get_landmarks(im):
    """ 用 dlib 获取面部特征点"""
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(PREDICTOR_PATH)
    rects = detector(im, 1)

    if len(rects) > 1:
        raise 'too many face detected in image {}'.format(im)
    if len(rects) == 0:
        raise 'No face detected in image {}'.format(im)
    points = []
    for p in predictor(im, rects[0]).parts():
        points.append([p.x, p.y])

    return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])


def face_points(image):
    im = cv2.imread(image, cv2.IMREAD_COLOR)  # IMREAD_COLOR 读入彩色图 IMREAD_GRAYSCALE以灰度图读入图片

    matrix_list = get_landmarks(im)

    point_list = []
    for p in matrix_list.tolist():
        point_list.append((int(p[0]), int(p[1])))

    return matrix_list, point_list, im


def matrix_rectangle(left, top, width, height):
    pointer = [
        (left, top),
        (left + width / 2, top),
        (left + width - 1, top),
        (left + width - 1, top + height / 2),
        (left, top + height / 2),
        (left, top + height - 1),
        (left + width / 2, top + height - 1),
        (left + width - 1, top + height - 1)
    ]

    return pointer
