import numpy as np


class Plan:
    def __init__(self):
        # Constants
        self.MaxNm = 4
        self.MaxNb = 31
        self.MaxNY = 5
        self.MaxK2 = 15
        self.MaxNO = 10
        self.MaxNmNy = 5
        self.MaxN_MIsFil = 297
        self.Xmi = -1.0
        self.Xma = 1.0
        self.maxNom = 30
        self.maxKolIzo = 100
        self.maxToch = 100
        self.Nm = 0
        self.Ny = 0

        # Typedefs (in Python, these will be handled as numpy arrays or lists)
        self.arrayX = np.zeros(self.MaxNm)
        self.array3 = np.zeros(3)
        self.array2 = np.zeros(2)

        class typToch:
            def __init__(self):
                self.nToch = 0
                self.xToch = 0
                self.xx1Toch = 0.0
                self.yy1Toch = 0.0
                self.YToch = 0
                self.bitmap = None  # Placeholder for the bitmap

            def __del__(self):
                pass  # Python handles memory management automatically

        # Global variables
        self.LWidth = 0
        self.LStyle = None
        self.Gran = 0.0
        self.KoorX = 0
        self.KoorY = 0
        self.OsX3KoorX = 0
        self.OsX3KoorY = 0
        self.OsY3KoorX = 0
        self.OsY3KoorY = 0
        self.OsZ3KoorX = 0
        self.OsZ3KoorY = 0
        self.FlRectangle2 = False
        self.FlRectangle1 = False
        self.X1Rectangle2 = 0
        self.Y1Rectangle2 = 0
        self.X2Rectangle2 = 0
        self.Y2Rectangle2 = 0
        self.X1Rectangle1 = 0
        self.Y1Rectangle1 = 0
        self.X2Rectangle1 = 0
        self.Y2Rectangle1 = 0
        self.PreBits = None
        self.PpiX = 0
        self.PpiY = 0
        self.PixelsPerInchY = 0
        self.Gamma = 0
        self.RGamma = 0.0
        self.GdeDown = 0
        self.FlMouseDown = False
        self.XMouseDown = 0
        self.YMouseDown = 0
        self.FlSpeedButton1 = False
        self.FlOFont = False
        self.GrFont = None
        self.fconf = None
        self.Xnm = np.zeros(self.MaxNm)
        self.Nxx = 0
        self.Nxy = 0
        self.NM = 0
        self.NB = 0
        self.Nb = 0
        self.N0 = 0
        self.AAAr = np.zeros(7)
        self.NY = 0
        self.X = np.zeros((self.MaxNm, self.MaxNb))
        self.XMin = np.zeros(self.MaxNm)
        self.XMax = np.zeros(self.MaxNm)
        self.XMin_Gr = np.zeros(self.MaxNm)
        self.XMax_Gr = np.zeros(self.MaxNm)
        self.Y = np.zeros((self.MaxNY, self.MaxNb, self.MaxNO))
        self.C = np.zeros(self.MaxNY, dtype=int)
        self.Ysr = np.zeros((self.MaxNY, self.MaxNb))
        self.B0 = np.zeros(self.MaxNY)
        self.B = np.zeros((self.MaxNY, self.MaxNm))
        self.BB = np.zeros((self.MaxNY, self.MaxNm, self.MaxNm))
        self.B2 = np.zeros((self.MaxNY, self.MaxNm))
        self.S2Y = np.zeros((self.MaxNY, self.MaxNb))
        self.SS2Y = np.zeros(self.MaxNY)
        self.S2 = np.zeros(self.MaxNY)
        self.Gmax = np.zeros(self.MaxNY)
        self.GTabl = np.zeros(self.MaxNY)
        self.Fras = np.zeros(self.MaxNY)
        self.Ftab = np.zeros(self.MaxNY)
        self.NameXY = [["" for _ in range(self.MaxNmNy)] for _ in range(2)]
        self.Ikohren = np.zeros(self.MaxNY, dtype=bool)
        self.Ifile = False
        self.IRaschet = False
        self.Imemo1 = 1
        self.MIsFil = ["" for _ in range(self.MaxN_MIsFil)]
        self.N_MIsFil = 0
        self.FormatX3 = ""
        self.FormatY3 = ""
        self.FormatX = ""
        self.FormatZ0 = ""
        self.OkForm3 = False
        self.KolIzo = 0
        self.NomIzo = 0
        self.Xmin_Gr = [0.0] * self.MaxNm
        self.Xmax_Gr = [0.0] * self.MaxNm
        self.FlY00 = np.zeros((self.MaxNY, self.maxNom), dtype=bool)
        self.ZnYmax0 = np.zeros((self.MaxNY, self.maxNom))
        self.ZnYmin0 = np.zeros((self.MaxNY, self.maxNom))

        self.Xmin = [0.0] * self.MaxNm
        self.Xmax = [0.0] * self.MaxNm

    def vvod(self, file_path):
        mst = [0] * self.MaxNm
        Zvpl = [0.0] * self.MaxNm
        nstr = 0

        try:
            if self.Imemo1 == 1:
                Zvpl = [1, 1, 1.215, 1.414]
                self.Gran = 1.5
            elif self.Imemo1 == 4:
                Zvpl = [1, 1.414, 1.682, 2.0]
                self.Gran = 2.0

            mst[0] = 2
            for i in range(1, self.MaxNm):
                mst[i] = mst[i - 1] * 2

            with open(file_path, 'r') as ATF:
                self.Ifile = True
                nstr += 1
                self.Nm = int(ATF.readline().strip())

                if self.Nm <= 1 or self.Nm > self.MaxNm:
                    self.Ifile = False
                else:
                    if self.Imemo1 == 1:
                        self.Nb = mst[self.Nm - 1] + 2 * self.Nm + 1
                    elif self.Imemo1 == 4:
                        if self.Nm == 2:
                            self.Nb = 13
                            self.N0 = 5
                            self.AAAr = [0.2000, 0.1000, 0.1250, 0.2500, 0.1251, 0.0187, 0.1438]
                        elif self.Nm == 3:
                            self.Nb = 20
                            self.N0 = 6
                            self.AAAr = [0.1663, 0.0568, 0.0732, 0.1250, 0.0675, 0.0069, 0.0695]
                        elif self.Nm == 4:
                            self.Nb = 31
                            self.N0 = 7
                            self.AAAr = [0.1428, 0.0357, 0.0417, 0.0625, 0.0312, 0.0037, 0.0350]

                    for i in range(self.Nm):
                        self.NameXY[0][i] = ATF.readline().strip()
                    for i in range(self.Nm):
                        self.Xmin[i], self.Xmax[i] = map(float, ATF.readline().strip().split())
                        self.Xmin_Gr[i] = self.Xmin[i] + (self.Xmax[i] - self.Xmin[i]) / 2 - (self.Xmax[i] - self.Xmin[i]) / 2 * self.Gran
                        self.Xmax_Gr[i] = self.Xmin[i] + (self.Xmax[i] - self.Xmin[i]) / 2 + (self.Xmax[i] - self.Xmin[i]) / 2 * self.Gran
                        nstr += 1

                    self.Ny = int(ATF.readline().strip())
                    nstr += 1

                    if self.Ny <= 0 or self.Ny > self.MaxNY:
                        self.Ifile = False
                    else:
                        for i in range(self.Ny):
                            self.NameXY[1][i] = ATF.readline().strip()
                            nstr += 1

                        i = 0
                        for value in ATF.readline().strip().split():
                            self.C[i] = int(value)
                            if self.C[i] <= 0 or self.C[i] > self.MaxNO:
                                self.Ifile = False
                                break
                            i += 1

                        nstr += 1

                        for i in range(self.Nb):
                            lineList = ATF.readline().strip().split()
                            for m in range(self.Nm):
                                self.X[m][i] = float(lineList[m])
                                if i > (mst[self.Nm - 1] - 1):
                                    self.X[m][i] *= Zvpl[self.Nm-1]

                            for j in range(self.Ny):
                                for k in range(self.C[j]):
                                    self.Y[j][i][k] = float(lineList[4+k+3*j])#???

                            nstr += 1
                
                ATF.seek(0)
                return ATF.read()
            # for i in range(self.MaxNm):
            #     Izor.XnmFix[i] = 0.0
            #     Izor.XnmFakt[i] = self.Xmin[i] + (self.Xmax[i] - self.Xmin[i]) / 2
            
            if not self.Ifile:
                print(f"Неверный формат файла, строка {nstr}")

        except ValueError as e:
            print(f"Ошибка ввода-вывода в строке {nstr}: {e}")
            self.Ifile = False

