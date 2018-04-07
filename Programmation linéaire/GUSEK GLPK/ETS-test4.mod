# Modele mathematique

# Indices-----------------------------------------------------------------------------------------------------
param M ;                                       # M nb portes indicés par m
param J ;                                       # J nb trailer indicés par j
param P ;                                       # P nb de commandes total indicé par p
#param R ;                                       #rang maxi (=capacité max du plus gros camion)

# Input parameters------------------------------------------------------------------------------------------
param d{(m,mp) in (1..M) cross (1..M)};         # distance entre les portes m et m'
param Tc;                                       # temps de changeover
param Q;                                        # grand nombre
param beta{p in 1..P};                          # ordre de déchargement
param U{j in 1..J, p in 1..P};                  # set de palette décharge
param L{j in 1..J, p in 1..P};                  # set de palette chargé ds trailer j en r ème
param A{j in 1..J};                             # date d'arrivée du trailer j
param D{j in 1..J};                             # date de départ du trailer j 
param gamma{p in 1..P,pp in 1..P};              # 1 if for pallet p and pp loaded onto the same trailer, p is loaded before pp

# Decision variables-----------------------------------------------------------------------------------------
var Cmax, >=0;                                  # Makespan
var a{j in 1..J}, >=0;                          # Assignement time of trailer j
var c{j in 1..J}, >=0;                          # Completion time of trailer j
var lambda{p in 1..P}, >=0;                     # time when moving of pallet p starts
var mu{p in 1..P}, >=0;                         # time when moving of pallet p is completed
var sigma{p in 1..P}, >=0;                      # time when loading of pallet p is completed
var delta{p in 1..P,pp in 1..P}, binary;        # 1 if for pallet p and pp loaded onto the same staging area, p is moved before pp
var x{j in 1..J,m in 1..M}, binary;             # 1 if trailer j is assigned to door m
var y{j in 1..J,jp in 1..J}, binary;            # 1 if for trailer j and jp assigned to the same door, j precedes jp
var v{j in 1..J,m in 1..M,jp in 1..J,mp in 1..M}, binary; # 1 if trailer j is assigned to door m AND trailer jp is assigned to door mp



#=============== Modele ====================================================================
minimize z: Cmax;

# 1) 1 camion/porte
s.t. c1 {j in 1..J} : sum{m in 1..M} x[j,m]=1;

# 2) respect des horaire pour 2 camions succesifs à une meme porte
s.t. c2 {(j,jp) in (1..J)cross(1..J): j<>jp}: a[jp]>=c[j]+Tc-Q*(1-y[j,jp]);

# 3) Tps déch. de palette p >= Tps arrivé camion + tps déch. Palettes avant p
s.t. c3 {j in 1..J,p in 1..P: U[j,p]=1}: lambda[p]>=a[j]+beta[p];

# 4) Chargement commence quand le trailer est arrive
s.t. c4 {p in 1..P, j in 1..J: L[j,p]=1}: lambda[p]>=a[j];

# 5) debute un deplacement que si la palette stocke avant a ete deplace
s.t. c5 {(p,pp) in (1..P)cross(1..P),(j,jp) in (1..J)cross(1..J),(m,mp) in (1..M)cross(1..M): p<>pp and U[j,p]=1 and L[jp,p]=1} : lambda[pp]>=lambda[p]+2*d[m,mp]*v[j,m,jp,mp]-Q*(1-delta[p,pp]);

# 6) tps fin deplacement palette >= tps de prise + tps deplacement
s.t. c6 {p in 1..P, (j,jp) in (1..J)cross(1..J),(m,mp) in (1..M)cross(1..M):U[j,p]=1 and L[jp,p]=1}: mu[p]>=lambda[p]+d[m,mp]*v[j,m,jp,mp];

# 7) tps de fin de chargement d'un palette dans un trailer
s.t. c7 {p in 1..P}: sigma[p]>=mu[p]+1;

# 8) On charge un trailer qu'après avoir decharge toutes les palettes qui devaient l'être
s.t. c8 {(p,pp) in (1..P)cross(1..P), j in 1..J: L[j,p]=1 and U[j,p]<>0}: sigma[p]>=a[j]+max(beta[pp],pp)+1;

# 9) Respect de l'ordre de chargement
s.t. c9 {(p,pp) in (1..P)cross(1..P), j in 1..J:p<>pp and L[j,p]=1 and L[j,pp]=1}: sigma[pp]>=sigma[p]+1-Q*(1-gamma[p,pp]);

# 10) date de sortie d'un trailer >= temps de chargement de sa dernière palette
s.t. c10 {p in 1..P, j in 1..J: L[j,p]=1}: c[j]>=sigma[p];

# 11) Makespan >= date de sortie du dernier trailer
s.t. c11 {j in 1..J}: Cmax>=c[j];

# 12) Evite les problèmes d'ordre dans les trailers (in et out)
s.t. c12 {(j,jp) in (1..J)cross(1..J),mp in (1..M): j<>jp }: y[j,jp]+y[jp,j]= sum{m in 1..M} v[j,m,jp,mp];

# 13) Evite les problèmes d’ordres dans les palettes déchargées
s.t. c13 {(p,pp) in (1..P)cross(1..P),(j,jp) in (1..J)cross(1..J),mp in (1..M):p<>pp and U[j,p]=1 and U[jp,pp]=1}: delta[p,pp]+delta[pp,p]= sum{m in 1..M} v[j,m,jp,mp];

