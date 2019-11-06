import matplotlib.pyplot as plt, numpy as np
def graphs(data):
    time = []
    temp = []
    prec = []
    mintemp = 0
    maxtemp = 0
    for i in range(len(data)):
        if i != 0:
            present = data[i]
            time.append(present[1])
            tem = int(present[2])
            temp.append(tem)
            prec.append(present[3])
            if i == 1:
                mintemp = tem
                maxtemp = tem
            else:
                if tem < mintemp:
                    mintemp = tem
                if tem > maxtemp:
                    maxtemp = tem
    for i in range(2):
        plt.plot(time, temp)
        plt.xticks(rotation=270)
        plt.ylabel('Temperature')
        plt.xlabel('Hours')
        plt.title('Temperature for each hours')
        if i == 1:
            plt.yticks(np.arange(0, maxtemp+5, 5))
            plt.savefig('TempZoomedOut.png')
        else:
            plt.yticks(np.arange(mintemp, maxtemp+1, 1))
            plt.savefig('TempZoomedIn.png')
