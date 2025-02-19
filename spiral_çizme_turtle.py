import turtle
turtle_ekran=turtle.Screen()
turtle_ekran.bgcolor("black")
turtle_ekran.title("turtle ile spiral çizmek(created by görkem bakan)")
turtle1=turtle.Turtle()
turtle1.color("pink")
turtlecolour_listesi=["orange","blue","green","purple","white","brown","red"] ## kalem rengini farklı farklı ypapmak için gezinebilinecek liste oluşturdum.
turtle1.speed(0) ## çok bekletmemek adına hızı arttırdım.(en yüksek hız 0'dır.)
for eleman in range(30):
    turtle1.color(turtlecolour_listesi[eleman%6]) ### eleman 7 olduğunda listede bir karşılığı olmayacak eleman%6 ile listeden çıkmasını önledik.
    turtle1.circle(10*eleman) ##her döngüde yarıçapı arttırdık.
    turtle1.circle(-10*eleman) ## -10 yarıçap vererek bir dairede alt tarafa çizdirdik.
    turtle1.left(eleman+5)  ## her döngüde 5 arttırarak döndürdük.
turtle.mainloop()