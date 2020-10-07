import numpy as np
import pandas as pd
from functools import reduce
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os


class amortizacion:
    __P_ = None
    __C_ = None
    __I_ = None
    __F_ = None
    __S_ = None
    _T = None

    def __init__(self, saldo, interes, periodo, fecha, ruta, nombre):
        """
        :param saldo: int, Monto a amortizar
        :param interes: float, Porcentaje del interes por ejemplo 25.4% poner 25.4
        :param periodo: int, Cuantos meses durara la amortizacion
        :param fecha: str, Fecha m/d/a donde empezaremos la amortizacion
        :param ruta: str, Lugar donde guardaremos el excel
        :param nombre:str, Nombre del archivos de excel

        """
        self.s = saldo
        self.f = datetime.strptime(fecha, '%m/%d/%y')
        self.i = (interes / 100) / 12
        self.pe = periodo
        self.ruta = ruta
        self.nombre = nombre
        self.Pa = round(self.s * (self.i / (1 - (1 + self.i) ** -self.pe)), 2)
        self.P = self.__P_
        self.C = self.__C_
        self.I = self.__I_
        self.F = self.__F_
        self.S = self.__S_
        self.T = self._T
        self.Fe = [z.strftime('%d/%m/%Y') for z in [self.f + relativedelta(months=+j) for j in range(self.pe)]]

    def Tabla(self):
        self.P = []
        self.C = []
        self.I = []
        self.F = []
        self.S = []
        self.P = [self.Pa for y in range(self.pe)]
        for i in range(self.pe):
            self.S.append(self.s)
            self.I.append(round(self.s * self.i, 2))
            self.C.append(round(self.Pa - self.s * self.i, 2))
            self.F.append(round(self.s - (self.Pa - self.s * self.i), 2))
            self.s = round(self.s - (self.Pa - self.s * self.i), 2)
        self.F[-1] = 0
        self._T = self.T = pd.DataFrame({'Fecha': self.Fe, 'Saldo inicial': self.S, 'Pago': self.P,
                                         'Capital': self.C, 'Interes': self.I, 'Saldo final': self.F})
        self.T.set_index('Fecha', inplace=True)
        return self.T

    def Pago(self, x):
        if x == self.pe:
            t = round(sum(self.P), 2)
            print('Lo que has pagado en total es %s%f' % ('$', t))
        elif x > self.pe:
            print('Introduciste mal la fecha de corte,prueba con un periodo menor igual a %d' % (self.pe))
        else:
            t = round(reduce(lambda x, y: x + y, [self.P[i] for i in range(x)]), 2)
            print('Hasta la fecha %s has pagado %s%f' % (self.Fe[x - 1], '$', t))

    def Interes(self, x):
        if x == self.pe:
            t = round(sum(self.I), 2)
            print('Lo que has pagado en total de intereses es de %s%f' % ('$', t))
        elif x > self.pe:
            print('Introduciste mal el periodo de corte,prueba con un periodo menor igual a %d' % (self.pe))
        else:
            t = round(reduce(lambda x, y: x + y, [self.I[i] for i in range(x)]), 2)
            print('Hasta la fecha %s has pagado %s%f de intereses' % (self.Fe[x - 1], '$', t))

    def Excel(self):
        if not os.path.exists(self.ruta):
            os.mkdir(self.ruta)
        with pd.ExcelWriter(os.path.join(self.ruta, '%s.xlsx' % self.nombre)) as xlwriter:
            self._T.to_excel(xlwriter, sheet_name='Amortizacion')
