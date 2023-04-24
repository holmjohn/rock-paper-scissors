function check_winner () {
    if (choice == opponent_choice) {
        basic.showString("Tie")
    } else if (choice == "Rock") {
        if (opponent_choice == "Paper") {
            basic.showLeds(`
                # . . . .
                # . . . .
                # . . . .
                # . . . .
                # # # # .
                `)
        } else {
            basic.showLeds(`
                # . # . #
                # . # . #
                # . # . #
                # . # . #
                . # . # .
                `)
        }
    } else {
    	
    }
}
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Square)
    choice = "Rock"
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.No)
    choice = "Scissors"
})
radio.onReceivedString(function (receivedString) {
    opponent_choice = receivedString
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Chessboard)
    choice = "Paper"
})
input.onGesture(Gesture.Shake, function () {
    radio.sendString(choice)
})
let opponent_choice = ""
let choice = ""
choice = "None"
opponent_choice = ""
radio.setGroup(1)
basic.forever(function () {
    check_winner()
})
