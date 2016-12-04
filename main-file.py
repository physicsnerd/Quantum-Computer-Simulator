import numpy as np
from random import randint
import cmath
import math

singates = ["Hadamard":hadop, "X":xop, "Z":zop, "Y":yop, "sqrtX":sqrtxop,"phase shift":phaseshiftop,"measurement":probability,"custom":customop]
twgates = ["cNOT", "swap"]
thrgates = ["Toffoli"]
qubits = float(input("How many qubits would you like to use? (Currently, only supports 1): "))
done = "n"
done2 = "n"
qstatask = input("Would you like your initial qubits to be in the |0> state or |1> state? 0 or 1: ")
if qstatask == "0":
    qstat = np.array([0,1])
    qstat2 = np.array([0,1])
elif qstatask == "1":
    qstat = np.array([1,0])
    qstat2 = np.array([1,0])
else:
    print("I'm sorry, that is not a valid input. State set to zero.")
    qstat = np.array([0,1])
    qstat2 = np.array([0,1])

print(singates)
print(twgates)
print(thrgates)

def hadop(qstat):
    matrix = (1/cmath.sqrt(2))*np.array([[1,1],[1,-1]])
    return np.dot(matrix, qstat)

def xop(qstat):
    matrix = np.array([[0,1],[1,0]])
    return np.dot(matrix,qstat)

def zop(qstat):
    matrix = np.array([[1,0],[0,-1]])
    return np.dot(matrix,qstat)

def yop(qstat):
    matrix = np.array([[0, cmath.sqrt(-1)],[-1*cmath.sqrt(-1),0]])
    return np.dot(matrix,qstat)

def sqrtxop(qstat):
    const1 = 1+cmath.sqrt(1)
    const2 = 1-cmath.sqrt(1)
    matrix = np.array([[const1/2,const2/2],[const2/2,const1/2]])
    return np.dot(matrix,qstat)

def phaseshiftop(qstat,x):
	const1 = cmath.sqrt(-1)*x
	matrix = np.array([[1,0],[0,math.e**const1]])
	return np.dot(matrix,qstat)

def customop(qstat,n1, n2, n3, n4):
    matrix = np.array([[n1,n3],[n2,n4]])
    matrix2 = matrix.conj().T
    result = np.dot(matrix, matrix2)
    identity = np.identity(2)
    if np.array_equal(result, identity) == True:
        return np.dot(matrix, qstat)
    else:
        print("matrix not unitary, pretending no gate was applied")
        return qstat

def probability(qstat, n):
    if n == 0:
        return (qstat[0])**2
    elif n == 1:
        return (qstat[1])**2

