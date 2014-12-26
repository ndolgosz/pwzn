# -*- coding: utf-8 -*-

from tasks.zaj5.zadanie2 import load_data # Musi tu być żeby testy przeszły

import numpy as np


def get_event_count(data):
    """

    Dane w pliku losowane są z takiego rozkładu:
    position, velocity: każda składowa losowana z rozkładu równomiernego 0-1
    mass: losowana z rozkładu równomiernego od 1 do 100.

    Zwraca ilość zdarzeń w pliku. Każda struktura ma przypisane do którego
    wydarzenia należy. Jeśli w pliku jest wydarzenie N > 0
    to jest i wydarzenie N-1.

    :param np.ndarray data: Wynik działania zadanie2.load_data
    """
    return len(set(data['event_id']))

def get_center_of_mass(event_id, data):
    """
    Zwraca macierz numpy zawierajacą położenie x, y i z środka masy układu.
    :param np.ndarray data: Wynik działania zadanie2.load_data
    :return: Macierz 3 x 1
    """
    indexes = data['event_id'] == event_id
    dataset = data[indexes]
    x = {}
    y = {}
    z = {}
    den = 0
    for i in range(0, len(dataset)) :
        x[i] = dataset['particle_position'][1][0]*dataset['particle_mass'][i]
        y[i] = dataset['particle_position'][1][1]*dataset['particle_mass'][i]
        z[i] = dataset['particle_position'][1][2]*dataset['particle_mass'][i]
        den += dataset['particle_mass'][i]
    return np.matrix([sum(x)/den, sum(y)/den, sum(z)/den])


def get_energy_spectrum(event_id, data, left, right, bins):
    """
    Zwraca wartości histogramu energii kinetycznej cząstek (tak: (m*v^2)/2).
    :param np.ndarray data: Wynik działania zadanie2.load_data
    :param int left: Lewa granica histogramowania
    :param int right: Prawa granica historamowania
    :param int bins: ilość binów w historamie
    :return: macierz o rozmiarze 1 x bins

    Podpowiedż: np.histogram
    """
    indexes = data['event_id'] == event_id
    dataset = data[indexes]
    E = [len(dataset['particle_mass'])]
    for i in range(0, len(dataset['particle_mass'])) :
        E_x = (dataset['particle_mass'][i] * dataset['particle_velocity'][i][0]**2)/2
        E_y = (dataset['particle_mass'][i] * dataset['particle_velocity'][i][1]**2)/2
        E_z = (dataset['particle_mass'][i] * dataset['particle_velocity'][i][2]**2)/2
        E.append(np.sqrt(E_x**2 + E_y**2 + E_z**2))
    hist = np.histogram(E, bins = np.linspace(left, right, bins))
    return hist[0]

if __name__ == "__main__":
    data = load_data("/opt/pwzn/zaj5/zadB")
    #print(data)
    #print(get_event_count(data))
    #print(get_center_of_mass(1, data))
    print(get_energy_spectrum(1,data,0 , 90, 100))

    #print(list(get_energy_spectrum(1, data, 0, 90, 100)))