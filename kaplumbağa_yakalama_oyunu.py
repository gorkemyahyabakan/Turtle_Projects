import turtle
import random
turtle_ekranı=turtle.Screen()
skor=0
game_over=False
turtle_ekranı.bgcolor("pink")
turtle_ekranı.title(" Kaplumbağaları Yakala :) ")
turtlelar=[] ## turtle lara kolay ulaşmak için oluşturduk.
turtle_skor=turtle.Turtle()
sanıye_turtle=turtle.Turtle()
FONT=("Arial","30","normal")
def skor_turtle():
   turtle_skor.hideturtle()
   turtle_skor.color("purple")
   turtle_skor.pensize(3)
   turtle_skor.penup()
   turtle_skor.setpos(0,300)
   turtle_skor.write(arg="Skor: 0",move=False,align="center",font=FONT)

x_koordinat=[-200,-100,0,100,200]
y_koordinat=[200,100,0,-100]

def turtle_olustur(x,y):
   a=turtle.Turtle()
   def tıklama(x,y):
       global skor
       skor+=1
       turtle_skor.clear()
       turtle_skor.write(arg=f"Skor:{skor}",move=False,align="center",font=FONT)
       
   a.onclick(tıklama)
   a.penup()
   a.shape("turtle")
   a.color("purple")
   a.shapesize(3,3)
   a.goto(x,y)
   turtlelar.append(a)  ## rahatça erişmek adına turtle ları listeye attık.

def turtlelar_eklenıyor():
 for x in x_koordinat:
    for y in y_koordinat:
        turtle_olustur(x,y)
def turtle_gızle():
   for a in turtlelar:
      a.hideturtle()   ### turtle lar listesinde gezinerek her turtle ı tek tek gizledik.
def rastgelegoster():
   if not game_over:  ### oyun devam ettiği sürece kısacası game over false olduğu sürece bunu yap demek.
    turtle_gızle()
    a=random.choice(turtlelar)            ### rastgele gösterde önce turtle ları gizledik 500 milisaniyede bir turtle gözsterilirken diğerinin silinmesi için.
    a.showturtle()           ### recursive yaptık bir fonkun içinde kendini kullandık bu sayede sürekli gerçekleştirecek.
   turtle_ekranı.ontimer(rastgelegoster,500)
def sanıyesay(time):
   global game_over
   sanıye_turtle.hideturtle()
   sanıye_turtle.color("purple")
   sanıye_turtle.pensize(3)
   sanıye_turtle.penup()
   sanıye_turtle.setpos(0,250)
   sanıye_turtle.clear()
   if time>0:
      sanıye_turtle.clear()
      sanıye_turtle.write(arg=f"Time:{time}",move=False,align="center",font=FONT)  
      turtle_ekranı.ontimer(lambda:sanıyesay(time-1),1000)  ## sadece fonk çağırdığımız için lambda kullandık.
   else:  
      game_over=True
      sanıye_turtle.clear()  ## game over true olduğunda oyun bitmiştir demek ve saniye silinir turtle lar gizlenir ve oyun bitti yazdım.
      sanıye_turtle.write(arg="OYUN BİTTİ",move=False,align="center",font=FONT)
      turtle_gızle()


turtle.tracer(0)   ### animasyonları kaldırır her şey pat diye oluşur.
skor_turtle()
turtlelar_eklenıyor()
turtle_gızle()
rastgelegoster()
sanıyesay(10)
turtle.tracer(1)   ### eski haline getirdik getirmezsek ekranda bir şey gözükmez.

turtle.mainloop()
