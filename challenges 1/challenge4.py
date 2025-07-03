

mon_dict = {
    "Aziz": 5,
    "Kamal": 2,
    "Hicham": 7,
    "Achraf": 1
}

cles = list(mon_dict.keys())

for i in range(len(cles)):
    for j in range(i + 1, len(cles)):
        if mon_dict[cles[i]] > mon_dict[cles[j]]:
            temp = cles[i]
            cles[i] = cles[j]
            cles[j] = temp

dictionnaire_trie = {}
for cle in cles:
    dictionnaire_trie[cle] = mon_dict[cle]

print(dictionnaire_trie)
