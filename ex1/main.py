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

if y1o < y < y2o:
    print("Вход")
elif y2o < y < y1o:
    print("Выход")
else:
    print("Не пересечена")

# Создать полностью черное изображение
img = np.zeros((512, 512, 3), np.uint8)
cv.line(img,(x1,y1),(x2,y2),(0,0,255),2,cv.LINE_8)
# Дисплей
cv.imshow('line', img)
cv.waitKey(0)
# Закрыть окно
cv.destroyAllWindows()
