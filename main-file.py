import numpy as np
from random import randint
import cmath
import math
from function import *

qubits = int(input("How many qubits would you like to use? (Currently, only supports 1): "))
done = "n"
qstatask = input("Would you like your initial qubits to be in the |0> state or |1> state? 0 or 1: ")
if qstatask == "0":
    qstat = np.array([0,1])
elif qstatask == "1":
    qstat = np.array([1,0])
else:
    print("I'm sorry, that is not a valid input. State set to zero.")
    qstat = np.array([0,1])

singates = {"Hadamard":hadop, "X":xop, "Z":zop, "Y":yop, "sqrtX":sqrtxop,"phase shift":phaseshiftop,"measurement":measurement,"custom":customop, "control":control, "target":target}
twgates = ["cNOT", "swap"]
thrgates = ["Toffoli"]

print(singates.keys())
print(twgates)
print(thrgates)

while done == "n":
    if qubits == 1:
        fstgat = input("what gate would you like to use? use the list of single gates at the top: ")
        if fstgat in singates:
            qstat = singates[fstgat](qstat)
            done = input("Done with your circuit? y or n: ")
        else:
            print("sorry, that gate is not yet implemented. maybe try custom gate.")
            done = "y"
    elif qubits >= 2:
        commands = {}
        for i in range(1,qubits+1):
            commands[i] = []
        x=1
        while x <= qubits:
            while done == "n":
                fstgat = input("what gate would you like to use for " + str(x) + " qubit? Use the list of single qubits at the top, plus control or target: ")
                commands[x].append(fstgat)
                done = input("Done with your " + str(x) + " qubit? y or n: ")
            x+=1
            done = "n"
        x=1
        while x <= qubits:
            for i in commands[x]:
                if i in singates:
                    if i != "target" or (i == "target" and mem1 in globals()):
                        qstat = singates[i](qstat)
                        print("done with a calculation")
                        if int(i) == len(commands[x]):
                            print(" ")
                            print("your result is", qstat, "qubit #", i+1)
                            print("probability of |0> state is", probability(qstat,0))
                            print("probability of |1> state is", probability(qstat,1))
                            x+=1
                    else:
                        x+=1
                else:
                    print(i, " has not yet been implemented. Maybe try the custom gate?")
                    break
           
    else:
        print("sorry, that functionality is not yet implemented")
        done = "y"
