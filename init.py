from PIL import Image, ImageDraw, ImageFont
import random


class VeriCodeinit():
    def __init__(self):
        # 新建空白文档
        self.img_infeed = Image.new("RGB", self.Draw_Width_Height(), (255, 255, 255))
        self.img_endwise = Image.new("RGB", self.Draw_Width_Height(60, 240), (255, 255, 255))
        # 创建Font对象
        self.font = ImageFont.truetype('arial.ttf', 36)
        # 创建Draw对象
        self.draw_infeed = ImageDraw.Draw(self.img_infeed)
        self.draw_endwise = ImageDraw.Draw(self.img_endwise)

    def Draw_Width_Height(self, Width=240, Height=60):
        """
        生成画板
        :param width:画板宽度
        :param height: 画板高度
        :return:W,H
        """
        return Width, Height

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

    # 横向背景填充像素
    def infeed_backdrop(self):
        width_infeed, height_infeed = self.Draw_Width_Height()
        for x in range(width_infeed):
            for y in range(height_infeed):
                self.draw_infeed.point((x, y), fill=self.randColor_backdrop())

    # 纵向背景填充像素
    def endwise_backdrop(self):
        width_endwise, height_endwise = self.Draw_Width_Height(60, 240)
        for x in range(width_endwise):
            for y in range(height_endwise):
                self.draw_endwise.point((x, y), fill=self.randColor_backdrop())







