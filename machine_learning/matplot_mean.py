#python matplot
import matplotlib.pyplot as plt

def mean(sampleset):
    total = 0
    for element in sampleset:
        total = total + element
    return total / len(sampleset)

myset = [2., 10., 3., 6., 4., 6., 10.]
mymean = mean(myset)
plt.plot(myset)
plt.plot([mymean]*7)
plt.show()