
#! challenge 1-1


First_dict = { "Appareil": "Laptop", "Marque": "IBM", "Carte mère": "MSI Z490", "Carte Graphique":"GeForce RTX 3070", "RAM": "16G", "Processeur": "Intel core i7-G11", "SSD": "1 To" } 


# print("*********  Q°1   **********")

# First_dict["RAM"] = "32G"


# print("*********  Q°3  **********")

# print(list(First_dict.keys()))
# print("*********  Q°4   **********")
# print(list(First_dict.values()))
# print("*********  Q°5   **********")
# print(list(First_dict.items()))


# ! Q°6 first try reverse the key and value

# if "Processeur" in First_dict:
#     pross = First_dict.pop("Processeur")
#     First_dict[pross] = "Processeur"

# if "Carte Graphique" in First_dict:
#     cg = First_dict.pop("Carte Graphique")
#     First_dict[cg] = "Carte Graphique"


# ! *******************

# for i in list(First_dict.keys()) :
#     if i=='Processeur' or i=='Carte Graphique':
#         pross = First_dict.pop(i)
#         First_dict[pross] = i
# print(list(First_dict.items()))

# print(First_dict)


# !  Q°7
# First_dict["Système d’exploitation"] = "Windows 10"


# print(First_dict)

#! challenge 1-2
notes_eleves = {
    "Amine": 15.5,
    "Yassine": 19.0,
    "Reda": 14.2,
    "Malak": 8.7,
    "Manal": 20.0,
    "Ahmed": 7.5,
    "Saad": 11.3,
    "Hannae": 9.8
}

etudiantAdmis= {}
etudiantNonAdmis= {}


for nom ,note in  notes_eleves.items() : 
    if note > 10 :
        etudiantAdmis[nom]= note
    else:
        etudiantNonAdmis[nom]= note
 

print(list(etudiantAdmis.items()))

print(list(etudiantNonAdmis.items()))

