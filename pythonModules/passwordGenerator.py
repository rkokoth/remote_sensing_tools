import string
import random

'''
TODO: rename this to password generator. Modify it to include special characters
'''
def generate_password():
    special_character = random.choice(string.punctuation)
    upper_case_chr = random.sample(string.ascii_uppercase,12)
    lower_case_chr = random.sample(string.ascii_lowercase,12)
    sample_chrs = list("".join(upper_case_chr) + "".join(lower_case_chr) + special_character)
    random.shuffle(sample_chrs)
    return "".join(sample_chrs)
#generate_password()
