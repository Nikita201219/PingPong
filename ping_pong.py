#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as tm

#создай окно игры
window = display.set_mode((700, 500))#set_mode функция которая создаёт экран рамезорм 700 на 500 (придаём картежем)
#задай фон сцены
display.set_caption('Пинг понг')#придаем название окну
background = transform.scale(image.load('pingfon.jpg'), (700, 500))#растягиваем и загружаем задний фон (картинку) и ставим ее под размеры окна (700, 500)

clock = time.Clock()#создали игровой таймер
FPS = 60#переменная FPS равна 60
'''
#модуль mixer который позволяет работать с музыкой
mixer.init()#подключение возможности использовать mixer
mixer.music.load('space.ogg')#считали музыку
mixer.music.play()#начать проигрывать музыку
mixer.music.set_volume(0.1)#music.set_wolume(0.5) делает звук в половину тише
gold = mixer.Sound('fire.ogg')#создает экземпляр класса .Sound
'''
class GameSprite(sprite.Sprite):#sprite.Sprite - из библиотеки pygame из модуля sprite ставим класс родитель Sprite
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (w, h))#создаем спрайт и растягиваем его на 65 и 65
        self.speed = player_speed
        self.rect = self.image.get_rect()#все спрайты будут прямоугольные
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):#метод reset нужен для того чтобы спрайт появился на экране
        window.blit(self.image, (self.rect.x, self.rect.y))#на окно window методом blit накладываем картинку self.image и она будет находиться в координатах self.rect.x, self.rect.y

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()#если какая-тот клавиша нажата то в key_pressed лежит True
        #управление первым спрайтом (то  что снизу)
        if key_pressed[K_s] and self.rect.y < 405:#если нажата стрелочка в право и координаты по иксу меньше 645
            self.rect.y += self.speed#перемещаем его по иксу на столько сколько равна скорость игрока
        if key_pressed[K_w] and self.rect.y > 10:#если нажата стрелочка в лево и координаты по иксу больше 0
            self.rect.y -= self.speed#перемещаем его по иксу на столько сколько равна скорость игрока
        #управление первым спрайтом (то что сверху)

    def update_r(self):
        key_pressed = key.get_pressed()#если какая-тот клавиша нажата то в key_pressed лежит True
        #управление первым спрайтом (то  что снизу)
        if key_pressed[K_DOWN] and self.rect.y < 405:#если нажата стрелочка в право и координаты по иксу меньше 645
            self.rect.y += self.speed#перемещаем его по иксу на столько сколько равна скорость игрока
        if key_pressed[K_UP] and self.rect.y > 10:#если нажата стрелочка в лево и координаты по иксу больше 0
            self.rect.y -= self.speed#перемещаем его по иксу на столько сколько равна скорость игрока
        #управление первым спрайтом (то что сверху)

player1 = Player('rocket.png', 5, 250, 5, 90, 90)
player2 = Player('rocket2.png', 605, 250, 5, 90, 90)
ball = GameSprite('ball.png', 305, 0, 3, 45, 45)

game = True#переменная game равна true
finish = False#переменная finish равна False если она будет равна True то игрок победил

font.init()#подключение возможности использовать объекты Font
font1 = font.SysFont('Arial', 70)#Установить шрифт / Создание объекта Font с параметрами: шрифт - по умолчанию (None самый первый который стоит в системе компьютера) кегль(размер шрифта) - 70
font2 = font.SysFont('Arial', 30)#Установить шрифт / Создание объекта Font с параметрами: шрифт - по умолчанию (None самый первый который стоит в системе компьютера) кегль(размер шрифта) - 30
win = font1.render('YOU WIN', True, (255, 215, 0))#создать видимую надпись "YOU WIN" желтого цвета (True/False - сглаживать пиксели текста или нет)
lose = font1.render('YOU LOSE', True, (255, 0, 0))#render/рендерить - создавать что-то

ball_x = 3
ball_y = 3

while game:#пока game будет True цикл не закончится
    
    for e in event.get():#для каждого события в списке событий совершаемых пользователем (отслеживаем то что нажимает пользователь)
        if e.type == QUIT:#если тип события(e.type) равен нажатие на крестик(QUIT) меняем значение game на false и заканчиваем цикл
            game = False#значение переменной game меняется на False

    if finish != True:
        window.blit(background, (0, 0))#помещаем фоновую картинку в начало точки координат

        player1.update_l()#теперь главный герой может двигаться при нажатии на стрелочки
        player2.update_r()#теперь главный герой может двигаться при нажатии на стрелочки

        player1.reset()#показываем главного героя на экране
        player2.reset()#показываем главного героя на экране
        ball.reset()

        ball.rect.x += ball_x#движение мячика по оси x
        ball.rect.y += ball_y#движение мячика по оси y
        
        if ball.rect.y > 455 or ball.rect.y < 0:
            ball_y *= -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball_x *= -1

    display.update()#обновление содержимого экрана (после каждого действия в цикле while экран отображается заново)
    clock.tick(FPS)#указываем частоту работы цикла while за 1 секунду
#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"
