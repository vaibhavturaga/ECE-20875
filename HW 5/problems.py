import re

from numpy import true_divide

def problem1(searchstring):
    """
    Match phone numbers.

    :param searchstring: string
    :return: True or False
    """
    if(searchstring[0] == ' ' or searchstring[len(searchstring) - 1] == ' '):
        return False
    reg_main = re.search(r'(?:\+?([1]))?(\+[5][2])?[ ]*[(]*(\d{3})[- )]*(\d{3})[-]*(\d{4})', searchstring)
    reg = re.search(r'(\d{3})[-]*(\d{4})', searchstring)
    if reg_main is None and reg is None:
        return False
    else:
        return True
        
def problem2(searchstring):
    """
    Extract street name from address.

    :param searchstring: string
    :return: string
    """
    reg_main= re.search(r'([0-9]+[ ]*)\b[A-Z].*\b(Ave.|St.|Dr.|Rd.)', searchstring).group(0)
    reg_main = reg_main.rsplit(' ', 1)[0]
    invalid_strings = ["Ave.", "St.", "Dr.", "Rd."]

    reg_word = ""
    num_occur = False
    for word in reg_main.split(" "):
        if word.islower():
            reg_word == ""
        elif word.isdigit() and num_occur == True:
            reg_word = word
            reg_word += " "
        elif word.isdigit():
            reg_word += word
            reg_word += " "
            num_occur = True
        else:
            reg_word += word
            reg_word += " "
        
    reg_word = reg_word[:-1]
    
    reg_final = ""
    for word in reg_word.split(" "):
        if word in invalid_strings:
            break
        else:
            reg_final += word
            reg_final += " "
    
    reg_final = reg_final[:-1]
    
    return(reg_final)
    
def problem3(searchstring):
    """
    Garble Street name.

    :param searchstring: string
    :return: string
    """
    reg_main= re.search(r'([0-9]+[ ]*)\b[A-Z].*\b(Ave.|St.|Dr.|Rd.)', searchstring).group(0)
    reg_main = reg_main.rsplit(' ', 1)[0]
    invalid_strings = ["Ave.", "St.", "Dr.", "Rd."]

    reg_word = ""
    num_occur = False
    for word in reg_main.split(" "):
        if word.islower():
            reg_word == ""
        elif word.isdigit() and num_occur == True:
            reg_word = word
            reg_word += " "
        elif word.isdigit():
            reg_word += word
            reg_word += " "
            num_occur = True
        else:
            reg_word += word
            reg_word += " "
        
    reg_word = reg_word[:-1]
    
    reg_final = ""
    for word in reg_word.split(" "):
        if word in invalid_strings:
            break
        else:
            reg_final += word
            reg_final += " "
    
    reg_street = re.search(r"[^\d]+", reg_final).group(0)
    reg_final = searchstring.replace(reg_street, reg_street[::-1])
    return(reg_final)


if __name__ == '__main__' :
    print("\nProblem 1:")
    print("Answer correct?",problem1('+1 765-494-4600')==True)
    print("Answer correct?",problem1('+52 765-494-4600 ')==False)
    print("Answer correct?",problem1('+1 (765) 494 4600')==False)
    print("Answer correct?",problem1('+52 (765) 494-4600')==True)
    print("Answer correct?",problem1('+52 7654944600')==True)
    print("Answer correct?",problem1('494-4600')==True)

    print("\nProblem 2:")
    print("Answer correct?",problem2('The EE building is at 465 Northwestern Ave.')=="465 Northwestern")
    print("Answer correct?",problem2('Meet me at 201 South First St. at noon')=="201 South First")
    print("Answer correct?",problem2('Type "404 Not Found St" on your phone at 201 South First St. at noon')=="201 South First")

    print("\nProblem 3:")
    print("Answer correct?",problem3('The EE building is at 465 Northwestern Ave.')=="The EE building is at 465 nretsewhtroN Ave.")
    print("Answer correct?",problem3('Meet me at 201 South First St. at noon')=="Meet me at 201 tsriF htuoS St. at noon")
