import csv
import sys
import numpy as np
import statistics
from math import sqrt
from math import pi
from math import exp

# /*--------------------------------------------------------------------------*/
# /*--------------------------------------------------------------------------*/
# Functions for KNN

def generate_tests(test_file):
    tests = []
    with open(test_file) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            tests.append(row)
    return tests


def generate_distances(train, test):
    distances = []

    with open(train) as data:
        data = csv.reader(data, delimiter=',')
        line_count = 0
        for row in data:
            converted_row = [float(string_num) for string_num in row[:-1]]
            a = np.array(converted_row)
            dist = np.linalg.norm(a-test)
            distances.append(dist)
            line_count += 1

        return distances

def find_id(distances, k):
    numpy_distances = np.array(distances)
    nearest_neighbor_ids = numpy_distances.argsort()[:k]
    # nearest_neighbor_ids = [x+1 for x in nearest_neighbor_ids]

    return nearest_neighbor_ids

def find_classes(train, nearest_neighbor_ids):
    with open(train) as data:
        data = csv.reader(data, delimiter=',')
        classes = []
        line_count = 0
        for row in data:
            if line_count in nearest_neighbor_ids:
                classes.append(row[-1])
            line_count += 1

    return classes


def find_decision(classes):
    yes_count = 0
    no_count = 0

    for i in classes:
        if i =='yes':
            yes_count += 1
        else:
            no_count += 1

    if yes_count == no_count or yes_count > no_count:
        print('yes')
    else:
        print('no')


def k_neigh(train, test, k):
    # print(generate_distances(train,test))
    distances = generate_distances(train, test)
    ids = find_id(distances, k)
    # print(ids)
    classes = find_classes(train, ids)
    # print(classes)
    find_decision(classes)

# /*--------------------------------------------------------------------------*/
# /*--------------------------------------------------------------------------*/
# Functions for NB

def read_test(test_file):
    tests = []
    with open(test_file) as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            converted_row = [float(string_num) for string_num in row]
            tests.append(converted_row)
    return tests

# reads and loads data
def read_data(train):
    data_array = []
    with open(train) as data:
        data = csv.reader(data, delimiter=',')
        line_count = 0
        for row in data:
            if row[-1] == "yes":
                row[-1] = "1"
            else:
                row[-1] = "0"
            converted_row = [float(string_num) for string_num in row]
            data_array.append(converted_row)
        line_count += 1
    return data_array

# seperates classes
def classes(data):
    classes = {}
    for i in range(len(data)):
        row = data[i]
        classified = row[-1]
        if classified not in classes:
            classes[classified] = []
        classes[classified].append(row)
    return classes

def average(integers):
    return sum(integers)/float(len(integers))

def standard_dev(integers):
    return statistics.stdev(integers)

def data_summary(data):
    overview = []
    for col in zip(*data):
        temp = []
        temp.append(average(col))
        temp.append(standard_dev(col))
        temp.append(len(col))
        overview.append(temp)
    del(overview[-1])
    return overview

def class_summary(data):
    seperated = classes(data)
    overview = {}
    for value, rows in seperated.items():
        overview[value] = data_summary(rows)
    return overview

def probability_density_function(x, average, stdev):
    exponent = exp(-((x-average)**2 / (2 * stdev**2 )))
    result = (1 / (sqrt(2 * pi) * stdev)) * exponent
    return result

def probability_of_classes(overviews, data):
    string_labels = []
    for row in data:
        row_total = sum([overviews[label][0][2] for label in overviews])
        row_probabilities = {}
        for value, overview in overviews.items():
            row_probabilities[value] = overviews[value][0][2]/float(row_total)
            for i in range(len(overview)):
                average = overview[i][0]
                stdev = overview[i][1]
                row_probabilities[value] *= probability_density_function(row[i], average, stdev)

        top_label, top_prob = None, -1
        for value, probability in row_probabilities.items():
            if top_label is None or probability > top_prob:
                top_label = value
                top_prob = probability


        string_label = ""
        if top_label == 0:
            string_label = "no"
            string_labels.append(string_label)
        else:
            string_label = "yes"
            string_labels.append(string_label)
    return string_labels

def decision(predictions):
    for i in predictions:
        if i == "no":
            print("no")
        else:
            print("yes")

def naive_bayes(train_data, test_data):
    overview = class_summary(train_data)
    output = probability_of_classes(overview, test_data)
    return decision(output)

train = sys.argv[1]
test_file = sys.argv[2]
classifer = sys.argv[3]

if len(classifer) == 3:
    k = int(classifer[0])
    tests = generate_tests(test_file)
    for test in tests:
        converted_test = [float(string_num) for string_num in test]
        k_neigh(train, converted_test, k)

elif classifer  == "NB":
    train_data = read_data(train)
    test_data = read_test(test_file)
    naive_bayes(train_data, test_data)
