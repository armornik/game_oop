class LightSwitch:
    def __init__(self, label) -> None:
        self.label = label
        # Устанавливаем выключатель в положение 'Выкл.'
        self.switch_is_on = False
        # Устанавливаем яркость на '0'
        self.brightness = 0

    def turn_on(self) -> None:
        """turn the switch on"""
        self.switch_is_on = True

    def turn_off(self) -> None:
        """turn the switch off"""
        self.switch_is_on = False

    def raise_level(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Показать текущие значения яркости и положения выключателя
    def show(self):
        print()
        print('Label', self.label)
        print(' Switch is on?', self.switch_is_on)
        print(' Brightness is:', self.brightness)


switch = LightSwitch('Switch_1')

# Turn switch on, and raise the level 5 times
switch.turn_on()
switch.raise_level()
switch.raise_level()
switch.raise_level()
switch.raise_level()
switch.raise_level()
switch.show()

# Lower the level 2 times, and turn switch off
switch.lower_level()
switch.lower_level()
switch.turn_off()
switch.show()

# Turn switch on, and raise the level 3 times
switch.turn_on()
switch.raise_level()
switch.raise_level()
switch.raise_level()
switch.show()

print('switch variables:', vars(switch))
