# -*- coding: utf-8 -*-

import numpy as np


def linear_func(x, a, b):
    """
    Funkcja ta zwraca wyznacza a*x + b, funkcja ta powinna działać bez względu
    na to czy x to tablica numpy czy liczba zmiennoprzecinkowa.

    Podpowiedź: Nie jest to bardzo trudne.

    :param np.ndarray x:
    :param float a:
    :param float b:
    """
    return x*a + b

def chisquared(xy, a, b):
    """

    Funkcja liczy sumę Chi^2 między wartościami zmierzonej funkcji a funkcją 
    liniową o wzorze a*x + b.

    Sumę chi^2 definiujemy jako:

    Chi^2 = Sum(( (y - f(x))/sigma_y)^2)

    gdzie f(x) to w naszym przypadku funkcja liniowa


    :param np.ndarray xy: Tablica o rozmiarze N x 3, w pierwszej kolumnie
        zawarte są wartości zmiennej a w drugiej wartości y.
    :param float a:
    :param float b:
    :return:
    """
    y = xy[:,0]*a + b
    return np.sum(np.power(((y-xy[:,1])/xy[:,2]),2))

    

def least_sq(xy):
    """
    Funkcja liczy parametry funkcji liniowej ax+b do danych za pomocą metody
    najmniejszych kwadratów.

    A = (Sum(x^2)*Sum(y)-Sum(x)*Sum(xy))/Delta
    B = (N*Sum(xy)-Sum(x)*Sum(y))/Delta
    Delta = N*Sum(x^2) - (Sum(x)^2)

    :param xy: Jak w chisquared, uwaga: sigma_y nie jest potrzebne.
    :return: Krotka
    """
    x=xy[:,0]
    y=xy[:,1]
    N=len(x)
    Delta = np.sum(np.power(x, 2)) * N - (np.power(np.sum(x),2))
    A = (np.sum(np.power(x, 2))*np.sum(y)-np.sum(x)*np.sum(x*y))/Delta
    B = (N*np.sum(x*y)-np.sum(x)*np.sum(y))/Delta
    return (A,B)
      
