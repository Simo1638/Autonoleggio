import csv

FILE_INPUT = "auto.csv"


def lettura():
    try:
        with open(FILE_INPUT, 'r', encoding='UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            info=[]
            for row in csv_reader:
                info.append(row)
            return info
    except IOError:
        print("file auto.csv not found!")


def disponibilita(info, scelta_auto):
    n=0
    disponibili=[]
    for i in range(len(info)):
        if str(info[i][0])==str(scelta_auto[0]):
            if str(info[i][3+int(scelta_auto[1])])=='L' and str(info[i][3+int(scelta_auto[2])])=='L':
                n+=1
                disponibili.append(info[i])
                print(str(n)+") "+info[i][1]+' '+info[i][2]+' colore '+info[i][3])
    scelta = int(input("Quale vuoi prenotare?: "))
    scelta = disponibili[scelta-1]
    n1 = int(scelta_auto[1])
    n2 = int(scelta_auto[2])
    while n1<=n2:
        scelta[3+n1] = 'A'
        n1+=1

    return scelta


def main():
    info = lettura()
    char=''
    while char != 'q':

        for i in range(len(info)):
            for j in range(len(info[i])):
                print(info[i][j], end=',')
            print()
        scelta_auto = [item for item in input("Inserire categoria e giorni: ").split()]
        output = disponibilita(info, scelta_auto)
        for i in range(len(info)):
            if info[i][1] == output[1] and info[i][2] == output[2]:
                info[i] = output
        char = input("Vuoi affittare altro? Altrimenti premi q per uscire")

main()

