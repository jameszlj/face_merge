# coding:utf-8 
# author:james.zhan
# datetime:4/10/19
import time

import core


def merge_one(src_img, dst_img, alpha):
    out_img = 'images/out.jpg'
    face_area = [50, 50, 500, 485]

    # 头像融合
    core.face_merge(src_img=src_img,
                    dst_img=dst_img,
                    out_img=out_img,
                    face_area=face_area,
                    alpha=alpha,
                    k_size=(15, 10),
                    mat_multiple=0.95)
    return out_img


# 要融合的图片下载一次就够了——用户上传的图片
dst_img = "/home/hadoop/Desktop/face_merge_master/images/smallgirl.jpg"
# 取得model的图片,下载一次就够了
src_img = "/home/hadoop/Desktop/face_merge_master/images/model.jpg"
output_image = merge_one(src_img,dst_img, 1)

