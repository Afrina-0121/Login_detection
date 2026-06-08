threshold = 3

with open("auth.log", "r") as file:
    lines = file.readlines()

failed_count = 0

for line in lines:
    if "FAILED" in line:
        failed_count += 1

print("Total Failed Logins:", failed_count)

if failed_count >= threshold:
    print("ALERT: Suspicious login activity detected!")
