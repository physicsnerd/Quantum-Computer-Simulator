import numpy as np
from random import randint
import cmath
import math
from function import *

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
    elif qubits == 2:
        while done2 == "n":
            fstgat = input("what gate would you like to use for 1st qubit? Use the list of single qubits at the top, plus control or target")
            if fstgat in singates:
                qstat = singates[fstgat](qstat)
                done2 = input("Done with your 1st qubit? y or n: ")     
        scndgat = input("what gate would you like to use for 2nd qubit? Use the list of single qubits at the top, plus control or target")
        if scndgat in singates:
            qstat = singates[scndgat](qstat)
            done = input("Done with your circuit? y or n: ")
    else:
        print("sorry, that functionality is not yet implemented")
        done = "y"
print(" ")
print("your result is", qstat)
if qubits == 2:
    print("              ", qstat2, "(second qubit)")
print("probability of |0> state is", probability(qstat,0))
print("probability of |1> state is", probability(qstat,1))
