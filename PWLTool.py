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
# formatting the string
# print(lines)
# for line in lines:
#     line = line.replace('\n', '')
    # print(line)

def plot_the_graph():
    plt.plot(time, voltage)
    plt.grid(True)
    plt.show()

# going through the lines
for line in lines:
    # print(line.strip())
    # line = line.replace('\n',"")
    command = line.split("=")
    command[0] = command[0].strip()
    # print(command)
    # print(command.shape)
    if command[0] in keywords[0]:
        # print(command[1])
        if command[0] != "end":
            command[1] = command[1].strip()
            command[1] = command[1].strip("\n")
            settings[command[0]] = command[1]
            # print(settings)
            # print(settings["voltage"])
        elif command[0] == "end":
            if len(voltage) == len(time):
                plot_the_graph()
            elif len(voltage) > len(time):
                voltage.pop()
                plot_the_graph()
            else:
                voltage.append(voltage[len(voltage) - 1])
                plot_the_graph()
        else:
            pass
        # print(settings)
    
    elif line.split(" ")[0] in keywords[1]:
        command = line.split(" ")
        # if settings["delayTime"] != 
        # print(command[0])
        print(str(command[0]) + ":" + str(command[1].strip()))
        val = float(command[1].strip("\n"))
        if command[0] == "go" and command[1] != None:
            if len(time) != 0:
                last_time_val = time[len(time)-1]
            else:
                time.append(0)
                voltage.append(float(settings["initialVoltage"]))
                last_time_val = 0
            time.append(last_time_val + float(command[1])*float(settings["timeStep"]))
        elif command[0] == "v" and command[1] != None:
            if len(voltage) == 0:
                voltage.append(float(settings["initialVoltage"]))
            elif (time[len(voltage) - 1] == command[1]):
                voltage.append(command[1])
            else:
                voltage.append(voltage[len(voltage) - 1])
                time.append(time[len(time)-1] + float(settings["riseTime"]))
                voltage.append(float(command[1]))
            
        else:
            print("error in line %s" % line)
        print("time: ",time)
        print("voltage: ",voltage)


    else:
        print("error in line %s" % line)
        # pass
    # for arg in command:
    #     arg = arg.replace('\n',"")
    #     print(arg)

