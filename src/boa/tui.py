import npyscreen

# This application class serves as a wrapper for the initialization of curses
# and also manages the actual forms of the application

class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", SplashForm())

# This form class defines the display that will be presented to the user.

class SplashForm(npyscreen.Form):
    def create(self):
        self.add(npyscreen.Pager,values=[
"▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄  ",
"█  ▄    █       █       █",
"█ █▄█   █   ▄   █   ▄   █",
"█       █  █ █  █  █▄█  █",
"█  ▄   ██  █▄█  █       █",
"█ █▄█   █       █   ▄   █",
"█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄█ █▄▄█",
"      Version 310        ",
            ])

    def afterEditing(self):
        self.parentApp.setNextForm(None)

if __name__ == '__main__':
    TA = MyTestApp()
    TA.run()