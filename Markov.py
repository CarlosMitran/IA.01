def obtain_probabilites():
    """Creating a matrix for all of the probabilities when the action is ON"""
    on_file = open("T_On.csv")
    lines = on_file.readlines()
    probabilities_on = append_probabilities(lines)

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
    return probabilities


def bellman(probabilities_on, probabilities_off, cost_on, cost_off):
    """Bellman equation"""
    # Create the 3 dictionaries
    values = {}
    prev_values = {}
    optimal_policy = {}
    # Create the keys and the initial values
    init = 16.0
    for i in range(len(probabilities_on[0])):
        values["V(" + str(init) + ")"] = 0
        prev_values["V(" + str(init) + ")"] = 1
        optimal_policy["V(" + str(init) + ")"] = None
        init += 0.5

    # Calculations, we will iterate until same output twice
    while prev_values != values:

        # Copy latest output into previous values
        for key, value in values.items():
            prev_values[key] = value

        # Begin the iteration for every key of the dictionary V(16)...
        counter_row = 0
        for key in values.keys():
            # Reset the costs to the initial ones
            counter_column = 0
            on = cost_on
            off = cost_off
            # Skip the goal key
            if key == "V(22.0)":
                continue
            # Second for loop where we perform the operation
            for value in prev_values.values():
                # For on and off costs, sum each probability by the previous value of its V (in prev_values)
                on += probabilities_on[counter_row][counter_column] * value
                off += probabilities_off[counter_row][counter_column] * value
                # Round to avoid almost infinite iterations
                on = round(on, 4)
                off = round(off, 4)
                counter_column += 1
            counter_row += 1
            # Set the new value through the minimum of on and off costs
            values[key] = min(on, off)
            # Update the optimal policies
            if on == min(on, off):
                optimal_policy[key] = "on"
            else:
                optimal_policy[key] = "off"

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
    # Obtain matrices of probabilities for both actions
    prob_on, prob_off = obtain_probabilites()
    # Create a csv file and store the optimal policies
    file_create(prob_on, prob_off)
    # Print them in the terminal
    print_values(prob_on, prob_off)

    """The next line is for trying specific values, uncomment it, introduce the values and execute"""
    # print(bellman(prob_on, prob_off, 100 , 100))


main()
