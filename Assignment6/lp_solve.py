from pulp import *

if __name__ == '__main__':
    # declare your variables
    # Without LP relaxation
    # x1 = LpVariable("x1", 0, cat='Integer')  # 0<= x1, x1 belongs to z
    # x2 = LpVariable("x2", 0, cat='Integer')  # 0<= x2, x2 belongs to z
    # x3 = LpVariable("x3", 0, cat='Integer')  # 0<= x2, x3 belongs to z

    # With LP relaxation
    x1 = LpVariable("x1", 0)  # 0<= x1
    x2 = LpVariable("x2", 0)  # 0<= x2
    x3 = LpVariable("x3", 0)  # 0<= x2

    # define the problem
    prob = LpProblem("problem", LpMaximize)

    # defines the constraints
    prob += x1-x2+x3 <= 5
    prob += 2*x2+x3 <= 4
    prob += x1 <= 3
    prob += x1 >= 0
    prob += x2 >= 0
    prob += x3 >= 0

    # define the objective function to maximize
    prob += 3 * x1 - x2 + 2 * x3

    # solve the problem
    status = prob.solve(GLPK(msg=0))
    LpStatus[status]

    # print the results
    print('The Value of x1 is: ')
    print('x1 = ' + str(value(x1)))
    print('The Value of x2 is: ')
    print('x2 = ' + str(value(x2)))
    print('The Value of x3 is: ')
    print('x3 = ' + str(value(x3)))

