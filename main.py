def check_winner():
    if choice == opponent_choice:
        basic.show_string("Tie")
    elif choice == "Rock":
        if opponent_choice == "Paper":
            basic.show_leds("""
                # . . . .
                                # . . . .
                                # . . . .
                                # . . . .
                                # # # # .
            """)
        else:
            basic.show_leds("""
                # . # . #
                                # . # . #
                                # . # . #
                                # . # . #
                                . # . # .
            """)
    else:
        pass

def on_button_pressed_a():
    global choice
    basic.show_icon(IconNames.SQUARE)
    choice = "Rock"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global choice
    basic.show_icon(IconNames.NO)
    choice = "Scissors"
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global opponent_choice
    opponent_choice = receivedString
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global choice
    basic.show_icon(IconNames.CHESSBOARD)
    choice = "Paper"
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.send_string(choice)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

opponent_choice = ""
choice = ""
choice = "None"
opponent_choice = ""
radio.set_group(1)

def on_forever():
    check_winner()
basic.forever(on_forever)
