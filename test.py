points = 0
question_number = 1
right_question_counter = 0
quest_in_raw= 5

# на якій мові задаємо питання
lang = input("На каком языке играем ? (eng / укр)")
if lang == "eng":
  ans = input(str(question_number) + " - What color is the Sun ? (1 - yellow / 2 - black )")
else:
  ans = input(str(question_number) + " - Какого цвета солнце ? (1 - жёлтое / 2 - чёрное )")


if ans == "1":
  if right_question_counter >= quest_in_raw:
    points = points + 2
  else:
    points = points + 1
  right_question_counter = right_question_counter + 1
  if lang == "eng":
    print("Yes, you are right !")
  else:
    print("Да, ты прав !")
else:
  right_question_counter = 0
  if lang == "eng":
    print("wrong answer !")
  else:
    print("неправильный ответ !")

question_number = question_number + 1
if lang == "eng":
  ans = input(str(question_number) + " - The water is wet ? (1 - yes / 2 - no)")
else: 
  ans = input(str(question_number) + " - Вода мокрая ? (1 - да / 2 - нет)")

if ans == "да":
  if right_question_counter >= quest_in_raw:
    points = points + 2
  else:
    points = points + 1
  right_question_counter = right_question_counter + 1
  # на якій мові відповідаємо
  if lang == "eng":
    print("Yes, you are right !")
  else:
    print("Да, ты прав !")

else:
  right_question_counter = 0
  # на якій мові відповідаємо
  if lang == "eng":
    print("wrong answer !")
  else:
    print("неправильный ответ !")

# варіанти відповіді
print("Молодець, ви виграли - ваши бали: " + str(points))
print("Молодець, ви виграли - ваши бали: ", points)