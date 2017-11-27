#!/usr/bin/env python3

# Python3 Robot code: Rhino Bot "Untitled"
# 2017 - 4480 "Forty48ie" "UC-Botics"
#
#

import wpilib # <---- main library with all the necessary code for controlling FRC robots
import wpilib.buttons # <---- for joystick buttons

class MyRobot(wpilib.IterativeRobot):


    def robotInit(self):

        self.M1 = wpilib.Talon(0) #
        self.M2 = wpilib.Talon(1) #

        self.dm = 2
        self.robot_drive = wpilib.RobotDrive(self.M1, self.M2)

        self.xboxController = wpilib.Joystick(0)
        self.xboxAbutton = wpilib.buttons.JoystickButton(self.xboxController, 1) #16 A button on xbox controller
        self.xboxBbutton = wpilib.buttons.JoystickButton(self.xboxController, 2) #16 A button on xbox controller

    def teleopInit(self):
        
        pass

    def teleopPeriodic(self):
        
        if self.xboxAbutton.get():
            self.dm = 1
        if self.xboxBbutton.get():
            self.dm = 2
        if self.dm == 1:
            self.robot_drive.arcadeDrive(self.xboxController.getY(), self.xboxController.getX(), True)
        if self.dm == 2:
            self.robot_drive.tankDrive(self.xboxController.getY(), self.xboxController.getRawAxis(5), True)


if __name__ == "__main__":
    wpilib.run(MyRobot) #runs the code!
