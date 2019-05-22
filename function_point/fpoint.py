

class Fpoint:

	def __init__(self,file_name):
		self.file_name = file_name
		self.factors = {}
		self.weight = {"EI": [3,4,6],
			"EO": [4,5,7],
			"EQ": [3,4,6], 
			"ILF": [7,10,15],
			"EIF": [5,7,10]}
		self.caf = []
		self.ufp = int(0)


	def get_input(self):
		with open(self.file_name, "r") as file:
			i = int(0)
			for line in file:
				i += 1
				if i < 6:
					line = line.split(":")
					zx = [int(line[1]), int(line[2].rstrip("\n"))]
					self.factors[line[0]] = zx
				else:
					self.caf = line.split(",")
					self.caf[len(self.caf)-1].rstrip("\n")
	
	def calculate(self):
		self.get_input()
		self.caf = map(int, self.caf)
		self.caf = sum(self.caf)
		self.caf = (0.65 + (0.01 * self.caf))
		for key in self.factors.keys():
			self.ufp += (self.weight[key][self.factors[key][1]] * self.factors[key][0])
		print("ufp: {}".format(self.ufp))
		print("caf: {}".format(self.caf))
		print("function point value is: {}".format(self.ufp * self.caf))



if __name__ == '__main__':
	fpoint = Fpoint("fpoint.txt")
	fpoint.calculate()


