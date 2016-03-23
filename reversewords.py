import re
sentence=raw_input('Enter a sentence: ')
sentence=re.sub(r'[-\w]+', lambda w:w.group()[::-1], sentence)
print sentence