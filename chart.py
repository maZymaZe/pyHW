import matplotlib.pyplot as plt
from  InputData import  input_data
def chart():
    data=input_data()
    y=[data[i] for i in range(1,30)]
    x=[str(i) for i in range(1,30)]
    plt.title("new patients in CN in each day of Febrary")
    plt.xlabel("date")
    plt.ylabel("number of new patients")
    plt.axis([0,31,0,16000])
    plt.plot(x,y,"b")
    plt.show()
