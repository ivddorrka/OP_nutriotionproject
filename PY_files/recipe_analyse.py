"""
To modify recipes
"""

import re

# lst = ['1 1/2 tablespoon sugar', '2 3/4 pounds water', '1 cup keks']

def get_grams_of_product(lst): 
    """Having a list of ingredients finding one by one measurements"""
    result = []
    for i in lst:
        splitted = i.split()
        if 'ounce)' in splitted[:3] or 'ounces' in splitted[:3]:
            if 'ounce)' in splitted:
                num = splitted[1][1:]
                if '/' in list(num):
                    try:
                        first = float(num.split('/')[0])
                    except ValueError:
                        first = 1.0
                    second = float(num.split('/')[1])
                    res = first/second
                    grams = f'{round(28.35 * res, 3)} g'
                else:
                    grams = f'{round(28.35 * float(num), 3)} g'
            else:
                num = splitted[0]
                if len(splitted[1].split('/'))  == 2:
                    
                    first = float(splitted[1].split('/')[0])
                    second = float(splitted[1].split('/')[1])
                    res = first/second
                    grams = f'{round(28.35 * res * float(num), 3)} g'
                else:
                    if len(num.split('/')) == 2:
                        first = float(num.split('/')[0])
                        second = float(num.split('/')[1])
                        res = first/second
                        grams = f'{round(28.35 * res, 3)} g'
                    else:
                        grams = f'{round(28.35 * float(num), 3)} g'
            
        elif 'pound)' in splitted[:3] or 'pounds)' in splitted[:3]:
            num = splitted[1][1:]
            if '/' in list(num):
                first = float(num.split('/')[0])
                second = float(num.split('/')[1])
                res = first/second
                grams = f'{round(453.592 * res, 3)} g'
            else:
                grams = f'{round(453.592 * float(num), 3)} g'
        elif 'pound' in splitted[:3] or 'pounds' in splitted[:3]:
            num = splitted[0]
            if len(splitted[1].split('/')) == 2:
                first = float(splitted[1].split('/')[0])
                second = float(splitted[1].split('/')[1])
                res = first/second
                grams = f'{round(453.592 * res * float(num), 3)} g'
            else:
                if '/' in list(num):
                    first = float(num.split('/')[0])
                    second = float(num.split('/')[1])
                    res = first/second
                    grams = f'{round(453.592 * res, 3)} g'
                else:
                    grams = f'{round(453.592 * float(num), 3)} g'
        elif 'inch)' in splitted[:3]:
            num = splitted[1][1:]
            if '/' in list(num):
                first = float(num.split('/')[0])
                second = float(num.split('/')[1])
                res = first/second
                grams = f'{round(16.39 * res, 3)} g'
            else:
                grams = f'{round(16.39 * float(num), 3)} g'
            if 'x' in list(num):
                first = float(num.split('x')[0])
                second = float(num.split('x')[1])
                res = first*second
                grams = f'{round(16.39 * res, 3)} g'
            else:
                grams = f'{round(16.39 * float(num), 3)} g'

        elif 'tablespoon' in splitted or 'tablespoons' in splitted:
            number = splitted[0]
            if len(splitted[1].split('/')) == 2:
                first = float(splitted[1].split('/')[0])
                second = float(splitted[1].split('/')[1])
                grams = f'{round((first/second) * 17.07 * float(number), 3)} g'
            else:
                if '/' in list(number):
                    first = float(number.split('/')[0])
                    second = float(number.split('/')[1])
                    grams = f'{round((first/second) * 17.07,3)} g' # one tablespoon has 17.07 grams
                else:
                    grams = f'{round(float(number) * 17.07, 3)} g'
        
        elif 'teaspoon' in splitted or 'teaspoons' in splitted:

            number = splitted[0]
            if len(splitted[1].split('/')) == 2:
                first = float(splitted[1].split('/')[0])
                second = float(splitted[1].split('/')[1])
                grams = f'{round((first/second) * 5.69 * float(number), 3)} g'
            else:
                if '/' in list(number):
                    first = float(number.split('/')[0])
                    second = float(number.split('/')[1])
                    grams = f'{round((first/second) * 5.69,3)} g' # one teaspoon has 5.69 grams
                else:
                    grams = f'{round(float(number) * 5.69, 3)} g'

        elif 'cup' in splitted or 'cups' in splitted:

            number = splitted[0]
            if len(splitted[1].split('/')) == 2:
                first = float(splitted[1].split('/')[0])
                second = float(splitted[1].split('/')[1])
                grams = f'{round((first/second) * 128 * float(number), 3)} g'
            else:
                if '/' in list(number):
                    first = float(number.split('/')[0])
                    second = float(number.split('/')[1])
                    grams = f'{round((first/second) * 128,3)} g' # one cup has 128 grams
                else:
                    grams = f'{round(float(number) * 128, 3)} g'


        elif 'can' in splitted or 'cans' in splitted:

            number = splitted[0]
            if len(splitted[1].split('/')):
                first = float(splitted[1].split('/')[0])
                second = float(splitted[1].split('/')[1])
                grams = f'{round((first/second) * 305 * float(number), 3)} g'
            else:
                if '/' in list(number):
                    first = float(number.split('/')[0])
                    second = float(number.split('/')[1])
                    grams = f'{round((first/second) * 305,3)} g' # one cup has 128 grams
                else:
                    grams = f'{round(float(number) * 305, 3)} g'

        else:
            try:
            # if splitted[0]:
                grams = f'{int(splitted[0])} num'
            except ValueError:
                grams = '1 num'
            
        result.append(grams)

    return result

