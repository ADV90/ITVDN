from prettytable import PrettyTable

#Color
R = "\033[31m" #RED
G = "\033[32m" # GREEN
Y = "\033[33m" # Yellow
B = "\033[34m" # Blue
N = "\033[0m" # Reset


a = "ok"
b = "Failed"
t = PrettyTable(['Input', 'status'])

#Adding Both example in table
t.add_row(['FAN', G+a+N])
t.add_row(['FAN', R+b+N])

print(t)