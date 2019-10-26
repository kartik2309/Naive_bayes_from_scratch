from pandas import read_csv


def count_unique_features(df, col_number):
	decision_attr = df.iloc[:, col_number]
	decision_col = decision_attr.copy()
	unique_features = []

	for i in range(0, df.shape[0]):
		decision = decision_col[i]
		count_single_unique_attr = []
		count = 0

		if decision != 0:
			count_single_unique_attr.append(decision)
			count = count + 1

			for j in range(i + 1, data.shape[0]):
				if decision_col[j] == decision and decision_col[j] != 0:
					count = count + 1
					decision_col[j] = 0

		if count != 0:
			count_single_unique_attr.append(count)
			unique_features.append(count_single_unique_attr)

	return unique_features


def get_probability(unique_features):
	count = 0
	for i in range(0, len(unique_features)):
		count = unique_features[i][1] + count

	for i in range(0, len(unique_features)):
		unique_features[i][1] = unique_features[i][1]/count

	return unique_features


def conditional_count(df, col_number):
	no_of_columns = df.shape[1]
	no_of_rows = df.shape[0]
	decision_col = df.iloc[:, no_of_columns - 1]
	required_col = df.iloc[:, col_number]
	count = 0
	final_count = []

	unique_decisions = count_unique_features(data, no_of_columns - 1)
	unique_required = count_unique_features(data, col_number)
	decision_attr = decision_col.copy()
	required_attr = required_col.copy()

	for i in range(0, len(unique_required)):
		current_count = []
		current_required = unique_required[i][0]
		current_count.append(current_required)

		for j in range(0, len(unique_decisions)):
			current_decision = unique_decisions[j][0]
			current_count.append(current_decision)

			for k in range(0, no_of_rows):
				if required_attr[k] == current_required and decision_attr[k] == current_decision:
					count = count + 1
			current_count.append(count)
			final_count.append(current_count[:])
			count = 0
			del current_count[1:3]

	return final_count


def get_conditional_probability(unique_features):
	count = 0
	i = 0
	while i < len(unique_features) - 1:
		element = unique_features[i]
		count = count + unique_features[i][2]
		j = i+1
		while j <= len(unique_features) - 1  and unique_features[j][0] == element[0]:
			count = count + unique_features[j][2]
			j = j+1
		index = j
		for k in range(i, index):
			unique_features[k][2] = unique_features[k][2]/count
		count = 0
		i = index
	return unique_features


def obtain_probability(input, conditional_probabilities, condition):
	probability = 0
	for k in conditional_probabilities:
		if k[0] == input and k[1] == condition:
			probability = k[2]
			break

	return probability


def predict(input, data):
	predicted_decision = ''
	if len(input) != len(data.columns) - 1:
		print("Invalid Input Size!")
	else:
		bayes_probability = []
		current_highest = 0

		decision_attr = count_unique_features(data, len(data.columns) - 1)
		decision_prob = get_probability(decision_attr)
		for k in range(0, len(decision_attr)):
			prob_count = 1
			current_decision = decision_attr[k][0]
			for i in range(0, len(input)):
				current_feature = input[i]
				conditional_counts = conditional_count(data, i)
				condition_probabilities = get_conditional_probability(conditional_counts)
				probability = obtain_probability(current_feature, condition_probabilities, current_decision)
				prob_count = probability * prob_count
			prob_count = prob_count * decision_prob[k][1]
			temp_list = [decision_prob[k][0], prob_count]
			bayes_probability.append(temp_list)
		for j in range(0, len(bayes_probability)):
			if bayes_probability[j][1] > current_highest:
				current_highest = bayes_probability[j][1]
				predicted_decision = bayes_probability[j][0]

	return predicted_decision


data = read_csv("credit.csv")
input = ['31-40', 'High', 'No', 'Fair']
print("output for", input, ": ", predict(input, data))
