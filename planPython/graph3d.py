import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class IzometrG:
    def __init__(self, Nm, B0, B, B2, BB):
        self.Nm = Nm
        self.B0 = B0
        self.B = B
        self.B2 = B2
        self.BB = BB

    def Yras(self, I, X):
        result = self.B0[I]
        for II in range(self.Nm):
            result += self.B[I][II] * X[II] + self.B2[I][II] * (X[II] ** 2)
            if II > 0:
                for L in range(II):
                    result += self.BB[I][II][L] * X[II] * X[L]
        return result

    def createGraph(self):
        # Параметры сетки
        min_val = -1.5
        max_val = 1.5
        num_points = 10

        # Создаем сетку данных
        x = np.linspace(min_val, max_val, num_points)
        y = np.linspace(min_val, max_val, num_points)
        x, y = np.meshgrid(x, y)
        
        # Вычисляем z как функцию от x и y
        z = np.zeros_like(x)
        for i in range(num_points):
            for j in range(num_points):
                Xnm = [x[i, j], y[i, j]] + [0] * (self.Nm - 2)  # расширяем до размера Nm
                z[i, j] = self.Yras(0, Xnm)  # предположим, что индекс I = 0

        # Создаем фигуру и 3D оси
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Построение поверхности
        ax.plot_surface(x, y, z, cmap='viridis')

        # Добавление меток
        ax.set_title('3D График')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Показ графика
        plt.show()


def createGraph(graph):
    # Пример коэффициентов (замените на свои)
    Nm = graph.Nm
    B0 = graph.B0
    B = graph.B
    B2 = graph.B2
    BB = graph.BB

    # Создаем объект и строим график
    izometrG = IzometrG(Nm, B0, B, B2, BB)
    izometrG.createGraph()
