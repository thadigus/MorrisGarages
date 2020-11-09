##*************************************************************
## PROGRAM NAME:    	Lab9_Morris_Garages.py
## AUTHOR:          	Thad W. Turner
## DATE:   	            11/2/2020
## PURPOSE:         	Lab #9. 
##                  	GUI interface for maintence service price
##                      calculations for Morris Garages.
##*************************************************************
##

# Import needed libraries
import tkinter
import tkinter.messagebox
import sys

########################################################################
##
##  CLASS Morris GUI
##
########################################################################

class MorrisGUI:
##----------------------------------------------------------------
## CONSTRUCTOR
##----------------------------------------------------------------       
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Morris Garages Price Estimator")
        self.main_window.geometry("400x275")
        
        self.title_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")
        self.oil_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")
        self.radiator_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")
        self.trans_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")
        self.brake_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")
        self.inspect_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")
        self.tirerotate_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")
        self.button_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")
        self.result_frame = tkinter.Frame(self.main_window, bd = 1, relief = "sunken")

        # Create and Pack Title Box Objects
        self.title_label = tkinter.Label(self.title_frame, anchor = "nw", text = "Morris Garages Price Estimator")
        self.author_label = tkinter.Label(self.title_frame, anchor = "ne", text = "Author: Thad W. Turner")

        self.title_label.pack(side = "left")
        self.author_label.pack(side = "right")
        # Create and Pack Checkboxes (Oil Change, Radiator Flush, Transmission Service, Brakes, Inspection, and Tire Rotation)
        self.oil_chng = tkinter.IntVar()
        self.rad_flush = tkinter.IntVar()
        self.trans_serv = tkinter.IntVar()
        self.brakes_serv = tkinter.IntVar()
        self.inspection = tkinter.IntVar()
        self.tire_rotate = tkinter.IntVar()

        self.oil_chng.set(0)
        self.rad_flush.set(0)
        self.trans_serv.set(0)
        self.brakes_serv.set(0)
        self.inspection.set(0)
        self.tire_rotate.set(0)

        self.oil_chng_check = tkinter.Checkbutton(self.oil_frame,
                                                text = "Oil Change",
                                                variable = self.oil_chng,
                                                onvalue = 1,
                                                command = self.toggle_oil)
        self.rad_flush_check = tkinter.Checkbutton(self.radiator_frame,
                                                    text = "Radiator Flush",
                                                    variable = self.rad_flush,
                                                    onvalue = 1)
        self.trans_serv_check = tkinter.Checkbutton(self.trans_frame,
                                                    text = "Transmission Service",
                                                    variable = self.trans_serv,
                                                    onvalue = 1)
        self.brakes_serv_check = tkinter.Checkbutton(self.brake_frame,
                                                    text = "Brakes Service",
                                                    variable = self.brakes_serv,
                                                    onvalue = 1,
                                                    command = self.toggle_brakes)
        self.inspection_check = tkinter.Checkbutton(self.inspect_frame,
                                                    text = "Inspection",
                                                    variable = self.inspection,
                                                    onvalue = 1)
        self.tire_rotate_check = tkinter.Checkbutton(self.tirerotate_frame,
                                                    text = "Tire Rotation",
                                                    variable = self.tire_rotate,
                                                    onvalue = 1)

        self.oil_chng_check.pack()
        self.rad_flush_check.pack()
        self.trans_serv_check.pack()
        self.brakes_serv_check.pack()
        self.inspection_check.pack()
        self.tire_rotate_check.pack()

        # Create amd Pack Radio Buttons (Oil Change Conventional Oil or Synthetic Oil, Brakes Turn Rotors and/or Replace Pads)
        self.oil_var = tkinter.IntVar()
        self.brake_var = tkinter.IntVar()

        self.oil_var.set(0)
        self.convRB = tkinter.Radiobutton(self.oil_frame,
                                            text = "Conventional Oil Change",
                                            variable = self.oil_var,
                                            value = 1,
                                            state = "disabled")
        
        self.synthRB = tkinter.Radiobutton(self.oil_frame,
                                            text = "Synthetic Oil Change",
                                            variable = self.oil_var,
                                            value = 2,
                                            state = "disabled")

        self.brake_var.set(0)
        self.rotorRB = tkinter.Radiobutton(self.brake_frame,
                                            text = "Rotors Turned",
                                            variable = self.brake_var,
                                            value = 1,
                                            state = "disabled")

        self.padsRB = tkinter.Radiobutton(self.brake_frame,
                                            text = "Pads Replaced",
                                            variable = self.brake_var,
                                            value = 2,
                                            state = "disabled")

        self.convRB.pack(side = "left")
        self.synthRB.pack(side = "right")
        self.rotorRB.pack(side = "left")
        self.padsRB.pack(side = "right")

        # Create and Pack Total and Quit Buttons
        self.totalButton = tkinter.Button(self.button_frame,
                                        text = "Total", 
                                        command = self.calculatePrice)
        self.quitButton = tkinter.Button(self.button_frame,
                                        text = "Quit",
                                        command = self.quitPgm)

        self.totalButton.pack(side = "left")
        self.quitButton.pack(side = "right")

        # Pack the Frames
        self.title_frame.pack(fill = "x")
        self.oil_frame.pack(fill = "x")
        self.radiator_frame.pack(fill = "x")
        self.trans_frame.pack(fill = "x")
        self.brake_frame.pack(fill = "x")
        self.inspect_frame.pack(fill = "x")
        self.tirerotate_frame.pack(fill = "x")
        self.button_frame.pack()
        self.result_frame.pack(fill = "x")

        # Start main loop
        tkinter.mainloop()
    
