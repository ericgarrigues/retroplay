import uinput

player_keys = {
    1: {
        1: uinput.KEY_LEFTCTRL,
        2: uinput.KEY_LEFTALT,
        3: uinput.KEY_SPACE,
        4: uinput.KEY_LEFTSHIFT,
        5: uinput.KEY_Z,
        6: uinput.KEY_X,
        7: uinput.KEY_ENTER,
        8: uinput.KEY_ESC,
        9: uinput.KEY_UP,
        10: uinput.KEY_DOWN,
        11: uinput.KEY_LEFT,
        12: uinput.KEY_RIGHT,
        13: uinput.KEY_1,
        14: uinput.KEY_5
    },
    2: {
        1: uinput.KEY_A,
        2: uinput.KEY_S,
        3: uinput.KEY_Q,
        4: uinput.KEY_W,
        5: uinput.KEY_V,
        6: uinput.KEY_B,
        7: uinput.KEY_M,
        8: uinput.KEY_P,
        9: uinput.KEY_R,
        10: uinput.KEY_F,
        11: uinput.KEY_D,
        12: uinput.KEY_G,
        13: uinput.KEY_2,
        14: uinput.KEY_6
    },
    3: {
        1: uinput.KEY_RIGHTCTRL,
        2: uinput.KEY_RIGHTSHIFT,
        3: uinput.KEY_C,
        4: uinput.KEY_N,
        5: uinput.KEY_H,
        6: uinput.KEY_Y,
        7: uinput.KEY_O,
        8: uinput.KEY_T,
        9: uinput.KEY_I,
        10: uinput.KEY_K,
        11: uinput.KEY_J,
        12: uinput.KEY_L,
        13: uinput.KEY_3,
        14: uinput.KEY_7
    },
    4: {
        1: uinput.KEY_KP0,
        2: uinput.KEY_KP1,
        3: uinput.KEY_KPENTER,
        4: uinput.KEY_KP3,
        5: uinput.KEY_KP9,
        6: uinput.KEY_KP5,
        7: uinput.KEY_KPDOT,
        8: uinput.KEY_KP7,
        9: uinput.KEY_KP8,
        10: uinput.KEY_KP2,
        11: uinput.KEY_KP4,
        12: uinput.KEY_KP6,
        13: uinput.KEY_4,
        14: uinput.KEY_8
   }
}

# DEFAULT MAME
# Player 1:
# Button 1 - Left Control
# Button 2 - Left Alt
# Button 3 - Spacebar
# Button 4 - Left Shift
# Button 5 - Z
# Button 6 - X
# Button 7 - C
# Button 8 - V
# Button 9 - B
# Button 10 - N
# Start - 1
# Coin - 5
# Up - Up Arrow
# Down - Down Arrow
# Left - Left Arrow
# Right - Right Arrow
#
# Player 2:
# Button 1 - A
# Button 2 - S
# Button 3 - Q
# Button 4 - W
# Up - R
# Down - F
# Left - D
# Right - G
# Start - 2
# Coin - 6
#
# Player 3:
# Button 1 - Right Control
# Button 2 - Right Shift
# Button 3 - Enter
# Up - I
# Down - K
# Left - J
# Right - L
# Start - 3
# Coin - 7
#
# Player 4:
# Button 1 - 0 Pad
# Button 2 - Del Pad
# Button 3 - Enter Pad
# Up - 8 Pad
# Down - 2 Pad
# Left - 4 Pad
# Right - 6 Pad
# Start - 4
# Coin - 8