def get_product(lst):
    """To get products from a list of ingredients one by one"""
    list_portions = ['tablespoon', 'tablespoons', 'teaspoon', 'teaspoons', 'can', 'cans', 'cup', 'cups', 'pound', 'pounds', 'ounce', 'ounces']
    list_brackets = ['pounds)', 'pound)', 'inch)', 'ounce)', 'sticks)', 'stick)', 'stick', 'chopped', 'more)', 'chilled', 'unsweetened', 'sliced', 'thinly', 'cup)', 'cups)', 'lb', 'beaten', '']
    result = []
    for i in lst:
        by_koma = i.split(',')
        food_pos = by_koma[0].split()
        if len(i.split()) <=4:
            if i.split()[-1] != 'ADVERTISEMENT':
                if i.split()[1] not in list_portions:
                    food = ' '.join(i.split()[1:])
                else:
                    food = ' '.join(i.split()[2:])
            else:
                if i.split()[1] not in list_portions:
                    food = ' '.join(i.split()[1:-1])
                else:
                    food = ' '.join(i.split()[2:-1])
        elif len(i.split()) == 5:
            if len(i.split(',')) >=2:
                food = ' '.join(i.split(',')[0].split()[1:])
            else:
                if i.split()[-1] != 'ADVERTISEMENT':
                    food = ' '.join(i.split()[-2:])
                else:
                    food = ' '.join(i.split()[-3:-1])
        else:
            for j in range(len(food_pos)):
                try:
                    if food_pos[-3] not in list_portions and food_pos[-1][-1] != ')':

                        if food_pos[-1] == 'ADVERTISEMENT':
                            food = ' '.join(food_pos[-4:-1])
                        else:
                            food = ' '.join(food_pos[-3:])
                    else:
                        if food_pos[-1] == 'ADVERTISEMENT':
                            food = ' '.join(food_pos[-3:-1])
                        else:
                            food = ' '.join(food_pos[-2:])
                except IndexError:
                    if food_pos[-2] not in list_portions and food_pos[-1][-1] != ')':
                        if food_pos[-1] == 'ADVERTISEMENT':
                            food = ' '.join(food_pos[-4:-1])
                        else:
                            food = ' '.join(food_pos[-3:])
                    else:
                        food = ' '.join(food_pos[-1:])

                if food_pos[-1][-1] == ')':
                    new_here = by_koma[0].split('(')
                    for elements in new_here:
                        if elements in list_brackets:
                            food_pos1 = new_here[1].split()
                            if food_pos1[-2] not in list_portions and food_pos1[-1] == 'ADVERTISEMENT':
                                food = ' '.join(food_pos1[-4:-1])
                            else:
                                food = ' '.join(food_pos1[-3:])
                        else:
                            food_pos2 = new_here[0].split()
                            try:
                                if food_pos2[-2] not in list_portions and food_pos2[-1] == 'ADVERTISEMENT':
                                    food = ' '.join(food_pos2[-4:-1])
                                else:
                                    food = ' '.join(food_pos2[-3:])
                            except IndexError:
                                food = ' '.join(food_pos2[-1])
               
        if food not in result:
            result.append(food)

    food_result = []
    for i in range(len(result)):
        if result[i] == '':
            result[i] ='-'

    for foods in result:
        local_list_1 = foods.split()
        local_list_new = local_list_1[::-1]
        if 'soup' in local_list_1:
            local_list_new.append('cream of')

        local_list = local_list_new[::-1]

        if local_list[0] not in list_portions:
            if local_list[-1][-1] == ')' and local_list[-1] != '(optional)':
                food_result.append(foods[:-1])   
            elif local_list[-1] == '(optional)':
                food_result.append(' '.join(local_list[:-1]))        
            else:
                food_result.append(' '.join(local_list))
        else:
            if local_list[-1][-1] == ')' and local_list[-1] != '(optional)':
                food_result.append(' '.join(local_list[1:])[:-1])    
            elif local_list[-1] == '(optional)':
                food_result.append(' '.join(local_list[1:-1]))         
            else:
                food_result.append(' '.join(local_list[1:]))
    size = ['small', 'large', 'medium', 'extra-large', 'medium-dry']
    final_check = []
    unneeded = ['of', 'and', 'or', 'with', 'such', 'as']
    number_str = [str(i) for i in range(100)]

    for x in food_result:
        lst_here = x.split()
        res = ''
        for words in range(len(x.split())):
            # res = ' '
            if lst_here[words] not in list_portions and lst_here[words] not in unneeded and len(lst_here[words].split('/')) < 2 and lst_here[words] not in list_brackets and lst_here[words] not in size: 
                if lst_here[words] not in number_str:
                    if 'pound' not in lst_here[words].split('-'):
                        if lst_here[words] not in re.findall(r'^\d+[-]$', lst_here[words]):
                            res += f'{lst_here[words]} '
            # final_check.append(' '.join(lst_here))
        final_check.append(res)


    return final_check
