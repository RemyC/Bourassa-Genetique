import random
import time
from utils_FF2 import *

" ================================== Fait l initialisation du problème (1er pop) ===================================== "


def initialisation(nb_enfant, nb_trailer, nb_porte, nb_cmd, u, tc, q, ub, lb, beta, d, gamma, qte):

    all_ind = create_enfant(nb_enfant, nb_trailer, nb_porte)
    # print('\n', "all_ind", '\n', all_ind)

    print("_______________________________________________________________________________")
    print("Initialisation en cours ...")

    fv = fitness_function(nb_porte, nb_trailer, nb_cmd, all_ind, nb_enfant, u, tc, q, ub, lb, beta, d, gamma, qte)
    # print('\n', "FV", '\n', fv)

    all_ind, fv = trie(fv, nb_trailer, all_ind)
    print("_______________________________________________________________________________")

    return fv, all_ind


def create_enfant(nb_enfant, nb_trailer, nb_porte):
    start = time.time()
    all_ind = np.zeros((nb_enfant, nb_trailer * 2))
    a = np.zeros(nb_trailer)
    for i in range(nb_enfant):
        "creer nb_enf chromosones aleatoirement de taille nb_trailer*2"
        b = np.arange(1, nb_trailer+1)
        np.random.shuffle(b)

        "construie toujours la même première partie du chromosome"
        c = 1
        for j in range(nb_trailer):
            if c > nb_porte:
                c = 1
            a[j] = c
            c += 1

        all_ind[i] = np.concatenate([a, b])

    end = time.time()
    print("Population initiale :", round(end - start, 3), "secondes")

    return all_ind


"----------------------------------- Sélection des parents (wheel selection, tournament) ------------------------------"


"""def select_parent_rdm(nb_parent):
    list_shf = list(range(nb_parent))  # fait une liste mélangée du numéro des parents
    np.random.shuffle(list_shf)
    list_parent = list_shf[:nb_parent]  # selectionne le nombre de parent a garder
    return list_parent"""


def wheel_selection(nb_enfant, nb_parent_wheel):
    """Selection des parents selon le principe de l'elitisme ou wheel selection"""
    parent_wheel = np.zeros(nb_enfant)
    list_parent_wheel = np.zeros(nb_parent_wheel)

    "définit la proba de selection des parents, 100% pour la meilleur FV"
    for i in range(nb_enfant):
        parent_wheel[i] = nb_enfant/100*(nb_enfant-i)

    "prend un parent random, si sa proba > à un random, alors selectionner pour croisement"
    "evite de prendre des doubles"
    k = 0
    while k < nb_parent_wheel:
        parent_choisi = random.randint(0, nb_enfant-1)
        aleatoire_wheel = random.random()*100
        if parent_wheel[parent_choisi] > aleatoire_wheel:
            if parent_choisi not in list_parent_wheel:
                list_parent_wheel[k] = parent_choisi
                k += 1

    return list_parent_wheel


def tournoi_selection(nb_enfant, nb_parent_tournoi, list_parent_wheel):
    """Selection des parents selon le principe du tournoi"""
    fv_tournoi = np.zeros(nb_enfant)
    list_parent_tournoi = np.zeros(nb_parent_tournoi)

    "définit la qualité des parents, 100% pour la meilleur FV"
    for i in range(nb_enfant):
        fv_tournoi[i] = nb_enfant/100*(nb_enfant-i)

    k = 0
    while k < nb_parent_tournoi:
        "Selectionne 3 parents, a b c, au hasard et garde le meilleur selon sa FV"
        a = random.randint(0, nb_enfant - 1)
        b = random.randint(0, nb_enfant - 1)
        c = random.randint(0, nb_enfant - 1)

        if fv_tournoi[a] > fv_tournoi[b] and fv_tournoi[a] > fv_tournoi[c]:
            if a not in list_parent_tournoi and a not in list_parent_wheel:
                list_parent_tournoi[k] = a
                k += 1
        elif fv_tournoi[b] > fv_tournoi[a] and fv_tournoi[b] > fv_tournoi[c]:
            if b not in list_parent_tournoi and b not in list_parent_wheel:
                list_parent_tournoi[k] = b
                k += 1
        elif fv_tournoi[c] > fv_tournoi[a] and fv_tournoi[c] > fv_tournoi[b]:
            if c not in list_parent_tournoi and c not in list_parent_wheel:
                list_parent_tournoi[k] = c
                k += 1

    return list_parent_tournoi


