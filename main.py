def on_button_pressed_a():
    global x
    led.unplot(x, y)
    x += -1
    led.plot(x, y)
    if x < 0:
        led.unplot(x, y)
        x = 4
        led.plot(x, y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global x
    led.unplot(x, y)
    x += 1
    led.plot(x, y)
    if x > 4:
        led.unplot(x, y)
        x = 0
        led.plot(x, y)
input.on_button_pressed(Button.B, on_button_pressed_b)

y = 0
x = 0
x = 0
y = 0
led.plot(0, 0)

def on_forever():
    global y
    while y != 4:
        led.unplot(x, y)
        y += 1
        led.plot(x, y)
        basic.pause(1000)
    while y != 0:
        led.unplot(x, y)
        y += -1
        led.plot(x, y)
        basic.pause(1000)
basic.forever(on_forever)
