while True:
    eeee = input('ветите строку')
    if eeee.lower() == "exit":
        break
    gls = 0
    sgl = 0
    vse_gls = "аеиёяэоуюы"
    vse_sgl = "бвгджзйклмнпрстфхцчщшьъ"
    lat_gls = "aeiouy"
    lat_sgl = "bcdfghjklmnpqrstvwxz"
    fff = vse_sgl + lat_sgl
    ggg = vse_gls + lat_gls
    sohik = 0
    sohik_2 = 0
    for ee in eeee:
        if ee.lower() in fff:
            sohik += 1
        elif ee.lower() in ggg:
            sohik_2 += 1
    xxx = fff + ggg
    print('кол-во букв вс троке', xxx)
    print('гласных', sohik)
    print('согласных', sohik_2)
    #
    # if xxx > 0:
    #     ccc = (sohik / xxx) * 100
    #     cc = (ggg / xxx) * 100
    #     print(f"согласные буквы:", ccc)
    #     print("согласные буквы:", cc)
    # else:
    #     print('еше рас')











