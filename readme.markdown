
# 根据图片内容判断 MIME 类型

## 支持如下 MIME 类型：

* image/gif
* image/jpeg
* image/tiff
* image/png
* image/bmp
* image/x-icon
* application/octet-stream

## 示例

    >>> with open('test', 'rb') as f:
    ...     print get_image_mime(f.read())
    ...
    image/png