def selection_parent(nb_enfant, nb_parent_wheel, nb_parent_tournoi):

    list_parent_wheel = wheel_selection(nb_enfant, nb_parent_wheel)
    list_parent_tournoi = tournoi_selection(nb_enfant, nb_parent_tournoi, list_parent_wheel)

    list_parent = np.concatenate([list_parent_wheel, list_parent_tournoi])

    return list_parent


"==================================== Cross-Over + Mutation ==========================================================="


def cross_mut(list_parent, nb_enfant, all_ind, proba_cross, proba_mut, nb_trailer):
    c_enfant = 0
    all_enfant = np.zeros((nb_enfant, nb_trailer * 2))
    chr_parent1, chr_parent2 = np.zeros(nb_trailer * 2), np.zeros(nb_trailer * 2)

    while c_enfant < nb_enfant:
        "selectionne deux parents au hasard, différent l'un de l'autre"
        flag = 0
        while flag == 0:
            parent1 = int(list_parent[random.randint(0, list_parent.size - 1)])
            parent2 = int(list_parent[random.randint(0, list_parent.size - 1)])
            chr_parent1, chr_parent2 = all_ind[parent1], all_ind[parent2]
            if not (chr_parent1 == chr_parent2).all():
                flag = 1

        "Croisement"
        rdm = random.random()
        if rdm <= proba_cross:
            enfant1, enfant2 = cross_over(chr_parent1, chr_parent2, nb_trailer)
            if c_enfant < nb_enfant:
                all_enfant[c_enfant] = enfant1
                c_enfant += 1
            if c_enfant < nb_enfant:
                all_enfant[c_enfant] = enfant2
                c_enfant += 1

        "Mutation"
        rdm = random.random()
        if rdm <= proba_mut:
            enfant1, enfant2 = mutation(chr_parent1, chr_parent2, nb_trailer)
            if c_enfant < nb_enfant:
                all_enfant[c_enfant] = enfant1
                c_enfant += 1
            if c_enfant < nb_enfant:
                all_enfant[c_enfant] = enfant2
                c_enfant += 1

    # print(all_enfant)
    return all_enfant


def cross_over(chr_parent1, chr_parent2, nb_trailer):
    enfant1, enfant2 = np.zeros(nb_trailer * 2), np.zeros(nb_trailer * 2)

    "selection des points de découpe"
    pt_cross1 = random.randint(1, nb_trailer - 1)  # evite d'avoir la limite sur une extremite
    pt_cross2 = random.randint(pt_cross1 + 1, nb_trailer)

    "copie la partie inchangée aux enfants"
    for i in range(pt_cross1, pt_cross2):
        enfant1[i + nb_trailer], enfant2[i + nb_trailer] = chr_parent1[i + nb_trailer], chr_parent2[i + nb_trailer]

    "reconstruit le reste de l enfant1 avec parent 2"
    j = 0
    for i in range(nb_trailer):
        if not (chr_parent2[i + nb_trailer] in enfant1[:]):
            enfant1[j + nb_trailer] = chr_parent2[i + nb_trailer]
            j += 1
            if j == pt_cross1:
                j = pt_cross2

    "reconstruit le reste de l enfant2 avec parent 1"
    j = 0
    for i in range(nb_trailer):
        if not (chr_parent1[i + nb_trailer] in enfant2[:]):
            enfant2[j + nb_trailer] = chr_parent1[i + nb_trailer]
            j += 1
            if j == pt_cross1:
                j = pt_cross2

    "refait la premier partie des enfants (partie ordre des portes)"
    for i in range(nb_trailer):
        enfant1[i], enfant2[i] = chr_parent1[i], chr_parent2[i]

    # print(parent1, enfant1)
    # print(parent2, enfant2)
    return enfant1, enfant2


def mutation(chr_parent1, chr_parent2, nb_trailer):
    pt_mut1, pt_mut2 = random.sample(range(nb_trailer, 2 * nb_trailer), 2)
    # print(pt_mut1, pt_mut2)

    enfant1, enfant2 = chr_parent1, chr_parent2
    enfant1[pt_mut1], enfant1[pt_mut2] = chr_parent1[pt_mut2], chr_parent1[pt_mut1]
    enfant2[pt_mut1], enfant2[pt_mut2] = chr_parent2[pt_mut2], chr_parent2[pt_mut1]
    # print(enfant1, enfant2)

    return enfant1, enfant2


"------------------------------------ Trie les individus et garde les meilleurs ---------------------------------------"


def trie_coupe(fv, all_ind, fv_enfant, all_enfant, nb_trailer):
    a = len(fv)
    fv, all_ind = np.concatenate([fv, fv_enfant]), np.concatenate([all_ind, all_enfant])

    "trie selon la FV"
    all_ind, fv = trie(fv, nb_trailer, all_ind)

    " Garde les meilleurs individus selon leurs FV "
    fv, all_ind = fv[:a], all_ind[:a]
    return fv, all_ind


def trie(fv, nb_trailer, all_ind):
    """ Trie selon la FV """
    for i in range(len(fv)):
        mini = i
        for j in range(i + 1, len(fv)):
            if fv[j] < fv[mini]:
                mini = j
        fv[i], fv[mini] = fv[mini], fv[i]
        for j in range(2 * nb_trailer):
            all_ind[i, j], all_ind[mini, j] = all_ind[mini, j], all_ind[i, j]
    return all_ind, fv


" =========================================== Iterations =============================================================="


def iteration(max_iter, nb_enfant, proba_cross, proba_mut, nb_trailer, nb_porte, nb_cmd,
              u, tc, q, ub, lb, beta, d, gamma, all_ind, fv, qte, nb_parent_wheel, nb_parent_tournoi):
    c_iter = 0
    while c_iter < max_iter:
        "------------------------------------------ selection des individu pour la reproduction -----------------------"
        """list_parent = select_parent_rdm(nb_parent)"""
        list_parent = selection_parent(nb_enfant, nb_parent_wheel, nb_parent_tournoi)

        " ---------------------------------------- croisement et mutation ---------------------------------------------"
        all_enfant = cross_mut(list_parent, nb_enfant, all_ind, proba_cross, proba_mut, nb_trailer)
        # print('\n', "all_enfant", '\n', all_enfant)

        " --------------------------------------- FV des nouveaux individus -------------------------------------------"
        fv_enfant = fitness_function(nb_porte, nb_trailer, nb_cmd, all_enfant, nb_enfant, u, tc, q, ub, lb, beta, d,
                                     gamma, qte)
        # print('\n', "fv_enfant", '\n', fv_enfant)

        " ---------------------------------------- Trie les individus -------------------------------------------------"
        fv, all_ind = trie_coupe(fv, all_ind, fv_enfant, all_enfant, nb_trailer)

        " ---------------------------------------- Affichage du resultat de l'iteration -------------------------------"
        print("Iteration :", c_iter + 1, "of", max_iter, "--- FV :", fv[0], "--- Combinaison :", all_ind[0, nb_trailer:]
              )
        c_iter += 1

    " ----------------------------------------- Affiche le meilleur individu ------------------------------------------"
    # print(fv, '\n', all_ind)
    # print("\n")
    hours = int(fv[0]/60)
    minutes = (int(fv[0])) - hours*60
    seconds = round((fv[0]-int(fv[0]))*60, 3)
    best = ("%dh %02dm %06.3fs" % (hours, minutes, seconds))

    print("_______________________________________________________________________________")
    print("Meilleur combinaison    :", all_ind[0, nb_trailer:])
    print("Temps obtenue           :", best)

    return fv, all_ind