##----------------------------------------------------------------
## FUNCTION: quitPgm()
## INPUT:    N/A
## OUTPUT:   N/A
## FUNCTION: When called, the program shows a message box then gracefully exits.
##----------------------------------------------------------------     
    # Button Methods
    # Method called by quit button
    def quitPgm(self):
        tkinter.messagebox.showinfo(title = "Quit", 
                                    message = "Thank you for choosing Morris Garages")
        self.main_window.destroy()
        sys.exit()

##----------------------------------------------------------------
## FUNCTION: calculatePrice()
## INPUT:    N/A
## OUTPUT:   N/A
## FUNCTION: When called, different get/set functions are used for each
##           aspect of selections made by customer to find and display total.
##----------------------------------------------------------------     
    # Method called by total button
    def calculatePrice(self):
        # Show in result_frame
        self.total_value = tkinter.IntVar()
        self.total_value.set(0)
        if self.oil_chng.get() == 1:
            # Add oil change by type
            if self.oil_var.get() == 1:
                # Add conventional oil change to total
                self.total_value.set(self.total_value.get() + 30)
            elif self.oil_var.get() == 2:
                # Add synthetic oil change to total
                self.total_value.set(self.total_value.get() + 75)
        if self.rad_flush.get() == 1:
            # Add radiator flush to total
            self.total_value.set(self.total_value.get() + 40)
        if self.trans_serv.get() == 1:
            # Add Transmission service to total
            self.total_value.set(self.total_value.get() + 100)
        if self.brakes_serv.get() == 1:
            # Add brakes by type
            if self.brake_var.get() == 1:
                # Add brake rotor surfacing to total
                self.total_value.set(self.total_value.get() + 50)
            elif self.brake_var.get() == 2:
                # Add brake replacement to total
                self.total_value.set(self.total_value.get() + 175)
        if self.inspection.get() == 1:
            # Add inspection to the total
            self.total_value.set(self.total_value.get() + 25)
        if self.tire_rotate.get() == 1:
            # Add tire rotation to total
            self.total_value.set(self.total_value.get() + 20)
        # Display total in message box
        tkinter.messagebox.showinfo(title = "Total", 
                                    message = ("The total for this configuration is $" + str(self.total_value.get()) + ".00"))

##----------------------------------------------------------------
## FUNCTION: toggle_oil
## INPUT:    N/A
## OUTPUT:   N/A
## FUNCTION: When called (by check mark boxes), the state of the oil
##           radio buttons is toggled from active to disabled or disabled to active.
##----------------------------------------------------------------     
    # Toggle activity methods
    def toggle_oil(self):
        # Toggles the active state of oil radio buttons (convRB and synthRB)
        if self.convRB["state"] == "disabled":
            self.convRB["state"] = "active"
            self.synthRB["state"] = "active"
        else:
            self.convRB["state"] = "disabled"
            self.synthRB["state"] = "disabled"
            self.convRB.deselect()
            self.synthRB.deselect()
##----------------------------------------------------------------
## FUNCTION: toggle_brakes())
## INPUT:    N/A
## OUTPUT:   N/A
## FUNCTION: When called (by check mark boxes), the state of the brake service
##           radio buttons is toggled from active to disabled or disabled to active.
##----------------------------------------------------------------     
    def toggle_brakes(self):
        # Toggles the active state of brake radio buttons (rotorRB and padsRB)
        if self.rotorRB["state"] == "disabled":
            self.rotorRB["state"] = "active"
            self.padsRB["state"] = "active"
        else:
            self.rotorRB["state"] = "disabled"
            self.padsRB["state"] = "disabled"
            self.rotorRB.deselect()
            self.padsRB.deselect()

########################################################################
##
##  MAIN
##
########################################################################
morris_GUI = MorrisGUI()