
import select_colors as s
import turtle

def draw(color1='cyan',color2='black'):
    turtle.color(color1,color2)
    turtle.speed(0)

    turtle.begin_fill()  # 开始填充颜色

    for i in range(36):
        turtle.left(10)
        turtle.fd(200)
        turtle.right(20)
        turtle.fd(200)
        turtle.right(160)
        turtle.fd(200)
        turtle.right(20)
        turtle.fd(200)
        turtle.right(180)

    turtle.end_fill()
    turtle.hideturtle()  # 隐藏画笔
    turtle.done()
    pass

if __name__ == '__main__':
    # print(s.color1,s.color2)
    draw(s.color1,s.color2)
