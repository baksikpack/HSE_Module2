# сельский палиндром, зато сам:)

def check_palindrome(palindrome):
    len_pal = int(len(palindrome))
    characters = list(palindrome)
    iteration_number = int(len_pal//2)

    for i in range(iteration_number):
        reverse_i = len_pal - i - 1
        if characters[i] != characters[reverse_i]:
            return False
    return True
