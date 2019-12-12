# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define m = Character('Мику', color="#c8ffc8")
define t = Character('Твич хуич', color="#7FFF00")

define answers = 0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene office

    show test

    m "Вы совершили самоубийство и решили запустить Ren'Py."

    m "Кароче это пока что демка но она очень грустная скажу я вам."

    m "Пойдем на сцену посмотрим работает ли там чета ваще."
    
    scene stage
    
    show 123
    
    t "Это мое, я это облизал."
    
menu:
       t "Чье это?"
    
       "Твое, ты это облизал.":
        show 123
        t "Ого ты правильно ответил!"
        $ answers += 1
    
       "Говна облизни, сучий ты сын.":
        hide 123
        show test
        m "Тебе ппц от Твича, беги отсюда."
        hide test
        show 123
        t "ЩА ТЕБЯ ОБЛИЖУ, УЕБАН."
    
if answers>=1:
    
    jump  good_ending
    
else:
    
    jump sad_ending

label good_ending:

    scene office
    show test 
    
    m "Маладец."
    
    jump end_story
    
label sad_ending:

    scene stage
    show 123
    t "Беги, пиздоруха 0/15/2."
    
    jump end_story
    
label end_story: