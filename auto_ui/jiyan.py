#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2018/6/25 9:40
# Author : lixingyun
# Description :
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from PIL import Image
from io import BytesIO
# https://zhuanlan.zhihu.com/p/38383797

class GrackGeetest():
    def __init__(self):
        self.url = 'https://auth.geetest.com/login/'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = 'test'
        self.password = '2111'

    def get_geetest_button(self):
        # 获取点击可以使现验证图出现的按钮节点元素并返回
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_image_position(self):
        # 获取验证图在网页中的位置并以元组的方式返回
        geetestImage = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_img')))
        time.sleep(2)
        location = geetestImage.location
        size = geetestImage.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
        return (top, bottom, left, right)

    # 截取当前页面
    def get_chrome_page(self):
        page_shot = self.browser.get_screenshot_as_png()
        page_shot = Image.open(BytesIO(page_shot))
        return page_shot

    # 从网页中截取验证码图片并返回
    def get_geetest_image(self, name='geetest.png'):
        top, bottom, left, right = self.get_image_position()
        # 截取当前页面的图片
        page_shot = self.get_chrome_page()
        # 截取其中出现的验证图的位置
        captchaImage = page_shot.crop((top, bottom, left, right))
        captchaImage.save(name)  # 保存当前文件夹中
        return captchaImage

    # 实现步骤2,获取缺口位置
    def get_slider(self):
        # 获取可滑动对象
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    # 通过对比2张图的像素点的差距得出缺口位置
    def get_gap(self, image1, image2):
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    # 因为小滑块和缺口是同一条水平线,所以就只取x轴方向上的值
                    left = i
                    return left
        return left

    def is_pixel_equal(self, image1, image2, x, y):
        # 判断2个像素是否相同
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        # 阀值当超出这个阀值的时候证明这2个像素点不匹配,为缺口左上角的像素点
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False
# 步骤三相关方法:最关键的一步也是突破极验验证机器学习算法的一步
# 采用