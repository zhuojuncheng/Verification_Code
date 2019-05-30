from init import VeriCodeinit as VCinit


VCinit = VCinit(240,60,60,240)
#背景填充像素
VCinit.backdrop()
if __name__ == '__main__':
    # 随机生成4位验证码并显示及保存
    for j in range(5):
        for i in range(4):
            VCinit.draw_infeed.text((58 * i + 20, 10), VCinit.randChar(), fill=VCinit.randColor_Font(),
                                    font=VCinit.font)  # 横向显示
            VCinit.draw_endwise.text((18, 58 * i + 10), VCinit.randChar(), fill=VCinit.randColor_Font(),
                                     font=VCinit.font)  # 纵向显示
        VCinit.img_infeed.show()
        VCinit.img_endwise.show()
        VCinit.img_infeed.save('E:\PycharmProjects\Verification_Code\CODE\img_infeed{}.jpg'.format(j))
        VCinit.img_endwise.save('E:\PycharmProjects\Verification_Code\CODE\img_endwise{}.jpg'.format(j))
        VCinit.backdrop()
    VCinit.img_infeed.close()
    VCinit.img_endwise.close()

