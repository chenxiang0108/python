answer = input("請輸入快樂的英文:")

while answer.upper() != 'HAPPY':
    if answer.upper() == 'QUIT':
        print('我不玩了!')
        break              #離開迴圈
    answer = input('答錯了，請重新輸入快樂的英文:')
else:print('答對了')

i = 0
while i < 10:
    i = i + 1
    if i % 3 != 0:
        continue           #返回迴圈開頭
    print(i)