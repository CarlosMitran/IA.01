
def obtain_probabilites():
    """Creating a matrix for all of the probabilities when the action is ON"""
    on_file = open("T_On.csv")
    lines = on_file.readlines()
    probabilities_on = append_probabilities(lines)

    #print("\n\n")
    """Creating a matrix for all of the probabilities when the action is OFF"""
    off_file = open("T_Off.csv")
    lines = off_file.readlines()
    probabilities_off = append_probabilities(lines)

    return probabilities_on, probabilities_off


def append_probabilities(lines):
    """Appending the probabilities from the file into a matrix"""
    probabilities = []
    for line in lines:
        probabilities.append(line.split(","))
    for i in range(len(probabilities)):
        for j in range(len(probabilities[i])):
            probabilities[i][j] = float(probabilities[i][j])
        # print(probabilities_on[i])
    return probabilities


def bellman(probabilities_on, probabilities_off, cost_on, cost_off):
    """Bellman equation, firstly we initialize our values"""
    values = {}
    prev_values = {}
    optimal_policy = {}
    init = 16.0
    for i in range(len(probabilities_on[0])):
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
                on += probabilities_on[counter_row][counter_column] * value
                off += probabilities_off[counter_row][counter_column] * value
                on = round(on, 4)
                off = round(off, 4)
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

    return optimal_policy


def print_values(prob_on, prob_off):
    """Function for printing the values of costs and the optimal policy on screen"""
    for i in range(1, 10):
        for j in range(1, 10):
            print("------------------------------------------------------------------")
            print("Cost on: ", i, "\nCost off: ", j)
            policy = bellman(prob_on, prob_off, i, j)
            print("\n----------------------OPTIMAL POLICY------------------------------")
            print(policy)


def file_create(prob_on, prob_off):
    """Function to create the output.csv file"""
    with open('Output.csv', 'w') as file:
        for i in range(1, 10):
            for j in range(1, 10):
                result = bellman(prob_on, prob_off, i, j)
                row = [str(i), str(j)]
                for key, value in result.items():
                    row.append(str(value))
                file.write(','.join(row) + '\n')


def main():
    """Main function"""
    prob_on, prob_off = obtain_probabilites()
    file_create(prob_on, prob_off)
    print_values(prob_on, prob_off)


main()













