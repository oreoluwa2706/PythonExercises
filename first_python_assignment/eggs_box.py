import math
egg_no = 28
egg_in_1_box = 6
boxes_needed = math.ceil(egg_no / egg_in_1_box)
print('no of boxes needed is: ', boxes_needed)

remaining_eggs = egg_no % egg_in_1_box
print('No of eggs placed in the remaining box is: ', remaining_eggs)

needed_eggs_to_fill_the_box = (egg_in_1_box - remaining_eggs)
print('no of eggs needed to fill the box is:', needed_eggs_to_fill_the_box)
