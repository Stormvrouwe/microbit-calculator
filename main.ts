let schakelaar = 0
let cijfer_1 = 0
let cijfer_2 = 0
let werking = 0
input.onButtonPressed(Button.A, function () {
    if (schakelaar == 0) {
        cijfer_1 += 1
        basic.showNumber(cijfer_1)
    }
    if (schakelaar == 1) {
        cijfer_2 += 1
        basic.showNumber(cijfer_2)
    }
})
input.onButtonPressed(Button.AB, function () {
    werking += 1
    if (werking == 1) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.pause(100)
        basic.clearScreen()
    } else {
        if (werking == 2) {
            basic.showLeds(`
                . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
                `)
            basic.pause(100)
        } else {
            if (werking == 3) {
                basic.showLeds(`
                    # . . . #
                    . # . # .
                    . . # . .
                    . # . # .
                    # . . . #
                    `)
                basic.pause(100)
                basic.clearScreen()
            } else {
                if (werking == 4) {
                    basic.showLeds(`
                        . . # . .
                        . . . . .
                        # # # # #
                        . . . . .
                        . . # . .
                        `)
                    basic.pause(100)
                    basic.clearScreen()
                } else {
                    werking = 1
                    basic.showLeds(`
                        . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
                        `)
                    basic.pause(100)
                    basic.clearScreen()
                }
            }
        }
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    schakelaar += 1
    if (schakelaar == 2) {
        basic.showNumber(cijfer_1 + cijfer_2)
        if (werking == 1) {
            basic.showNumber(cijfer_1 + cijfer_2)
        } else {
            if (werking == 2) {
                basic.showNumber(cijfer_1 - cijfer_2)
            } else {
                if (werking == 3) {
                    basic.showNumber(cijfer_1 * cijfer_2)
                } else {
                    basic.showNumber(cijfer_1 / cijfer_2)
                }
            }
        }
    }
})
basic.forever(function () {
    werking = 0
    cijfer_1 = 0
    cijfer_2 = 0
    schakelaar = 0
})
