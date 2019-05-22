-import math

class Cocomo:

	def __init__(self, basic_file, intermediate_file):
		self.basic_file = basic_file
		self.intermediate_file = intermediate_file


	def basic_cocomo(self):
		cocomo_coefficients = {}
		i = int(0)
		kloc = int(0)
		cat = ""
		with open(self.basic_file, "r") as file:
			for line in file:
				i+=1
				if i < 4 and i :
					line = line.split(" ")
					cocomo_coefficients[line[0]] = [line[1], line[2], line[3], line[4].rstrip("\n")]
				elif i is 4:
					line = line.split(" ")
					kloc = int(line[1].rstrip("\n"))
				elif i is 5:
					cat = line.split(" ")[1].rstrip("\n")

			a,b,c,d = map(float, cocomo_coefficients[cat])
			e = (a * math.pow(kloc, b))
			d = (c * math.pow(e, d)) 
			print("{}: \n\tEffort applied person-moonth(E): {}\n\tDevelpment time in months(D): {}\n\tAverage staff size: {} persons\n\tproductivity: {} LOC/PM".format(cat,e,d, (e/d), kloc/e))
	
	def intermediate_cocomo(self):
		i = int(0)
		cost_drivers = {}
		cocomo_coefficients = {}
		EAF = int(1)
		KLOC = int(0)
		cat = ""
		with open (self.intermediate_file, "r") as file:
			for line in file:
				i += 1
				if i is 1:
					rating = line.split(" ")
				elif i > 1 and i < 17:
					line = line.split(" ")
					cost_drivers[line[0]] = {rating[0]: line[1],  rating[1]: line[2], rating[2]: line[3],\
					rating[3]: line[4], rating[4]: line[5], rating[5].rstrip("\n"): line[6].rstrip("\n") }
				elif i > 17 and i < 21:
					line = line.split(" ")
					cocomo_coefficients[line[0]] = [line[1], line[2], line[3], line[4].rstrip("\n")]
				elif i > 22 and i < 38:
					line = line.split(" ")
					EAF *= float(cost_drivers[line[0]][line[1].rstrip("\n")])
				elif i == 41:
					KLOC = int(line.split(" ")[1].rstrip("\n"))
				if i is 39:
					cat = line.split(" ")[1].rstrip("\n")
		
			a,b,c,d = map(float, cocomo_coefficients[cat])
			e = (a * math.pow(KLOC, b)) * EAF
			d = (c * math.pow(e, d)) 
			print("{}: \n\tEffort applied person-moonth(E): {}\n\tDevelpment time in months(D): {}\n\tAverage staff size: {} persons\n\tproductivity: {} LOC/PM".format(cat,e,d, (e/d), KLOC/e))
	


if __name__ == '__main__':
	cocomo = Cocomo("basic_cocomo.txt", "intermediate_cocomo.txt")
	print("\tBASIC COCOMO")
	cocomo.basic_cocomo()
	print("="*60)
	print("\tINTERMADIATE COCOMO")
	cocomo.intermediate_cocomo()