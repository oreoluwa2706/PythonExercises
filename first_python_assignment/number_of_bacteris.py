print('hour     number_of_bacteria')

number = 0
while number < 4:
    # print(f'{number * 5}        {(200) * 2** (number * 5)}')

    print(f' %2d' % (number * 5), '%12d' % (200 * 2 ** (number * 5)))
    number += 1
