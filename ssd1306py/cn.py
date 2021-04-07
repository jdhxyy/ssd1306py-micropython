"""
Copyright 2021-2021 The jdh99 Authors. All rights reserved.
ssd1306操作封装.支持多种英文字库
Authors: jdh99 <jdh821@163.com>
"""

_fonts = dict()


def set_font(font, font_size):
    """设置字库"""
    global _fonts
    _fonts[font_size] = font


def display(oled, string, x_axis, y_axis, font_size):
    if font_size not in _fonts:
        return
    if font_size == 16:
        _display_font16(oled, string, x_axis, y_axis)
    if font_size == 24:
        _display_font24(oled, string, x_axis, y_axis)
    if font_size == 32:
        _display_font32(oled, string, x_axis, y_axis)


def _display_font16(oled, string, x_axis, y_axis):
    offset = 0
    for k in string:
        code = 0x00
        data_code = k.encode("utf-8")
        code |= data_code[0] << 16
        code |= data_code[1] << 8
        code |= data_code[2]
        byte_data = _fonts[16][code]
        for y in range(0, 16):
            a = bin(byte_data[y]).replace('0b', '')
            while len(a) < 8:
                a = '0' + a

            b = bin(byte_data[y + 16]).replace('0b', '')
            while len(b) < 8:
                b = '0' + b
            for x in range(0, 8):
                oled.pixel(x_axis + offset + x, y + y_axis, int(a[x]))
                oled.pixel(x_axis + offset + x + 8, y + y_axis, int(b[x]))
        offset += 16


def _display_font24(oled, string, x_axis, y_axis):
    offset = 0
    for k in string:
        code = 0x00
        data_code = k.encode("utf-8")
        code |= data_code[0] << 16
        code |= data_code[1] << 8
        code |= data_code[2]
        byte_data = _fonts[24][code]
        for y in range(0, 24):
            a = bin(byte_data[y]).replace('0b', '')
            while len(a) < 8:
                a = '0' + a

            b = bin(byte_data[y + 24]).replace('0b', '')
            while len(b) < 8:
                b = '0' + b

            c = bin(byte_data[y + 48]).replace('0b', '')
            while len(c) < 8:
                c = '0' + c
            for x in range(0, 8):
                oled.pixel(x_axis + offset + x, y + y_axis, int(a[x]))
                oled.pixel(x_axis + offset + x + 8, y + y_axis, int(b[x]))
                oled.pixel(x_axis + offset + x + 16, y + y_axis, int(c[x]))
        offset += 24


def _display_font32(oled, string, x_axis, y_axis):
    offset = 0
    for k in string:
        code = 0x00
        data_code = k.encode("utf-8")
        code |= data_code[0] << 16
        code |= data_code[1] << 8
        code |= data_code[2]
        byte_data = _fonts[32][code]
        for y in range(0, 32):
            a = bin(byte_data[y]).replace('0b', '')
            while len(a) < 8:
                a = '0' + a

            b = bin(byte_data[y + 32]).replace('0b', '')
            while len(b) < 8:
                b = '0' + b

            c = bin(byte_data[y + 64]).replace('0b', '')
            while len(c) < 8:
                c = '0' + c

            d = bin(byte_data[y + 96]).replace('0b', '')
            while len(d) < 8:
                d = '0' + d
            for x in range(0, 8):
                oled.pixel(x_axis + offset + x, y + y_axis, int(a[x]))
                oled.pixel(x_axis + offset + x + 8, y + y_axis, int(b[x]))
                oled.pixel(x_axis + offset + x + 16, y + y_axis, int(c[x]))
                oled.pixel(x_axis + offset + x + 24, y + y_axis, int(d[x]))
        offset += 32
