import numpy as np
import cv2 as cv

print("Координаты точки A(x1;y1):")
x1 = int(input("\tx1 = "))
y1 = int(input("\ty1 = "))

print("Координаты точки B(x2;y2):")
x2 = int(input("\tx2 = "))
y2 = int(input("\ty2 = "))

print("Координаты точки A(x1o;y1o):")
x1o = int(input("\tx1o = "))
y1o = int(input("\ty1o = "))

print("Координаты точки B(x2o;y2o):")
x2o = int(input("\tx2o = "))
y2o = int(input("\ty2o = "))

print("Уравнение прямой, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print(" y = %.2f*x + %.2f" % (k, b))
y = k * x2o + b
x = (y - b) / k
if y1o < y < y2o:
    print("Вход")

elif y2o < y < y1o:
    print("Выход")
else:
    print("Не пересечена")

# Создать полностью черное изображение
img = np.zeros((512, 512, 3), np.uint8)
cv.line(img,(int(-b/k),0),(int((512 -b) / k),512),(0,0,255),2,cv.LINE_8)
cv.line(img,(x1o,y1o),(x2o,y2o),(255,0,0),2, cv.LINE_8)
if y1o < y < y2o:
    cv.putText(img, 'Enter', (10, 100), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (255, 255, 255), 2, cv.LINE_AA)
elif y2o < y < y1o:
    cv.putText(img, 'Exit', (10, 100), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (255, 255, 255), 2, cv.LINE_AA)
else:
    cv.putText(img, 'NotCrossed', (10, 100), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (255, 255, 255), 2, cv.LINE_AA)
# Дисплей
cv.imshow('line', img)
cv.imshow('Text', img)
cv.waitKey(0)
# Закрыть окно
cv.destroyAllWindows()
