import numpy as np

if __name__ == '__main__':
    # Create a Matrix
    # Our system of equations is as follows:
    # x + y + z = 6
    # 3x + 2y + z = 10
    # z = 3
    # Therefore, we define matrices as
    co_effs = np.array([[1,1,1], [3,2,1], [0,0,1]])
    eq = np.array([6,10,3])
    solun = np.linalg.solve(co_effs, eq)
    print('The solution to the equations are:')
    print('x = ' + str(solun[0]))
    print('y = ' + str(solun[1]))
    print('z = ' + str(solun[2]))
    print('The combined solution is:')
    print(str(solun))

    # Check if solution is correct
    print('Checking if solution is correct...')
    w = np.allclose(np.dot(co_effs, solun), eq)
    if w:
        print('The solution is correct')
    else:
        print('The solution is incorrect')