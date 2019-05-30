from init import VeriCodeinit as VCinit


VCinit = VCinit(width_infeed=240,height_infeed=60,width_endwise=60,height_endwise=240)
VCinit.backdrop()#背景填充像素

if __name__ == '__main__':
    # 随机生成4位验证码
    for j in range(5):
        for i in range(4):
            VCinit.draw_infeed.text((58 * i + 20, 10), VCinit.randChar(), fill=VCinit.randColor_Font(),
                                    font=VCinit.font)  # 横向显示
            VCinit.draw_endwise.text((18, 58 * i + 10), VCinit.randChar(), fill=VCinit.randColor_Font(),
                                     font=VCinit.font)  # 纵向显示
        VCinit.img_infeed.show()#横向验证码显示
        VCinit.img_endwise.show()#纵向验证码显示
        VCinit.img_infeed.save('E:\PycharmProjects\Verification_Code\CODE\img_infeed{}.jpg'.format(j))#保存横向验证码
        VCinit.img_endwise.save('E:\PycharmProjects\Verification_Code\CODE\img_endwise{}.jpg'.format(j))#保存纵向验证码
        VCinit.backdrop()#背景填充像素
    VCinit.img_infeed.close()
    VCinit.img_endwise.close()

