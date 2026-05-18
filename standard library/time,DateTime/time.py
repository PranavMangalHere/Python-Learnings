import time 

# def func():
#     for i in range(10000):
#         pass

# current_time = time.time()
# print(current_time)
# func()
# time.sleep(3)
# end_time = time.time() - current_time
# print(end_time)

current_time = time.time()

# readable_time = time.ctime(current_time)
# print(readable_time)

# local_time = time.localtime()
# print(local_time)

## GMTime
# gm_time = time.gmtime()
# print(gm_time)

# time_tuple = (2024, 10, 12, 15, 30, 0, 5, 285, -1)
# epoch_time = time.mktime(time_tuple)
# print(f"Seconds since the epoch: {epoch_time}

local_time = time.localtime()
# print(local_time)
# formatted_time = time.strftime("%Y-%m-%d", local_time)
# print(formatted_time)

# stripTime = "2024-10-12 15:30:00"
# time_struct = time.strptime(stripTime, "%Y-%m-%d %H:%M:%S")
# print(time_struct)

# start = time.perf_counter()
# time.sleep(3)
# end = time.perf_counter()

# print(f"Elapsed time: {end - start} seconds")


""" 
Real-Time Use Cases of time Module:

Monitoring Execution Time: When optimizing code or measuring the performance of
algorithms, the time module provides tools to measure both wall-clock time (time.time()) and CPU time (time.process_time()).

Delaying Execution: The time.sleep() function is useful in various scenarios like rate limiting API calls, throttling resource access, or adding a delay in automation scripts.

Working with Timestamps: The module provides functions like time.time() and time.ctime() to easily work with timestamps for logging events, tracking changes, or storing time-based data.

Benchmarking: time.perf_counter() and time.monotonic() are useful for accurate performance measurement when you need precise time intervals, even across system sleep or resynchronizations.

System-Level Programming: time module functions are ideal when dealing with OS-level operations, such as scheduling system tasks, measuring CPU processing times, or handling real-time delays.
""" 