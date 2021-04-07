"""
Copyright 2021-2021 The jdh99 Authors. All rights reserved.
32号字体ascii码字库
Authors: jdh99 <jdh821@163.com>
"""

import sys

_file = None


def _get_ch(ch):
    global _file
    if _file is None:
        _file = open(sys.path[1] + '/ssd1306py/ascii32.txt', 'r')

    _file.seek(ord(ch) * 329)
    get_line1 = _file.readline()
    get_line2 = _file.readline()

    data = []
    n = 0
    for v in get_line1.split(','):
        data.append(int(v))
        n += 1
        if n == 32:
            break
    n = 0
    for v in get_line2.split(','):
        data.append(int(v))
        n += 1
        if n == 32:
            break
    return data


def display(oled, string, x_axis, y_axis):
    offset = 0
    for k in string:
        byte_data = _get_ch(k)
        for y in range(0, 32):
            a = bin(byte_data[y]).replace('0b', '')
            while len(a) < 8:
                a = '0' + a

            b = bin(byte_data[y + 32]).replace('0b', '')
            while len(b) < 8:
                b = '0' + b
            for x in range(0, 8):
                oled.pixel(x_axis + offset + x, y + y_axis, int(a[x]))
                oled.pixel(x_axis + offset + x + 8, y + y_axis, int(b[x]))
        offset += 16
