import os
import re

my_txt_path_1 = os.path.join("raw_data", "paragraph_1.txt")
my_txt_path_2 = os.path.join("raw_data", "paragraph_2.txt")
my_txt_path_3 = os.path.join("raw_data", "passage.txt")

def read_txt(my_txt_path):
    with open(my_txt_path, 'r') as txtfile:
        myText = txtfile.read()
    return myText

def print_results(myData):
    myData.lower()
    word_count = len(myData.split())
    sentence_count = len(myData.split('. '))
    total_letters = 0

    for word in myData.split():
        total_letters = total_letters + len(word)
        average_sentence_length = re.split("\W+", myData)


    print("Approximate Word Count:"+str(word_count))
    print("Approximate Sentence Count:"+str(sentence_count))
    print("Approximate letter count (per word):"+str(total_letters/word_count))
    print("Average sentence length (in words):"+str(len(average_sentence_length)/sentence_count))


def main():
    """main function."""
    read_txt_data = read_txt(my_txt_path_3)
    print_results(read_txt_data)


if __name__ == "__main__":
    main()
