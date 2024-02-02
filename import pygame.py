import pygame
import time
from random import randint #random digunakan untuk TULISAN CLIKNYA
pygame.init() #menginisiasikan awal ketika ingin membuat game


"membuat jendela program (kanvas/background/kotak)"
back = (200, 255, 255) #warna latar belakang (back, mw adalah variabel)
mw = pygame.display.set_mode((500, 500)) #jendela utama (untuk mengatur ukuran game (500,500))
mw.fill(back) #untuk memberikan warna dari mw
clock = pygame.time.Clock() #utk inisiasi waktu awal


"kelas segiempat"
class Area(): #area adalah hithbox
   def __init__(self, x=0, y=0, width=10, height=10, color=None): #menginisiasikan/memberikan value parameter supaya menghindari error (widht & height adalah panjang & lebar)
       self.rect = pygame.Rect(x, y, width, height) #segiempat
       self.fill_color = color
   def color(self, new_color):
       self.fill_color = new_color
   def fill(self): #untuk memgisi warna seluruhnya yang ada di dalam box/hithboxny
       pygame.draw.rect(mw, self.fill_color, self.rect)
   def outline(self, frame_color, thickness): #outline segiempat yang sudah ada
       pygame.draw.rect(mw, frame_color, self.rect, thickness) 
   def collidepoint(self, x, y): #posisi objeknya (harus click yg mana)
       return self.rect.collidepoint(x, y)


'''kelas label'''
class Label(Area):
   def set_text(self, text, fsize=12, text_color=(0, 0, 0)): #untuk tulisan yang time&point
       self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
   def draw(self, shift_x=0, shift_y=0): #untuk posisi gambarnya
       self.fill()
       mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


RED = (255, 0, 0)
GREEN = (0, 255, 51)
YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
cards = []
num_cards = 4
x = 70 #posisi kordinat awalnya


#untuk mendefinisikan waktu awalnyaa(tiap detik)
start_time = time.time()
cur_time = start_time


time_text = Label(0, 0, 50, 50, back)
time_text.set_text("Time:", 50, DARK_BLUE)
time_text.draw(25, 25)


time_num = Label(35, 55, 80, 80, back)
time_num.set_text("0", 50, DARK_BLUE)
time_num.draw(25, 25)


point_text = Label(350, 0, 50, 50, back)
point_text.set_text("Point:", 50, DARK_BLUE)
point_text.draw(25, 25)


point_num = Label(380, 55, 80, 80, back)
point_num.set_text("0", 50, DARK_BLUE)
point_num.draw(25, 25)


#digunakan untuk membuat cardnya (kotak/kartu)
for i in range(num_cards):
   new_card = Label(x, 170, 70, 100, YELLOW)
   new_card.outline(BLUE, 10)
   new_card.set_text('CLICK', 26) #knp disini ada 2, diatas ada 3.. karena diawal sdh didefiniskan & yang dimau sma
   cards.append(new_card) #append digunakan untk menambahkan di dlm list
   x = x + 100 #untuk memberikan jarak/batasan


point = 0


wait = 0 #digunakan untuk mendefinisikan waktu awal
while True: #WHILE TRUE akan melooping selamanya(forever)
   if wait == 0:
       #memindahkan label:
       wait = 30 #untuk berapa banyak kutu label akan berada di satu tempat
       click = randint(1, num_cards)
       for i in range(num_cards):
           cards[i].color((255,255,0))
           if (i + 1) == click:
               cards[i].draw(10, 40)
           else:
               cards[i].fill()
   else:
       wait -= 1
   #headling interaksi antara mouse/
   for event in pygame.event.get():
       #pygame.MOUSEBUTTONDOWN untuk mendeteksi klik kiri, event.button == 1 untuk
       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           x,y = event.pos
           for i in range (num_cards):
               if cards[i].collidepoint(x,y):
                   if i+1 == click:
                       cards[i].color(GREEN)
                       point += 1
                   else:
                       cards[i].color(RED)
                       point -= 1
                   cards[i].fill() #mengembalikan warna semula
                   point_num.set_text(point, 50, DARK_BLUE)
                   point_num.draw(25, 25)
   new_time = time.time()
   if int(new_time) - int(cur_time) == 1: #periksa apakah ada perbedaan 1 detik antara waktu lama dan baru
       time_num.set_text(str(int(new_time - start_time)),40, DARK_BLUE)
       time_num.draw(25, 25)
       cur_time = new_time
   #untuk waktu kalah
   if new_time - start_time  >= 11:
       lose = Label(0, 0, 700, 700, RED)
       lose.set_text("Waktunya sudah habis!!!", 60, DARK_BLUE)
       lose.draw(110, 180)
               
   if point >= 5:
       win = Label(0, 0, 500, 500, GREEN)
       win.set_text("Anda menang!!!", 60, DARK_BLUE)
       win.draw(140, 180)
      


   pygame.display.update() #selalu adaa di akhir python game
   clock.tick(40) #fps (frame per seconds)
