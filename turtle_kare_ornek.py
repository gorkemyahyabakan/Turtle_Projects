import turtle
turtle_screen=turtle.Screen()
turtle_screen.bgcolor("blue")
turtle_screen.title("turtle ornek")
turtle1=turtle.Turtle()
for eleman in range(1,5):  ### range ile dögümüzü 4 defa gerçekleştiriyoruz.
    turtle1.forward(100)
    turtle1.left(90)      #### her bir 100 piksellik düz çizgi sonucunda turtle'ı 90 derece döndürerek kare oluşmasını sağlıuoruz
turtle.done()