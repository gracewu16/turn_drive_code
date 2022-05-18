import commands2
from wpimath.controller import PIDController
from constants import turn_K_p, turn_K_I, turn_K_D
from subsytems.drivetrain import Drivetrain

class TurnCommand(commands2.PIDCommand):
   # /**
   # * Creates a new DriveStraight.
   # */
   def __init__(self, angleSetPt: float, drivetrain: Drivetrain):
       super().__init__(
           PIDController(turn_K_p, turn_K_I,
                         turn_K_D),

           drivetrain.gyro.getYaw,

           angleSetPt,

           drivetrain.turn,
           [drivetrain])

   def isFinished(self):
       return self.getController().atSetpoint();