def islocation(s):
    return isinstance(s, str) and s.startswith('http') and s.endswith('.json')

def isstatuscode(c):
    return isinstance(c, int) and 100 <= c <= 600
