import sys

# Function to calculate the least cost of job assignment using Branch and Bound
def calculate_cost(cost_matrix, n):
    # Initialize an array to track the assignment of jobs to workers
    assigned_jobs = [-1] * n
    # Initialize the minimum cost to be the maximum possible integer value
    min_cost = sys.maxsize
    # Start solving the problem by exploring different possibilities
    min_cost = branch_and_bound(cost_matrix, n, 0, 0, assigned_jobs, [False] * n)
    return min_cost

# Function that implements the Branch and Bound algorithm
def branch_and_bound(cost_matrix, n, worker, current_cost, assigned_jobs, job_assigned):
    # If all workers are assigned a job, return the current cost
    if worker == n:
        return current_cost
    
    # Set the minimum cost as maximum integer value initially
    min_cost = sys.maxsize
    
    # Try assigning each job to the current worker
    for job in range(n):
        # If the job is not yet assigned
        if not job_assigned[job]:
            # Assign the job to the worker
            assigned_jobs[worker] = job
            job_assigned[job] = True
            
            # Recursively calculate the cost of assigning jobs to the remaining workers
            total_cost = branch_and_bound(cost_matrix, n, worker + 1, 
                                          current_cost + cost_matrix[worker][job], 
                                          assigned_jobs, job_assigned)
            
            # Update the minimum cost if a lower cost assignment is found
            min_cost = min(min_cost, total_cost)
            
            # Backtrack and unassign the job for the next iteration
            job_assigned[job] = False
            assigned_jobs[worker] = -1
    
    return min_cost

# Function to print the cost matrix and call the solution
def solve_job_assignment_problem(cost_matrix):
    n = len(cost_matrix)
    min_cost = calculate_cost(cost_matrix, n)
    print("The minimum cost assignment is:", min_cost)

# Example inputs (from the image)
cost_matrix_1 = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

cost_matrix_2 = [
    [1, 2, 1, 9],
    [4, 5, 2, 2],
    [7, 3, 9, 3],
    [2, 3, 5, 1]
]

# Test the solution with both inputs
print("Input 1:")
solve_job_assignment_problem(cost_matrix_1)

print("\nInput 2:")
solve_job_assignment_problem(cost_matrix_2)