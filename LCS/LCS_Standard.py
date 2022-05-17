import os
import sys
import time

sys.setrecursionlimit(180000)

def lcs_length(string_1, string_2):
    """lcs implementation nach Cormen et al p. 397"""
    m = len(string_1)
    n = len(string_2)

    # b[1..m][1..n]
    b = [[0 for x in range(n+1)] for x in range(m+1)]
    # c[0..m][0..n]
    c = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(1, m+1):
        c[i][0] = 0

    for j in range(0, n+1):
        c[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if string_1[i-1] == string_2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '\\'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '|'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '-'

    return c, b


def print_lcs(b, string_1, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == '\\':
        print_lcs(b, string_1, i-1, j-1)
        print(string_1[i-1], end='')
    elif b[i][j] == '|':
        print_lcs(b, string_1, i-1, j)
    else:
        print_lcs(b, string_1, i, j-1)



###### Konfiguration ######
#sys.setrecursionlimit(18000)
def main():
    path1 = "./tomate-virus.txt"
    file_1 = open(path1, "r")
    stripped_1 = ''.join([line.rstrip('\n') for line in file_1])
    #
    path2 = "botryosphaeria_dothidea_chrysovirus_1_uid382570.txt"
    file_2 = open(path2, "r")
    stripped_2 = ''.join([line.rstrip('\n') for line in file_2])

    ###### Start Messung ######
    bench_start = time.time()
    c, b = lcs_length(stripped_1, stripped_2)
    print("Length:", c[len(stripped_1)][len(stripped_2)])

    print_lcs(b, stripped_1, len(stripped_1), len(stripped_2))
    print("\nDone!")
    bench_end = time.time()
    print('Laufzeit: {:.4f}s'.format(bench_end - bench_start))
    ###### Ende Messung ######

if __name__ == '__main__':
    main()
