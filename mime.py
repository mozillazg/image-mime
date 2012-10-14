#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 判断图片 MIME 类型
usage:

>>> mime = get_image_mime(binary)

binary: utf8 编码的图片内容
mime: 图片 MIME 类型，类似"image/png"
"""

def get_image_mime(binary):
    """ 根据图片内容返回图片 MIME 类型
    >>> with open('test.png', 'rb') as f:
    ...     print get_image_mime(f.read())
    ...
    image/png
    >>>
    """
    size = len(binary)
    if size >= 6 and binary.startswith("GIF"):
        return "image/gif"
    elif size >= 8 and binary.startswith("\x89PNG\x0D\x0A\x1A\x0A"):
        return "image/png"
    elif size >= 2 and binary.startswith("\xff\xD8"):
        return "image/jpeg"
    elif (size >= 6 and (binary.startswith("II*\x00") or
                         binary.startswith("MM\x00*")
                         )):
        return "image/tiff"
    elif size >= 2 and binary.startswith("BM"):
        return "image/bmp"
    elif size >= 4 and binary.startswith("\x00\x00\x01\x00"):
        return "image/x-icon"
    else:
        return "application/octet-stream"

if __name__ == '__main__':
    with open('test.gif', 'rb') as f:
        print repr(get_image_mime(f.read()))
