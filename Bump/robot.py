#!/usr/bin/env python3
# Python3 Robot code: Rhino Bot "Untitled"
# 2017 - 4480 "Forty48ie" "UC-Botics"

import wpilib
import wpilib.buttons
from robotpy_ext.autonomous import AutonomousModeSelector
from robotpy_ext.common_drivers import units, navx
import networktables

class MyRobot(wpilib.IterativeRobot):


    def robotInit(self):

        if not wpilib.RobotBase.isSimulation():
            import ctre
            self.motor1 = ctre.CANTalon(1)
            self.motor2 = ctre.CANTalon(2)
            self.motor3 = ctre.CANTalon(3)
            self.motor4 = ctre.CANTalon(4)
        else:
            self.motor1 = wpilib.Talon(1)
            self.motor2 = wpilib.Talon(2)
            self.motor3 = wpilib.Talon(3)
            self.motor4 = wpilib.Talon(4)
        
        
       #Defining Constants
   #     self.LeftTread = wpilib.Talon(0)
    #    self.RightTread = wpilib.Talon(1)
        self.robotDrive = wpilib.RobotDrive(self.motor1, self.motor2, self.motor3, self.motor4)
        self.xboxController = wpilib.Joystick(0)
        self.xboxAbutton = wpilib.buttons.JoystickButton(self.xboxController, 1)
        self.xboxBbutton = wpilib.buttons.JoystickButton(self.xboxController, 2)
        self.xboxYbutton = wpilib.buttons.JoystickButton(self.xboxController, 4)
        #self.navx = navx.AHRS.create_spi()
       # self.drive = drive.Drive(self.robotDrive, self.xboxController, self.navx)
        
       #Defining Variables
        self.dm = True
    
        #Auto mode variables
        #self.components = {
         #   'drive': self.drive
        #}
        #self.automodes = AutonomousModeSelector('autonomous', self.components)
    
    def autonomousPeriodic(self):

        pass
        #self.automodes.run()

    def teleopPeriodic(self):

        self.robotDrive.tankDrive(self.xboxController.getY(), self.xboxController.getRawAxis(5))
       
        if self.xboxAbutton.get():
            self.dm = False
   
        if self.xboxBbutton.get():
            self.dm = True
        if self.dm == True:
            self.robotDrive.tankDrive(self.xboxController.getY(), self.xboxController.getRawAxis(5))
        if self.dm == False:
            self.robotDrive.arcadeDrive(self.xboxController.getX(), self.xboxController.getY())


if __name__ == "__main__":
    wpilib.run(MyRobot)
