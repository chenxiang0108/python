import numpy as np
import cv2


img = cv2.imread('pudding.png',cv2.cv2.IMREAD_GRAYSCALE)
print(type(img))
print(img.shape)

# 顯示圖片
cv2.imshow('My IMG',img)

# 持續等待按下任意鍵
cv2.waitKey(0)

# 關閉指定視窗
cv2.destroyWindow('My IMG')
# 關閉全部視窗
# cv2.destroyAllWindows()

cv2.imwrite('output.jpg',img)

