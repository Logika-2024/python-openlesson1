points = 0 # бали гравця
# points = points + 1 - збільшеня значення
question_number = 1 # порядковий номер питання
right_question_counter = 0 # рахує правільні відповіді підряд
supergame_start_score = 3 # З якої правільні відповіді підряд починається супер_гра (+2 бали)

# на якій мові задаємо питання
lang = input("На каком языке играем ? (eng / будь що інше)")

def proper_lang_ans(arg, ans_true, ans_false):
  if arg == "eng":
    print(ans_true)
  else:
    print(ans_false)


if lang == "eng":
  ans = input(str(question_number) + " - What color is the Sun ? (1 - yellow / 2 - black )")
else:
  ans = input(str(question_number) + " - Какого цвета солнце ? (1 - жёлтое / 2 - чёрное )")


if ans == "1":
  if right_question_counter >= supergame_start_score:
    print("super_game_mode + 2 scores")
    points = points + 2
  else:
    points = points + 1
  right_question_counter = right_question_counter + 1
  proper_lang_ans(lang, "Yes, you are right !", "Так, ти прав !")

else:
  right_question_counter = 0
  proper_lang_ans(lang, "wrong answer !", "невірна відповідь !")

question_number = question_number + 1
if lang == "eng":
  ans = input(str(question_number) + " - The water is wet ? (1 - yes / 2 - no)")
else: 
  ans = input(str(question_number) + " - Вода мокрая ? (1 - да / 2 - нет)")

if ans == "1":
  if right_question_counter >= supergame_start_score:
    print("super_game_mode + 2 scores")
    points = points + 2
  else:
    points = points + 1
  right_question_counter = right_question_counter + 1
  # на якій мові відповідаємо
  proper_lang_ans(lang, "Yes, you are right !", "Так, ти прав !")

else:
  right_question_counter = 0
  # на якій мові відповідаємо
  proper_lang_ans(lang, "wrong answer !", "невірна відповідь !")

# варіанти відповіді
proper_lang_ans(lang, "Welldone, you win - " + str(points) + " points", "Молодець, ви виграли - " + str(points) + " балів")
