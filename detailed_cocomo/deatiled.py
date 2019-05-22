import math


class Detailed:

	def __init__(self, in_file_name):
		self.in_file_name = in_file_name


	def main(self):
			i = int(0)
			cost_drivers = {}
			mp = {}
			tp = {}
			cocomo_coefficients = {}
			EAF = int(1)
			KLOC = int(0)
			cat = ""
			cat_of_project = ""
			with open (self.in_file_name, "r") as file:
				for line in file:
					i += 1
					if i is 1:
						rating = line.split(" ")
					elif i is 58:
						cat = line.split(" ")[1].rstrip("\n")
					elif i > 1 and i < 17:
						line = line.split(" ")
						cost_drivers[line[0]] = {rating[0]: line[1],  rating[1]: line[2], rating[2]: line[3],\
						rating[3]: line[4], rating[4]: line[5], rating[5].rstrip("\n"): line[6].rstrip("\n") }
					elif i > 17 and i < 21:
						line = line.split(" ")
						cocomo_coefficients[line[0]] = [line[1], line[2], line[3], line[4].rstrip("\n")]
					elif i > 41 and i < 57:
						line = line.split(" ")
						EAF *= float(cost_drivers[line[0]][line[1].rstrip("\n")])
					elif i is 60:
						KLOC = int(line.split(" ")[1].rstrip("\n"))
						if KLOC >= 320:
							cat_of_project = "Embedded_extra_large"
						elif (KLOC >= 128 and cat == "Embedded"):
							cat_of_project = "Embedded_large"
						elif (KLOC >= 128 and cat == "Semidetached"):
							cat_of_project = "Semidetached_large"
						elif (KLOC >= 32 and cat == "Semidetached"):
							cat_of_project = "Semidetached_medium"
						elif (KLOC >= 32 and cat == "Organic"):
							cat_of_project = Organic_medium
						else:
							cat_of_project = "Organic_Small"
					elif i is 23:
						mp_header = line.split(" ")

					elif i > 22 and i < 30:
						line = line.split(" ")
						mp[line[0]] = {mp_header[0]: line[1], mp_header[1]: line[2], mp_header[2]:line[3],\
						mp_header[3].rstrip("\n"): line[4], mp_header[4].rstrip("\n"): line[5].rstrip("\n")}
					elif i > 32 and i < 39:
						line = line.split(" ")
						tp[line[0]] = {mp_header[0]: line[1], mp_header[1]: line[2], mp_header[2]:line[3],\
						mp_header[3].rstrip("\n"): line[4], mp_header[4].rstrip("\n"): line[5].rstrip("\n")}
			
				a,b,c,d = map(float, cocomo_coefficients[cat])
				e = (a * math.pow(KLOC, b)) * EAF
				d = (c * math.pow(e, d)) 
				# print("{}: \n\tEffort applied person-moonth(E): {}\n\tDevelpment time in months(D): {}\n\tAverage staff size: {} persons\n\tproductivity: {} LOC/PM".format(cat,e,d, (e/d), KLOC/e))
				category = mp[cat_of_project]
				print(cat_of_project)
				print("phase wise effort distribution:")
				for key in category.keys():
					print("\t{}: \t{}".format(key, (float(category[key]) * e)))
				print("phase wise Develpment time distribution:")
				category = tp[cat_of_project]
				for key in category.keys():
					print("\t{}: \t{}".format(key, float(category[key]) * d))





if __name__ == '__main__':
	detailed = Detailed("detailed.txt")
	detailed.main()