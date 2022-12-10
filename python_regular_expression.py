import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890


010-5551-1111
010.2222.1111
010*2222*1111
900-2222-1111
800-2222-1111
Ha haha

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

# metaCharcters (need to be escaped with "\"):
# . ^ $ * + ? { } [ ] \ | ( )

'''
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

'''

# pattern = re.compile(r'[89]00[-.]\d\d\d\d[-.]\d\d\d\d')
'''match the phone numbers start from 800 or 900 and 
using - or . to seperate number and four digits'''

# pattern = re.compile(r'[a-z]')
''' find charactor letter a to z'''

# pattern = re.compile(r'[^b]at')
'''except string not start with 'b' and second and third charactor is a t'''

# pattern = re.compile(r'\d{3}.\d{4}.\d{4}')
'''using exact numbers {}'''


# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w+')
'''start from 'Mr' and '.' be or not be and 'one capital chractor
and more then one letter'''

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)
#     print(match.start(), match.end())
#     print(match.group())
# print(pattern)
# print(text_to_search[1:4])
# print('\t tab')


#--------------------------------------------------
'''read data from txt file and phasing phone numbers'''

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# with open('regular_expression_data.txt', 'r', encoding='utf-8') as  f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
    
#     p_num = []
#     for match in matches:
#         print(match)

#-----------------------------------------------------
'''matching email address '''

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

#--------------------------------------------------
'''url'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# subbed_urls = pattern.sub(r'\2\3', urls)

# print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match.group(0))


#-----------------------------------------
'''sample'''


# sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'and')

# # matches = pattern.match(sentence) #only first word can search

# matches = pattern.search(sentence) #any word

# print(matches)

#-------------------------------------------------------
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.IGNORECASE)

matches = pattern.search(sentence)

print(matches)