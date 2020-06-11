"""
CS 331 - Program #3
Name: Hao Jia
"""

import sys


"""
Strip the punctuation.
"""
def strip_Punctuation(sentence):
    arr = []
    non_punctuations = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for word in sentence:
        if word not in punctuations:
            non_punctuations += word
    arr.extend(non_punctuations.split())

    return arr


"""
Convert capital to lowercase and store word to vocabulary list
"""
def capital_to_lowercase(arr):
    for i in range (len(arr)):
        arr[i] = arr[i].lower()

    return arr


"""
Remove all punctuations, numbers and spaces from word list.
"""
def read_file(file_name):
    file = open(file_name)
    arr_1 = []
    arr_2 = []

    # Read training file and strip punctuations
    for sentence in file:
        arr_1 += strip_Punctuation(sentence)

    # Delete numbers which in the list
    for word in arr_1:
        if not word.isdigit():
            arr_2.append(word)

    arr_2 = capital_to_lowercase(arr_2)
    file.close()

    return arr_2


"""
Form the vocabulary.
The vocabulary consists of the set of all the words that are in the training data.
And keeping the vocabulary in alphabetical order.
"""
def create_vocabulary(arr):
    vocabulary = []

    # Convert capital to lowercase and store word to vocabulary list
    for word in arr:
        if word not in vocabulary:
            vocabulary.append(word)

    # Keep vocabulary in alphabetical order
    vocabulary.sort()

    return vocabulary


"""
Output the pre-processed training and testing data to two files called preprocessed_train.txt
and preprocessed_test.txt.
"""
def output_data(first_line, data, preprocessed_txt):
    file = open(preprocessed_txt, "w+")

    # Write the first line to preprocessed txt
    for i in range(len(first_line)):
        # the last attribution doen't follow a ", "
        if i == len(first_line) - 1:
            file.write(str(first_line[i]))
        else:
            file.write(str(first_line[i]) + ", ")
    file.write("\n")

    # Write the data to preprocessed txt
    for i in range(len(data)):
        for j in range(len(data[i])):
            # the last attribution doen't follow a ", "
            if j == len(data[i]) - 1:
                file.write(str(data[i][j]))
            else:
                file.write(str(data[i][j]) + ", ")
        file.write("\n")

    file.close()


"""
Convert the training and test data into a set of features.
"""
def get_preprocessed_data(vocabulary, preprocessed_txt, file_name):
    data = []
    first_line = vocabulary

    # Add "classlabel" in the last of feature array
    if first_line[len(first_line) - 1] is not 'classlabel':
        first_line.append('classlabel')

    file = open(file_name)

    # Read training file and strip punctuations
    for sentence in file:
        arr_1 = []
        temp_data = []

        arr_1 = strip_Punctuation(sentence)
        arr_1 = capital_to_lowercase(arr_1)

        # If the ith word in the vocabulary, the ith slot has the value 1,
        # If not, the ith slot has the value 0.
        for i in range(len(first_line) - 1):
            if first_line[i] in arr_1:
                temp_data.insert(i, 1)
            else:
                temp_data.insert(i, 0)

        # Set the classlabel
        temp_data.append(int(arr_1[-1]))
        data.append(temp_data)

    output_data(first_line, data, preprocessed_txt)
    file.close()
    return data


"""
Get the numbers of words, they are in the vocabulary or they are not
"""
def get_num_words(v, train):
    vocabulary = {}
    yes_vocabulary = {}
    no_vocabulary = {}
    yes = 0
    no = 0

    for t in train:
        for i in range(len(v) - 1):
            if t[i] is 1 and v[i] not in vocabulary:
                vocabulary[v[i]] = 1
            elif t[i] is 1:
                vocabulary[v[i]] += 1

    for t in train:
        for i in range(len(v) - 1):
            if t[i] is 1 and v[i] not in yes_vocabulary and t[len(t) - 1] is 1:
                yes_vocabulary[v[i]] = 1
            elif t[i] is 1 and t[len(t) - 1] is 1:
                yes_vocabulary[v[i]] += 1

    for t in train:
        for i in range(len(v) -1):
            if t[i] is 1 and v[i] not in no_vocabulary and t[len(t) - 1] is 0:
                no_vocabulary[v[i]] = 1
            elif t[i] is 1 and t[len(t) - 1] is 0:
                no_vocabulary[v[i]] += 1

    for t in train:
        if t[len(t) - 1] is 1:
            yes += 1
        else:
            no += 1

    return vocabulary, yes_vocabulary,no_vocabulary, yes, no


