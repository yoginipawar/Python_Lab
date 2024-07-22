#Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"Total number of words: {word_count}")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the file name
count_words_in_file("ABC.txt")

#OUTPUT
Total number of words: 109
