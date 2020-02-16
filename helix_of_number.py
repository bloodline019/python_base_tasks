n = int(input()) # Ввод числа
out = [[0] * n for i in range(n)] # Задание матрицы из нулей n*n
dx = 1; dy = 0; x = 0; y = 0; # Начальные значения для случая когда заполнение начинается из верхнего левого угла
for i in range(1,n**2+1):
    out[y][x] = i
    if (x+dx) == n or (y+dy) == n or out[y+dy][x+dx] != 0: # Условие при котором заполнение "поворачивает"
        dx,dy = -dy,dx # Алгоритм поворота
    x += dx; # Приращения для следующей итерации
    y += dy
for i in out:
    print()
    for j in i:
        print(j, end="\t")

