import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
'''

# metaCharcters (need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )



pattern = re.compile(r'.')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:4])

print('\t tab')