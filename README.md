# python-openlesson1
## Example of final code for game (module 2)
	dragon-fighter.py
	rogalik.py
	school-escape.py

## Один із варіантів - Потрібно розробити гру квіз (опитування).
(приклад у файлі - kahoot-game.py)  

Вимоги:  
- [ ]	1. На початку вивести на екран правила гри для користувача.  
- [ ] 	2. У грі мінімум 10 запитань (будь-які, не має значення) із варіантами відповіді.  
- 3. Кожне запитання супроводжується номером питання.  
- 4. Наприкінці потрібно вивести результат - кількість правильних відповідей чи балів.  
- (наприклад за вірну відповідь +1 бал)  
- 5. Відповідь супроводжувати текстом, наприклад "Правильно, + 1 бал", "Невірно"  

1 ускладнення  
	6. Варіантів відповіді більше ніж 2, наприклад: "Скільки вух у собаки (1, 2, 3)"  
	7. Не дати можливість ввести щось поза наданими варіантами відповіді.  
		(робимо перевірку що ввели, якщо жоден з варіантів не наш,  
		 пишемо, "не зрозумів, спробуй ще раз" - використовуємо цикл "while")  

2 ускладнення  
	8. Даємо можливість на початку гри обрати мову - eng / укр - і відповідно всі питання  
		 та відповіді показуємо на обраній мові. Можно скоротити кількість запитань до 7.  

3 ускладнення  
	9. Робимо супер_приз за вірні відповіді більш ніж 3 підряд - подвоєння балів.  
	10. Вигадайте самі якусь цікаву "фішку".  
