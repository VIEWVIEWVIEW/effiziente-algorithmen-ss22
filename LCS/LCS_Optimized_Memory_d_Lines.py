import os
import sys
import time
import math

def lcs_length(string_1, string_2, d):
    """lcs implementation nach Cormen et al p. 397"""
    """Änderung: Zwischenspeicherung von d Zeilen"""
    m = len(string_1)
    n = len(string_2)

    b = [[0 for i in range(n+1)] for j in range(2)]
    c = [[0 for i in range(n+1)] for j in range(2)]
    cb = [[0 for i in range(n+1)] for j in range(m // d+1)]
    bb = [[0 for i in range(n+1)] for j in range(m // d+1)]

    rowIndex = 0
    cbRow = 1
    cbCnt = 1

    for i in range(1, m+1):
        if(rowIndex == 0):
            rowIndex = 1
        else:
            rowIndex = 0

        for j in range(1, n+1):
            if string_1[i-1] == string_2[j-1]:
                c[rowIndex][j] = c[1-rowIndex][j-1] + 1
                b[rowIndex][j] = '\\'
            elif c[rowIndex-1][j] >= c[rowIndex][j-1]:
                c[rowIndex][j] = c[1-rowIndex][j]
                b[rowIndex][j] = '|'
            else:
                c[rowIndex][j] = c[rowIndex][j-1]
                b[rowIndex][j] = '-'

            if cbCnt % d == 0:
                cb[cbRow][j] = c[rowIndex][j]
                bb[cbRow][j] = b[rowIndex][j]
                if j == n:
                    cbRow += 1
        cbCnt+=1
    return c[rowIndex][n], cb, bb

def print_lcs_reconstruct(cb, bb, string_1, string_2, d):
    cbRow = len(cb)
    m = len(string_1)
    n = len(string_2)
    mIndex = m-1
    indexJ = n
    lcsStr = ""

    # Schleife durchläuft alle Blöcke
    while cbRow > 0:
        lenRowGroup = 0
        if cbRow == len(cb) and (m+1) % d > 0:
            lenRowGroup = (m+1) % d
        else:
            lenRowGroup = d

        b = [[0 for i in range(n+1)] for j in range(lenRowGroup)]
        c = [[0 for i in range(n+1)] for j in range(lenRowGroup)]

        # Backup Zeilen in neuen Block einfügen
        for i in range(n+1):
            c[0][i] = cb[cbRow-1][i]

        for i in range(n+1):
            b[0][i] = bb[cbRow-1][i]

        # Rekonstruktion des neuen Blocks anhand der Backup-Zeile
        mIndex =  (cbRow-1) * d 
        for i in (range(1,lenRowGroup)):
            for j in range(1, n+1):
                if string_1[mIndex] == string_2[j-1]:
                    c[i][j] = c[i-1][j-1] + 1
                    b[i][j] = '\\'
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = '|'
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = '-'
            mIndex += 1

        # Block auswerten und Ergebnis-String aktualisieren
        i = lenRowGroup-1
        while i >= 0 and indexJ != 0:
            if b[i][indexJ] == '\\':
                lcsStr += string_2[indexJ-1]
                i -=1
                indexJ -= 1
            elif b[i][indexJ] == '|':
                i -= 1
            else:
                indexJ -= 1
        cbRow -= 1

    # Ergebnis-String rückwärts ausgeben
    print(lcsStr[::-1])


###### Konfiguration ######
sys.setrecursionlimit(18000)

#path1 = "E:\Google Drive\Studium\Kurse\Effiziente Algorithmen\Skripte\LCS\\tomate-virus.txt"
#file_1 = open(path1, "r")
#stripped_1 = ''.join([line.rstrip('\n') for line in file_1])

#path2 = "E:\Google Drive\Studium\Kurse\Effiziente Algorithmen\Skripte\LCS\\chrysovirus.txt"
#file_2 = open(path2, "r")
#stripped_2 = ''.join([line.rstrip('\n') for line in file_2])

#d = round(math.sqrt(len(stripped_2) + 1)) # d=runden(wurzel(n+1))
#print("d: ",d)

###### Start Messung ######
#bench_start = time.time()
#lenLCS, cb, bb = lcs_length(stripped_1, stripped_2, d)
#print("Length:", lenLCS)

#print_lcs_reconstruct(cb, bb, stripped_1, stripped_2, d)
#print("\nDone!")
#bench_end = time.time()
#print('Laufzeit: {:.4f}s'.format(bench_end - bench_start))
###### Ende Messung ######
