import numpy as np
from random import randint
import cmath
import math
from function import *

qubits = int(input("How many qubits would you like to use? (Currently, only supports 1): "))
done = "n"
qstatask = input("Would you like your initial qubits to be in the |0> state or |1> state? 0 or 1: ")
if qstatask == "0":
    qstats = {key:np.array([0,1]) for key in range(1,qubits+1)}
elif qstatask == "1":
    qstats = {key:np.array([1,0]) for key in range(1,qubits+1)}
else:
    print("I'm sorry, that is not a valid input. State set to zero.")
    qstats = {key:np.array([0,1]) for key in range(1,qubits+1)}

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
            qstat = qstats[1]
            qstat = singates[fstgat](qstat)
            qstats[1] = qstat
            done = input("Done with your circuit? y or n: ")
        else:
            print("sorry, that gate is not yet implemented. maybe try custom gate.")
            done = "y"
    elif qubits >= 2:
        commands = {}
        for i in range(1,qubits+1):
            commands[i] = []
        qubitnum=1
        while qubitnum <= qubits:
            while done == "n":
                fstgat = input("what gate would you like to use for " + str(qubitnum) + " qubit? Use the list of single qubits at the top, plus control or target: ")
                commands[qubitnum].append(fstgat)
                done = input("Done with your " + str(qubitnum) + " qubit? y or n: ")
            qubitnum+=1
            done = "n"
        qubitnum=1
        while qubitnum <= qubits:
            for index,gate in enumerate(commands[qubitnum]):
                if gate in singates:
                    if gate != "target" or (gate == "target" and mem1 in globals()):
                        qstat = qstats[index+1]
                        qstat = singates[gate](qstat)
                        qstats[index+1] = qstat
                        print("done with a calculation")
                        if index+1 == len(commands[qubitnum]):
                            print(" ")
                            print("your result is", qstats[index+1], "qubit #", index+1)
                            print("probability of |0> state is", probability(qstats[index+1],0))
                            print("probability of |1> state is", probability(qstats[index+1],1))
                    else:
                        print("checking for information")
                else:
                    print(gate, " has not yet been implemented. Maybe try the custom gate?")
                    break
                qubitnum+=1
        print("Program complete.")
        done = "y"
    else:
        print("sorry, that functionality is not yet implemented")
        done = "y"
