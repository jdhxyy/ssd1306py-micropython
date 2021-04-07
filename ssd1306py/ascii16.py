"""
Copyright 2021-2021 The jdh99 Authors. All rights reserved.
16号字体ascii码字库
Authors: jdh99 <jdh821@163.com>
"""

import sys

_file = None


def _get_ch(ch):
    global _file
    if _file is None:
        _file = open(sys.path[1] + '/ssd1306py/ascii16.txt', 'r')

    _file.seek(ord(ch) * 86)
    get_line = _file.readline()

    data = []
    n = 0
    for v in get_line.split(','):
        data.append(int(v))
        n += 1
        if n == 16:
            break
    return data


def display(oled, string, x_axis, y_axis):
    offset = 0
    bytes_size = 16
    for k in string:
        byte_data = _get_ch(k)
        for y in range(0, bytes_size):
            a = bin(byte_data[y]).replace('0b', '')
            while len(a) < 8:
                a = '0' + a
            for x in range(0, 8):
                oled.pixel(x_axis + offset + x, y + y_axis, int(a[x]))
        offset += 8
