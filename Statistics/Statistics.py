import math

class Statistics:

	def __init__(self, dataset):

		self.dataset = dataset


	@property
	def no_of_datapoints(self):
		return len(self.dataset)


	def average(self, dataset=None):
		sum_of_data = 0

		if dataset==None:
			for data in self.dataset:
				sum_of_data += data
			return sum_of_data / self.no_of_datapoints
		else:
			for data in dataset:
				sum_of_data += data
			return sum_of_data / len(dataset)


	def sample_stadard_deviation(self, dataset=None, mean=None):
		if dataset==None:
			if mean==None:
				mean = self.average()
				numerator = sum(
							(self.dataset[i] - mean) ** 2
							for i in range(len(self.dataset)) 
					)
				return (numerator / (self.no_of_datapoints - 1)) ** 0.5
		else:
			numerator = sum(
						(dataset[i] - mean) ** 2
						for i in range(len(dataset)) 
				)
			return (numerator / (self.no_of_datapoints - 1)) ** 0.5



	def population_standard_deviation(self):
		
		mean = self.average()

		numerator = sum(
					(self.dataset[i] - mean) ** 2
					for i in range(len(self.dataset)) 
			)
		return (numerator / no_of_datapoints) ** 0.5



	def mean_absolute_deviation(self):

		mean = self.average()
		numerator = sum(
				abs(self.dataset[i] - mean)
				for i in range(len(self.dataset))
			)
		return numerator / self.no_of_datapoints



	def insertion_sort(self):

		length = len(self.dataset)

		for i in range(1, length):
			while i > 0:
				if self.dataset[i] < self.dataset[i - 1]:
					self.dataset[i], self.dataset[i - 1] = self.dataset[i - 1], self.dataset[i]
				i -= 1

		return self.dataset


	def no_of_datapoint_is_even(self):

		self.dataset = self.insertion_sort()
		no_of_datapoints = len(self.dataset)

		c1 = int(len(self.dataset) / 2)
		c2 = c1 + 1
		median1, median2 = self.dataset[c1 - 1], self.dataset[c1]
		median = (median1 + median2) / 2
		# If no. of datapoint in first & second portion is even
		if c1 % 2 == 0:
			if c2 % 2 != 0:
				f = (1 + c1) // 2 
				first_quartile1, first_quartile2 = self.dataset[f - 1], self.dataset[f]
				first_quartile = (first_quartile1 + first_quartile2) / 2

				s = (c2 + no_of_datapoints) // 2 
				third_quartile1, third_quartile2 = self.dataset[s - 1], self.dataset[s]
				third_quartile = (third_quartile1 + third_quartile2) / 2
		# If no. of datapoint in first & second portion is odd 
		if c1 % 2 != 0 & c2 % 2 == 0:
			f = int((1 + c1) / 2)
			s = int((c2 + no_of_datapoints) / 2)

			first_quartile, third_quartile = self.dataset[f - 1], self.dataset[s - 1]

		return third_quartile - first_quartile
	

	def no_of_datapoint_is_odd(self):

		self.dataset = self.insertion_sort()
		no_of_datapoints = len(self.dataset)

		c = math.ceil(no_of_datapoints / 2)
		median = self.dataset[c - 1]

		#----If no. of datapoint in first and second portion is odd ---#
		if c % 2 == 0:
			f = math.ceil((1 + (c-1)) / 2)
			s = math.ceil(((c+1) + no_of_datapoints) / 2)
			first_quartile = self.dataset[f - 1]
			third_quartile = self.dataset[s - 1]
		#----If no. of datapoints in first and second portion is even----#
		if c % 2 != 0:
			fq = math.ceil((1 + (c-1)) / 2)
			first_quartile1, first_quartile2 = self.dataset[fq-1], self.dataset[fq]
			first_quartile = (first_quartile1 + first_quartile2) / 2

			tq = math.ceil(((c+1) + no_of_datapoints) / 2)
			third_quartile1, third_quartile2 = self.dataset[tq-1], self.dataset[tq]
			third_quartile = (third_quartile1 + third_quartile2) / 2
		return third_quartile - first_quartile



	def interquartile_range(self):

		if len(self.dataset) % 2 ==0:
			return self.no_of_datapoint_is_even()

		else:
			return self.no_of_datapoint_is_odd()


	def z_score(self, data_point, mean, std_deviation):

		return (data_point - mean) / std_deviation


def bivariate_correlation_factor(co_ordinates):
	stat = Statistics(co_ordinates)

	x_dataset = [co_ordinates[i][0] for i in range(len(co_ordinates))]
	y_dataset = [co_ordinates[i][1] for i in range(len(co_ordinates))]

	mean_x = stat.average(x_dataset)
	mean_y = stat.average(y_dataset)

	std_deviation_x = stat.sample_stadard_deviation(x_dataset, mean_x)
	std_deviation_y = stat.sample_stadard_deviation(y_dataset, mean_y)

	return 1/(len(co_ordinates)-1) * sum(
			((x_dataset[i] - mean_x) / std_deviation_x) * ((y_dataset[i] - mean_y) / std_deviation_y)
			for i in range(len(x_dataset))
		)







data_set = [[1,1], [2,2], [2,3], [3,6]]

# s = Statistics()
print(bivariate_correlation_factor(data_set))	