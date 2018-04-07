import numpy as np
from itertools import product
import progressbar


'=============================================== FITNESS FUNCTION ====================================================='

'----------------------------------------------- Creation des variables -----------------------------------------------'


def fv_variables(nb_porte, nb_trailer, nb_cmd, all_ind, c_ind, u):
    delta = create_delta(nb_porte, nb_cmd, nb_trailer, c_ind, all_ind, u)
    x = create_x(nb_trailer, all_ind, c_ind, nb_porte)
    y = create_y(nb_trailer, all_ind, c_ind)
    v = create_v(nb_trailer, nb_porte, x)
    return delta, y, v


'Creation des varibles une par une'


def create_delta(nb_porte, nb_cmd, nb_trailer, c_ind, all_ind, u):
    c_rank, x, y, bb, cc = 0, 0, 0, 0, 0
    c_porte = 1
    list_delta = np.zeros((nb_porte, nb_cmd))
    delta = np.zeros((nb_cmd, nb_cmd))
    rank_porte = [np.ceil((i + 1) / nb_porte) for i in range(nb_trailer)]
    while c_porte - 1 < nb_porte:
        while c_rank < (nb_trailer / nb_porte):
            for j in range(nb_trailer):
                if rank_porte[j] == c_rank and all_ind[0, j] == c_porte:
                    while y <= u.shape[0]-1:
                        if u[y, int(all_ind[c_ind, j + nb_trailer]) - 1] != 0:
                            list_delta[int(all_ind[c_ind, j]) - 1, x] = u[y, int(all_ind[c_ind, j + nb_trailer]) - 1]
                            x += 1
                        y += 1
                    y = 0
            c_rank += 1
        c_rank = 0
        c_porte += 1

    for a, b in product(range(nb_porte), range(nb_cmd - 1)):
        if list_delta[a, b] != 0:
            bb = int(list_delta[a, b]) - 1
        for c in range(b, nb_cmd):
            if list_delta[a, c] != 0:
                cc = int(list_delta[a, c]) - 1
        if bb != cc:
            delta[bb, cc] = 1
    return delta


def create_x(nb_trailer, all_ind, c_ind, nb_porte):
    x = np.zeros((nb_trailer, nb_porte))
    for i in range(nb_trailer):
        ligne = int(all_ind[c_ind, i + nb_trailer]) - 1
        col = int(all_ind[c_ind, i]) - 1
        x[ligne, col] = 1
    return x


def create_y(nb_trailer, all_ind, c_ind):
    y = np.zeros((nb_trailer, nb_trailer))
    for i in range(0, nb_trailer - 1):
        for j in range(i + 1, nb_trailer):
            if all_ind[c_ind, i] == all_ind[c_ind, j]:
                alig = int(all_ind[c_ind, i + nb_trailer]) - 1
                acol = int(all_ind[c_ind, j + nb_trailer]) - 1
                y[alig, acol] = 1
    return y


def create_v(nb_trailer, nb_porte, x):
    v = np.zeros((nb_trailer, nb_porte, nb_trailer, nb_porte))
    for i, j in product(range(nb_trailer), range(nb_porte)):
        if x[i, j] == 1:
            for ii, jj in product(range(nb_trailer), range(nb_porte)):
                if x[ii, jj] == 1:
                    v[i, j, ii, jj] = 1
    return v


'-------------------------------- Ensembles des fonctions contraintes (modèle)-----------------------------------------'


