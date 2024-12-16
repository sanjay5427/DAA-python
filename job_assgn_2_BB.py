import sys

# Function to calculate the least cost of job assignment using Branch and Bound
def calculate_cost(cost_matrix, n):
    assigned_jobs = [-1] * n
    min_cost = sys.maxsize
    min_cost = branch_and_bound(cost_matrix, n, 0, 0, assigned_jobs, [False] * n)
    return min_cost

# Function that implements the Branch and Bound algorithm
def branch_and_bound(cost_matrix, n, worker, current_cost, assigned_jobs, job_assigned):
    if worker == n:
        return current_cost
    
    min_cost = sys.maxsize
    
    for job in range(n):
        if not job_assigned[job]:
            assigned_jobs[worker] = job
            job_assigned[job] = True
            total_cost = branch_and_bound(cost_matrix, n, worker + 1, 
                                          current_cost + cost_matrix[worker][job], 
                                          assigned_jobs, job_assigned)
            min_cost = min(min_cost, total_cost)
            job_assigned[job] = False
            assigned_jobs[worker] = -1
    
    return min_cost

# Function to print the cost matrix and call the solution
def solve_job_assignment_problem(cost_matrix):
    n = len(cost_matrix)
    min_cost = calculate_cost(cost_matrix, n)
    print("The minimum cost assignment is:", min_cost)

# Get the cost matrix input from the user
n = int(input("Enter the number of workers/jobs: "))
cost_matrix = []
print("Enter the cost matrix row by row (space-separated values):")
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    if len(row) != n:
        raise ValueError(f"Each row must have {n} elements.")
    cost_matrix.append(row)

# Solve the job assignment problem with the user-provided cost matrix
solve_job_assignment_problem(cost_matrix)
 