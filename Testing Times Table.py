import random
max_range = 20


def timestable_tester():
    num_1 = random.randint(1,max_range)
    num_2 = random.randint(1,max_range)
    print(f'{num_1} x {num_2} =')
    answer = int(input(''))
    if num_1 * num_2 == answer:
        print('good job')
    else:
        print(f'wrong the answer is {num_1 * num_2}')
def change_max_range():
    max_range = int(input('New max range(Default is 20)'))
    return max_range




max_range = change_max_range()
print(max_range)
while True:
    timestable_tester()