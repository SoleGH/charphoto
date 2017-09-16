#coding:utf-8
from PIL import Image

"""
char_string = 'abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+`[],.<>?/'
new_char_string = ""
for i in range(len(char_string)):
    new_char_string += char_string[i]

char_string = new_char_string
"""
char_string = ".*^->| "

def rgb2char(r, g, b):
    length = len(char_string)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 每个字符对应的gray值区间宽度
    unit = (256.0 + 1) / length

    # gray值对应到char_string中的位置（索引值）
    idx = int(gray / unit)
    return char_string[idx]



#预处理（将图片尺寸压缩，并转为灰度图） 
def preprocess(img_path,delta=100):
    img = Image.open(img_path) 
    # 获取图片尺寸
    width, height = img.size
    # 获取图片最大边的长度 
    if width > height:
        max = width
    else:
        max = height

    # 伸缩倍数scale
    scale = max / delta
    #width, height = int(width / scale), int(height / scale)
    width, height = int(width / 12), int(height / 24)
    img = img.resize((width, height)) 
    return img


def img2char(img_obj, savepath):
    txt = ''
    width, height = img_obj.size
    # 获取像素点的rgb元组值，如(254, 0, 0)，并将其转化为字符
    for i in range(height):
        line = ''
        for j in range(width):
            line += rgb2char(*img_obj.getpixel((j, i)))
        txt = txt + line + '\n'

    # 保存字符画
    with open(savepath, 'w+') as f:
        f.write(txt)



if __name__ == "__main__":
    img_obj = preprocess("3.jpg")
    img2char(img_obj, "char.txt") 