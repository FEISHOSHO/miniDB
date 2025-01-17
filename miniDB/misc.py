import operator

#FUNCTION TO CHECK IF A NUMBER IS WITHIN A RANGE
def between(to_be_checked,range):
    range=range.split("&")
    if(type(to_be_checked)==int or type(to_be_checked)==float):
        #THIS CONVERTS THE RANGE TO FLOATS FOR WHEN WE HAVE TO PERFORM NUMERICAL COMPARISONS
        r=[]
        r.append(float(range[0]))
        r.append(float(range[1]))
        range=r
    if(to_be_checked>range[0] and to_be_checked<range[1]):
        return True
    else:
        return False

def get_op(op, a, b):
    '''
    Get op as a function of a and b by using a symbol
    '''
    ops = {'>': operator.gt,
                '<': operator.lt,
                '>=': operator.ge,
                '<=': operator.le,
                '=': operator.eq,
                #DIFFERENCE OPERATOR
                'not'.casefold(): operator.ne,
                'between'.casefold():between}

    try:
        return ops[op](a,b)
    except TypeError:  # if a or b is None (deleted record), python3 raises typerror
        return False

def split_condition(condition):
    ops = {'>=': operator.ge,
           '<=': operator.le,
           '=': operator.eq,
           '>': operator.gt,
           '<': operator.lt,
           #DIFFERENCE OPERATOR
           'not'.casefold(): operator.ne,
           'between'.casefold():between}

    for op_key in ops.keys():
        splt=condition.split(op_key)
        if len(splt)>1:
            left, right = splt[0].strip(), splt[1].strip()

            if right[0] == '"' == right[-1]: # If the value has leading and trailing quotes, remove them.
                right = right.strip('"')
            elif ' ' in right: # If it has whitespaces but no leading and trailing double quotes, throw.
                raise ValueError(f'Invalid condition: {condition}\nValue must be enclosed in double quotation marks to include whitespaces.')

            if right.find('"') != -1: # If there are any double quotes in the value, throw. (Notice we've already removed the leading and trailing ones)
                raise ValueError(f'Invalid condition: {condition}\nDouble quotation marks are not allowed inside values.')
            return left, op_key, right

def reverse_op(op):
    '''
    Reverse the operator given
    '''
    return {
        '>' : '<',
        '>=' : '<=',
        '<' : '>',
        '<=' : '>=',
        '=' : '='
    }.get(op)
