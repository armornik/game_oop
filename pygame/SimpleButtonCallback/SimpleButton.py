# SimpleButton class
#
# Uses a "state machine" approach
#

import pygame
from pygame.locals import *


class SimpleButton:
    # Used to track the state of the button
    STATE_IDLE = 'idle'  # button is up, mouse not over button
    STATE_ARMED = 'armed'  # button is down, mouse over button
    STATE_DISARMED = 'disarmed'  # clicked down on button, rolled off
        
    def __init__(self, window, loc, up, down, call_back=None):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)
        self.call_back = call_back

        # Get the rect of the button (used to see if the mouse is over the button)
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handle_event(self, event_obj):
        # This method will return True if user clicks the button.
        # Normally returns False.

        if event_obj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            # The button only cares about mouse-related events
            return False

        event_point_in_button_rect = self.rect.collidepoint(event_obj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (event_obj.type == MOUSEBUTTONDOWN) and event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (event_obj.type == MOUSEBUTTONUP) and event_point_in_button_rect:
                self.state = SimpleButton.STATE_IDLE
                # If a callback was specified, call it back
                if self.call_back is not None:
                    self.call_back()
                return True  # clicked!

            if (event_obj.type == MOUSEMOTION) and (not event_point_in_button_rect):
                self.state = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED
            elif event_obj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        # Draw the button's current appearance to the window
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)

        else:  # IDLE or DISARMED
            self.window.blit(self.surfaceUp, self.loc)
