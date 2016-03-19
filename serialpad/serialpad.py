#!/usr/bin/python

import sys
import serial
import yaml
import uinput


class Pad(object):
    """Serial Pad class"""
    def __init__(self, device, player_keys, speed, num_buttons=14, timeout=10):
        self.device = device
        self.num_buttons = num_buttons
        self.serial_speed = speed
        self.serial_timeout = timeout
        self.keymap = player_keys

        self.keystates = {}
        self.serial_port = None
        self.input = None
        self.events = player_keys.values()
        self.Terminated = False

    def update_keymap(self, keymap):
        self.keymap = keymap

    def setup_serial(self, device, speed, timeout):
        self.serial_port = serial.Serial(device)
        self.serial_port.baudrate = speed
        self.serial_port.timeout = timeout

    def create_keystates(self):
        for button in self.keymap:
            self.keystates[button] = 0

    def create_input(self):
        self.input = uinput.Device(self.events, name='serialpad')

    def attach_device(self):
        self.serial = serial.Serial()

    def press_key(self, keycode):
        self.input.emit(keycode, 1)  # KEY down

    def release_key(self, keycode):
        self.input.emit(keycode, 0)  # KEY up

    def run(self):
        """Main method."""
        try:
            self.setup_serial(self.device,
                              self.serial_speed,
                              self.serial_timeout)
        except Exception, e:
            # log_error(e)
            print "unable to open %s" % self.device
        else:
            self.create_keystates()

            # create uinput
            try:
                self.create_input()
            except Exception, e:
                print e
                # log_error(e)
                sys.exit(1)

            self.loop()

    def update_input_status(self, key_index, key_value):
        if key_value != self.keystates[key_index]:
            keycode = self.keymap[key_index]

            if key_value == 1:
                self.press_key(keycode)
            else:
                self.release_key(keycode)
            self.keystates[key_index] = key_value

    def handle_buttons(self, values):
        input_index = 1
        for input_value in values:
            try:
                self.update_input_status(input_index, int(input_value))
            except:
                pass
            input_index += 1

    def loop(self):
        while not self.Terminated:
            try:
                button_values = self.serial_port.readline()
            except Exception, e:
                print "unable to read %s" % self.device
                # log_error(e)
                break
            else:
                values = button_values.split(";")[:14]
                if len(values) == self.num_buttons:
                    self.handle_buttons(values)

        self.stop()

    def stop(self):
        print "stopping process"
        self.input.close()
        self.serial_port.close()
        self.Terminated = True
