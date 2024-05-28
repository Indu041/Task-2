def count_words(text):

   # Function to count the number of words in the input text.
  
    # Check if the input text is empty
    if not text.strip():
        return 0

    # Split the text into words based on spaces
    words = text.split()

    # Return the count of words
    return len(words)

print("Welcome to the Word Counter!")

        # Ask the user to input a sentence or paragraph
user_input = input("Please enter a sentence or paragraph : ")

        # Count the number of words in the input
word_count = count_words(user_input)

        # Print the word count
print("Word count:", word_count)
