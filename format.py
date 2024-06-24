""""" 
Program to right-justify a list of digit strings, 
by padding each string with zeros on the left to match the length of the longest string in the list.
Ntobeko Mhlongo
2024-04-16
"""""


def right_justify(strings):
    """
    Right-justifies a list of digit strings to the length of the longest string by padding with zeros.

    Args:
    strings (list): A list of digit strings.

    Returns:
    list: A new list where each string is right-justified to the length of the longest string.
    """
    long_string = longest(strings)
    numbers = []
    for string in strings:
        if len(string) != long_string:
            string = (long_string - len(string)) * '0' + string
        numbers.append(string)
    return numbers

def longest(strings):
    """
    Finds the length of the longest string in a list of strings.

    Args:
    strings (list): A list of strings.

    Returns:
    int: The length of the longest string in the list.
    """
    max_length = 0
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
    return max_length



# testformat.py
"""
>>> import format
>>> format.right_justify([])
[]
>>> format.right_justify(['1'])
['1']
>>> format.right_justify(['092346'])
['092346']
>>> format.right_justify(['1', '10'])
['01', '10']
>>> format.right_justify(['29', '3'])
['29', '03']
>>> format.right_justify(['002368', '9862', '100'])
['002368', '009862', '000100']
>>> a = ['32', '2236']
>>> format.right_justify(a) 
['0032', '2236']
>>> a[0] == '32'
True

"""

    
if __name__ == '__main__':
    import doctest
    doctest.testfile('format.py', verbose=True)
