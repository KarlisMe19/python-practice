my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

my_str = '  hello world  '
string = '      hello       karl        welcome       t     o     python        '

trimmed_my_str = my_str.strip()
string = string.strip()
string = string.replace('karl','KARL')
print(trimmed_my_str)  # "hello world"
print(string.strip())

my_list = ['Hello', 'Karl', 'I', 'would', 'like', 'to', 'welcome', 'you', 'to', 'my', 'practice', 'google', 'colab', 'notebook']
my_list = ' '.join(my_list)
print(my_list)

mixed_list = {'Karl', 'Andrei', 'Garcia', 'Laurente'}
mixed_list = ' '.join(mixed_list)
print(mixed_list)

new_string = "Hi Vsauce, Michael here, what is a black hole?"
prefix_new_string = new_string.startswith('Hi')
print(prefix_new_string)

suffix_new_string = new_string.endswith('hole')
print(suffix_new_string)

string_index = new_string.find('e')
print(string_index)  # 6

print(len(new_string))

new_string_count = new_string.count('sauce')
print(new_string_count)

capitalized_new_string = new_string.capitalize()
print(capitalized_new_string)  # Hello world

uppercased_new_string = new_string.upper()
print(uppercased_new_string)  # HELLO WORLD

print(uppercased_new_string.isupper())

lowercased_new_string = new_string.lower()
print(lowercased_new_string.islower())

title_new_string = new_string.title()
print(title_new_string)  # Hello World

multiline_string = """
        Hello
My
        Name
      Is
              Karl
    Andrei
        Garcia
                Laurente
21      years           old          
"""

multiline_string = multiline_string.strip()
multiline_string = multiline_string.split()
single_line = ' '.join(multiline_string)
print(single_line)
capitalized_single_line = single_line.capitalize()
print(capitalized_single_line)
uppercased_single_line = single_line.upper()
print(uppercased_single_line)

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

message = "Hello my name is \"Karl\" and I am here today to teach you something \"important\"."

print(msg)
print(quote)
print(message)

print(single_line)
print('Hello' in single_line)  # True
print('hey' in multiline_string)    # False
print('hi' in multiline_string)    # False
print('e' in multiline_string)  # True
print('f' in multiline_string)  # False