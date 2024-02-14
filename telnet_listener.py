#This script is used to isolate and comfortably view Telnet traffic.

import re
import subprocess

# Format - <src ip/host> to <dest ip/host> - <message>

# Regex for checking date format. Looks for b'00:00:00.000000
regex = "[b][']\d{2}:\d{2}:\d{2}\.\d{6}"

# Start tcpdump
listen = subprocess.Popen(('sudo', 'tcpdump', '-A', 'port', 'telnet', '-l'), stdout=subprocess.PIPE)

#Iterate over standard output. I couldn't figure out how to get it to print without the sentinel value.
for line in listen.stdout:
	# Split a row of output by spaces
	rowarray = str(line).split(" ")

	# Checks for a match for the intended date format
	if re.match(regex, rowarray[0]):
		print(" ")

		# Prints a message giving the time of the sniff, the source host, and the dest. host
		heading = rowarray[0] + ": " + rowarray[2] + " to " + rowarray[4]
		print(heading)

	# Prints the row unmodified otherwise. Reserved for raw telnet data.
	else:
		print(line)