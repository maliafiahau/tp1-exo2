input.onButtonPressed(Button.A, function () {
    led.unplot(x, y)
    x += -1
    led.plot(x, y)
    if (x < 0) {
        led.unplot(x, y)
        x = 4
        led.plot(x, y)
    }
})
input.onButtonPressed(Button.B, function () {
    led.unplot(x, y)
    x += 1
    led.plot(x, y)
    if (x > 4) {
        led.unplot(x, y)
        x = 0
        led.plot(x, y)
    }
})
let y = 0
let x = 0
x = 0
y = 0
led.plot(0, 0)
basic.forever(function () {
    while (y != 4) {
        led.unplot(x, y)
        y += 1
        led.plot(x, y)
        basic.pause(1000)
    }
    while (y != 0) {
        led.unplot(x, y)
        y += -1
        led.plot(x, y)
        basic.pause(1000)
    }
})
