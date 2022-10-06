original_hourly_wage = 10
print('original hourly wage is: ', original_hourly_wage)

percentage_increase = 0.03
print('percentage increase is: ', percentage_increase)

number_of_years_of_good_review = 5
print('number of years of good review is:', number_of_years_of_good_review)
w = original_hourly_wage * ((1 + percentage_increase) ** number_of_years_of_good_review)
print('hourly wage this employee is earning after 5years of consistent good review is : ', w)

number_of_years_of_bad_review = 2
percentage_decrease = -0.03
original_hourly_wage = w
print('number of years of bad review is:', number_of_years_of_bad_review)
w = original_hourly_wage * ((1 + percentage_decrease) ** number_of_years_of_bad_review)
print('houely wage this employee is earning after 2years of bad review is: ', w)
