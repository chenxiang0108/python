import time
secs = eval(input('請輸入要倒數的秒數:'))

for i in range(secs,0,-1): #從輸入的秒數開始 -1
    print('倒數',i,'秒...')
    time.sleep(1)          #停止 1 秒
print('開始')