def job_sequencing(jobs):
    # Sort jobs by decreasing profit
    def get_profit(job):
        return job[2]
    jobs.sort(key=get_profit, reverse=True)
    
    n = len(jobs)
    max_deadline = max(job[1] for job in jobs)
    
    # Initialize result slots and job sequence
    result = [None] * max_deadline
    slot_filled = [False] * max_deadline
    
    total_profit = 0
    for job in jobs:
        job_id, deadline, profit = job
        
        # Find a free slot for this job (starting from the latest possible slot)
        for j in range(min(deadline, max_deadline) - 1, -1, -1):
            if not slot_filled[j]:
                slot_filled[j] = True
                result[j] = job_id
                total_profit += profit
                break
    
    # Print the job sequence and total profit
    print("Job sequence:", [job for job in result if job is not None])
    print("Total profit:", total_profit)

# Get user input for jobs
n = int(input("Enter the number of jobs: "))
jobs = []
print("Enter the jobs in the format 'JobID Deadline Profit':")
for _ in range(n):
    job = input().split()
    job_id = job[0]
    deadline = int(job[1])
    profit = int(job[2])
    jobs.append((job_id, deadline, profit))

job_sequencing(jobs)
