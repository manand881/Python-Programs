from math import *
import matplotlib.pyplot    as plt

V=float(input("Enter Input Voltage: "))
R=float(input("Enter Input Resistance: "))
t=float(input("Enter Time Period: "))
L=float(input("Enter Inductance Value: "))

start   =   0.0
Step    =   0.01
values  =   []
time    =   []
buffer  =   0.0
tau     =   L/R

while(buffer<t):
    time.append(buffer)
    I=(V/R)*(1-e**((-R*buffer)/L))
    values.append(I)
    buffer+=Step

# t = int(t)
# for x in range(0,t,Step):
#     time.append(x)
#     I=(V/R)*(1-e**((-R*x)/L))
#     values.append(I)



plt.plot(time,values,'b.')
plt.title ("Time Vs Current")
plt.xlabel('Time', fontsize=10)
plt.ylabel('Current', fontsize=10)
# plt.axvspan(values[0], tau, ymax=0.63*I, alpha=0.5, color='red')
plt.show()