while done == "n":
    if qubits == 1:
        fstgat = input("what g ate would you like to use? use the list of single gates at the top: ")
        if fstgat in singates:
            qstat = singates[fstgat](qstat)
            done = input("Done with your circuit? y or n: "))
            elif fstgat == "phase shift":
                phasepos = [math.pi/4, math.pi/2]
                print(phasepos)
                x = input("Please pick one of the two phase shifts, 0 for the first, 1 for the second: ")
                if x == "0":
                    y = phasepos[0]
                elif x == "1":
                    y = phasepos[1]
                qstat = phaseshiftop(qstat,y)
                done = input("Done with your circuit? y or n: ")
            elif fstgat == "measurement":
                prob1 = probability(qstat,0)
                prob2 = probability(qstat,1)
                random = randint(0,1)
                if random <= prob1:
                    qstat = np.array([0,1])
                elif prob1 < random:
                    qstat = np.array([1,0])
                done = input("Done with your circuit? y or n: ")
            elif fstgat == "custom":
                num1 = float(input("Please input a number (no pi, e, etc) for the first number in your matrix (row 1 column 1): "))
                num2 = float(input("Number for matrix - row 1 column 2: "))
                num3 = float(input("Number for matrix - row 2 column 1: "))
                num4 = float(input("Number for matrix - row 2 column 2: "))
                qstat = customop(qstat,num1,num2,num3,num4)
                done = input("Done with your circuit? y or n: ")
        else:
            print("sorry, that gate is not yet implemented. maybe try custom gate.")
            done = "y"
    elif qubits == 2:
        while done2 == "n":
            fstgat = input("what gate would you like to use for 1st qubit? Use the list of single qubits at the top, plus control or target")
            if fstgat == "Hadamard":
                qstat = hadop(qstat)
                done2 = input("Done with your 1st qubit? y or n: ")
            elif fstgat == "X":
                qstat = xop(qstat)
                done2 = input("Done with your 1st qubit? y or n: ")
            elif fstgat == "Z":
                qstat = zop(qstat)
                done2 = input("Done with your 1st qubit? y or n: ")
            elif fstgat == "Y":
                qstat = yop(qstat)
                done2 = input("Done with your 1st qubit? y or n: ")
            elif fstgat == "sqrtX":
                qstat = sqrtxop(qstat)
                done2 = input("Done with your 1st qubit? y or n: ")
            elif fstgat == "phase shift":
                phasepos = [math.pi/4, math.pi/2]
                print(phasepos)
                x = input("Please pick one of the two phase shifts, 0 for the first, 1 for the second: ")
                if x == "0":
                    y = phasepos[0]
                elif x == "1":
                    y = phasepos[1]
                qstat = phaseshiftop(qstat,y)
                done2 = input("Done with your 1st qubit? y or n: ")
            elif fstgat == "measurement":
                prob1 = probability(qstat,0)
                prob2 = probability(qstat,1)
                random = randint(0,1)
                if random <= prob1:
                    qstat = np.array([0,1])
                elif prob1 < random:
                    qstat = np.array([1,0])
                    done2 = input("Done with your 1st qubit? y or n: ")
            elif fstgat == "custom":
                num1 = float(input("Please input a number (no pi, e, etc) for the first number in your matrix (row 1 column 1): "))
                num2 = float(input("Number for matrix - row 1 column 2: "))
                num3 = float(input("Number for matrix - row 2 column 1: "))
                num4 = float(input("Number for matrix - row 2 column 2: "))
                qstat = customop(qstat,num1,num2,num3,num4)
                done2 = input("Done with your 1st qubit? y or n: ")
            elif fstgat == "control":
                typegat = input("Which gate is this the control qubit for? See list of two qubit gates at the top.")
                if typegat == "cNOT":
                    mem1 = qstat
                elif typegat == "swap":
                    mem2 = qstat
                done2 = input("Done with your 1st qubit? y or n")
            elif fstgat == "target":
                typegat2 = input("Which gate is this target qubit for? See list of two qubit gates at the top.")
                if typegat2 == "cNOT":
                    if np.array_equal(mem3, [0,1]) == True:
            	        qstat = qstat
                    elif np.array_equal(mem3, [1,0]) == True:
            	        qstat = np.dot(qstat,mem3)
                    else:
            	        print("superposition...not implemented")
                elif typegat2 == "swap":
                    qstat = mem4
                done2 = input("Done with your 1st qubit? y or n")
        scndgat = input("what gate would you like to use for 2nd qubit? Use the list of single qubits at the top, plus control or target")
        if scndgat == "Hadamard":
            qstat = hadop(qstat)
            done = input("Done with your circuit? y or n: ")
        elif scndgat == "X":
            qstat = xop(qstat)
            done = input("Done with your circuit? y or n: ")
        elif scndgat == "Z":
            qstat = zop(qstat)
            done = input("Done with your circuit? y or n: ")
        elif scndgat == "Y":
            qstat = yop(qstat)
            done = input("Done with your circuit? y or n: ")
        elif scndgat == "sqrtX":
            qstat = sqrtxop(qstat)
            done = input("Done with your circuit? y or n: ")
        elif scndgat == "phase shift":
            phasepos = [math.pi/4, math.pi/2]
            print(phasepos)
            x = input("Please pick one of the two phase shifts, 0 for the first, 1 for the second: ")
            if x == "0":
                y = phasepos[0]
            elif x == "1":
                y = phasepos[1]
            qstat = phaseshiftop(qstat,y)
            done = input("Done with your circuit? y or n: ")
        elif scndgat == "measurement":
            prob1 = probability(qstat,0)
            prob2 = probability(qstat,1)
            random = randint(0,1)
            if random <= prob1:
                qstat = np.array([0,1])
            elif prob1 < random:
                qstat = np.array([1,0])
            done = input("Done with your circuit? y or n: ")
        elif scndgat == "custom":
            num1 = float(input("Please input a number (no pi, e, etc) for the first number in your matrix (row 1 column 1): "))
            num2 = float(input("Number for matrix - row 1 column 2: "))
            num3 = float(input("Number for matrix - row 2 column 1: "))
            num4 = float(input("Number for matrix - row 2 column 2: "))
            qstat = customop(qstat,num1,num2,num3,num4)
            done = input("Done with your circuit? y or n: ")
        elif scndgat == "control":
            typegat3 = input("Which gate is this the control qubit for? See list of two qubit gates at the top.")
            if typegat3 == "cNOT":
                mem3 = qstat
            elif typegat3 == "swap":
                mem4 = qstat
            done = input("Done with your circuit? y or n")
        elif scndgat == "target":
            typegat4 = input("Which gate is this target qubit for? See list of two qubit gates at the top.")
            if typegat4 == "cNOT":
                if np.array_equal(mem1,[0,1]) == True:
            	    qstat = qstat
                elif np.array_equal(mem1, [1,0]) == True:
            	    qstat = np.dot(qstat,mem3)
                else:
            	    print("superposition...not implemented")
            elif typegat4 == "swap":
                qstat = mem2
            done = input("Done with your circuit? y or n")
    else:
        print("sorry, that functionality is not yet implemented")
        done = "y"
print(" ")
print("your result is", qstat)
if qubits == 2:
    print("              ", qstat2, "(second qubit)")
print("probability of |0> state is", probability(qstat,0))
print("probability of |1> state is", probability(qstat,1))
