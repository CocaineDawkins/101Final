#This class represents the Rushing statistic which will include total yards, touchdowns, rushing attempts, and avg yds/carry
class Rushing:
    
    def __init__ (self, yards, attempts, touchdowns, yds_per_carry):
        self.yards = yards
        self.attempts = attempts
        self.touchdowns = touchdowns
        self.yds_per_carry = yds_per_carry

#This class represents the Receiving statistic which will include targets, catches, touchdowns, and average depth of target
class Receiving:

    def __init__(self, targets, catches, touchdowns, avg_depth):
        self.targets = targets
        self.catches = catches
        self.touchdowns = touchdowns
        self.avg_depth = avg_depth

#This clas represents the Passing statistic which will include yards, touchdowns, attempts, completions, and interceptions.
#There is a method in this class that will calculate completion percentage and give a percentage rounded to one decimal point
class Passing:

    def __init__(self, yards, touchdowns, attempts, completions, interceptions):
        self.yards = yards
        self.touchdowns = touchdowns
        self.attempts = attempts
        self.completions = completions
        self.interceptions = interceptions

    def completion_percentage(self, attempts, completions):
        percentage = self.completions / self.attempts
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
class Running_back(Rushing, Receiving):
    pass

#This class represents a Wide Receiver. It inherits the Receiving class.
class Wide_receiver(Receiving):
    pass

#This class represents Tight Ends. It inherits the Receiving class.
class Tight_end(Receiving):
    pass

#This class represents Quarterbacks.  It inherits both Passing and Rushing classes as Quarterbacks are able to do both.
class Quarterback(Passing, Rushing):
    pass

#This class represents Kickers. It inherits the Kicking class
class Kicker(Kicking):
    pass

#This class represents team Defenses.  It inherits the defense class.
class Defenses(Defense):
    pass

