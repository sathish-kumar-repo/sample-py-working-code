# 1. Create a List of Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)

# 2. Create a list of Even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# 3. Generate a List of characters from a string
string = "Hello, world!"
chars = [char for char in string if char.isalpha()]
print(chars)

# 4. Create a list of lengths of words in a sentence
sentence = "This is a Sample sentence"
word_length = [len(word) for word in sentence.split()]
print(sentence)
print(word_length)

# 5. Generate a list of tuples containing a number and its square
num_squares = [(x, x**2) for x in range(1, 6)]
print(num_squares)

# 6. Create a list of lowercase letters
lowercase_letter = [chr(x) for x in range(ord("a"), ord("z") + 1)]
print(lowercase_letter)

uppercase_letters = [chr(x) for x in range(ord("A"), ord("Z") + 1)]
print(uppercase_letters)

result = [x**2 if x % 2 == 0 else x**3 for x in range(1, 11)]
print(result)

common_multiples = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(common_multiples)

words = ["apple", "banana", "cherry"]
reversed_words = [word[::-1] for word in words]
print(words)
print(reversed_words)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


prime_numbers = [x for x in range(1, 51) if is_prime(x)]
print(prime_numbers)

result = [x**2 if x % 2 == 0 else x**3 for x in range(-5, 6)]
print(result)

words = ["apple", "banana", "cherry"]
word_lengths = [(word, len(word)) for word in words]
print(words)
print(word_lengths)

words = ["apple", "banana", "cherry"]
first_chars = [word[0] for word in words]
print(words)
print(first_chars)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = [x**2 for x in numbers if x % 2 == 0]
print(numbers)
print(squared_evens)

sentence = "This is a sample sentence."
uppercase_words = [word.upper() for word in sentence.split()]
print(sentence)
print(uppercase_words)