"""
Get the accuracy of the naive Bayes classifier by comparing the predicted class
label of each sentence in the test data to the actual class label
"""
def classifer(yes, no, vocabulary, yes_vocabulary, no_vocabulary, test_set, v, total_yes, total_no):
    num_correct = 0

    # Naive Bayes classifer
    for s in test_set:
        p_yes = yes/(yes + no)
        p_no = 1 - p_yes
        for i in range(len(v) - 1):
            if s[i] is 1:
                if v[i] not in yes_vocabulary:
                    p_yes = p_yes * (1/(total_yes + len(vocabulary)))
                elif v[i] in yes_vocabulary:
                    p_yes = p_yes * ((yes_vocabulary[v[i]] + 1) / (yes + 2))
                if v[i] not in no_vocabulary:
                    p_no = p_no * (1/(total_no + len(vocabulary)))
                elif v[i] in no_vocabulary:
                    p_no = p_no * ((no_vocabulary[v[i]]+1) / (no+2))
        if p_yes > p_no:
            result = 1
        else:
            result = 0
        if result is s[len(s) - 1]:
            num_correct += 1

    # Calculate the accuracy
    acc = num_correct / len(test_set)
    return num_correct, len(test_set), acc


"""
Print and write the result
"""
def print_result(train_data, test_data, train_correct, train_num, train_acc, test_correct, test_num, test_acc):
    file = open("result.txt","w+")

    print("Results #1: ")
    file.write("Results #1:\n")
    print("correct number: " + str(train_correct))
    file.write("correct number: " + str(train_correct) + "\n")
    print("total number: " + str(train_num))
    file.write("total number: " + str(train_num) + "\n")
    print("accuracy: " + str(train_acc))
    file.write("accuracy: " + str(train_acc) + "\n\n")

    print()
    print("Results #2: ")
    file.write("Results #2:\n")
    print("correct number: " + str(test_correct))
    file.write("correct number: " + str(test_correct) + "\n")
    print("total number: " + str(test_num))
    file.write("total number: " + str(test_num) + "\n")
    print("accuracy: " + str(test_acc))
    file.write("accuracy: " + str(test_acc) + "\n\n")

    file.close()


"""
Drive function
"""
def main():
    n = len(sys.argv)

    if n != 3:
        print("Please enter file names")
        exit()

    arr_1 = read_file(sys.argv[1])
    vocabulary = create_vocabulary(arr_1)
    train_data = get_preprocessed_data(vocabulary, "preprocessed_train.txt", sys.argv[1])
    test_data = get_preprocessed_data(vocabulary, "preprocessed_test.txt", sys.argv[2])
    v, yes_vocabulary,no_vocabulary, yes, no = get_num_words(vocabulary, train_data)

    total_yes = 0
    total_no = 0
    for i in yes_vocabulary:
        total_yes += yes_vocabulary[i]
    for i in no_vocabulary:
        total_no += no_vocabulary[i]

    train_correct, train_num, train_acc = classifer(yes, no, v, yes_vocabulary, no_vocabulary, train_data, vocabulary, total_yes, total_no)
    test_correct, test_num, test_acc = classifer(yes, no, v, yes_vocabulary, no_vocabulary, test_data, vocabulary, total_yes, total_no)
    print_result(train_data, test_data, train_correct, train_num, train_acc, test_correct, test_num, test_acc)


if __name__ == "__main__":
    main()
