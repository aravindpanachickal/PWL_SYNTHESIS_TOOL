# PWL SYNTHESIS TOOL
## A tool to generate a long piece-wise linear voltage source using a simple-to-write scripting language.

Piece-wise linear(PWL) is a voltage source used to supply voltages without a particular pattern and the user should define each lienear elements of the voltage curve. The code start with "PWL" followed by time, votage value pairs at each instance. an example of pwl source is given here.
```spice
pwl(0ms,0v, 5ms,0v, 5.1ms,5v, 10.1ms,5v, 10.2ms,0v 15.2ms,0v )
```
The input for the PWL tool is accepted from a file with a specific set of settings at the top, followed by continuous entries of voltage and time values in separate lines. As the changes in the voltage level increase, the number of lines in the script also increases. But the user doesn't want to worry about the timing of the rising and falling edges in the voltage levels since it is automatically addressed by the algorithm. 
Example of the script
```
voltage = v
timeScale = nS
timeStep = 100
riseTime = 0.1
fallTime = 0.1
initialVoltage = 0
go 1
v 5
go 10
v 0
go 1
end  
```
The resulting voltage
[result](result.png)

### Parts of the settings
| Keywords| Definitions |
| ------ | ------ |
| voltage | Unit of voltage (v, mv, uv, nv,etc.) |
| timeScale | Unit of time (s, ms, us, ns,etc. ) |
| timeStep | The unit value of one time step |
| riseTime | Time taken by the voltage to change from a lower to higher level |
| fallTime | Time taken by the voltage to change from a higher to lower level |
| initialVoltage | Voltage at time zero |

### Parts of the body of the script
| Keywords| Definitions |
| ------ | ------ |
| go | Time steps to move forward in graph |
| v | Voltage at that particular time |
| end | To stop the scripting |

## Features

- Easy to implement
- Live plotting using matplotlib library
- Easy to debug
- Time saving

## Requirements

- Python3
- matplotlib

## Usage

The go command will define how much time to move in axis and v command will define the shift in voltage level. If the voltage is set to v, time scale is set to second(s) and time step is set to 1, then `go 5` means the voltage level will be same for five seconds. if the time step is 10 then `go 5` means the voltage level will be same for 50 seconds. If a time of 25 is required then the command will be `go 2.5`.

