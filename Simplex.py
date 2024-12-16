from scipy.optimize import linprog

def solve_linear_program():
    # Get the input for the objective function
    objective = list(map(float, input("Enter the coefficients of the objective function (space-separated, e.g., -3 5 for maximizing 3x1 + 5x2): ").split()))
    
    # Get the number of constraints
    num_constraints = int(input("Enter the number of constraints: "))
    
    # Get the coefficients of the constraints
    lhs_ineq = []
    rhs_ineq = []
    print("Enter the constraints in the format 'a1 a2 <= b':")
    for _ in range(num_constraints):
        constraint = input().split()
        a1, a2 = float(constraint[0]), float(constraint[1])
        lhs_ineq.append([a1, a2])
        rhs_ineq.append(float(constraint[3]))
    
    # Convert the problem to a minimization problem by negating the objective function
    c = [-coeff for coeff in objective]
    
    # Solve the linear program using the simplex method
    result = linprog(c, A_ub=lhs_ineq, b_ub=rhs_ineq, method='simplex')
    
    if result.success:
        print("Optimal values for x1 and x2:", result.x)
        print("Optimal value of the objective function z:", -result.fun)
    else:
        print("No feasible solution found.")

solve_linear_program()
