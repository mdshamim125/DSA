def job_scheduling(jobs):
    # প্রতিটি কাজকে মুনাফা অনুযায়ী সর্ট করা হচ্ছে
    jobs.sort(key=lambda x: x[2], reverse=True)
    n = max([job[1] for job in jobs])  # সর্বোচ্চ সময়সীমা
    schedule = [None] * n
    max_profit = 0
   
    for job in jobs:
        for j in range(job[1] - 1, -1, -1):
            if schedule[j] is None:
                schedule[j] = job[0]
                max_profit += job[2]
                break
   
    return schedule, max_profit


# উদাহরণ ব্যবহার
jobs = [("A", 2, 100), ("B", 1, 19), ("C", 2, 27), ("D", 1, 25), ("E", 3, 15)]
schedule, max_profit = job_scheduling(jobs)
print("নির্ধারিত কাজ:", schedule)
print("সর্বাধিক মুনাফা:", max_profit)