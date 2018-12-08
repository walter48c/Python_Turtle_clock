import turtle
from datetime import *


def skip(step):

    turtle.penup()
    turtle.forward(step)
    turtle.pendown()


def mkHand(name, length):

    # 注册Turtle形状，建立表针Turtle
    turtle.reset()  # 清空当前窗口，并重置位置等信息为默认值
    skip(-length * 0.1)
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    turtle.end_poly()
    handForm = turtle.get_poly()
    turtle.register_shape(name, handForm)

def Init():
    global secHand, minHand, hurHand, printer
    turtle.mode("logo")  # 重置Turtle指向北
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 135)
    mkHand("minHand", 110)
    mkHand("hurHand", 90)
    secHand = turtle.Turtle()
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    # 建立输出文字Turtle
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()

def SetupClock(radius):
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            turtle.forward(20)
            skip(-radius - 20)
        else:
            turtle.dot(5)
            skip(-radius)
        turtle.right(6)

def Week(t):
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]


def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d %d" % (y, m, d)


def Tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)  # 设置朝向，每秒转动6度
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)

    turtle.tracer(False)  # 不显示绘制的过程，直接显示绘制结果
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(50)
    printer.write("Aide_Wu", align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    turtle.tracer(True)

    turtle.ontimer(Tick, 1000)  # 1000ms后继续调用tick

def main():
    turtle.tracer(False)  # 使多个绘制对象同时显示
    Init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    turtle.mainloop()


if __name__ == "__main__":
    main()
