# Author: JD 01/12/2022

def add_linit(names,linit):

    x = 0
    for irow, row in enumerate(names):
        for iseat, seat in enumerate(row):
            names[irow][iseat] += " "+ linit[x] + "."
            x += 1
    return names


last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

rows = add_linit(rows, last_initials)

print(rows)
