#!/usr/bin/env python3
# Python3 Robot code: Rhino Bot "Untitled"
# 2017 - 4480 "Forty48ie" "UC-Botics"


import wpilib
import wpilib.buttons
from robotpy_ext.autonomous import AutonomousModeSelector
from robotpy_ext.common_drivers import units, navx
import networktables
from components import drive

class MyRobot(wpilib.IterativeRobot):


    def robotInit(self):


       #Defining Constants
        self.LeftTread = wpilib.Talon(0)
        self.RightTread = wpilib.Talon(1)
        self.robotDrive = wpilib.RobotDrive(self.LeftTread, self.RightTread)
        self.xboxController = wpilib.Joystick(0)
        self.xboxAbutton = wpilib.buttons.JoystickButton(self.xboxController, 1)
        self.xboxBbutton = wpilib.buttons.JoystickButton(self.xboxController, 2)
        self.xboxYbutton = wpilib.buttons.JoystickButton(self.xboxController, 4)
        self.navx = navx.AHRS.create_spi()
        self.drive = drive.Drive(self.robotDrive, self.xboxController, self.navx)
        
       #Defining Variables
        self.dm = True
    
        #Auto mode variables
        self.components = {
            'drive': self.drive
        }
        self.automodes = AutonomousModeSelector('autonomous', self.components)
    

    def autonomousPeriodic(self):


        self.automodes.run()


    def teleopPeriodic(self):
        if self.xboxYbutton.get():
            self.drive.flipflip()
     
        if self.xboxAbutton.get():
            self.dm = False
   

        if self.xboxBbutton.get():
            self.dm = True

        self.drive.customDrive(self.xboxController.getX(), self.xboxController.getY(), self.xboxController.getRawAxis(2), self.dm)

if __name__ == "__main__":
    wpilib.run(MyRobot)
