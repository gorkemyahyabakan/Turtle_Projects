import turtle
turtle_pencere=turtle.Screen()
turtle_pencere.bgcolor("pink")
turtle_pencere.title("iç içe kareler(created by görkem bakan)")
turtlekalem=turtle.Turtle()
turtlekalem.color("white")   ### turtle' ın rengini değiştirdik.
turtlekalem.pensize(5)  ### turtle kalınlığını arttırdık.
kalemrenk=["black","brown","red","green"]
def forward(uzunluk):
    for kenar in range(4):
     turtlekalem.color(kalemrenk[kenar])  ## her farklı kenar değerinde farklı bir renk olacak turtle rengi.
     turtlekalem.forward(uzunluk)
     turtlekalem.left(90)
     uzunluk-=5   #### iç içe kare çizebilmek ve çizgilerin birbiri üstüne geçmemsi için her kenar değerinden bir sonraki 
                  #### kenar değerine geçilmeden önce düz gidilecek piksel uzunluğunu azaltıyoruz.
forward(260)
forward(240)
forward(220)
forward(200)
forward(180)
forward(160)
forward(140)
forward(120)
forward(100)
forward(80)
forward(60)
forward(40)
forward(20)

turtle.mainloop()

