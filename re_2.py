import re 
# sub() function
text = """
Download Python | Python.org
Python is a popular programming language for various purposes. 
Find the latest version of Python for different operating systems, download release notes
"""

regex = re.compile(r"Python")
result = re.sub(pattern=regex,"R", string=text)