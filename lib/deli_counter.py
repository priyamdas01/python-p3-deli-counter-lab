katz_deli = []

def line(current_line):
    if len(current_line) == 0:
        print("The line is currently empty.")
    else:
        que = []
        for index, person in enumerate(current_line):
            que.append(f"{index+1}. {person}")
        print(f"The line is currently: {' '.join(que)}")

def take_a_number(current_line, name):
    current_line.append(name.capitalize())
    print(f"Welcome, {name.capitalize()}. You are number {len(current_line)} in line.")
def now_serving(current_line):
    if(len(current_line) == 0):
        print("There is nobody waiting to be served!")
    else:
        
        print(f"Currently serving {current_line[0]}.")
        del current_line[0]

# take_a_number(katz_deli, "ADA")
# take_a_number(katz_deli, "Grace")
# take_a_number(katz_deli, "Kent")

# now_serving(katz_deli)

# line(katz_deli)

# take_a_number(katz_deli, "Matz")

# line(katz_deli)

# now_serving(katz_deli)

# line(katz_deli)