def fv_contraintes(nb_trailer, nb_cmd, nb_porte, tc, q, ub, lb, v, y, delta, fv, c_ind, beta, d, gamma, qte):
    a, c = np.zeros(nb_trailer), np.zeros(nb_trailer)
    lam, mu, sig, max_beta = np.zeros(nb_cmd), np.zeros(nb_cmd), np.zeros(nb_cmd), np.zeros(nb_cmd)
    cmax, passage = 0, 0
    modif = 1

    maj_j = np.zeros((2, nb_trailer))
    maj_p = np.zeros((3, nb_cmd))

    for j, p, pp in product(range(nb_trailer), range(nb_cmd), range(nb_cmd)):
        if ub[j, p] == 1 and ub[j, pp] == 1:
            max_beta[p] += 1

    # ............................................Constraints........................................................
    # boucle
    while modif != 0:
        modif = 0

        'Contrainte 2'
        for j in range(nb_trailer):
            if passage == 0 or maj_j[1, j] >= 1:
                for jj in range(nb_trailer):
                    if j != jj:
                        if a[jj] < c[j] + tc - q * (1 - y[j, jj]):
                            modif += 1
                            a[jj] = c[j] + tc - q * (1 - y[j, jj])
                            maj_j[0, jj] += 1

        'Raz Cj'
        maj_j[1, :] = 0

        'Contrainte 3'
        for j in range(nb_trailer):
            if passage == 0 or maj_j[0, j] >= 1:
                for p in range(nb_cmd):
                    if ub[j, p] == 1:
                        if lam[p] < a[j] + beta[p] * qte[p]:
                            modif += 1
                            lam[p] = a[j] + beta[p] * qte[p]
                            maj_p[0, p] += 1

        'Contrainte 4'
        for j in range(nb_trailer):
            if passage == 0 or maj_j[0, j] >= 1:
                for p in range(nb_cmd):
                    if lb[j, p] == 1:
                        if lam[p] < a[j]:
                            modif += 1
                            lam[p] = a[j]
                            maj_p[0, p] += 1

        'Contrainte 5'
        for p in range(nb_cmd):
            if passage == 0 or maj_p[0, p] >= 1:
                for j, jj in product(range(nb_trailer), range(nb_trailer)):
                    if ub[j, p] == 1 and lb[jj, p] == 1:
                        for pp in range(nb_cmd):
                            if p != pp:
                                for m, mm in product(range(nb_porte), range(nb_porte)):
                                    if lam[pp] < lam[p] + 2 * d[m, mm] * v[j, m, jj, mm] * qte[p] - q * (1 - delta[p,
                                                                                                                   pp]):
                                        modif += 1
                                        lam[pp] = lam[p] + 2 * d[m, mm] * v[j, m, jj, mm] * qte[p] - q * (1 - delta[p,
                                                                                                                    pp])
                                        maj_p[0, pp] += 1

        'Contrainte 6'
        for p in range(nb_cmd):
            if passage == 0 or maj_p[0, p] >= 1:
                for j, jj in product(range(nb_trailer), range(nb_trailer)):
                    if ub[j, p] == 1 and lb[jj, p] == 1:
                        for m, mm in product(range(nb_porte), range(nb_porte)):
                            if mu[p] < lam[p] + d[m, mm] * v[j, m, jj, mm] * qte[p]:
                                modif += 1
                                mu[p] = lam[p] + d[m, mm] * v[j, m, jj, mm] * qte[p]
                                maj_p[1, p] += 1

        'Raz lam p'
        maj_p[0, :] = 0

        'Contrainte 7'
        for p in range(nb_cmd):
            if passage == 0 or maj_p[1, p] >= 1:
                if sig[p] < mu[p] + qte[p]:
                    modif += 1
                    sig[p] = mu[p] + qte[p]
                    maj_p[2, p] += 1

        'Raz mu p'
        maj_p[1, :] = 0

        'Contrainte 8'
        for j in range(nb_trailer):
            if passage == 0 or maj_j[0, j] >= 1:
                for p, pp in product(range(nb_cmd), range(nb_cmd)):
                    if lb[j, p] == 1 and ub[j, pp] == 1:
                        if sig[p] < a[j] + max_beta[pp] * qte[pp] + qte[p]:
                            modif += 1
                            sig[p] = a[j] + max_beta[pp] * qte[pp] + qte[p]
                            maj_p[2, p] += 1

        'Raz Aj'
        maj_j[0, :] = 0

        'Contrainte 9'
        for p in range(nb_cmd):
            if passage == 0 or maj_p[2, p] >= 1:
                for j, pp in product(range(nb_trailer), range(nb_cmd)):
                    if lb[j, p] == 1 and lb[j, pp] == 1 and p != pp:
                        if sig[pp] < sig[p] + qte[p] - q * (1 - gamma[p, pp]):
                            modif += 1
                            sig[pp] = sig[p] + qte[p] - q * (1 - gamma[p, pp])
                            maj_p[2, pp] += 1

        'Contrainte 10'
        for p in range(nb_cmd):
            if passage == 0 or maj_p[2, p] >= 1:
                for j in range(nb_trailer):
                    if lb[j, p] == 1:
                        if c[j] < sig[p]:
                            modif += 1
                            c[j] = sig[p]
                            maj_j[1, j] += 1

        'Raz sigma p'
        maj_p[2, :] = 0

        # print(lam, '\n', mu, '\n', sig, '\n', A, '\n', C)

        'Evite boucle infinie si non convergence'
        passage += 1
        if passage >= 10:
            modif = 0

    'Contrainte 11'
    cmax = max(c[:])

    '''if Cmax == 11:
        print(passage, '-', int(Cmax))
        print(c_ind)'''
    # print(a, '\n', c, '\n', lam, '\n', mu, '\n', sig)

    fv[c_ind] = cmax
    return fv


'-------------------------------- Itérations à toute la population ----------------------------------------------------'


def fitness_function(nb_porte, nb_trailer, nb_cmd, all_ind, nb_ind, u, tc, q, ub, lb, beta, d, gamma, qte):
    fv = np.zeros(nb_ind)
    bar = progressbar.ProgressBar(max_value=nb_ind)
    for c_ind in range(nb_ind):
        delta, y, v = fv_variables(nb_porte, nb_trailer, nb_cmd, all_ind, c_ind, u)
        fv = fv_contraintes(nb_trailer, nb_cmd, nb_porte, tc, q, ub, lb, v, y, delta, fv, c_ind, beta, d, gamma, qte)
        bar.update(c_ind)
    return fv
