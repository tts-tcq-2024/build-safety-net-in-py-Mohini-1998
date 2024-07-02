def generate_soundex(name):
    if not name:
        return ""
 
    soundex = []
    name = name.upper()
    soundex.append(name[0])
 
    mapping = {
        'BFPV': '1',
        'CGJKQSXZ': '2',
        'DT': '3',
        'L': '4',
        'MN': '5',
        'R': '6'
    }
 
    prev_code = mapping.get(name[0], '0')
 
    for char in name[1:]:
        for key in mapping:
            if char in key:
                code = mapping[key]
                if code != '0' and code != prev_code:
                    soundex.append(code)
                    prev_code = code
                break
        else:
            prev_code = '0'
 
        if len(soundex) == 4:
            break
 
    soundex.extend(['0'] * (4 - len(soundex)))
 
    return ''.join(soundex[:4])