# del lst[-1]
# print(get_product(lst))

def result_ingredients(lst):
    """To get a full list of ing.: measurements"""
    if lst[-1] == 'ADVERTISEMENT':
        del lst[-1]
    lst_measurements = get_grams_of_product(lst)
    lst_food = get_product(lst)
    if 'to taste' in lst_food:
        del lst_food[lst_food.index('to taste')]
    result = []
    for i in range(len(lst_food)):
        new_str = f'{lst_food[i]}: {lst_measurements[i]}'
        result.append(new_str)
    # nums = [str(i) for i in range(100)]
    final = []

    for i in range(len(result)):
        if len(result[i].split(' : ')[0]) > 1:
            # if result[i].split(' : ')[0][0] != '(' and result[i].split(' : ')[0][1] != ')':
            #     if 'pound' not in result[i][1].split('-'):
            #         if result[i][0] not in nums:
            final.append(result[i])

    return '\n'.join(final)




# lst = ['1 1/2 pounds fresh tuna steaks, minced ADVERTISEMENT', '1/2 cup dry bread crumbs ADVERTISEMENT', '1/4 cup finely chopped green onion ADVERTISEMENT', '1/4 cup grated carrot ADVERTISEMENT', '1 tablespoon minced fresh ginger root ADVERTISEMENT', '1 tablespoon chopped fresh cilantro ADVERTISEMENT', '1 teaspoon sesame oil ADVERTISEMENT', '1 tablespoon ketchup ADVERTISEMENT', '1 tablespoon lite soy sauce ADVERTISEMENT', '1/2 teaspoon ground cumin ADVERTISEMENT', '1/4 teaspoon salt ADVERTISEMENT', '1/4 teaspoon black pepper ADVERTISEMENT', '1 egg, beaten ADVERTISEMENT', '6 hamburger buns ADVERTISEMENT', '6 lettuce leaves - rinsed and dried ADVERTISEMENT', '2 medium tomatoes, sliced ADVERTISEMENT', 'ADVERTISEMENT']
# # lst = ['1 pound ground beef ADVERTISEMENT', '1 onion, chopped ADVERTISEMENT', '1 (16 ounce) can chili beans, with liquid ADVERTISEMENT', '1 (15 ounce) can kidney beans with liquid ADVERTISEMENT', '1 (15 ounce) can whole kernel corn, with liquid ADVERTISEMENT', '1 (8 ounce) can tomato sauce ADVERTISEMENT', '2 cups water ADVERTISEMENT', '2 (14.5 ounce) cans peeled and diced tomatoes ADVERTISEMENT', '1 (4 ounce) can diced green chile peppers ADVERTISEMENT', '1 (1.25 ounce) package taco seasoning mix ADVERTISEMENT', 'ADVERTISEMENT']
# # lst = ['1/4 cup vegetable oil ADVERTISEMENT', '1 head cauliflower, broken into small florets ADVERTISEMENT', '2 onions, chopped ADVERTISEMENT', '1 cup chopped tomato ADVERTISEMENT', '1/4 cup chopped fresh parsley ADVERTISEMENT', '1 jalapeno pepper, chopped ADVERTISEMENT', '1 teaspoon ground cumin ADVERTISEMENT', '1/2 teaspoon ground coriander ADVERTISEMENT', '1/2 teaspoon ground turmeric ADVERTISEMENT', '1 cup chicken broth ADVERTISEMENT', '1 clove garlic, minced ADVERTISEMENT', '1/2 teaspoon salt ADVERTISEMENT', 'ADVERTISEMENT']
# print(result_ingredients(lst))