import re

# Take input from the user
input_string = input("Enter a string: ").strip()

# Handle empty input
if not input_string:
    print("The input text is empty. Please enter valid text.")
else:
    # Filter out alphabetic characters only
    ch = [char for char in input_string if char.isalpha()]

    # Split the input_string into sentences using '.', '!', and '?' as delimiters
    sentences = re.split(r'[.!?]', input_string)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]  # Remove empty strings/spaces

    # Split the text into words
    words = input_string.split()

    # Calculate average letters per 100 words
    if len(words) == 0:
        print("No words found in the input.")
    else:
        l = (len(ch) / len(words)) * 100  # Average letters per 100 words
        s = (len(sentences) / len(words)) * 100  # Average sentences per 100 words

        # Coleman-Liau readability formula
        grade = (0.0588 * l) - (0.296 * s) - 15.8

        # Display the grade
        if grade > 16:
            print("Grade: 16+ (College Level or Above)")
        elif grade < 1:
            print("Grade: Before Grade 1")
        else:
            print(f"Grade: {round(grade)}")
        
        # Debugging Information (Optional)
        print("\n--- Debugging Info ---")
        print(f"Total Letters: {len(ch)}")
        print(f"Total Words: {len(words)}")
        print(f"Total Sentences: {len(sentences)}")
        print(f"Average Letters per 100 Words: {l:.2f}")
        print(f"Average Sentences per 100 Words: {s:.2f}")
