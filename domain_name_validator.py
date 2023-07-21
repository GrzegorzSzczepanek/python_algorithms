import re
def validate(domain):
    if len(domain) > 253: return False
    elif domain.count(".") > 127: return False
    elif "." not in domain or (domain[0] == "." or domain[0] == "-" or domain[-1] == "-" or domain[-1] == "."): return False
    elif bool(re.search(r'[^a-zA-Z0-9\.\-]', domain)): return False
    elif domain.split(".")[-1].isdigit(): return False
    elif len(list(filter(lambda x: len(x) > 63, domain.split(".")))) > 0: return False
    
    for i in range(1, len(domain)):
        if (domain[i] == "-" and domain[i - 1]  == ".") or (domain[i] == "." and domain[i - 1] in ".-"):
            return False
    
    
    return True
