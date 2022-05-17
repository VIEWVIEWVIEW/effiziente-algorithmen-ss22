import os
import sys

def lcs_length(string_1, string_2):
    """lcs implementation nach Cormen et al p. 397"""
    """Änderung: Zwischenspeicherung von 2 Zeilen"""
    m = len(string_1)
    n = len(string_2)

    l = [[0 for i in range(n+1)] for j in range(2)]

    rowIndex = 0
    for i in range(1,m+1):
        if(rowIndex == 0):
            rowIndex = 1
        else:
            rowIndex = 0

        for j in range(1,n+1):
            if string_1[i-1] == string_2[j-1]:
                l[rowIndex][j] = l[1-rowIndex][j-1] + 1
            elif l[rowIndex-1][j] >= l[rowIndex][j-1]:
                l[rowIndex][j] = l[1-rowIndex][j]
            else:
                l[rowIndex][j] = l[rowIndex][j-1]

    return l[rowIndex][n]


def main():
    path1 = "E:\Google Drive\Studium\Kurse\Effiziente Algorithmen\Skripte\LCS\\tomate-virus.txt"
    file_1 = open(path1, "r")
    stripped_1 = ''.join([line.rstrip('\n') for line in file_1])

    path2 = "E:\Google Drive\Studium\Kurse\Effiziente Algorithmen\Skripte\LCS\\chrysovirus.txt"
    file_2 = open(path2, "r")
    stripped_2 = ''.join([line.rstrip('\n') for line in file_2])

    print("Length:", lcs_length(stripped_1, stripped_2))
    print("\nDone!")


if __name__ == '__main__':
    sys.setrecursionlimit(18000)
    main()
