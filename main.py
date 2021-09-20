schakelaar = 0
cijfer_1 = 0
cijfer_2 = 0
werking = 0

def on_button_pressed_a():
    global cijfer_1, cijfer_2
    if schakelaar == 0:
        cijfer_1 += 1
        basic.show_number(cijfer_1)
    if schakelaar == 1:
        cijfer_2 += 1
        basic.show_number(cijfer_2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global werking
    werking += 1
    if werking == 1:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        basic.pause(100)
        basic.clear_screen()
    else:
        if werking == 2:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                # # # # #
                                . . . . .
                                . . . . .
            """)
            basic.pause(100)
        else:
            if werking == 3:
                basic.show_leds("""
                    # . . . #
                                        . # . # .
                                        . . # . .
                                        . # . # .
                                        # . . . #
                """)
                basic.pause(100)
                basic.clear_screen()
            else:
                if werking == 4:
                    basic.show_leds("""
                        . . # . .
                                                . . . . .
                                                # # # # #
                                                . . . . .
                                                . . # . .
                    """)
                    basic.pause(100)
                    basic.clear_screen()
                else:
                    werking = 1
                    basic.show_leds("""
                        . . # . .
                                                . . # . .
                                                # # # # #
                                                . . # . .
                                                . . # . .
                    """)
                    basic.pause(100)
                    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global schakelaar
    schakelaar += 1
    if schakelaar == 2:
        if werking == 1:
            basic.show_number(cijfer_1 + cijfer_2)
        else:
            if werking == 2:
                basic.show_number(cijfer_1 - cijfer_2)
            else:
                if werking == 3:
                    basic.show_number(cijfer_1 * cijfer_2)
                else:
                    basic.show_number(cijfer_1 / cijfer_2)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global werking, cijfer_1, cijfer_2, schakelaar
    werking = 0
    cijfer_1 = 0
    cijfer_2 = 0
    schakelaar = 0
basic.forever(on_forever)
