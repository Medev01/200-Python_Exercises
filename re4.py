import re 
text = (
    "Please send an email to info@template.com or "
    "call to: 123-456-789."
)

replace_reg = re.compile(r"\d{3}-\d{3}-\d{3}")
''' Replace any Phone Number with starts *** .'''
hide_phone = '***-***-***'
result = re.sub(replace_reg, "***-***-***", string=text, flags=0)


print(result)