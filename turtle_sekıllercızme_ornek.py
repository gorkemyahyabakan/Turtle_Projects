import turtle
turtle_screen=turtle.Screen()
turtle_screen.bgcolor("purple")
turtle_screen.title("sekıller çizme")
turtle1=turtle.Turtle()
kenar=3           ### kenar sayısını değiştirerek bir iç açısının ölçüsünü bulup ona göre turtle ı döndürüyoruz.
ıc_acı=360.0/kenar
for eleman in range(1,kenar+1):
    turtle1.right(ıc_acı)
    turtle1.forward(130)
turtle.done()