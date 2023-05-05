
def obtain_probabilites():
    on_file = open("T_On.csv")
    lines = on_file.readlines()
    probabilities_on = []


    for line in lines:
        probabilities_on.append(line.split(","))

    for i in range(len(probabilities_on)):
        for j in range(len(probabilities_on[i])):
            probabilities_on[i][j] = float(probabilities_on[i][j])
        print(probabilities_on[i])


    print("\n\n")

    off_file = open("T_Off.csv")
    lines = off_file.readlines()
    probabilities_off = []

    for line in lines:
        probabilities_off.append(line.split(","))

    for i in range(len(probabilities_off)):
        for j in range(len(probabilities_off[i])):
            probabilities_off[i][j] = float(probabilities_off[i][j])
        print(probabilities_off[i])

obtain_probabilites()









