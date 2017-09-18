import cmath
import numpy as np
import math
from random import randint

def gate_scale(gate, ap_qubit):
    dimensions = int(math.sqrt(np.size(gate)))
    ap_qubit-=1
    if 2**qnum == dimensions:
        return gate
    else:
        iterator = 1
        kron_num = []
        identity = np.identity(dimensions, np.matrix)
        while iterator <= dimensions:
            kron_num.append(identity)
            iterator+=1
        kron_num[ap_qubit] = gate
        kron_iterator = list(range(len(kron_num)))
        for i in kron_iterator:
            if i == 0:
                x = kron_num[i]
            if i > 0:
                x = np.kron(x, kron_num[i])
        return x

def hadop(qstat, ap_qubit):
    matrix = (1/cmath.sqrt(2))*np.array([[1,1],[1,-1]])
    matrix = gate_scale(matrix, ap_qubit)
    return np.dot(matrix, qstat)

def xop(qstat, ap_qubit):
    matrix = np.array([[0,1],[1,0]])
    matrix = gate_scale(matrix, ap_qubit)
    return np.dot(matrix,qstat)

def zop(qstat, ap_qubit):
    matrix = np.array([[1,0],[0,-1]])
    matrix = gate_scale(matrix, ap_qubit)
    return np.dot(matrix,qstat)

def yop(qstat, ap_qubit):
    matrix = np.array([[0, cmath.sqrt(-1)],[-1*cmath.sqrt(-1),0]])
    matrix = gate_scale(matrix, ap_qubit)
    return np.dot(matrix,qstat)

def sqrtxop(qstat, ap_qubit):
    const1 = 1+cmath.sqrt(1)
    const2 = 1-cmath.sqrt(1)
    matrix = np.array([[const1/2,const2/2],[const2/2,const1/2]])
    matrix = gate_scale(matrix, ap_qubit)
    return np.dot(matrix,qstat)

def phaseshiftop(qstat, ap_qubit):
    phasepos = [math.pi/4, math.pi/2]
    print('pi/4 or pi/2')
    x = input("Please pick one of the two phase shifts, 0 for the first, 1 for the second: ")
    if x == "0":
        y = phasepos[0]
    elif x == "1":
        y = phasepos[1]
    const1 = cmath.sqrt(-1)*y
    matrix = np.array([[1,0],[0,math.e**const1]])
    matrix = gate_scale(matrix, ap_qubit)
    return np.dot(matrix,qstat)

#use of eval because I want the user to be able to input constants, etc - easier way to do this?
save_gates = {} #add way to access saved gates and save them for another program run
def customop(qstat, ap_qubit):
    dimension = eval(input("What are the dimensions of your (square) matrix? Please input a single number: "))
    ls = []
    for y in range(dimension): 
        for x in range(dimension):
            ls.append(float(input('What value for position ({}, {}): '.format(y+1, x+1))))
            matrix = np.matrix(np.resize(ls, (dimension, dimension)))
    #check if matrix is unitary
    if np.array_equal(np.dot(matrix, matrix.conj().T), np.identity(dimension)) == True:
        save = input('would you like to save this gate for future use? y or n: ')
        if save == 'y':
            save_name = input('what would you like to save the gate as (a name): ')
            save_gates[save_name] = matrix
        matrix = gate_scale(matrix, ap_qubit)
        return np.dot(matrix, qstat)
    else:
        print("matrix not unitary, pretending none was applied")
        return qstat

def cnot(qstat, ap_qubit):
    matrix = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    matrix = gate_scale(matrix, ap_qubit)
    return np.dot(matrix,qstat)

def probability(qstat, n): #fix to handle larger state vectors (see printing)
    if n == 0:
        return (qstat[0])**2
    elif n == 1:
        return (qstat[-1])**2

def measurement(qstat, ap_qubit): #fix to handle larger state vectors
    prob1 = probability(qstat,0)
    prob2 = probability(qstat,1)
    random = randint(0,1)
    if random <= prob1:
        qstat = np.array([0,1])
    elif prob1 < random:
        qstat = np.array([1,0])
    return qstat

qnum = int(input("how many qubits: "))
zero_state = np.matrix([[1],[0]])
one_state = np.matrix([[0],[1]])
z_or_o = input('would you like to start in the 0 or 1 state: ')
iterate = 1
while iterate <= qnum:
    if iterate == 1:
        if z_or_o == '0':
            x = zero_state
        elif z_or_o == '1':
            x = one_state
    if iterate == qnum:
        qstat = x
        print(qstat)
    else:
        x = np.kron(x,zero_state)
    iterate+=1
    

gates = {"Hadamard":hadop, "X":xop, "Z":zop, "Y":yop, "sqrtX":sqrtxop,"phase shift":phaseshiftop,"measurement":measurement,"custom":customop, "cnot":cnot}
print(gates.keys())

done = "n"#needs to handle multi qubit gates
while done == "n":
    if qnum == 1:
        fstgat = input("what gate would you like to use? use the list of gates at the top minus control and target: ")
        ap_qubit = int(input("what qubit would you like it to be applied to?"))
        if fstgat in gates:
            qstat = gates[fstgat](qstat,ap_qubit)
            done = input("Done with your circuit? y or n: ")
        else:
            print("sorry, that gate is not yet implemented. maybe try custom gate.")
    else:
        fstgat = input('what gate would you like to use? (proceed at your own risk): ')
        ap_qubit = int(input('what qubit would you like that gate to be applied to: '))
        if fstgat in gates:
            qstat = gates[fstgat](qstat,ap_qubit)
            done = input('done with your circuit? y or n: ')
        else:
            print('sorry, gate not implemented, maybe try custom gate.')

#printing - fix the probabilities
print(" ")
print("final state:", qstat)
print("probability of |0> state upon measurement is", probability(qstat,0))
print("probability of |1> state upon measurement is", probability(qstat,1))
