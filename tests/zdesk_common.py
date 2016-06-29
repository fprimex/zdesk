def islocation(s):
    return isinstance(s, str) and s.startswith('http') and s.endswith('.json')

def isstatuscode(s):
    return isinstance(s, str) and s.isdecimal() and len(s) == 3