# Example usage:
    def Yras(self, I, X):
        result = self.B0[I]
        for II in range(self.Nm):
            result += self.B[I][II] * X[II] + self.B2[I][II] * (X[II] ** 2)
            if II > 0:
                for L in range(II):
                    result += self.BB[I][II][L] * X[II] * X[L]
        return result

    def T(self, V, A):
        NV = 26
        NA = 2

        ts = [
            [12.71, 6.313], [4.302, 2.920], [3.182, 2.353], [2.776, 2.132], [2.571, 2.015], 
            [2.446, 1.943], [2.365, 1.895], [2.306, 1.859], [2.262, 1.833], [2.228, 1.812], 
            [2.201, 1.795], [2.179, 1.782], [2.160, 1.771], [2.145, 1.761], [2.131, 1.753], 
            [2.119, 1.745], [2.110, 1.740], [2.101, 1.734], [2.093, 1.729], [2.086, 1.725], 
            [2.059, 1.708], [2.042, 1.697], [2.021, 1.684], [2.009, 1.676], [1.984, 1.660], 
            [1.964, 1.647]
        ]
        vd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30, 40, 50, 100, 500]
        ad = [0.05, 0.1]

        ii = 0
        while V > vd[ii] and ii < NV - 1:
            ii += 1

        jj = 0
        while A > ad[jj] and jj < NA - 1:
            jj += 1

        return ts[ii][jj]

    def Fi(self, V1, V2, A):
        NV1 = 21
        NV2 = 26

        F = [
            [161, 18.51, 10.13, 7.71, 6.61, 5.99, 5.59, 5.32, 5.12, 4.96, 4.84, 4.75, 4.67, 4.60, 4.54, 4.49, 4.45, 4.41, 4.38, 4.35, 4.26, 4.20, 4.15, 4.03, 3.94, 3.84],
            [200, 19.00, 9.55, 6.94, 5.79, 5.14, 4.74, 4.46, 4.26, 4.10, 3.98, 3.88, 3.80, 3.74, 3.68, 3.63, 3.59, 3.55, 3.52, 3.49, 3.40, 3.34, 3.30, 3.18, 3.09, 2.99],
            [216, 19.16, 9.28, 6.59, 5.41, 4.76, 4.35, 4.07, 3.86, 3.71, 3.59, 3.49, 3.41, 3.34, 3.29, 3.24, 3.20, 3.16, 3.13, 3.10, 3.01, 2.95, 2.90, 2.79, 2.70, 2.60],
            [225, 19.25, 9.12, 6.39, 5.19, 4.53, 4.12, 3.84, 3.63, 3.48, 3.36, 3.26, 3.18, 3.11, 3.06, 3.01, 2.96, 2.93, 2.90, 2.87, 2.78, 2.71, 2.67, 2.56, 2.46, 2.37],
            [230, 19.30, 9.01, 6.26, 5.05, 4.39, 3.97, 3.69, 3.48, 3.33, 3.20, 3.11, 3.02, 2.96, 2.90, 2.85, 2.81, 2.77, 2.74, 2.71, 2.62, 2.56, 2.51, 2.40, 2.30, 2.21],
            [234, 19.33, 8.94, 6.16, 4.95, 4.28, 3.87, 3.58, 3.37, 3.22, 3.09, 3.00, 2.92, 2.85, 2.79, 2.74, 2.70, 2.66, 2.63, 2.60, 2.51, 2.44, 2.40, 2.29, 2.19, 2.09],
            [237, 19.36, 8.88, 6.09, 4.88, 4.21, 3.79, 3.50, 3.29, 3.14, 3.01, 2.92, 2.84, 2.77, 2.70, 2.66, 2.62, 2.58, 2.55, 2.52, 2.43, 2.36, 2.32, 2.20, 2.10, 2.01],
            [239, 19.37, 8.84, 6.04, 4.82, 4.15, 3.73, 3.44, 3.23, 3.07, 2.95, 2.85, 2.77, 2.70, 2.64, 2.59, 2.55, 2.51, 2.48, 2.45, 2.36, 2.29, 2.25, 2.13, 2.03, 1.94],
            [241, 19.38, 8.81, 6.00, 4.78, 4.10, 3.68, 3.39, 3.18, 3.02, 2.90, 2.80, 2.72, 2.65, 2.59, 2.54, 2.50, 2.46, 2.43, 2.40, 2.30, 2.24, 2.19, 2.07, 1.97, 1.88],
            [242, 19.39, 8.78, 5.96, 4.74, 4.06, 3.63, 3.34, 3.13, 2.97, 2.86, 2.76, 2.67, 2.60, 2.55, 2.49, 2.45, 2.41, 2.38, 2.35, 2.26, 2.19, 2.14, 2.02, 1.92, 1.83],
            [243, 19.40, 8.76, 5.93, 4.70, 4.03, 3.60, 3.31, 3.10, 2.94, 2.82, 2.72, 2.63, 2.56, 2.51, 2.45, 2.41, 2.37, 2.34, 2.31, 2.22, 2.15, 2.10, 1.98, 1.88, 1.79],
            [244, 19.41, 8.74, 5.91, 4.68, 4.00, 3.57, 3.28, 3.07, 2.91, 2.79, 2.69, 2.60, 2.53, 2.48, 2.42, 2.38, 2.34, 2.31, 2.28, 2.18, 2.12, 2.07, 1.95, 1.85, 1.75],
            [245, 19.42, 8.71, 5.87, 4.64, 3.96, 3.52, 3.23, 3.02, 2.86, 2.74, 2.64, 2.55, 2.48, 2.43, 2.37, 2.33, 2.29, 2.26, 2.23, 2.13, 2.06, 2.02, 1.90, 1.79, 1.69],
            [246, 19.43, 8.69, 5.84, 4.60, 3.92, 3.49, 3.20, 2.98, 2.82, 2.70, 2.60, 2.51, 2.44, 2.39, 2.33, 2.29, 2.25, 2.21, 2.18, 2.09, 2.02, 1.97, 1.85, 1.75, 1.64],
            [248, 19.44, 8.66, 5.80, 4.56, 3.87, 3.44, 3.15, 2.93, 2.77, 2.65, 2.54, 2.46, 2.39, 2.33, 2.28, 2.23, 2.19, 2.15, 2.12, 2.02, 1.96, 1.91, 1.78, 1.68, 1.57],
            [249, 19.45, 8.64, 5.77, 4.53, 3.84, 3.41, 3.12, 2.90, 2.74, 2.61, 2.50, 2.42, 2.35, 2.29, 2.24, 2.19, 2.15, 2.11, 2.08, 1.98, 1.91, 1.86, 1.74, 1.63, 1.52],
            [250, 19.46, 8.62, 5.74, 4.50, 3.81, 3.38, 3.08, 2.86, 2.70, 2.57, 2.46, 2.38, 2.31, 2.25, 2.22, 2.15, 2.11, 2.07, 2.04, 1.94, 1.87, 1.82, 1.69, 1.57, 1.46],
            [251, 19.47, 8.60, 5.71, 4.46, 3.77, 3.34, 3.05, 2.82, 2.67, 2.53, 2.42, 2.34, 2.27, 2.21, 2.16, 2.11, 2.07, 2.02, 1.99, 1.89, 1.81, 1.76, 2.63, 1.51, 1.40],
            [252, 19.47, 8.58, 5.70, 4.44, 3.75, 3.32, 3.03, 2.80, 2.64, 2.50, 2.40, 2.32, 2.24, 2.18, 2.13, 2.08, 2.04, 2.00, 1.96, 1.86, 1.78, 1.74, 1.60, 1.48, 1.35],
            [253, 19.49, 8.56, 5.66, 4.40, 3.71, 3.28, 2.98, 2.76, 2.59, 2.45, 2.35, 2.28, 2.19, 2.12, 2.07, 2.02, 1.98, 1.91, 1.87, 1.80, 1.72, 1.67, 1.52, 1.39, 1.24],
            [254, 19.50, 8.53, 5.63, 4.36, 3.67, 3.23, 2.93, 2.71, 2.54, 2.40, 2.30, 2.21, 2.13, 2.07, 2.01, 1.96, 1.92, 1.88, 1.84, 1.73, 1.65, 1.59, 1.44, 1.28, 1.00]
        ]

        v1d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 20, 24, 30, 40, 50, 100, 10000]
        v2d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 28, 32, 50, 100, 10000]

        if abs(A - 0.05) < 0.000001:
            ii = 0
            while V1 > v1d[ii] and ii < NV1:
                ii += 1

            jj = 0
            while V2 > v2d[jj] and jj < NV2:
                jj += 1

            return F[ii][jj]
        return 0

    def G(self, V1, V2, A):
        nv1 = 14
        nv2 = 18

        Gkr = [
            [0.998, 0.967, 0.906, 0.841, 0.781, 0.727, 0.680, 0.638, 0.602, 0.541, 0.471, 0.398, 0.343, 0.293, 0.237, 0.174, 0.099, 0.000],
            [0.975, 0.871, 0.768, 0.684, 0.616, 0.561, 0.516, 0.477, 0.445, 0.392, 0.335, 0.270, 0.235, 0.198, 0.158, 0.113, 0.063, 0.000],
            [0.939, 0.798, 0.784, 0.598, 0.532, 0.480, 0.438, 0.403, 0.373, 0.326, 0.276, 0.220, 0.191, 0.159, 0.126, 0.089, 0.050, 0.000],
            [0.906, 0.746, 0.629, 0.544, 0.480, 0.431, 0.391, 0.358, 0.331, 0.288, 0.242, 0.192, 0.166, 0.138, 0.108, 0.076, 0.042, 0.000],
            [0.877, 0.707, 0.589, 0.506, 0.445, 0.397, 0.359, 0.329, 0.303, 0.262, 0.219, 0.173, 0.149, 0.124, 0.097, 0.068, 0.037, 0.000],
            [0.853, 0.677, 0.560, 0.478, 0.418, 0.373, 0.336, 0.307, 0.282, 0.244, 0.203, 0.160, 0.137, 0.114, 0.098, 0.062, 0.034, 0.000],
            [0.833, 0.653, 0.536, 0.456, 0.398, 0.353, 0.318, 0.290, 0.266, 0.230, 0.191, 0.150, 0.129, 0.106, 0.083, 0.058, 0.031, 0.000],
            [0.816, 0.633, 0.517, 0.439, 0.382, 0.338, 0.304, 0.277, 0.254, 0.219, 0.181, 0.142, 0.122, 0.100, 0.078, 0.055, 0.029, 0.000],
            [0.801, 0.617, 0.502, 0.424, 0.368, 0.326, 0.293, 0.266, 0.244, 0.210, 0.174, 0.136, 0.116, 0.096, 0.074, 0.052, 0.028, 0.000],
            [0.788, 0.602, 0.488, 0.412, 0.357, 0.315, 0.283, 0.257, 0.235, 0.202, 0.167, 0.130, 0.111, 0.092, 0.071, 0.050, 0.027, 0.000],
            [0.734, 0.657, 0.437, 0.364, 0.313, 0.276, 0.246, 0.227, 0.203, 0.174, 0.143, 0.111, 0.094, 0.077, 0.059, 0.041, 0.022, 0.000],
            [0.660, 0.475, 0.372, 0.307, 0.261, 0.228, 0.202, 0.182, 0.165, 0.140, 0.114, 0.088, 0.074, 0.060, 0.046, 0.032, 0.017, 0.000],
            [0.581, 0.403, 0.309, 0.251, 0.212, 0.183, 0.162, 0.145, 0.131, 0.110, 0.089, 0.067, 0.057, 0.046, 0.035, 0.023, 0.012, 0.000],
            [0.500, 0.333, 0.250, 0.200, 0.167, 0.143, 0.125, 0.111, 0.100, 0.083, 0.067, 0.050, 0.042, 0.033, 0.025, 0.017, 0.008, 0.000]
        ]

        v1d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 36, 14, 10000]
        v2d = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 24, 30, 40, 60, 120, 10000]

        if abs(A - 0.05) < 0.000001:
            ii = 0
            while V1 > v1d[ii] and ii < nv1 - 1:
                ii += 1

            jj = 0
            while V2 > v2d[jj] and jj < nv2 - 1:
                jj += 1

            return Gkr[ii][jj]
        return 0

    def KOHREN(self, I):
        self.A = 0.05
        self.S2Y = [[0 for _ in range(self.Nb)] for _ in range(len(self.C))]
        self.SS2Y = [0.0 for _ in range(len(self.C))]
        self.Gmax = [0.0 for _ in range(len(self.C))]
        self.GT = [0.0 for _ in range(len(self.C))]

        for j in range(self.Nb):
            self.Ysr[I][j] = 0
            for k in range(self.C[I]):
                self.Ysr[I][j] += self.Y[I][j][k]
            self.Ysr[I][j] /= self.C[I]

        self.SS2Y[I] = 0.0
        for j in range(self.Nb):
            self.S2Y[I][j] = 0
            for k in range(self.C[I]):
                self.S2Y[I][j] += (self.Y[I][j][k] - self.Ysr[I][j]) ** 2
            if self.C[I] > 1:
                self.S2Y[I][j] /= (self.C[I] - 1)
            else:
                self.S2Y[I][j] = 0
            self.SS2Y[I] += self.S2Y[I][j]
            if j == 0:
                S2Ymax = self.S2Y[I][j]
            else:
                if S2Ymax < self.S2Y[I][j]:
                    S2Ymax = self.S2Y[I][j]

        if self.SS2Y[I] != 0:
            self.Gmax[I] = S2Ymax / self.SS2Y[I]
        else:
            self.Gmax[I] = 1

        self.SS2Y[I] /= self.Nb  # Дисперсия воспроизводимости
        V1 = self.C[I] - 1
        V2 = self.Nb * (self.C[I] - 1)
        self.GT[I] = self.G(V1, V2, self.A)

        return self.GT[I] > self.Gmax[I]


    def KOEFIC(self, I):
        A = 0.05
        V = self.Nb * (self.C[I] - 1)
        d = round((self.Nm + 1) * (self.Nm + 2) / 2)
        self.S2[I] = self.SS2Y[I] / self.Nb
        self.B0[I] = 0.0
        for JJ in range(self.Nb):
            self.B0[I] += self.Ysr[I][JJ]
        self.B0[I] /= self.Nb

        for II in range(self.Nm):            
            self.B[I][II] = 0.0
            Zn = 0.0
            for JJ in range(self.Nb):
                self.B[I][II] += self.X[II][JJ] * self.Ysr[I][JJ]
                Zn += self.X[II][JJ] ** 2
            self.B[I][II] /= Zn
            Db = self.T(V, A) * (self.SS2Y[I] / (Zn * self.C[I])) ** 0.5
            if abs(Db) >= abs(self.B[I][II]):
                self.B[I][II] = 0.0
                d -= 1  # Число коэффициентов уменьшается

            if II > 0:
                for L in range(II):
                    self.BB[I][II][L] = 0.0
                    Zn = 0.0
                    for JJ in range(self.Nb):
                        self.BB[I][II][L] += self.X[II][JJ] * self.X[L][JJ] * self.Ysr[I][JJ]
                        Zn += (self.X[II][JJ] * self.X[L][JJ]) ** 2
                    self.BB[I][II][L] /= Zn
                    Db = self.T(V, A) * (self.SS2Y[I] / (self.C[I] * Zn)) ** 0.5
                    if abs(Db) >= abs(self.BB[I][II][L]):
                        self.BB[I][II][L] = 0.0
                        d -= 1  # Число коэффициентов уменьшается

            self.B2[I][II] = 0.0
            Zn = 0.0
            Xvol = 0.0
            for JJ in range(self.Nb):
                Xvol += self.X[II][JJ] ** 2
            Xvol /= self.Nb
            for JJ in range(self.Nb):
                self.B2[I][II] += (self.X[II][JJ] ** 2 - Xvol) * self.Ysr[I][JJ]
                Zn += (self.X[II][JJ] ** 2 - Xvol) ** 2
            self.B2[I][II] /= Zn
            self.B0[I] -= Xvol * self.B2[I][II]
            Db = self.T(V, A) * (self.SS2Y[I] / (self.C[I] * Zn)) ** 0.5
            if abs(Db) >= abs(self.B2[I][II]):
                self.B2[I][II] = 0.0
                d -= 1  # Число коэффициентов уменьшается
            self.S2[I] += (self.SS2Y[I] / (self.C[I] * Zn)) * Xvol ** 2
            
        Db = self.T(V, A) * (self.S2[I]) ** 0.5
        if abs(Db) >= abs(self.B0[I]):
            self.B0[I] = 0.0
            d -= 1

        S2ad = 0.0
        for JJ in range(self.Nb):
            self.Xnm = [0.0] * self.Nm  # Инициализация Xnm
            for kkk in range(self.Nm):
                self.Xnm[kkk] = self.X[kkk][JJ]
            S2ad += (self.Ysr[I][JJ] - self.Yras(I, self.Xnm)) ** 2
        S2ad /= (self.Nb - d)
        self.Fras[I] = S2ad / self.SS2Y[I]
        self.Ftab[I] = self.Fi(self.Nb - d, self.Nb - 1, 0.05)

    def GAUSS(self, IFuO):
        iter = 0
        osh = 0.0
        aag = [[0.0 for _ in range(self.MaxK2)] for _ in range(self.MaxK2)]
        bbg = [0.0 for _ in range(self.MaxK2)]
        bbg0 = [0.0 for _ in range(self.MaxK2)]
        xxg = [0.0 for _ in range(self.MaxK2)]
        xxg0 = [0.0 for _ in range(self.MaxK2)]
        XX = [[0.0 for _ in range(self.MaxK2)] for _ in range(self.maxNb)]

        for ii in range(self.Nb):
            XX[ii][0] = 1.0

        for ii in range(self.Nm):
            for jj in range(self.Nb):
                rr = self.X[ii][jj]
                XX[jj][1 + ii] = rr
                rr = self.X[ii][jj]
                rr = rr * rr
                XX[jj][1 + self.Nm + ii] = rr

        for jj in range(self.Nb):
            kk = 1 + self.Nm + self.Nm
            for iii in range(self.Nm):
                for jjj in range(iii + 1, self.Nm):
                    kk += 1
                    rr = self.X[iii][jj]
                    rm = self.X[jjj][jj]
                    rr = rr * rm
                    XX[jj][kk] = rr

        n = round(0.5 * (self.Nm + 1) * (self.Nm + 2))

        for ii in range(n):
            for jj in range(n):
                rr = sum(XX[kk][ii] * XX[kk][jj] for kk in range(self.Nb))
                aag[ii][jj] = rr

        for jj in range(n):
            rr = sum(XX[kk][jj] * self.Ysr[IFuO][kk] for kk in range(self.Nb))
            bbg[jj] = rr

        iter = 0
        while True:
            iter += 1
            for k in range(n - 1):
                L = k
                for m in range(k + 1, n):
                    if abs(aag[m][k]) > abs(aag[L][k]):
                        L = m
                if L != k:
                    for j in range(k, n):
                        rr = aag[k][j]
                        aag[k][j] = aag[L][j]
                        aag[L][j] = rr
                    rr = bbg[k]
                    bbg[k] = bbg[L]
                    bbg[L] = rr

                for i in range(k + 1, n):
                    rm = aag[i][k] / aag[k][k]
                    aag[i][k] = 0.0
                    if rm != 0:
                        for j in range(k + 1, n):
                            rr = aag[i][j] - rm * aag[k][j]
                            aag[i][j] = rr
                        rr = bbg[i] - rm * bbg[k]
                        bbg[i] = rr

            xxg[n - 1] = bbg[n - 1] / aag[n - 1][n - 1]
            for i in range(n - 2, -1, -1):
                rr = sum(aag[i][j] * xxg[j] for j in range(i + 1, n))
                xxg[i] = (bbg[i] - rr) / aag[i][i]

            if iter == 1:
                for ii in range(n):
                    xxg0[ii] = xxg[ii]
                    bbg0[ii] = bbg[ii]
                for ii in range(n):
                    rr = sum(aag[ii][jj] * xxg[jj] for jj in range(n))
                    bbg[ii] = bbg0[ii] - rr
            else:
                osh = max(abs(xxg[ii]) for ii in range(n))
                for ii in range(n):
                    xxg0[ii] += xxg[ii]
                for ii in range(n):
                    rr = sum(aag[ii][jj] * xxg0[jj] for jj in range(n))
                    bbg[ii] = bbg0[ii] - rr

            if iter > 1 and osh < 0.0000001:
                break

        self.B0[IFuO] = xxg0[0]
        for jj in range(self.Nm):
            self.B[IFuO][jj] = xxg0[1 + jj]
            self.B2[IFuO][jj] = xxg0[1 + self.Nm + jj]
        kk = 1 + self.Nm + self.Nm
        for jj in range(self.Nm):
            for ii in range(jj + 1, self.Nm):
                kk += 1
                self.BB[IFuO][ii][jj] = xxg0[kk]
                
                
    def KOEFICR(self, I):
        A = 0.05
        d = round((self.Nm + 1) * (self.Nm + 2) / 2)
        self.S2[I] = self.SS2Y[I] / self.Nb

        self.GAUSS(I)

        Y0sr = sum(self.Ysr[I][JJ] for JJ in range(self.Nb - self.N0, self.Nb)) / self.N0

        F0 = sum((self.Ysr[I][JJ] - Y0sr) ** 2 for JJ in range(self.Nb - self.N0, self.Nb))

        F1 = sum((self.Yras(I, [self.X[kkk][JJ] for kkk in range(self.Nm)]) - self.Ysr[I][JJ]) ** 2 for JJ in range(self.Nb))

        S2ad = (F1 - F0) / (self.Nb - d - self.N0 + 1)

        if self.SS2Y[I] != 0:
            self.Fras[I] = S2ad / self.SS2Y[I]
        else:
            self.Fras[I] = 0

        self.Ftab[I] = self.Fi(self.Nb - d - self.N0 + 1, self.Nb - 1, 0.05)