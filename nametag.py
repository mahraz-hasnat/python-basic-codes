#the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period.
#For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
	return("{x} {y}.".format(x=first_name, y=last_name[:1]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 