# 14) 15) Respect de l’ordre de chargement pour des palettes chargées dans le même trailer
s.t. c14 {(p,pp) in (1..P)cross(1..P), j in 1..J: p<>pp and L[j,p]=1 and L[j,pp]=1}: gamma[p,pp]>=(mu[pp]-mu[p])/Q;
s.t. c15 {(p,pp) in (1..P)cross(1..P), j in 1..J: p<>pp and L[j,p]=1 and L[j,pp]=1}: gamma[p,pp]<=1+(mu[pp]-mu[p])/Q;

# 16) 17) 18) Enlève la non-linéarité des x
s.t. c16 {(j,jp) in (1..J)cross(1..J),(m,mp) in (1..M)cross(1..M)}: v[j,m,jp,mp] <= x[j,m];
s.t. c17 {(j,jp) in (1..J)cross(1..J),(m,mp) in (1..M)cross(1..M)}: v[j,m,jp,mp] <= x[jp,mp];
s.t. c18 {(j,jp) in (1..J)cross(1..J),(m,mp) in (1..M)cross(1..M)}: v[j,m,jp,mp] >= x[j,m]+x[jp,mp]-1;

# 19) date d'arrivée
s.t. c19 {j in 1..J}:a[j]>=A[j];

# 20) date départ
s.t. c20 {j in 1..J}:c[j]<=D[j];

/*# 21) essai pour la préemption
s.t. c21 {r in 1..R,j in 1..J, p in 1..P: p=U[j,r] }: lambda[p]>=Q*(1-sum{m in 1..M} x[j,m]);*/



solve;


# Affiche les resultats -------------------------------------------------------------------------------------
display Cmax;
display {(j,jp) in (1..J)cross(1..J)} y[j,jp];

printf "\n\n";
for {j in 1..J} printf "%7d",c[j];

printf "\n\n";
for {p in 1..P} printf "%7d",lambda[p];
printf "\n\n";
for {p in 1..P} printf "%7d",sigma[p];
printf "\n\n";
for {p in 1..P} printf "%7d",mu[p];

printf "\n\n";
for{j in 1..J}
	{printf {m in 1..M} "%7d",x[j,m]; printf "\n";}

display {(j,jp) in (1..J)cross(1..J),(m,mp) in (1..M)cross(1..M)} v[j,m,jp,mp];

printf "\n\n";
for{p in 1..P}
	{printf {pp in 1..P} "%7d",delta[p,pp]; printf "\n";}
printf "\n\n";
for{p in 1..P}
	{printf {pp in 1..P} "%7d",gamma[p,pp]; printf "\n";}




# Data -------------------------------------------------------------------------------------------------------
data;
param M:=4;                    # nb de porte
param J:=6;                    # nb de trailer
param P:=10;                   # nb de palettes
param Tc:=5;                  # temps de changeover
param Q:=70;                  # grand nombre
/*param d : 1 2 :=               # distance de la porte m vers mp
		1 0 1
		2 1 0;*/
param d: 1 2 3 4 :=
	   1 0 1 2 3
	   2 1 0 1 2
	   3 2 1 0 1
	   4 3 2 1 0;
param beta := 1 2              # ordre de déchargement (1er col : palette p ; 2e col : ordre)
			  2 1
			  3 2
			  4 1
			  5 1
			  6 1
			  7 2
			  8 2
			  9 1
			  10 1; 
param U : 1 2 3 4 5 6 7 8 9 10:=           # Position des palettes dans les trailers entrants
		1 0 0 0 0 0 1 0 1 0 0
		2 0 1 0 0 0 0 0 0 0 0
		3 0 0 0 0 1 0 0 0 0 0
		4 1 0 0 0 0 0 0 0 0 1
		5 0 0 0 1 0 0 1 0 0 0
		6 0 0 1 0 0 0 0 0 1 0;
param L : 1 2 3 4 5 6 7 8 9 10:=           # Position des palettes dans les trailers sortants
		1 0 1 0 1 0 1 0 1 0 0
		2 0 0 0 0 0 0 1 0 0 0
		3 0 0 0 0 1 0 0 0 1 0
		4 1 0 0 0 0 0 0 0 0 0
		5 0 0 0 0 0 0 0 0 0 1
		6 0 0 1 0 0 0 0 0 0 0;
param gamma : 1 2 3 4 5 6 7 8 9 10:=
			1 0 0 0 0 0 0 0 0 0 0 
			2 0 0 0 0 0 1 0 0 0 0
			3 0 0 0 0 0 0 0 0 0 0
			4 0 1 0 0 0 0 0 0 0 0
			5 0 0 0 0 0 0 0 0 1 0
			6 0 0 0 0 0 0 0 0 0 0
			7 0 0 0 0 0 0 0 0 0 0
			8 0 0 0 1 0 0 0 0 0 0
			9 0 0 0 0 0 0 0 0 0 0
			10 0 0 0 0 0 0 0 0 0 0;
param A := 1 0 2 0 3 0 4 0 5 0 6 0;        # Heure d'arrivé des trailers (trailer j *espace* Heure)
param D := 1 100 2 100 3 100 4 100 5 100 6 100;  # Heures de départs des trailers


end;

