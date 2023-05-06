
def obtain_probabilites():
    on_file = open("T_On.csv")
    lines = on_file.readlines()
    probabilities_on = []
    for line in lines:
        probabilities_on.append(line.split(","))
    for i in range(len(probabilities_on)):
        for j in range(len(probabilities_on[i])):
            probabilities_on[i][j] = float(probabilities_on[i][j])
        #print(probabilities_on[i])

    #print("\n\n")

    off_file = open("T_Off.csv")
    lines = off_file.readlines()
    probabilities_off = []

    for line in lines:
        probabilities_off.append(line.split(","))

    for i in range(len(probabilities_off)):
        for j in range(len(probabilities_off[i])):
            probabilities_off[i][j] = float(probabilities_off[i][j])
        #print(probabilities_off[i])

    return probabilities_on, probabilities_off


def bellman(probabilies_on, probabilities_off, cost_on, cost_off):
    values = {}
    prev_values = {}
    optimal_policy = {}
    init = 16.0
    for i in range(len(probabilies_on[0])):
        values["V("+str(init)+")"] = 0
        prev_values["V(" + str(init) + ")"] = 1
        optimal_policy["V(" + str(init) + ")"] = None
        init += 0.5

    #print(values)
    #print("----------------------------------------------------")
    while prev_values != values:
        #hacer for para copiar valores y no igualarlo porque se convierte en un espejo

        for key, value in values.items():
            prev_values[key] = value

        counter_row = 0
        for key in values.keys():
            counter_column = 0
            on = cost_on
            off = cost_off
            if key == "V(22.0)":
                continue
            for value in prev_values.values():
                #if key == "V(16.0)" or key == "V(17.0)":
                #print(counter_row, counter_column, probabilies_on[counter_row][counter_column], value)
                on += probabilies_on[counter_row][counter_column] * value
                off += probabilities_off[counter_row][counter_column] * value
                on = round(on, 2)
                off = round(off, 2)
                #if key == "V(16.0)":
                #   print(probabilies_on[counter_row][counter_column], on)

                counter_column += 1

            counter_row += 1

            values[key] = min(on, off)
            if on == min(on, off):
                optimal_policy[key] = "on"
            else:
                optimal_policy[key] = "off"


        #print(prev_values)
        #print(values)
        #print("----------------------------------------------------")

    print("\n----------------------OPTIMAL POLICY------------------------------")
    print(optimal_policy)





prob_on, prob_off = obtain_probabilites()
for i in range(1, 10):
    for j in range(1, 10):
        print("------------------------------------------------------------------")
        print("Cost on: ", i,  "\nCost off: ", j)
        bellman(prob_on, prob_off, i, j)











