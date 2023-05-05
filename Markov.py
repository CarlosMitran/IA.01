
f = open("T_On.csv")
lines = f.readlines()

probabilities_on = []
first_line = False

for line in lines:
    if not first_line:
        first_line = True
    else:
        probabilities_on.append(line.split(",")[1:])


for i in range(len(probabilities_on)):
        print(probabilities_on[i])





