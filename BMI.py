while True:
    width = int(input('體重:'))
    height = int(input('身高:'))
    BMI = (width / (height/100)**2)
    print('體重 %s 公斤，身高 %s 公分的BMI為 %s'%(width,height,BMI))
    if BMI < 18.5:
        print('過輕')
        continue
    elif BMI > 24:
        print('過重')
        continue
    elif BMI > 27:
        print('肥胖')
        continue
    elif BMI > 35:
        print('極肥胖')
        continue
    else:
        print('正常')
        continue