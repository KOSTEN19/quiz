from urllib.parse import unquote
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q, F
from django.contrib.auth import authenticate, login, logout
from django.http import FileResponse
import hashlib
import logging
from pathlib import Path
from datetime import datetime, timezone, timedelta

data = [[ 'Дата рождения Тимофея', '16.0.2000', '17.06.2004', '18.07.2004', '19.08.2008', '2'],
[ 'Как хотели назвать Тимофея изначально', 'Руслан','Алексей','Леонид','Владлен','1'],
[ 'Сколько лет учился в школе', '10 лет','11 лет','12 лет','1 год ','3'],
[ 'Сколько у Тимофея родных братьев и сестер?', '1','2','3','4','3'],
[ 'Каким спортом занимался Тимофей в 4 года (первый вид спорта)?', 'плавание','футбол','хоккей','керлинг','1'],
[ 'В какой стране Тимофей впервые побывал за границей','Турция', 'Финляндия', 'ОАЭ', 'Украина','4'],
[ 'Любимый мультик Тимофея в детстве', 'Остров сокровищ', 'Лунтик', 'Лебеди Непрядвы', 'Губка Боб','3'],
['Какой язык Тимофею нравится больше всего?', 'Французский', 'Английский', 'Арабский','Говяжий','3' ],
[ 'По какому предмету Тимофей получил единственную пятерку за экзамен в первом семестре?', 'Матан', 'Информатика', 'Философия', 'География','4'],
['Сколько колес пробил Тимофей за год вождения на автомобиле?', '1', '2', '3', 'все 4','4'],
['В какую страну Тимофей впервые поехал в языкой лагерь', 'Великобритания', 'США', 'Канада', 'Мальта','4'],
[' Первый опыт работы Тимофея', 'Раздавал листовки','Языковой летний лагерь', 'Автосервис', 'Топ менеджер Газпрома','1'],
['Какую страну Тимофей посетил впервые без родителей с друзьями в 13 лет (не лагерь)', 'Турция', 'Китай', 'Нидерланды', 'Чехия','4'],
['Где у Тимофея находится дача', 'Рублевка', 'Дубайск', 'Витенево', 'Бахмут', '3'],
['За какой хоккейный клуб болел в детстве?', 'Спартак', 'ЦСКА', 'Атлант', 'Барыс','3' ],
['Какой самый разочаровывающий подарок получал от родителей на Новый год?', 'Шарик', 'ничего', 'будильник', 'книгу', '3'],
['Когда впервые сел за руль', 'Меньше года', '3 года','6 лет','10 лет' ,'1'],
['Какой суперспособностью обладал Тимофей в два года?','Умел читать','Легко учил стихи', 'Разговаривал на английском языке', 'знал все марки автомобилей','4'],
['Куда Тимофей ездил во время карантина?', 'Никуда (сидел дома)', 'Владивосток', 'Беларусь', 'Сочи','3'],
['С каким предметом связан план-капкан Тимофея и Георгия отмечаться в начале пары и уходить?', 'Логика' , 'Социология', 'Английский', 'Физрa','4']]
# ***.all().only('name'm'value') динамически подгружает остальные
# ***.all().valuse('name') {'val': 1} быстрее, но не подгружает остальные


def main_page(request):
    score=0
    number=0
    try:
        score = int(request.session.get('score'))
        number = int(request.session.get('number'))
    except:
        score = 0
        number = 0
    print(f'score: {score} number {number}')
    
    if request.method=='POST':
        try:
            ans= request.POST.get('answer')
            
        except:
            ans = 1
        #try:   
        print(type(score)) 
        print(f'score: {score} number" {number}')
        if  data[number][5]== ans:
            print('right')
            score+=1
        elif data[number][5] != ans:
            print('false')
        number+=1      
        if number==20:
            print('yes 20')
            if score==20:
                print('WIn')
                context={'win': 'True',
                'text': 'Вы приглашены на день рождения!!!'}
                response = render(request, 'main.html', context)
                return response
            else:
                print('LOSE')
                context={'win': 'False',
                'text': 'Вы не друг'}
                response = render(request, 'main.html', context)
                return response    
           # answer = Answer.objects.create(name=)

        print(ans)    
     

    request.session['number'] = number    
    request.session['score'] = score   
    print(f'score: {score} number" {number}')
    #request.session['nft_id'] = str(make)
    context = {
        'progres':number+1,
        'image': str(number+1)+'.jpg',
        'question':data[number][0],
         'answer1':data[number][1],
          'answer2':data[number][2],  
          'answer3':data[number][3],
          'answer4':data[number][4],
           }
    print(context)
    #    context.update({'folders':  GroupDocuments.objects.all()})
    response = render(request, 'main.html', context)
    return response
#


def restart_page(request):
    request.session['number'] = 0
    request.session['score'] = 0 
    return redirect('/')  

def scoreboard_page(request):
    pass

