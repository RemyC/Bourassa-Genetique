from utils_data import *
from utils_GA import *
import time
import winsound

start1 = time.time()
start = time.time()

' ------------------------------------------ Donnees du probleme -----------------------------------------------------'
'Choisir entre : 1-scenario, 2-aleatoire, 3-csv'
data = 1.02
nb_porte, nb_cmd, tc, nb_dech, nb_mont, aleatoire, u, l, qte, choix_porte = read_data(data)

'------------------------------------------- Creation des autres données du problème ---------------------------------'
d, q, u, ub, l, lb, beta, gamma, nb_trailer = create_data(nb_porte, nb_cmd, tc, nb_dech, nb_mont, aleatoire, u, l,
                                                          choix_porte)

print("u" + '\n', u)
print("l" + '\n', l)
print("qte" + '\n', qte)
print("ub" + '\n', ub)
print("lb" + '\n', lb)
print("beta" + '\n', beta)
print("gamma" + '\n', gamma)
print("d", '\n', d)
print("q", '\n', q)

end = time.time()
print("\n")
print("Donnees du probleme :", round(end - start, 3), 'secondes')


'=========================================== ALGORITHME GENETIQUE ===================================================='
' ------------------------------------------ Initialisation ----------------------------------------------------------'

nb_enfant = 5
fv, all_ind = initialisation(nb_enfant, nb_trailer, nb_porte, nb_cmd, u, tc, q, ub, lb, beta, d, gamma, qte)

' ------------------------------------------ Iterations --------------------------------------------------------------'
max_iter = 1

proba_cross = 0.8
proba_mut = 0.2

'nb_parent_wheel = 1'
'nb_parent_tournoi = 1'

nb_parent_wheel = int(nb_enfant*0.10)
nb_parent_tournoi = int(nb_enfant*0.50)

iteration(max_iter, nb_enfant, proba_cross, proba_mut, nb_trailer, nb_porte, nb_cmd, u, tc, q, ub,
          lb, beta, d, gamma, all_ind, fv, qte, nb_parent_wheel, nb_parent_tournoi)

" ------------------------------------------ Affiche le temps de calcul ----------------------------------------------"
end = time.time()
hours = int((end - start1)/3600)
minutes = int((end - start1)/60) - (hours*60)
seconds = round((end - start1) - (hours*3600) - (minutes*60), 3)
tps_cpu = ("%dh %02dm %06.3fs" % (hours, minutes, seconds))
print("Temps de calcul         :", tps_cpu)
print("_______________________________________________________________________________")
winsound.Beep(frequency=2000, duration=200)
winsound.Beep(frequency=3000, duration=400)
