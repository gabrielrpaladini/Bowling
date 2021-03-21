from __future__ import annotations

class BowlingGame:

    def __init__(self):

        self.rolls = []

    def roll(self, pins):

        self.rolls.append(pins)

    def score(self):

        result = 0

        roll_index = 0
        
        for frame_index in range(10):

            if self._check_if_is_strike(roll_index):

                result += self._strike_score(roll_index)

                roll_index += 1

            elif self._check_if_is_spare(roll_index):

                result += self._spare_score(roll_index)

                roll_index += 2

            else :
                
                result += self._frame_score(roll_index)

                roll_index += 2

        return result

    def _check_if_is_spare(self, roll_index):

        return self.rolls[roll_index] +  self.rolls[roll_index + 1] == 10

    def _check_if_is_strike(self, roll_index):

        return self.rolls[roll_index] == 10

    def _spare_score(self, roll_index):

        return 10 + self.rolls[roll_index + 2]

    def _frame_score(self, roll_index):

        return self.rolls[roll_index] + self.rolls[roll_index + 1]

    def _strike_score(self, roll_index):

        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]