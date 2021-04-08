"""
Copyright 2021-2021 The jdh99 Authors. All rights reserved.
ssd1306操作封装.支持多种英文字库
Authors: jdh99 <jdh821@163.com>
"""

import machine

import ssd1306py.ssd1306 as ssd1306
import ssd1306py.ascii16 as ascii16
import ssd1306py.ascii32 as ascii32
import ssd1306py.ascii24 as ascii24
import ssd1306py.cn as cn

_oled = None
_i2c = None
_width = 0
_height = 0


def init_i2c(scl, sda, width, height, i2c=-1):
    """
    初始化i2c接口
    :param scl: i2c的时钟脚
    :param sda: i2c的数据脚
    :param width: oled屏幕的宽度像素
    :param height: oled屏幕的高度像素
    :param i2c: i2c口
    """
    global _oled, _width, _height
    _i2c = machine.I2C(i2c, scl=machine.Pin(scl), sda=machine.Pin(sda))
    _width = width
    _height = height
    _oled = ssd1306.SSD1306_I2C(_width, _height, _i2c)


def clear():
    """清除屏幕"""
    global _oled
    _oled.fill(0)


def show():
    """屏幕刷新显示"""
    global _oled
    _oled.show()


def pixel(x, y):
    """画点"""
    global _oled
    _oled.pixel(x, y, 1)


def text(string, x_axis, y_axis, font_size):
    """显示字符串.注意字符串必须是英文或者数字"""
    global _oled
    if font_size != 8 and font_size != 16 and font_size != 24 and font_size != 32:
        return

    if font_size == 8:
        _oled.text(string, x_axis, y_axis)
        return

    if font_size == 16:
        ascii16.display(_oled, string, x_axis, y_axis)
    if font_size == 24:
        ascii24.display(_oled, string, x_axis, y_axis)
    if font_size == 32:
        ascii32.display(_oled, string, x_axis, y_axis)


def set_font(font, font_size):
    """
    设置中文字库.允许设置多个不同大小的字库
    字库必须是字典,格式示例:
    font = {
    0xe4bda0:
        [0x08, 0x08, 0x08, 0x11, 0x11, 0x32, 0x34, 0x50, 0x91, 0x11, 0x12, 0x12, 0x14, 0x10, 0x10, 0x10, 0x80, 0x80,
         0x80, 0xFE, 0x02, 0x04, 0x20, 0x20, 0x28, 0x24, 0x24, 0x22, 0x22, 0x20, 0xA0, 0x40],  # 你
    0xe5a5bd:
        [0x10, 0x10, 0x10, 0x10, 0xFC, 0x24, 0x24, 0x25, 0x24, 0x48, 0x28, 0x10, 0x28, 0x44, 0x84, 0x00, 0x00, 0xFC,
         0x04, 0x08, 0x10, 0x20, 0x20, 0xFE, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0xA0, 0x40]  # 好
    }
    """
    cn.set_font(font, font_size)


def text_cn(string, x_axis, y_axis, font_size):
    """显示中文字符.注意字符必须是utf-8编码"""
    global _oled
    cn.display(_oled, string, x_axis, y_axis, font_size)
