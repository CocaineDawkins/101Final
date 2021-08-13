

#This class represents the Rushing statistic which will include total yards, touchdowns, rushing attempts, and avg yds/carry
#There is a method in this class that calculates yards per carry rounded to 1 decimal place
class Rushing:
    
    def __init__ (self, rush_yards, rush_attempts, rush_touchdowns):
        self.rush_yards = rush_yards
        self.rush_attempts = rush_attempts
        self.rush_touchdowns = rush_touchdowns
    
    def yds_per_carry(self):
        yards_per_carry = self.rush_yards/ self.rush_attempts
        return round(yards_per_carry, 1)

#This class represents the Receiving statistic which will include targets, catches, and touchdowns
class Receiving:

    def __init__(self, rec_yards, rec_targets, rec_catches, rec_touchdowns):
        self.rec_yards = rec_yards
        self.rec_targets = rec_targets
        self.rec_catches = rec_catches
        self.rec_touchdowns = rec_touchdowns

#This clas represents the Passing statistic which will include yards, touchdowns, attempts, completions, and interceptions.
#There is a method in this class that will calculate completion percentage and give a percentage rounded to one decimal point
class Passing:

    def __init__(self, pass_yards, pass_touchdowns, pass_attempts, pass_completions, pass_interceptions, percentage):
        self.pass_yards = pass_yards
        self.pass_touchdowns = pass_touchdowns
        self.pass_attempts = pass_attempts
        self.pass_completions = pass_completions
        self.pass_interceptions = pass_interceptions
        self.percentage = self.completion_percentage

    def completion_percentage(self):
        percentage = self.pass_completions / self.pass_attempts
        return round(percentage, 1)

#This class represents the Kicking statistic which includes field goals(fg) attempted and field goals made
class Kicking:
    
    def __init__(self, fg_attempts, fg_made):
        self.fg_attempts = fg_attempts
        self.fg_made = fg_made

#This class represents Defense which includes sacks, interceptions, and points allowed
class Defense:

    def __init__(self, sacks, interceptions, pts_allowed):
        self.sacks = sacks
        self.interceptions = interceptions
        self.pts_allowed = pts_allowed

#This class represents a Running Back.  It inherits the Rushing and Receiving classes because running backs perform both in a game.
class RunningBack(Rushing, Receiving):
    def __init__(self, rush_yards, rush_attempts, rush_touchdowns, rec_yards, rec_targets, rec_catches, rec_touchdowns):
        super().__init__(rush_yards, rush_attempts, rush_touchdowns)
        super().__init__(rec_yards, rec_targets, rec_catches, rec_touchdowns)

#This class represents a Wide Receiver. It inherits the Receiving class.
class WideReceiver(Rushing, Receiving):
    def __init__(self, rush_yards, rush_attempts, rush_touchdowns, rec_yards, rec_targets, rec_catches, rec_touchdowns):
        super().__init__(rush_yards, rush_attempts, rush_touchdowns)
        super().__init__(rec_yards, rec_targets, rec_catches, rec_touchdowns)

#This class represents Tight Ends. It inherits the Receiving class.
class TightEnd(Receiving):
    def __init__(self, rec_targets, rec_catches, rec_touchdowns):
        super().__init__(rec_targets, rec_catches, rec_touchdowns)

#This class represents Quarterbacks.  It inherits both Passing and Rushing classes as Quarterbacks are able to do both.
class Quarterback(Passing, Rushing):
    def __init__(self, pass_yards, pass_attempts, pass_completions, pass_touchdowns, pass_interceptions, percentage, rush_yards, rush_attempts, rush_touchdowns):
        super().__init__(pass_yards, pass_attempts, pass_completions, pass_touchdowns, pass_interceptions, percentage)
        super().__init__(rush_yards, rush_attempts, rush_touchdowns)

#This class represents Kickers. It inherits the Kicking class
class Kicker(Kicking):
    def __init__(self, fg_attempts, fg_made):
        super().__init__(fg_attempts, fg_made)

#This class represents team Defenses.  It inherits the defense class.
class Defenses(Defense):
    def __init__(self, sacks, interceptions, pts_allowed):
        super().__init__(sacks, interceptions, pts_allowed)

#These are the 5 RunningBack instances to be ranked initialized with the arguments of 
#rush_yards, rush_attempts, rush_touchdowns, rec_yards, rec_targets, rec_catches, rec_touchdowns
derrick_henry = RunningBack(2027, 378, 17, 114, 31, 19, 4)
dalvin_cook = RunningBack(1557, 312, 16, 361, 54, 44, 1)
nick_chubb = RunningBack(1067, 190, 12, 150, 18, 16, 0)
aaron_jones = RunningBack(1104, 201, 9, 355, 63, 47, 2)
jonathan_taylor = RunningBack(1169, 232, 11, 299, 39, 36, 1)

#These are 5 WideReceiver instances that will be ranked with the arguments of
#rush_yards, rush_attempts, rush_touchdowns, rec_yards, rec_targets, rec_catches, rec_touchdowns
'''stefon_diggs = WideReceiver(1, 1, 0, 1535, 166, 127, 8)
davante_adams = WideReceiver(0, 0, 0, 1374, 149, 115, 18)
deandre_hopkins = WideReceiver(1, 1, 0, 1407, 160, 115, 6)
allen_robinson = WideReceiver(-1, 1, 0, 1250, 151, 102, 6)
keenan_allen = WideReceiver(-1, 1, 0, 992, 147, 100, 992, 8)'''