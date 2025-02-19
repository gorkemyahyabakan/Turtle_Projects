import turtle
turtle_ekran=turtle.Screen()
turtle_ekran.title("interaktif çizim(created by görkem bakan)")
turtle_ekran.bgcolor("pink")
turtle_kalem=turtle.Turtle()
turtle_kalem.color("purple")
turtle_kalem.pensize(3)
def duzcızgı():
    turtle_kalem.forward(70)
def soladondur():
    turtle_kalem.left(90)
def sagadondur():
    turtle_kalem.right(90)
def silme():
    turtle_kalem.clear()
def turtlebaslangıca_don():
    turtle_kalem.penup()     ## bu fonksiyon çalıştığında kalemi kaldırır basa döner ve sonra tekrar indirir bu sayede başa dönerken aynı zamanda çizmez.
    turtle_kalem.home()
    turtle_kalem.pendown()
def kalemıkaldır():
    turtle_kalem.penup()
def kalemıındır():
    turtle_kalem.pendown()
turtle_ekran.listen()
turtle_ekran.onkey(fun=duzcızgı,key="space")  ## onkey fonksiyonu ile bir fonksiyonu bir tuşa aktarıyoruz ve o tuşa basıldığında o fonksion çalışır.
turtle_ekran.onkey(fun=soladondur,key="Up")  ## kalemi sola döndürür.
turtle_ekran.onkey(fun=sagadondur,key="Down") ##  kalemi sağa döndürür.
turtle_ekran.onkey(fun=silme,key="f") ## ekrana çizilen her şeyi siler
turtle_ekran.onkey(fun=turtlebaslangıca_don,key="b") ## en başlangıçta imlecimiz neredeyse oraya tekrar döner.
turtle_ekran.onkey(fun=kalemıkaldır,key="k")  ## kalemi kaldırır ve yazamayız
turtle_ekran.onkey(fun=kalemıındır,key="l")  ## kaldırılan kalemi indirerek tekrar çizmemizi sağlar.

turtle.mainloop()