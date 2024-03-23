import matplotlib.pyplot as plt

# reading the script
with open('graphing.txt', 'r') as f:
    lines = f.readlines()

# define keywords
keywords = [["voltage", "timeScale", "timeStep", "riseTime", "fallTime", "initialVoltage", "delayTime", "end"],["go", "v"]]

# arrays
voltage = []
time = []
settings = {}

# Function to plot the graph.
def plot_the_graph():
    plt.plot(time, voltage)
    plt.grid(True)
    plt.show()

# Function to format the pwl command.
def pwl_formatter():
    pwl = "pwl( "
    for i in range(len(time)):
        pwl_update = str(round(time[i],3)) + settings["timeScale"] + ", " + str(voltage[i]) + settings["voltage"]
        if  i == len(time)-1:
            pass
        else:
            pwl_update = pwl_update + ", "
        pwl = pwl + pwl_update  
    pwl = pwl + ")"
    print(pwl)


# going through the lines
for line in lines:
    command = line.split("=")
    command[0] = command[0].strip()

    # check if the line contains settings parameters.
    if command[0] in keywords[0]:
        
        if command[0] != "end":
            command[1] = command[1].strip()
            command[1] = command[1].strip("\n")
            # adding settings parameters to settings dictionary
            settings[command[0]] = command[1]
        
        # If the end of the script reached.
        elif command[0] == "end":

            # check whether the voltage and time arrays have same length.
            # if not corrent the missmatch
            if len(voltage) == len(time):
                plot_the_graph()

            elif len(voltage) > len(time):
                voltage.pop()
                plot_the_graph()

            else:
                voltage.append(voltage[len(voltage) - 1])
                plot_the_graph()
            pwl_formatter()
        else:
            pass
        # print(settings)
    
    # checking for the go or v commands
    elif line.split(" ")[0] in keywords[1]:
        command = line.split(" ")
        val = float(command[1].strip("\n"))

        # if a go command is present.
        if command[0] == "go" and command[1] != None:
            if len(time) != 0:
                last_time_val = time[len(time)-1]
            else:
                time.append(0)
                voltage.append(float(settings["initialVoltage"]))
                last_time_val = 0
            # appending the value to the time array
            time.append(last_time_val + float(command[1])*float(settings["timeStep"]))

        # if a v command is present.
        elif command[0] == "v" and command[1] != None:
            if len(voltage) == 0:
                voltage.append(float(settings["initialVoltage"]))
            elif (time[len(voltage) - 1] == command[1]):
                voltage.append(command[1])
            else:
                # If the new voltage is greater than the previous voltage, then use rise time
                if float(command[1]) > voltage[len(voltage) - 1]:
                    voltage.append(voltage[len(voltage) - 1])
                    time.append(time[len(time)-1] + float(settings["riseTime"]))
                    voltage.append(float(command[1]))
                # If the new voltage is less than the previous voltage, then use fall time
                else:
                    voltage.append(voltage[len(voltage) - 1])
                    time.append(time[len(time)-1] + float(settings["fallTime"]))
                    voltage.append(float(command[1]))
        
        # If unknown parameters present in the file then give an error
        else:
            print("error in line %s" % line)

    # If unknown parameters present in the file then give an error
    else:
        print("error in line %s" % line)