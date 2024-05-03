import re
 
text = "Python 3.11.1"
# Extract only the Numbers from thsi text
numbers = re.findall(r"\d",text)
# Extrcat only text 
characters = re.findall(r"[a-zA-Z]", text)

# extract all digits except zero as a
code = '0010-000-423'

# extracta list of the following values['0010', '000', '423', '22']
code1 = '0010-000-423-22'

digits = re.findall(r"[1-9]", string=code)
regGroups = re.compile(r"(\d+)")
results = regGroups.findall(code1)

# Second solution 
print(re.split(pattern='-', string=code1))

#extract from the following code2 a list of the following values: ['PL', '110']
code2 = 'PL code: XG-GH-110'
code2_r = re.findall(r"PL|\d+", string = code2)

# extract all e-mail addresses 
text1 = "Please send an email to info@template.com or sales-info@template.it"
emails = re.findall(r"[a-zA-Z0-9]+\W[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z]{2,}", string = text1)

# Exctract all words except the punctuations 
text2 = """Python plays a key role in our production pipeline.
Without it a project the size of Star Wars: Episode II would have been very difficult to pull off."""

split_result = re.split(pattern=r"\W+", string=text2)

# find all words that start with a capital letter
capital_words = re.findall(r"[A-Z]\w+", string=text2)

print(capital_words)
print(split_result)
print(emails)
print(code2_r)
print(results)
print(numbers)
print(characters)
print(digits)