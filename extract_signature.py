import sys, os

def usage():
	print "Usage {} filename number_bytes".format(sys.argv[0])

def main():
	if len(sys.argv) != 3:
		usage()
		return

	filename = os.path.realpath(sys.argv[1])
	number_bytes = int(sys.argv[2])

	if number_bytes <= 0:
		print "Invalid number of bytes ({})".format(number_bytes)
		return

	with open(filename, "rb") as f:
		data = f.read()
		if len(data) < number_bytes:
			print "Error: file only {}-byte long".format(len(data))
			return

		hexdata = "\\x" + "\\x".join("{:02x}".format(ord(c)) for c in data[:number_bytes])

		print "Filename: {}".format(filename)
		print "Number of bytes: {}".format(number_bytes)
		print "Value: {}".format(hexdata)

if __name__ == "__main__":
	main()