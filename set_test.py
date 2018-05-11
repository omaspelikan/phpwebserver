import matplotlib.pyplot as plt #Import the plot library.
def mean(sampleset):  #Definition header for the mean function
    total=0
    for element in sampleset:
        total=total+element
    return total/len(sampleset)
myset=[2.,10.,3.,6.,4.,6.,10.]  #We create the data set
mymean=mean(myset) #Call the mean funcion
plt.plot(myset)  #Plot the dataset
plt.plot([mymean] * 7)  #Plot a line of 7 points located on the mean