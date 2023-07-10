print("=== Task1 ===")
"""
Task 1:
We have example messages from 6 persons in JSON format. There are at least 3 persons
who are older than 17. Find out those who are most probably older than 17 years old based
on example messages. Print their names in the console.
"""

def find_and_print(messages):
    # write down your judgment rules in comments
    # your code here, based on your own rules
    keywords = ["18 years old", "college student", "legal age", "vote"]
    for name, v in messages.items():
        for condition in keywords:
            if condition in v:
                print(name)

find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})

print("=== Task2 ===")
"""
Task 2:
Complete functions below to calculate sum of bonus of all employees in TWD and print it.
1. Bonus should depend on salary, performance and role fields. Define your own rules
and calculate a bonus for each employee based on it.
2. Sum of bonus of all employees cannot exceed 10000 TWD based on your rules and
example data.
3. You can assume the USD to TWD Exchange Rate is 30.
4. Salary is default to TWD if there is no specific mark.
"""
def calculate_sum_of_bonus(data):
    """
    performance bonus ratio "above average" : 5%
    performance bonus ratio "average": 3%
    performance bonus ratio "below average": 1%

    role bonus ratio "Engineer": 5%
    role bonus ratio "Sales": 3%
    role bonus ratio "CEO": 1%

    The bonus of each staff is: min(salary * (performance ratio + role ratio), 2500)
    """
    # write down your bonus rules in comments
    # your code here, based on your own rules

    total_bonus = 0
    for staff in data["employees"]:
        staff['bonus_ratio'] = 0

        if staff["performance"] == "above average":
            staff['bonus_ratio'] += 0.05
        elif staff["performance"] == "average":
            staff['bonus_ratio'] += 0.03
        elif staff["performance"] == "below average":
            staff['bonus_ratio'] += 0.01

        if staff["role"] == "Engineer":
            staff['bonus_ratio'] += 0.05
        elif staff["role"] == "Sales":
            staff['bonus_ratio'] += 0.03
        elif staff["role"] == "CEO":
            staff['bonus_ratio'] += 0.01

        if isinstance(staff["salary"], str):
            if "USD" in staff["salary"]:
                staff["salary"] = int(staff["salary"].replace("USD", "")) * 30
            elif "," in staff["salary"]:
                staff["salary"] = int(staff["salary"].replace(",", ""))

        staff["bonus"] = min(staff["salary"] * staff['bonus_ratio'], 2500)
        
        total_bonus += staff["bonus"]

    print(f"total bonus: {total_bonus}")

calculate_sum_of_bonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}) # call calculate_sum_of_bonus function

print("=== Task3 ===")
"""
Task 3:
Find out whose middle name is unique among all the names, and print it. You can assume
every input is a Chinese name with 2 ~ 3 words. If there are only 2 words in a name, the
middle name is defined as the second word.
"""

def func(*data):
    # your code here
    temp = {}
    for name in data:
        temp[name[1]] = temp.get(name[1], [])
        temp[name[1]].append(name)

    for k, v in temp.items():
        if len(v) == 1:
            print(v[0])
            return
    
    print("沒有")
    return

func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

print("=== Task4 ===")
"""
Task 4:
There is a number sequence: 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, ...
Find out the nth term in this sequence.
"""

def get_number(index:int):
    if index >= 0:
        ret = ((index + 1) // 2 * 4) - ((index // 2))
        print(f"Ans: {ret}")

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

print("=== Task5 ===")
"""
Task 5 (Optional):
Given available seats for each car of a train, status bitmap, and number of incoming
passengers, writing a procedure to find out the index of the most fitted car to serve
passengers. Print -1 if there is no car which can serve incoming passengers.
- Available Seats: list/array containing number of available seats for each car.
- Status Bitmap: list/array containing only 0 or 1. 1 means the corresponding car can
serve passengers for now.
- Passenger Number: number of incoming passengers.
We can assume all incoming passengers should be served in the same car.
"""

def find_index_of_car(seats, status, number):
    # your code here
    ret = {}
    for i, v in enumerate(status):
        if v == 1:
            if seats[i] >= number:
                ret[i] = seats[i] - number
    if not ret:
        min_key = -1
    else:
        min_key = min(ret, key=ret.get)
    print(min_key)

find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2