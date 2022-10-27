from difflib import SequenceMatcher, get_close_matches
import re
import os


# (\d+/[0-7])|(\d+/)|(\d{5}) - mai multe numere
# (?<!\d{5})[a-zA-ZŞ-]+\W - lookbehind pe nume, cu prezentu si ora - not good
# (?<!\d{5})([a-z A-ZĂîŞ-]+\W) - lookbehind cu grup ca sa nu fie overlappuri ca sa mearga re.findall

def func_simpleSplit(data_list, colegi_group, colegi_dict, threshold):
    k = 1
    print(f'***** PREZENTA - split: {threshold} percentage *****\n')
    for one_txt in data_list:  # trace through .txt files
        x = re.split("\d+/[0-7]", one_txt)
        for c in x:  # trace through each present candidate
            for s in colegi_group:  # trace through each student from the group
                if SequenceMatcher(None, s, c).ratio() > threshold:
                    print(f'{k}: {s} has a match! from {c}')
                    k += 1
                    colegi_dict[s] += 1
    print()
    [print(key, ':', value) for key, value in colegi_dict.items()]
    func_output(colegi_group, colegi_dict, threshold, "simpleSplit")


def func_lookBehind(data_list, colegi_group, colegi_dict, threshold):
    k = 1
    print(f'***** PREZENTA - lookbehind: {threshold} percentage *****\n')
    for one_txt in data_list:  # trace through .txt files
        x = re.findall("(?<!\d{5})([a-z A-ZĂîŞ-]+\W)", one_txt)  # nu vede diacriticele
        for c in x:  # trace through each present candidate
            for s in colegi_group:  # trace through each student from the group
                if SequenceMatcher(None, s, c).ratio() > threshold:
                    print(f'{k}: {s} has a match! from {c}')
                    k += 1
                    colegi_dict[s] += 1
    print()
    [print(key, ':', value) for key, value in colegi_dict.items()]
    func_output(colegi_group, colegi_dict, threshold, "lookBehind")


def func_output(colegi_group, colegi_dict, threshold, mode):
    name = "Tusa_Laurentiu_" + mode + f'_{threshold}' + ".txt"
    v = open(name, 'w')
    v.write(f'Presence for group 30431, mode: {mode}, threshold {threshold}\n')
    for e in colegi_group:
        v.write(f'{e}: {colegi_dict[e]}\n')

    v.close()


colegi = ["GHERASIM TEODOR-SAMUEL", "BAR LUCA-NARCIS", "COSMA FELICIA IULIA", "CUPSA BOGDAN", "GATEJ NICOLAE",
             "ANTONESCU MARIA-CRISTINA", "BUZAN MEDA", "DEAC DENISA BIANCA", "CRISAN OANA ANDRA", "BUDEA PATRICK",
             "DEAC MELINDA-ANCA", "CHIRA CRISTIAN", "CORNEA MIHAI", "BUMBUC IOANA", "CURAC MIHAI - IONUT",
             "TUSA LAURENTIU", "SICOBEAN ALEXANDRA MARIA", "MARIN ANDREEA", "ZEIBEL ANTONIA", "VOICU SARA-IOANA",
             "SICHET-UNGURAS DARIUS-EMANUEL", "PISU CRISTINA", "PUSCAS OANA", "TURCSA ALEXANDRU", "OLTEAN ANDREI PETRU",
             "NALBITORU FLORIN", "SAVU COSMIN-CLAUDIU", "NEAGOI MIHAI", "RATOI RAZVAN VALERIU"]

colegi.sort()
colegi_dictionary = dict.fromkeys(colegi, 0)

#   pass through all the txt files from the given folder
data_folder = os.path.join(os.getcwd(), 'texts')
data = []  # list that hold each entry

for root, folders, files in os.walk(data_folder):
    for f in files:
        path = os.path.join(root, f)
        with open(path) as inp:
            data.append(inp.read())

data1 = data.copy()
colegi1 = colegi.copy()
colegi_dictionary1 = colegi_dictionary.copy()

data2 = data.copy()
colegi2 = colegi.copy()
colegi_dictionary2 = colegi_dictionary.copy()

data3 = data.copy()
colegi3 = colegi.copy()
colegi_dictionary3 = colegi_dictionary.copy()

func_simpleSplit(data, colegi, colegi_dictionary, 0.6)
print("--------------------------")
func_simpleSplit(data1, colegi1, colegi_dictionary1, 0.65)

print("*****************************")

func_lookBehind(data2, colegi2, colegi_dictionary2, 0.6)
print("--------------------------")
func_lookBehind(data3, colegi3, colegi_dictionary3, 0.65)
