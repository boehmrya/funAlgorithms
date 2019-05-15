import re

def validate_code(code):
    codeString = str(code)
    pattern = '(1|2|3).'
    result = re.match(pattern, codeString)
    if result != None:
        return True
    else:
        return False


validate_code(123)
validate_code(248)
validate_code(8)
validate_code(321)
validate_code(9453)
