import numpy as np
import matplotlib.pyplot as p

to = 0
tn = 300
manusia = 1000

t = np.linspace(to,tn,manusia)
h = t[2]-t[1]

N = 1000
I0 = 1
R0 = 0
S0 = N - I0 - R0

I = np.zeros(manusia)
S = np.zeros(manusia)
R = np.zeros(manusia)

I[0] = I0
R[0] = R0
S[0] = S0

beta = 0.2
gamma = 0.1

for M in range (0,manusia-1):
    S[M+1] = S[M] - h*beta/N*S[M]*I[M]
    I[M+1] = I[M] + h*beta/N*S[M]*I[M] - h*gamma*I[M]
    R[M+1] = R[M] + h*gamma*I[M]

p.plot(t,S,label = 'S')
p.plot(t,I,label = 'I')
p.plot(t,R,label = 'R')

p.legend()
p.show()
