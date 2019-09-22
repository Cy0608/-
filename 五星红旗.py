from turtle import *
#画背景
color('red','red')
begin_fill()
while True:
    forward(288)
    right(90)
    forward(192)
    right(90)
    if abs(pos())<1:
        break
end_fill()
#大星星
penup()
setposition(19.2,-38.4)
pendown()
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(57.6)
    right(144)
end_fill()
#小星星1
penup()
setposition(86.4,-24)
pendown()
left(60)
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(19.2)
    right(144)
end_fill()
#小星星2
penup()
setposition(105.6,-40)
pendown()
right(30)
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(19.2)
    right(144)
end_fill()
#小星星3
penup()
setposition(105.6,-65.6)
pendown()
right(30)
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(19.2)
    right(144)
end_fill()
#小星星4
penup()
setposition(86.4,-80)
pendown()
right(30)
color('yellow','yellow')
begin_fill()
for i in range(5):
    forward(19.2)
    right(144)
end_fill()
penup()
setposition(0,0)
pendown()
done()














