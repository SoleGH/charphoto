# coding: utf-8
import os
import time

from PIL import Image


ORIGIN_IMG_DIR = './data/origin_img'
FORMAT_IMG_DIR = './data/format_img'


def cut_img(image):
    width, height = image.size
    bew = abs(width - height) / 2
    if width > height:
        box = (bew, 0, width - bew, height)
    else:
        box = (0, bew, width, height - bew)
    return image.crop(box)


def save_images(image_list):
    index = 1
    for image in image_list:
        image.save(str(index) + '.png', 'PNG')
        index += 1


def get_origin_img_list():
    return os.listdir(ORIGIN_IMG_DIR)


def format_img(file_name):
    image = Image.open('{}/{}'.format(ORIGIN_IMG_DIR, file_name))
    image = cut_img(image)
    image.save('{}/{}'.format(FORMAT_IMG_DIR, file_name))


if __name__ == '__main__':
    origin_img_list = get_origin_img_list()
    for file_name in origin_img_list:
        format_img(file_name)




