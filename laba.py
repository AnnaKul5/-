import math
import time
import random
import matplotlib.pyplot as plt
import numpy as np

def create(x, P):
    P[x] = x

def search(x, P): 
    return P[x]       

def join(x, y, P):
    z = min(x,y)
    for i in range(0, len(P)):
        if(P[i]==x or P[i]==y):
            P[i]=z

#Наивный алгоритм 
def component_naive(comp, E, n, m):
    for i in range (0, n):
        comp[i] = i
    for i in range (0, n-1):
        for j in range (0, m):
            q = min(comp[E[j][0]], comp[E[j][1]])
            comp[E[j][0]] = q
            comp[E[j][1]] = q


#Алгоритм Рэма на массиве
def array_RAM(comp, E, n, m, P):
    for i in range(0, n):
        create(i, P)
    for i in range(0, m):
        n1 = search(E[i][0], P)
        n2 = search(E[i][1], P)
        
        if (n1 != n2):
            join(n1, n2, P)
            
    for i in range(0, n):
        comp[i] = search(i, P)
         
    
def task2(): 
    n = int(input("Введите количество вершин графа: "))
    m = int(input("Введите количество рёбер графа: "))
    comp1 = [0]*n 
    comp2 = [0]*n 
    P = [0]*n 

    #Генерация случайного графа
    E = [[]*2 for k in range(0, m)]
    for j in range(0, m): 
        a = random.randint(0, n-1)
        b = random.randint(0, n-1)
        #Обеспечивает, чтобы рёбра не повторялись
        while (([a,b] in E) == True) or (([b,a] in E) == True) or (a==b):
            a = random.randint(0, n-1)
            b = random.randint(0, n-1)
        E[j] = [a,b]
     
    time_naive = 0 #время работы наивного алгоритма        
    time_RAM = 0 #время работы алгоритма Рэма на массиве

    #Вызов наивного алгоритма
    start = time.time()
    component_naive(comp1, E, n, m)
    time_naive = time.time() - start
    print("Массив comp при использовании наивного алгоритма:")
    print(comp1)
    print("Время работы наивного алгоритма:")
    print(time_naive)

    #Вызов алгоритма Рэма
    start = time.time()
    array_RAM(comp2, E, n, m, P)
    time_RAM = time.time() - start
    print("Массив comp при использовании алгоритма Рэма:")
    print(comp2)
    print("Время работы алгоритма Рэма:")
    print(time_RAM)

    #Выводим граф в виде матрицы смежности
    if n <= 10:
        print("Граф задан матрицей смежности:")
        matrix = np.zeros((n,n)) 
        for i in range(0,m):
            matrix[E[i][0], E[i][1]] = 1
            matrix[E[i][1], E[i][0]] = 1
        for i in range(len(matrix)):         
            for j in range(len(matrix[i])):  
                print(matrix[i][j], end = ' ')
            print()  


def task3():
    time_naive = [0] #время работы наивного алгоритма     
    time_RAM = [0] #время работы алгоритма Рэма на массиве
    time_size = 0

    for i in range(1, 10**2 + 2, 10):
        n = i
        m = int(n**2/10)
        #m = n-1
        #m = int(math.log2(n))
        comp1 = [0]*n 
        comp2 = [0]*n 
        P = [0]*n 

        #Генерация случайного графа
        E = [[]*2 for k in range(0, m)]
        for j in range(0, m): 
            a = random.randint(0, n-1)
            b = random.randint(0, n-1)
            #Обеспечивает, чтобы рёбра не повторялись
            while (([a,b] in E) == True) or (([b,a] in E) == True) or (a==b):
                a = random.randint(0, n-1)
                b = random.randint(0, n-1)
            E[j] = [a,b]

        #Вызов наивного алгоритма
        start = time.time()
        component_naive(comp1, E, n, m)
        time_naive.append(time.time() - start)

        #Вызов алгоритма Рэма
        start = time.time()
        array_RAM(comp2, E, n, m, P)
        time_RAM.append(time.time() - start)
        time_size += 1
        print(time_size)


    xaxis = [0]
    for i in range(1, 10**2 + 2, 10):
        xaxis.append(i)
    plt.title("Сравнение бесхитростного алгоритма и алгоритма Рэма на массиве")
    plt.xlabel("количество вершин графа")
    plt.ylabel("время работы алгоритма")
    plt.plot(xaxis, time_naive, marker = 'o', linestyle = '-', color = 'yellow', label = "наивный алгоритм")    
    plt.plot(xaxis, time_RAM, marker = 'o', linestyle = '-', color = 'purple', label = "алгоритм Рэма")   
    plt.legend()  
    plt.show()

    #with open("D:\\Институт\\АиАС\\My_lab\\result.txt", "w") as text_file:
        #text_file.write("Время работы наивного алгоритма для m = int(n**2/10):\n")
        #for i in range(0, time_size): 
        #    text_file.write(str(time_naive[i]) + "\n")
        #text_file.write("Время работы алгоритма Рэма для m = int(n**2/10):\n")
        #for i in range(0, time_size):
        #    text_file.write(str(time_RAM[i]) + "\n")

        #text_file.write("Время работы наивного алгоритма для m = n-1:\n")
        #for i in range(0, time_size): 
        #    text_file.write(str(time_naive[i]) + "\n")
        #text_file.write("Время работы алгоритма Рэма для m = n-1:\n")
        #for i in range(0, time_size):
        #    text_file.write(str(time_RAM[i]) + "\n")

        #text_file.write("Время работы наивного алгоритма для m = int(math.log2(n)):\n")
        #for i in range(0, time_size): 
        #    text_file.write(str(time_naive[i]) + "\n")
        #text_file.write("Время работы алгоритма Рэма для m = int(math.log2(n)):\n")
        #for i in range(0, time_size):
        #    text_file.write(str(time_RAM[i]) + "\n")


def task4():
    M = [0]
    tmp = 0

    for i in range(1, 10**3 + 2, 10):
        n = i
        m = 0
        comp = [0]*n 
        comp_connected = [0]*n 
        P = [0]*n 
        E = []

        array_RAM(comp, E, n, m, P)
        while comp!=comp_connected:
            m += 1
            a = random.randint(0, n-1)
            b = random.randint(0, n-1)
            #Обеспечивает, чтобы рёбра не повторялись
            while (([a,b] in E) == True) or (([b,a] in E) == True) or (a==b):
                a = random.randint(0, n-1)
                b = random.randint(0, n-1)
            E.append([a,b])
            array_RAM(comp, E, n, m, P)
        M.append(m)
        print(i)
        print(m)
        tmp+=1

    xaxis = [0]
    for i in range(1, 10**3 + 2, 10):
        xaxis.append(i)
    plt.title("Зависимость потребовавшегося для построения связного графа числа ребер от числа вершин n")
    plt.xlabel("количество вершин графа")
    plt.ylabel("число рёбер графа")
    plt.plot(xaxis, M, marker = 'o')  
    plt.show()

    with open("D:\\Институт\\АиАС\\My_lab\\result.txt", "w") as text_file:
        for i in range(0, tmp):
            text_file.write("Количество вершин n: \n")
            text_file.write(str(1 + 10*i) + "\n")
            text_file.write("Потребовавшееся число рёбер m: \n")
            text_file.write(str(M[i]) + "\n")


def main():
    #task2()
    task3()
    #task4()


if __name__ == "__main__":
    main()
