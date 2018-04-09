import numpy as np
import random
from itertools import product
import csv
import codecs

'---------------------------------------------- Lecture des donnees du problème --------------------------------------'


def read_data(data):
    nb_porte, nb_mont, nb_dech, nb_cmd, tc, aleatoire, choix_porte = 0, 0, 0, 0, 0, 0, 0
    u = np.zeros(())
    l = np.zeros(())
    qte = np.zeros(())

    # scenario
    if int(data) == 1:
        if data == 1.01:
            # scenario 1
            nb_porte = 2
            nb_mont = 2
            nb_dech = 2
            nb_cmd = 4
            u = np.transpose([[3, 0, 0], [1, 4, 2]])
            l = np.transpose([[3, 4], [1, 2]])
            tc = 5
            qte = np.array([1, 1, 1, 1])
            choix_porte = 1
            """time_in = [0] * nb_dech
            time_out = [50] * nb_mont"""

        elif data == 1.02:
            # scenario 2
            nb_porte = 4
            nb_mont = 6
            nb_dech = 6
            nb_cmd = 10
            u = np.transpose([[9, 0, 0], [1, 8, 0], [10, 4, 0], [3, 0, 0], [6, 0, 0], [2, 7, 5]])
            l = np.transpose([[6, 9, 0], [1, 8, 0], [4, 0, 0], [3, 2, 7], [10, 0, 0], [5, 0, 0]])
            tc = 5
            qte = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            choix_porte = 1

        elif data == 1.03:
            # scenario 3
            nb_porte = 4
            nb_mont = 8
            nb_dech = 8
            nb_cmd = 12
            u = np.transpose([[11, 0, 0], [10, 6, 3], [7, 1, 0], [12, 0, 0], [5, 8, 0], [4, 0, 0], [2, 0, 0],
                              [9, 0, 0]])
            l = np.transpose([[11, 9], [10, 0], [7, 1], [12, 4], [5, 8], [2, 0], [3, 0], [6, 0]])
            tc = 5
            qte = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            choix_porte = 1

        elif data == 1.04:
            # scenario 4
            nb_porte = 6
            nb_mont = 8
            nb_dech = 8
            nb_cmd = 15
            u = np.transpose([[10, 0, 0], [1, 13, 0], [15, 8, 0], [6, 0, 0], [3, 2, 0], [14, 5, 0], [12, 7, 11],
                              [4, 9, 0]])
            l = np.transpose([[9, 10, 7], [13, 4, 0], [15, 5, 0], [6, 0, 0], [2, 14, 0], [8, 3, 0], [12, 0, 0],
                              [1, 11, 0]])
            tc = 5
            qte = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            choix_porte = 1

        elif data == 1.05:
            # scenario 5
            nb_porte = 4
            nb_mont = 10
            nb_dech = 10
            nb_cmd = 18
            u = np.transpose([[1, 17, 11], [18, 12, 15], [5, 3, 0], [7, 0, 0], [8, 10, 0], [2, 9, 0], [14, 13, 0],
                              [16, 0, 0], [6, 0, 0], [4, 0, 0]])
            l = np.transpose([[1, 0, 0, 0], [18, 0, 0, 0], [3, 0, 0, 0], [13, 7, 8, 2], [14, 0, 0, 0], [9, 0, 0, 0],
                              [5, 15, 0, 0], [16, 10, 12, 0], [6, 11, 0, 0], [4, 17, 0, 0]])
            tc = 5
            qte = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            choix_porte = 1

        elif data == 1.06:
            # scenario 6
            nb_porte = 10
            nb_mont = 20
            nb_dech = 20
            nb_cmd = 50

            u = np.array([[38, 39, 49, 19, 11, 20, 27, 8, 24, 45, 32, 50, 9, 26, 33, 25, 4, 42, 15, 43],
                          [40, 41, 7, 13, 46, 48, 22, 34, 0, 23, 0, 2, 16, 36, 44, 21, 28, 31, 1, 10],
                          [14, 0, 0, 0, 12, 5, 0, 6, 0, 0, 0, 0, 0, 0, 0, 29, 0, 3, 30, 17],
                          [0, 0, 0, 0, 0, 35, 0, 47, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

            l = np.array([[45, 46, 1, 30, 16, 42, 7, 3, 22, 5, 43, 47, 27, 33, 21, 35, 41, 17, 48, 19],
                          [36, 40, 15, 0, 49, 29, 0, 23, 13, 0, 20, 26, 39, 38, 31, 11, 0, 37, 28, 0],
                          [12, 9, 0, 0, 0, 0, 0, 8, 0, 0, 6, 18, 2, 0, 0, 34, 0, 4, 0, 0],
                          [0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 24, 0, 14, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 44, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0]])
            tc = 5
            qte = np.ones(nb_cmd)
            choix_porte = 1

        elif data == 1.07:
            # scenario 7
            nb_porte = 5
            nb_mont = 20
            nb_dech = 20
            nb_cmd = 50

            u = np.array([[38, 22, 16, 50, 8, 31, 1, 28, 37, 4, 9, 39, 49, 47, 44, 17, 13, 6, 46, 5],
                          [0, 32, 11, 34, 0, 20, 18, 48, 27, 0, 36, 2, 42, 35, 41, 10, 7, 33, 19, 29],
                          [0, 26, 0, 30, 0, 0, 24, 0, 0, 0, 40, 14, 43, 0, 23, 3, 45, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 0, 0, 15, 0, 25, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0]])

            l = np.array([[33, 37, 24, 36, 25, 10, 32, 41, 12, 42, 15, 43, 13, 6, 26, 20, 31, 46, 1, 40],
                          [8, 27, 44, 23, 0, 5, 14, 7, 39, 17, 19, 38, 22, 18, 0, 21, 0, 50, 9, 16],
                          [29, 28, 49, 0, 0, 35, 0, 0, 34, 3, 0, 48, 47, 0, 0, 11, 0, 4, 30, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]])
            tc = 5
            qte = np.ones(nb_cmd)
            choix_porte = 1

        elif data == 1.08:
            # scenario 8
            nb_porte = 20
            nb_mont = 20
            nb_dech = 20
            nb_cmd = 50

            u = np.array([[12, 33, 39, 24, 29, 5, 21, 48, 14, 16, 4, 8, 46, 41, 36, 28, 20, 3, 17, 11],
                          [9, 10, 2, 25, 40, 0, 19, 43, 0, 15, 0, 47, 42, 35, 13, 22, 0, 50, 18, 6],
                          [30, 0, 49, 23, 0, 0, 1, 0, 0, 37, 0, 0, 0, 44, 27, 0, 0, 0, 0, 32],
                          [0, 0, 26, 31, 0, 0, 7, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

            l = np.array([[19, 45, 14, 2, 18, 15, 11, 23, 28, 31, 37, 6, 35, 48, 42, 8, 21, 44, 50, 25],
                          [7, 39, 0, 3, 36, 5, 16, 0, 0, 1, 0, 47, 49, 0, 9, 34, 0, 10, 0, 20],
                          [4, 0, 0, 0, 33, 0, 0, 0, 0, 32, 0, 12, 13, 0, 0, 38, 0, 22, 0, 46],
                          [26, 0, 0, 0, 17, 0, 0, 0, 0, 29, 0, 0, 43, 0, 0, 0, 0, 30, 0, 41],
                          [24, 0, 0, 0, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0, 0]])
            tc = 5
            qte = np.ones(nb_cmd)
            choix_porte = 1

        elif data == 1.09:
            # scenario 9
            nb_porte = 10
            nb_mont = 10
            nb_dech = 10
            nb_cmd = 50

            u = np.array([[17, 3, 1, 47, 11, 14, 5, 12, 8, 4],
                          [49, 25, 26, 28, 46, 31, 34, 33, 0, 10],
                          [45, 41, 48, 29, 9, 19, 37, 22, 0, 44],
                          [13, 23, 36, 0, 27, 20, 40, 0, 0, 50],
                          [0, 2, 32, 0, 39, 43, 24, 0, 0, 15],
                          [0, 0, 35, 0, 6, 7, 42, 0, 0, 18],
                          [0, 0, 21, 0, 0, 0, 0, 0, 0, 38],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 16],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 30]])

            l = np.array([[24, 38, 43, 10, 17, 35, 44, 1, 5, 16],
                          [46, 2, 25, 11, 23, 21, 41, 33, 32, 20],
                          [36, 29, 50, 8, 28, 31, 15, 13, 42, 7],
                          [27, 0, 26, 48, 4, 6, 22, 47, 40, 0],
                          [0, 0, 19, 14, 0, 0, 49, 18, 30, 0],
                          [0, 0, 0, 12, 0, 0, 39, 3, 34, 0],
                          [0, 0, 0, 9, 0, 0, 45, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 37, 0, 0, 0]])
            tc = 5
            qte = np.ones(nb_cmd)
            choix_porte = 1

        elif data == 1.10:
            # scenario 10
            nb_porte = 10
            nb_mont = 40
            nb_dech = 40
            nb_cmd = 50

            u = np.array([[9, 38, 28, 47, 1, 49, 18, 10, 26, 8, 16, 45, 42, 43, 37, 29, 3, 40, 35, 30, 5, 34, 33,
                           41, 14, 13, 20, 2, 27, 44, 22, 36, 15, 31, 7, 21, 12, 24, 39, 48],
                          [0, 17, 0, 0, 0, 0, 50, 0, 0, 0, 0, 32, 0, 0, 0, 4, 0, 11, 0, 0, 0, 0, 0,
                           0, 6, 0, 0, 0, 0, 23, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

            l = np.array([[11, 28, 25, 4, 38, 10, 16, 23, 46, 26, 41, 6, 15, 31, 12, 14, 43, 13, 19, 48, 44, 2, 29,
                           3, 49, 7, 45, 8, 42, 1, 39, 22, 32, 47, 27, 5, 21, 50, 30, 17],
                          [0, 0, 0, 0, 0, 0, 0, 20, 0, 35, 18, 36, 0, 0, 0, 0, 0, 0, 24, 0, 0, 9, 40,
                           0, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0, 37, 0, 0, 0, 0, 33]])
            tc = 5
            qte = np.ones(nb_cmd)
            choix_porte = 1

        elif data == 1.11:
            # scenario 11
            nb_porte = 10
            nb_mont = 20
            nb_dech = 20
            nb_cmd = 25

            u = np.array([[20, 14, 16, 6, 11, 17, 21, 22, 4, 15, 19, 18, 24, 2, 1, 12, 25, 5, 7, 13],
                          [0, 0, 3, 0, 0, 0, 0, 9, 0, 0, 0, 10, 0, 0, 0, 0, 0, 23, 0, 0],
                          [0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

            l = np.array([[1, 11, 17, 23, 25, 20, 9, 12, 7, 21, 2, 24, 8, 19, 3, 4, 13, 16, 22, 5],
                          [0, 0, 10, 0, 0, 0, 18, 0, 15, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0]])
            tc = 5
            qte = np.ones(nb_cmd)
            choix_porte = 1

        elif data == 1.12:
            # scenario 12
            nb_porte = 10
            nb_mont = 20
            nb_dech = 20
            nb_cmd = 100

            u = np.array([[31, 45, 20, 35, 32, 57, 77, 42, 83, 87, 75, 21, 90, 74, 94, 54, 8, 27, 95,
                           44],
                          [18, 55, 30, 19, 22, 14, 16, 41, 0, 67, 29, 10, 52, 82, 96, 98, 34, 56, 38,
                           6],
                          [64, 12, 9, 100, 59, 46, 89, 49, 0, 79, 81, 63, 5, 78, 25, 48, 17, 70, 13,
                           80],
                          [0, 47, 43, 0, 62, 0, 60, 0, 0, 76, 11, 65, 61, 72, 0, 0, 37, 91, 99,
                           84],
                          [0, 39, 58, 0, 26, 0, 1, 0, 0, 0, 2, 85, 73, 3, 0, 0, 97, 28, 40,
                           0],
                          [0, 69, 53, 0, 0, 0, 4, 0, 0, 0, 88, 92, 0, 36, 0, 0, 7, 0, 71,
                           0],
                          [0, 24, 68, 0, 0, 0, 15, 0, 0, 0, 0, 51, 0, 66, 0, 0, 23, 0, 93,
                           0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 33, 0, 0, 0, 0, 50, 0, 0,
                           0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 0,
                           0]])

            l = np.array([[93, 54, 31, 14, 70, 92, 36, 71, 99, 79, 78, 8, 46, 86, 51, 41, 66, 50, 76,
                           67],
                          [44, 34, 40, 59, 65, 77, 11, 0, 94, 47, 90, 49, 61, 45, 89, 30, 1, 73, 62,
                           72],
                          [84, 5, 88, 29, 85, 37, 20, 0, 22, 9, 13, 56, 75, 53, 48, 25, 64, 100, 18,
                           0],
                          [97, 81, 57, 10, 32, 58, 69, 0, 28, 3, 4, 12, 26, 63, 98, 6, 83, 0, 0,
                           0],
                          [15, 0, 7, 87, 0, 0, 42, 0, 0, 21, 38, 82, 95, 24, 0, 0, 0, 0, 0,
                           0],
                          [80, 0, 0, 0, 0, 0, 39, 0, 0, 60, 33, 0, 23, 74, 0, 0, 0, 0, 0,
                           0],
                          [27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 91, 0, 16, 68, 0, 0, 0, 0, 0,
                           0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43, 0, 17, 52, 0, 0, 0, 0, 0,
                           0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 35, 0, 0, 55, 0, 0, 0, 0, 0,
                           0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0,
                           0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0,
                           0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 96, 0, 0, 0, 0, 0,
                           0]])
            tc = 5
            qte = np.ones(nb_cmd)
            choix_porte = 1

        elif data == 1.13:
            # scenario 13
            nb_porte = 10
            nb_mont = 16
            nb_dech = 16
            nb_cmd = 141
            u = np.array([[32, 72, 5, 115, 89, 64, 103, 68, 109, 88, 74, 129, 67, 97, 93, 76],
                          [58, 16, 135, 42, 20, 86, 8, 45, 120, 83, 69, 140, 25, 63, 84, 18],
                          [133, 31, 19, 119, 125, 79, 15, 117, 80, 123, 99, 82, 98, 141, 106, 30],
                          [9, 27, 56, 28, 46, 44, 110, 40, 39, 111, 132, 10, 107, 47, 21, 121],
                          [116, 94, 114, 3, 130, 26, 100, 122, 65, 85, 43, 51, 113, 4, 1, 59],
                          [134, 70, 38, 13, 105, 22, 0, 138, 127, 60, 108, 41, 131, 6, 112, 57],
                          [53, 118, 0, 126, 81, 137, 0, 136, 7, 71, 61, 101, 62, 52, 11, 55],
                          [87, 24, 0, 0, 2, 73, 0, 17, 48, 77, 35, 12, 0, 14, 75, 34],
                          [124, 29, 0, 0, 66, 0, 0, 102, 0, 128, 91, 0, 0, 0, 104, 23],
                          [0, 95, 0, 0, 36, 0, 0, 90, 0, 0, 0, 0, 0, 0, 92, 96],
                          [0, 49, 0, 0, 37, 0, 0, 33, 0, 0, 0, 0, 0, 0, 0, 50],
                          [0, 0, 0, 0, 139, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
            l = np.array([[120, 91, 138, 57, 19, 111, 136, 98, 51, 116, 56, 106, 21, 8, 17, 123],
                          [87, 63, 132, 53, 139, 46, 92, 133, 34, 78, 86, 32, 118, 60, 41, 33],
                          [10, 101, 81, 29, 140, 93, 108, 69, 126, 75, 22, 23, 58, 74, 72, 59],
                          [117, 42, 114, 99, 109, 71, 88, 121, 90, 96, 141, 13, 14, 82, 20, 94],
                          [9, 119, 37, 128, 43, 112, 36, 130, 49, 137, 40, 134, 15, 35, 67, 85],
                          [89, 70, 26, 1, 95, 38, 102, 97, 110, 104, 129, 115, 80, 65, 25, 84],
                          [0, 103, 48, 122, 66, 64, 131, 18, 6, 76, 61, 0, 0, 24, 47, 55],
                          [0, 12, 0, 2, 83, 31, 0, 7, 27, 100, 73, 0, 0, 54, 28, 105],
                          [0, 62, 0, 113, 68, 39, 0, 79, 0, 4, 52, 0, 0, 0, 77, 50],
                          [0, 0, 0, 125, 30, 11, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
                          [0, 0, 0, 135, 5, 45, 0, 0, 0, 0, 44, 0, 0, 0, 0, 0],
                          [0, 0, 0, 127, 0, 16, 0, 0, 0, 0, 124, 0, 0, 0, 0, 0],
                          [0, 0, 0, 107, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
            qte = np.random.randint(low=1, high=6, size=nb_cmd)
            tc = 18.75
            choix_porte = 2

    # aleatoire
    elif data == 2:
        aleatoire = 1
        nb_porte = 30
        nb_mont = 49
        nb_dech = 49
        nb_cmd = 423
        tc = 18.75
        choix_porte = 2
        # qte = np.ones(nb_cmd)
        qte = np.random.randint(low=1, high=6, size=nb_cmd)

    # csv
    elif data == 3:
        '''# Mise en forme de l a partir du fichier CSV-Excel
        trip = ""
        l = np.zeros((100, 100))
        i = -1
        a = 0
        with open('Classeur4.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';', dialect='excel')
            for row in readCSV:
                if row[0] == trip:
                    l[a, i] = int(row[1])
                    a += 1
                else:
                    trip = row[0]
                    i += 1
                    a = 0
                    l[a, i] = int(row[1])
        l = np.transpose(l)'''
        nb_porte, tc, nb_cmd, nb_mont, l, u, nb_dech, qte, beta = read_csv()

    return nb_porte, nb_cmd, tc, nb_dech, nb_mont, aleatoire, u, l, qte, choix_porte


def read_csv():
    """Creer U et L en partir du CSV de l'entreprise"""
    nb_porte = 52
    tc = 18.75
    voyages = 'voyages.txt'
    read_voyages = csv.reader(codecs.open(voyages, 'rU', 'utf-16'), delimiter='|')
    remorques = 'remorques.txt'
    read_remorques = csv.reader(codecs.open(remorques, 'rU', 'utf-16'), delimiter='|')
    portes = 'portes.txt'
    read_portes = csv.reader(codecs.open(portes, 'rU', 'utf-16'), delimiter='|')

    montage = ""
    max_cmd, nb_cmd, cmd, rr, c, r, nb_mont = 0, 0, 0, 0, 0, -1, 0

    'Remplissage de L, Beta et Qte'
    for row in read_voyages:
        if row[0] == montage:
            nb_cmd += 1
            cmd += 1
        else:
            montage = row[0]
            nb_cmd += 1
            nb_mont += 1
            if cmd > max_cmd:
                max_cmd = cmd
            cmd = 1

    qte, beta = np.zeros(nb_cmd), np.zeros(nb_cmd)
    l = np.zeros((nb_mont, max_cmd))

    file = 'voyages.txt'
    read_voyages = csv.reader(codecs.open(file, 'rU', 'utf-16'), delimiter='|')
    for row in read_voyages:
        # Rempli la matrice l (1 ligne = 1 montage)
        if row[0] == montage:
            c += 1
            l[r, c] = int(row[1])
        else:
            montage = row[0]
            r += 1
            c = 0
            l[r, c] = int(row[1])

        # Rempli le vecteur de quantite
        qte[rr] = row[2]
        if row[2] == '0':
            qte[rr] = 1

        # Rempli beta
        beta[rr] = row[4]
        if row[4] == '0':
            beta[rr] = 1
        rr += 1

    l = np.transpose(l)

    'Remplir U en fonction de portes, voyages et remorques'
    u1, u2, u3, u4 = np.zeros((1000, 1000)), np.zeros((1000, 1000)), np.zeros((52, 1000)), np.zeros((1000, 1000))

    """max_cmd, cmd = 0, 0
    for row in read_remorques:
        nb_dech += 1
        cmd = len(row[1].split(','))
        if cmd > max_cmd:
            max_cmd = cmd
    print(max_cmd)"""
    # lit le fichier remorque pour construire U1
    r, c = 0, 0

    for row in read_remorques:
        a = np.fromstring(row[1], sep=",")
        for i in range(len(row[1].split(","))):
            if a[i] in l[:, :]:  # verifie que les cmd sont bien dans L
                if not a[i] in u1[:, :]:  # evite les doubles
                    u1[r, c] = a[i]
                    c += 1
        c = 0
        r += 1

    # lit le fichier porte pour construire U2
    r, c = 0, 0
    flag = 0
    for row in read_portes:
        a = np.fromstring(row[2], sep=",")
        if a.size != 0:
            for i in range(len(row[2].split(","))):
                if a[i] in l[:, :]:  # verifie que les cmd sont bien dans L
                    if not a[i] in u1[:, :] and not a[i] in u2[:, :]:  # evite les doubles
                        u2[r, c] = a[i]
                        c += 1
                        flag = 1
        if flag == 0:
            r -= 1
        flag = 0
        c = 0
        r += 1

    # lit le fichier voyage pour construire U3
    file = 'voyages.txt'
    read_voyages = csv.reader(codecs.open(file, 'rU', 'utf-16'), delimiter='|')
    for row in read_voyages:
        a = row[3][:6]  # extraire 'rangee'
        if a == 'rangee':
            rangee = row[3][8:11]
            porte = convert_rang_porte(rangee)
            b = int(row[1])
            if b not in u1[:, :] and b not in u2[:, :] and b not in u3[:, :]:  # evite les doubles
                flag, c = 0, 0
                while flag == 0:
                    if u3[porte, c] == 0:
                        u3[porte, c] = b
                        flag = 1
                        c = 0
                    else:
                        c += 1

    'retire les lignes vides, les "rangees" sans palettes '
    flag, i, suppr = 0, 0, 0
    while flag == 0:
        if i < 51 - suppr:
            if u3[i, 0] == 0:
                u3 = np.delete(u3, i, 0)
                suppr += 1
                i -= 1
            i += 1
        else:
            flag = 1

    # lit le fichier voyage pour construire U4
    c = 0
    file = 'voyages.txt'
    read_voyages = csv.reader(codecs.open(file, 'rU', 'utf-16'), delimiter='|')
    for row in read_voyages:
        a = row[3]
        if a == '':
            b = int(row[1])
            if b not in u1[:, :] and b not in u2[:, :] and b not in u3[:, :] and b not in u4[:, :]:  # evite les doubles
                u4[0, c] = row[1]
                c += 1

    # supprime les lignes et colonnes de zeros
    'u1'
    max_i1, max_j1, cmd = 0, 0, 0
    for i in range(1000):
        if u1[i, 0] == 0:
            i += 1
        else:
            max_i1 = i
            i += 1
    for i in range(max_i1 + 1):
        for j in range(1000):
            if u1[i, j] != 0:
                cmd = j
        if cmd > max_j1:
            max_j1 = cmd

    'u2'
    max_i2, max_j2, cmd = 0, 0, 0
    for i in range(1000):
        if u2[i, 0] == 0:
            i += 1
        else:
            max_i2 = i
            i += 1
    for i in range(max_i2 + 1):
        for j in range(1000):
            if u2[i, j] != 0:
                cmd = j
        if cmd > max_j2:
            max_j2 = cmd

    'u3'
    max_i3, max_j3, cmd = 0, 0, 0
    for i in range(52 - suppr):
        if u3[i, 0] == 0:
            i += 1
        else:
            max_i3 = i
            i += 1
    for i in range(max_i3 + 1):
        for j in range(1000):
            if u3[i, j] != 0:
                cmd = j
        if cmd > max_j3:
            max_j3 = cmd

    'u4'
    max_i4, max_j4, cmd = 0, 0, 0
    for i in range(1000):
        if u4[i, 0] == 0:
            i += 1
        else:
            max_i4 = i
            i += 1
    for i in range(max_i4 + 1):
        for j in range(1000):
            if u4[i, j] != 0:
                cmd = j
        if cmd > max_j4:
            max_j4 = cmd

    max_i = max_i1 + max_i2 + max_i3 + max_i4 + 4
    max_j = max(max_j1, max_j2, max_j3, max_j4) + 1

    'remplit la matrice u'
    u = np.zeros((max_i, max_j))
    for i in range(max_i1 + 1):
        for j in range(max_j):
            u[i, j] = u1[i, j]
    for i in range(max_i2 + 1):
        for j in range(max_j):
            u[i + max_i1 + 1, j] = u2[i, j]
    for i in range(max_i3 + 1):
        for j in range(max_j):
            u[i + max_i1 + max_i2 + 2, j] = u3[i, j]
    for i in range(max_i4 + 1):
        for j in range(max_j):
            u[i + max_i1 + max_i2 + max_i3 + 3, j] = u4[i, j]

    nb_dech, x = u.shape
    return nb_porte, tc, nb_cmd, nb_mont, l, u, nb_dech, qte, beta


def convert_rang_porte(rangee):
    """ renvoie la porte correspondante à la porte la plus proche """
    convert = np.array([[1, '001', '003', '501', '601', ''],
                        [2, '002', '004', '502', '602', ''],
                        [3, '005', '007', '603', '', ''],
                        [4, '006', '008', '604', '', ''],
                        [5, '009', '011', '605', '', ''],
                        [6, '010', '012', '606', '', ''],
                        [7, '013', '015', '607', '', ''],
                        [8, '014', '016', '608', '', ''],
                        [9, '017', '019', '609', '', ''],
                        [10, '018', '020', '610', '', ''],
                        [11, '021', '023', '611', '', ''],
                        [12, '022', '024', '612', '', ''],
                        [13, '025', '027', '613', '', ''],
                        [14, '026', '028', '614', '', ''],
                        [15, '029', '049', '615', '', ''],
                        [16, '030', '050', '616', '', ''],
                        [17, '051', '053', '055', '617', ''],
                        [18, '052', '054', '056', '618', ''],
                        [19, '057', '059', '619', '', ''],
                        [20, '058', '060', '620', '', ''],
                        [21, '061', '063', '621', '', ''],
                        [22, '062', '064', '622', '', ''],
                        [23, '065', '067', '623', '', ''],
                        [24, '066', '068', '624', '', ''],
                        [25, '069', '071', '625', '', ''],
                        [26, '070', '072', '626', '', ''],
                        [27, '073', '075', '627', '', ''],
                        [28, '074', '076', '503', '628', ''],
                        [29, '101', '301', '303', '305', ''],
                        [30, '100', '414', '504', '630', ''],
                        [31, '103', '105', '307', '309', ''],
                        [32, '102', '104', '632', '', ''],
                        [33, '107', '109', '311', '313', ''],
                        [34, '106', '108', '634', '', ''],
                        [35, '111', '113', '315', '317', ''],
                        [36, '110', '112', '636', '', ''],
                        [37, '115', '117', '319', '321', ''],
                        [38, '114', '116', '638', '', ''],
                        [39, '119', '121', '323', '325', ''],
                        [40, '118', '120', '640', '', ''],
                        [41, '141', '143', '317', '329', ''],
                        [42, '140', '142', '642', '', ''],
                        [43, '145', '147', '331', '333', ''],
                        [44, '144', '146', '644', '', ''],
                        [45, '149', '151', '335', '337', '339'],
                        [46, '148', '150', '646', '', ''],
                        [47, '153', '155', '341', '343', '345'],
                        [48, '152', '154', '648', '', ''],
                        [49, '157', '159', '347', '349', '351'],
                        [50, '156', '158', '650', '', ''],
                        [51, '161', '163', '353', '355', '507'],
                        [52, '160', '162', '506', '652', '']])
    porte = 0

    # rangee = int(rangee)
    for i in range(52):
        if rangee in convert[i, 1:]:
            porte = i
    return porte


'---------------------------------------------- Creation des donnees du problème -------------------------------------'


def create_data(nb_porte, nb_cmd, tc, nb_dech, nb_mont, aleatoire, u, l, choix_porte):
    nb_trailer = max(nb_dech, nb_mont)
    d = create_d(nb_porte, choix_porte)
    q = 2 * nb_cmd + sum(map(sum, d)) + nb_trailer * tc
    if aleatoire == 1:
        u = create_u(nb_dech, nb_cmd, nb_trailer)
        l = create_l(nb_mont, nb_cmd, nb_trailer)
    ub = create_ub(nb_trailer, nb_cmd, u)
    lb = create_lb(nb_trailer, nb_cmd, l)
    beta = create_beta(nb_cmd, u)
    gamma = create_gamma(nb_cmd, l)

    return d, q, u, ub, l, lb, beta, gamma, nb_trailer


' Creation des donnees une par une '


def create_d(nb_porte, choix_porte):
    d = np.zeros((nb_porte, nb_porte))

    if choix_porte == 1:
        """ distance pour les tests, avec portes en lignes"""
        for i, j in product(range(nb_porte), range(nb_porte)):
            d[i, j] = ((i - j) ** 2) ** (1 / 2)

    elif choix_porte == 2:
        """ distance reel, selon historique (voir excel) """
        a, b, c = 0.25, 1, 49
        for i in range(nb_porte):
            for j in range(i, nb_porte):
                if int((i + j) / 2) == (i + j) / 2:
                    d[i, j] = (c + (j - i) * a / 2) / 60
                else:
                    d[i, j] = (c + (j - i - 1) * a / 2 + b) / 60
        d = d + d.T - np.diag(d.diagonal())
    return d


def create_u(nb_dech, nb_cmd, nb_trailer):
    """Creation de la matrice U, au hasard si besoin"""
    nb_cmd_dech = np.ones(nb_dech)  # nombre de cmd pour chaque dechargement
    total = nb_dech

    while total != nb_cmd:
        total += 1
        x = random.randint(1, nb_dech)
        nb_cmd_dech[x - 1] += 1

    shf_cmd = np.array(range(nb_cmd))  # melange les cmd
    np.random.shuffle(shf_cmd)

    a = int(np.amax(nb_cmd_dech))  # affecte les cmd a u selon le nb_cmd_dech
    u = np.zeros((a, nb_trailer))
    compteur = 0
    for j, i in product(range(nb_dech), range(nb_cmd - nb_dech)):
        if i < nb_cmd_dech[j]:
            u[i, j] = shf_cmd[compteur] + 1
            compteur += 1
    return u


def create_ub(nb_trailer, nb_cmd, u):
    """ mise en forme bianire de la matrice U """
    ub = np.zeros((nb_trailer, nb_cmd))
    for i in range(len(u)):
        for j in range(len(u[i])):
            if u[i, j]:
                ub[j, int(u[i, j]) - 1] = 1
    return ub


def create_l(nb_mont, nb_cmd, nb_trailer):
    nb_cmd_mont = np.ones(nb_mont)  # nombre de cmd pour chaque montage
    total = nb_mont

    while total != nb_cmd:
        total += 1
        x = random.randint(1, nb_mont)
        nb_cmd_mont[x - 1] += 1

    shf_cmd = np.array(range(nb_cmd))
    np.random.shuffle(shf_cmd)

    a = int(np.amax(nb_cmd_mont))
    l = np.zeros((a, nb_trailer))  # affecte les cmd a l selon le nb_cmd_mont
    compteur = 0
    for j in range(nb_mont):
        for i in range(nb_cmd - nb_mont):
            if i < nb_cmd_mont[j]:
                l[i, j] = shf_cmd[compteur] + 1
                compteur += 1
    return l


def create_lb(nb_trailer, nb_cmd, l):
    lb = np.zeros((nb_trailer, nb_cmd))  # mise en forme bianire de la matrice l
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i, j] != 0:
                lb[j, int(l[i, j]) - 1] = 1
    return lb


def create_beta(nb_cmd, u):
    beta = np.zeros(nb_cmd)
    k = 1
    while k <= nb_cmd:
        for i in range(len(u)):
            for j in range(len(u[i])):
                if u[i, j] == k:
                    beta[k - 1] = i + 1
                    k += 1
    return beta


def create_gamma(nb_cmd, l):
    gamma = np.zeros((nb_cmd, nb_cmd))
    lt = np.matrix.transpose(l)
    for i in range(len(lt)):
        for j in range(0, len(lt[i]) - 1):
            if lt[i, j + 1] != 0:
                gamma[int(lt[i, j]) - 1, int(lt[i, j + 1]) - 1] = 1
    return gamma
