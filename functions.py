#set qnum for dimension of matrix, set it so target can be identified

def hadop(qstat, qnum):
    matrix = (1/cmath.sqrt(2))*np.array([[1,1],[1,-1]])
    return np.dot(matrix, qstat)

def xop(qstat, qnum):
    matrix = np.array([[0,1],[1,0]])
    return np.dot(matrix,qstat)

def zop(qstat, qnum):
    matrix = np.array([[1,0],[0,-1]])
    return np.dot(matrix,qstat)

def yop(qstat, qnum):
    matrix = np.array([[0, cmath.sqrt(-1)],[-1*cmath.sqrt(-1),0]])
    return np.dot(matrix,qstat)

def sqrtxop(qstat, qnum):
    const1 = 1+cmath.sqrt(1)
    const2 = 1-cmath.sqrt(1)
    matrix = np.array([[const1/2,const2/2],[const2/2,const1/2]])
    return np.dot(matrix,qstat)

def phaseshiftop(qstat, qnum):
    phasepos = [math.pi/4, math.pi/2]
    print(phasepos)
    x = input("Please pick one of the two phase shifts, 0 for the first, 1 for the second: ")
    if x == "0":
        y = phasepos[0]
    elif x == "1":
        y = phasepos[1]
    const1 = cmath.sqrt(-1)*y
    matrix = np.array([[1,0],[0,math.e**const1]])
    return np.dot(matrix,qstat)

def customop(qstat, qnum):
    num1 = float(input("Please input a number (no pi, e, etc) for the first number in your matrix (row 1 column 1): "))
    num2 = float(input("Number for matrix - row 1 column 2: "))
    num3 = float(input("Number for matrix - row 2 column 1: "))
    num4 = float(input("Number for matrix - row 2 column 2: "))
    matrix = np.array([[num1,num3],[num2,num4]])
    matrix2 = matrix.conj().T
    result = np.dot(matrix, matrix2)
    identity = np.identity(2)
    if np.array_equal(result, identity) == True:
        return np.dot(matrix, qstat)
    else:
        print("matrix not unitary, pretending no gate was applied")
        return qstat

def probability(qstat, n, qnum):
    if n == 0:
        return (qstat[0])**2
    elif n == 1:
        return (qstat[1])**2

def measurement(qstat, qnum):
    prob1 = probability(qstat,0)
    prob2 = probability(qstat,1)
    random = randint(0,1)
    if random <= prob1:
        qstat = np.array([0,1])
    elif prob1 < random:
        qstat = np.array([1,0])
    return qstat
