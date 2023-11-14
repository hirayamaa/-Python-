import pyinputplus as pyip

response = pyip.inputNum('>', min=4, lessThan=6)
print(response)
response = pyip.inputFloat('>', min=4.0)
print(response)


def adds_up_to_ten(numbers):
    number_list = list(numbers)
    for i, digit in enumerate(number_list):
        number_list[i] = int(digit)
    if sum(number_list) != 10:
        raise Exception(f'The digits must add up to 10 not {sum(number_list)}.')
    return int(numbers)


response = pyip.inputCustom(adds_up_to_ten)
