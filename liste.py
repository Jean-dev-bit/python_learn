# Exercice 1
# Une fonction qui permet de trouver 
# la plus grande entre une liste de chaîne de caractères
def longue_chaines(liste_chaines):
    if not liste_chaines:
        return None
    plus_longues_chaines = max(liste_chaines, key=len)
    
    return plus_longues_chaines

# La liste composé de 3 chaînes de caractères

liste = ["Salomon", "Jean-Pierre", "Aimé GBADESSI", "TCHANGO", "TOTO VA", "Giresse", "Christophe"]

# L'opértation pour trouver la chaînes la plus longue
listlong = longue_chaines(liste)

print(listlong)

# Exercice 2

# Une fonction qui permet de trouver les nombres pairs
new_liste = []
def nbpaires(nb_liste):
    if not nb_liste:
        return None
    else:
        for nb in nb_liste:
            if nb % 2 == 0:
                ajout = nb
                new_liste.append(ajout)
        
        
    print(new_liste)      




liste = [2,14,17,18,21,54,65,98,48,11,441,144,15,85,78,86,100]
res = nbpaires(liste)

# Exercice 4

# Une fonction qui permet de trouver les nombres pairs
new_list = []
def maj(nb_list):
    for chaine in nb_list :
        if chaine[0].isupper() :
            add = chaine
            new_list.append(add)
    
    print(new_list)   
 
 
list_maj = ["ChatGPT", "Bénin", "openAi", "Bonjour","maman","Papa","grand-frere"]
res = maj(list_maj)

# Exercice 6 
newList = []

def newListe(Liste1, Liste2):
    for int1 in Liste1 :
        for int2 in Liste2:
            if int1 == int2:
                newList.append(int1)
    print(newList)            
    

List1 = [1, 2, 9, 18,50,65,19] 
List2 = [1, 12, 10, 22,2,18,9]     
result = newListe(List1,List2)

# Exercice sur les objets
