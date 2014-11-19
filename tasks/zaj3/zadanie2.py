# -*- coding: utf-8 -*-
import operator
import csv

def merge(path1, path2, out_file):
    """
    Funkcja pobiera nazwy dwóch plików z n-gramami (takie jak w poprzedmim
    zadaniu) i łączy zawartość tych plików i zapisuje do pliku w ścieżce ``out``.

    Pliki z n-gramami są posortowane względem zawartości n-grama.

    :param str path1: Ścieżka do pierwszego pliku
    :param str path2: Ścieżka do drugiego pliku
    :param str out_file:  Ścieżka wynikowa

    Testowanie tej funkcji na pełnych danych może być mało wygodne, możecie
    stworzyć inną funkcję która działa na dwóch listach/generatorach i testować
    ją.

    Naiwna implementacja polegałaby na stworzeniu dwóch słowników które
    zawierają mapowanie ngram -> ilość wystąpień i połączeniu ich.

    Lepsza implementacja ładuje jeden z plików do pamięci RAM (jako słownik
    bądź listę) a po drugim iteruje.

    Najlepsza implementacja nie wymaga ma złożoność pamięciową ``O(1)``.
    Podpowiedź: merge sort. Nie jest to trywialne zadanie, ale jest do zrobienia.
    """
    lista_gram = {}
    with open(path1, 'r') as file1:
        r = csv.reader(file1, dialect=csv.unix_dialect)
        for line in r:
            lista_gram[line[0]] = line[1]
    with open(path2, 'r') as file2:
        r = csv.reader(file2, dialect=csv.unix_dialect)
        for line in r:
            if line[0] in lista_gram.keys():
                lista_gram[line[0]] = int(lista_gram[line[0]]) + int(line[1])
            else:
                lista_gram[line[0]] = int(line[1])
    dict_list = sorted(lista_gram.items(), key=operator.itemgetter(0))
    with open(out_file,'w') as f:
        writer = csv.writer(f)
        writer.writerows(dict_list)  
if __name__ == '__main__':

    merge(
        '/home/emil/Pulpit/Uczelnia/python/enwiki-20140903-pages-articles_part_0.xml.csv',
        '/home/emil/Pulpit/Uczelnia/python/enwiki-20140903-pages-articles_part_1.xml.csv',
        '/home/emil/Pulpit/Uczelnia/python/pwzn/tasks/zaj3/output.csv')
