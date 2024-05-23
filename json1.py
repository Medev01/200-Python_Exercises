import json
from pprint import pprint

'''
Using the built-in json module
load the above text into the 
dictionary named employees.
'''

employees_json = """
{"IT": [{"employee_id": "0010", "stack": ["Python", "Java", "AWS", "Docker", "Linux"], "experience": 5},
{"employee_id": "0360", "stack": ["Python", "AWS", "Docker", "Linux", "Azure"], "experience": 6},
{"employee_id": "0323", "stack": ["Python", "AWS", "JavaScript"]}],
"Marketing": [{"employee_id": "0863", "stack": ["Google Analytics", "Google Ads", "Facebook Ads"]},
{"employee_id": "0543", "stack": ["Google Ads", "Facebook Ads"]}]}
"""

# Load the data into dictionary 
employees = json.loads(employees_json)
print(employees)

# Using pprint 
pprint(employees)

#print the names of all departments
for department in employees:
    print(department)

# print the data of all IT employees
pprint(employees['IT'])

