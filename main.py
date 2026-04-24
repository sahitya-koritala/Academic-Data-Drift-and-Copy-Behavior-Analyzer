import random
import math
import copy
import numpy as np
import pandas as pd

def generate_data(n):
    data = []
    for i in range(n):
        d = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(d)
    return data

def make_df(data):
    return pd.DataFrame(data)

def modify(data, roll):
    rule = roll % 3
    for i in range(len(data)):
        if i % 3 == rule:
            data[i]["marks"] = data[i]["marks"] + math.sqrt(data[i]["marks"])
            data[i]["scores"][0] += 5
            data[i]["attendance"] -= 5

def analysis(orig, mod):
    o = [i["marks"] for i in orig]
    m = np.array([i["marks"] for i in mod])

    mean1 = np.mean(o)
    mean2 = np.mean(m)
    std = np.std(m)

    s = sorted(m)
    n = len(s)
    if n % 2 == 0:
        median = (s[n//2] + s[n//2 - 1]) / 2
    else:
        median = s[n//2]

    drift = abs(mean1 - mean2)

    norm = (m - np.min(m)) / (np.max(m) - np.min(m))

    return mean2, median, std, drift, norm

def check(drift, original, backup):
    threshold = 5

    if original != backup:
        return "Copy Failure Detected"
    elif drift < 2:
        return "Stable Data"
    elif drift < threshold:
        return "Minor Drift"
    else:
        return "Critical Drift"

roll_no = int(input("Enter your roll number: "))

n = random.randint(10, 15)
students = generate_data(n)

unique_attendance = set([i["attendance"] for i in students])

original_backup = copy.deepcopy(students)

shallow = copy.copy(students)
deep = copy.deepcopy(students)

modify(shallow, roll_no)
modify(deep, roll_no)

df1 = make_df(students)
df2 = make_df(shallow)
df3 = make_df(deep)

mean, median, std, drift, norm = analysis(students, deep)

result = check(drift, students, original_backup)

t = (mean, drift, std)

print("\nNumber of students generated:", n)

print("\nOriginal Data:\n", df1)
print("\nShallow Copy Data:\n", df2)
print("\nDeep Copy Data:\n", df3)

print("\nUnique Attendance Values:", unique_attendance)

print("\nDrift Value:", drift)
print("Median:", median)
print("Tuple (mean, drift, std_dev):", t)
print("Normalized Marks:", norm)
print("Final Classification:", result)
