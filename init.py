from PIL import Image, ImageDraw, ImageFont
import random


class VeriCodeinit():
    def __init__(self, width_infeed, height_infeed, width_endwise, height_endwise):
        # 新建空白文档
        self.width_infeed = width_infeed
        self.height_infeed = height_infeed
        self.width_endwise = width_endwise
        self.height_endwise = height_endwise
        self.img_infeed = Image.new("RGB", (width_infeed, height_infeed), (255, 255, 255))
        self.img_endwise = Image.new("RGB", (width_endwise, height_endwise), (255, 255, 255))
        # 创建Font对象
        self.font = ImageFont.truetype('arial.ttf', 36)
        # 创建Draw对象
        self.draw_infeed = ImageDraw.Draw(self.img_infeed)
        self.draw_endwise = ImageDraw.Draw(self.img_endwise)

    def randChar(self):
        """
        生成并返回随机字母
        :return:0~9，A~Z
        """
        rand_char = random.randint(48, 90)
        if 58 <= rand_char <= 64:
            rand_char = rand_char - 10
        return chr(rand_char)

    def randColor_backdrop(self):
        """
        生成并返回背景RGB颜色值
        :return: GBR
        """
        return (random.randint(50, 150),
                random.randint(50, 150),
                random.randint(50, 150))

    def randColor_Font(self):
        """
        生成并返回验证码RGB颜色值
        :return: GBR
        """
        return (random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255))

    def backdrop(self):
        """
        横向和纵向背景填充像素
        :return:
        """
        for x in range(self.width_infeed):# 横向背景填充像素
            for y in range(self.height_infeed):
                self.draw_infeed.point((x, y), fill=self.randColor_backdrop())
        for x in range(self.width_endwise):# 纵向背景填充像素
            for y in range(self.height_endwise):
                self.draw_endwise.point((x, y), fill=self.randColor_backdrop())







