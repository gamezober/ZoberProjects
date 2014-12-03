import Tkinter
import datetime
import workoutappdb

#Create Dictionary for insert database functions defined in workoutappdb.py
liftDict = { 
    "Back Squat": workoutappdb.bSquatInsert,
    "Front Squat": workoutappdb.fSquatInsert,
    "Bench Press": workoutappdb.benchInsert,
    "Deadlift": workoutappdb.dLiftInsert,
    "Push Press": workoutappdb.pressInsert
    
    }
    
#function creates GUI
def main():
    root = Tkinter.Tk()
    root.title("Lift Logger")
    canvas = Tkinter.Canvas(root, width = 750, height = 750)
    canvas.pack()

    #Option Menu for list
    lift = Tkinter.StringVar()
    lift.set("Back Squat")
    liftMenu = Tkinter.OptionMenu(canvas, lift, "Back Squat", "Front Squat", "Bench Press", "Deadlift",
                                  "Push Press")
    liftMenu.grid_configure(column = 3, row = 2, padx = 10, pady = 10)
    liftMenuLabel = Tkinter.Label(canvas, text = "Select a Lift Below")
    liftMenuLabel.grid_configure(column = 3, row = 1, padx= 10, pady = 5)

    #creates action for button event handler
    def optionSelect():
        x = lift.get()
        liftdate = str(datetime.date.today())
        liftset = setEntry.get()
        reps = repEntry.get()
        weight = weightEntry.get()
        data = (liftdate, liftset, reps, weight)
        liftDict[x](data)
    
    #Entry for Set number
    setValue = Tkinter.IntVar()
    setEntry = Tkinter.Entry(canvas, textvariable = setValue)
    setEntry.grid_configure(column = 2, row = 1, padx = 10, pady = 10)
    setEntryLabel = Tkinter.Label(canvas, text = 'Set Number')
    setEntryLabel.grid_configure(column = 1, row = 1, padx =10, pady = 10)

    #Entry for Number of Reps
    repValue = Tkinter.IntVar()
    repEntry = Tkinter.Entry(canvas, textvariable = repValue)
    repEntry.grid_configure(column = 2, row = 2, padx = 10, pady = 10)
    repEntryLabel = Tkinter.Label(canvas, text = 'Number of Reps')
    repEntryLabel.grid_configure(column = 1, row = 2, padx = 10, pady = 10)

    #Entry for Weight Lifted
    weight = Tkinter.DoubleVar()
    weightEntry = Tkinter.Entry(canvas, textvariable = weight)
    weightEntry.grid_configure(column = 2, row = 3, padx = 10, pady = 10)
    weightEntryLabel = Tkinter.Label(canvas, text = 'Weight')
    weightEntryLabel.grid_configure(column = 1, row = 3, padx = 10, pady = 10)

    #Button to add data
    button = Tkinter.Button(canvas, text = "Add to Log", command = optionSelect)
    button.grid_configure(column = 3, row = 3, padx = 5, pady = 5)
    
    Tkinter.mainloop()

#def getEntryValue():
    



if __name__ == '__main__':
    main()

