import matplotlib.pyplot as plt 
import numpy as np
x = range(0, 10)
# y1 = [16037, 
#     (248264 + 16037) / 2, 
#     (1826 + 248264 + 16037) / 3, 
#     (81771 + 1826 + 248264 + 16037) / 4, 
#     (2920 + 1826 + 248264 + 16037 + 81771) / 5, 
#     (3963 + 2920 + 1826 + 248264 + 16037 + 81771) / 6, 
#     (4018 + 2920 + 1826 + 248264 + 16037 + 81771 + 3963) / 7, 
#     (50523 + 4018 + 2920 + 1826 + 248264 + 16037 + 81771 + 3963) / 8, 
#     (75075 + 50523 + 4018 + 2920 + 1826 + 248264 + 16037 + 81771 + 3963) / 9, 
#     (4369 + 75075 + 50523 + 4018 + 2920 + 1826 + 248264 + 16037 + 81771 + 3963) / 10]

# y2 = [750490, 
#     (1336 + 750490) / 2, 
#     (5967 + 1336 + 750490) / 3, 
#     (909 + 5967 + 1336 + 750490) / 4, 
#     (122844 + 909 + 5967 + 1336 + 750490) / 5, 
#     (4844 + 122844 + 909 + 5967 + 1336 + 750490) / 6, 
#     (3309 + 4844 + 122844 + 909 + 5967 + 1336 + 750490) / 7 , 
#     (1714 + 3309 + 4844 + 122844 + 909 + 5967 + 1336 + 750490) / 8, 
#     (224143 + 1714 + 3309 + 4844 + 122844 + 909 + 5967 + 1336 + 750490) / 9, 
#     (57975 + 224143 + 1714 + 3309 + 4844 + 122844 + 909 + 5967 + 1336 + 750490) / 10]
#flat
y1 = [2391, 1877, 759, 4297, 2994, 4600, 1028, 2367, 4395, 1169]
#hill
y2 = [6616, 8350, 5628, 6825, 1067, 236, 10868, 5243, 989, 42904]
#forest
y3 = [50586, 96395, 10650, 650, 2357, 2262, 85425, 189, 9099, 387492]
#cave
y4 = [1302149, 204, 711213, 3672, 758, 2343, 942629, 1241474, 190058, 7432]

#u = np.subtract(y,z)

y1avg = []
y2avg = []
y3avg = []
y4avg= []

y1avg.append(y1[0])
y2avg.append(y2[0])
y3avg.append(y3[0])
y4avg.append(y4[0])
for i in range(1, 10):
    y1avg.append(y1avg[i-1] + y1[i])
    y2avg.append(y2avg[i-1] + y2[i])
    y3avg.append(y3avg[i-1] + y3[i])
    y4avg.append(y4avg[i-1] + y4[i])
print(y4avg)

for i in range(10):
    y1avg[i] /= (i+1)
    y2avg[i] /= (i+1)
    y3avg[i] /= (i+1)
    y4avg[i] /= (i+1)
print(y4avg)


plt.plot(x, y1avg, label = "Flat" )
plt.plot(x, y2avg, label = "Hill" )
plt.plot(x, y3avg, label = "Forest" )
plt.plot(x, y4avg, label = "Cave" )
plt.xlabel(' Number of Maps ')
plt.ylabel(' Average of Total Score ')
plt.title(' Comparison of Average Total Scores of the Terrain (Basic Agent 1)')
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
plt.yticks(np.arange(0, 1500000, 100000))
plt.legend()
plt.show()