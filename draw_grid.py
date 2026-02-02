import turtle as chiripah

def draw_grid(size, step):
    chiripah.speed(0)
    chiripah.color("gray")
    for x in range(-size, size + 1, step):
        chiripah.penup()
        chiripah.goto(x, -size)
        chiripah.pendown()
        chiripah.goto(x, size)
    for y in range(-size, size + 1, step):
        chiripah.penup()
        chiripah.goto(-size, y)
        chiripah.pendown()
        chiripah.goto(size, y)

    chiripah.penup()
    chiripah.goto(0,0)
    # chiripah.done()
# ??? CHIRIPAH ???
