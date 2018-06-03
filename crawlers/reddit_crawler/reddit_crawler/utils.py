'''
Function from answer of Kimvais on stackoverflow
https://stackoverflow.com/questions/5459256/python-parse-a-string-with-custom-price-units?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
'''
def numerize(s):
    multipliers = {'k': 10**3, 'm': 10**6 }

    if s[-1] in multipliers:
        return float(s[:-1]) * multipliers[s[-1]]
    else:
        return int(s)

