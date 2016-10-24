#Eva Hayek and Audrey Elkus
#Whatever the Weather 

from Tkinter import *

#made the OurGUI class 
class OurGUI(Tk):
    #used init
    def __init__(self):
        Tk.__init__(self)
        #titled, put in instance variables 
        self.title('Whatever the Weather')
        self.grid()
        self.createWidgets()
        self.tempActivities = Temperature()
        self.picLabel 
        self.returnList = []
        self.statusList= []
        
        #defined create widgets
    def createWidgets(self):
        #added the title and changed the font and its color
        titleLabel = Label(self, text='Whatever the Weather', fg='skyblue3', font='Rockwell 22')
        #put it in the right spot
        titleLabel.grid(row=1, columnspan=5) 
    
        #added the title pic 
        pic = PhotoImage(file='firstpic.gif') # initial image
        #put it in the right spot and made it 'stick' to the right corners (all of them) 
        self.picLabel = Label(self, image=pic, borderwidth=3)
        self.picLabel.pic = pic 
        self.picLabel.grid(row=4, columnspan=5, sticky = N+E+S+W)
        
        #description label
        descriptionLabel = Label(self, text='No matter what the weather is, make sure you have a fun day!', fg= 'hotpink',font='Rockwell 12')
        descriptionLabel.grid(row=2, column=2)
        
        #second description label
        description2Label = Label(self, text='Even if it looks nothing like this outside...', font='Rockwell 10 italic')
        description2Label.grid(row=3, column=2)
        
        #temperature label
        temperatureLabel = Label(self, text = 'Choose your temperature', fg='darkgreen', font='Rockwell 16')
        temperatureLabel.grid(row=5, column=2)
       #make the options for the temperatures 
        self.options = ['Cold', 'Mild', 'Hot']
        self.temperatureIndex = IntVar() 
        #going through list of temperatures, adding radio buttons and a temperature index 
        for i in range(0, len(self.options)):
            rb1 = Radiobutton(self, text=self.options[i],variable=self.temperatureIndex, value = i)
            #making a grid 
            rb1.grid(row=6+i, column=2, sticky=W)
        
        #weather label
        weatherLabel = Label(self, text = 'Choose your weather', fg='darkgreen', font='Rockwell 16')
        weatherLabel.grid(row=10, column=2)
        #putting in the weather options
        self.options2 = ['Sunny', 'Rainy', 'Cloudy', 'Windy']
        self.weatherIndex = IntVar()
        for i in range(0, len(self.options2)):
            #same weather buttons just as above 
            rb2 = Radiobutton(self, text=self.options2[i],variable=self.weatherIndex, value = i)
            rb2.grid(row=11+i, column=2, sticky=W)
            
        #submit button
        submitButton = Button(self, text = 'Submit', command=self.onSubmitButtonClick)
        submitButton.grid(row=16, column=4, sticky=E)
        
        #quit button
        quitButton = Button(self, text='Quit', command=self.onQuitButtonClick)
        quitButton.grid(row=16, column=0, sticky=W)
        
    #when you click on the submit button, it will return the intersection of the two options you chose     
    def onSubmitButtonClick(self):
        #makes a new window
        self.intersection() 
        self.myWindow = ActivityWindow(self.options[self.temperatureIndex.get()], self.options2[self.weatherIndex.get()], self.returnList)
        self.myWindow.mainloop() 
    
    def onQuitButtonClick(self):
        #it will disappear when you click Quit 
        self.destroy()
        
    def intersection(self):
        #the intersection definition returns a list of all the activities found in 
        #BOTH the weather the user selected as well as the temperature they chose
        temperature = self.options[self.temperatureIndex.get()]
        weather = self.options2[self.weatherIndex.get()]
        tempAndWeatherList = []
        tempAndWeatherList = (self.tempActivities.tempAndWeatherDictionary[temperature] + self.tempActivities.tempAndWeatherDictionary[weather])
        #if it's in both lists, add it to the new list 
        for elt in tempAndWeatherList:
            if tempAndWeatherList.count(elt) > 1:
                self.returnList.append(elt)
                tempAndWeatherList.remove(elt)
                #return the new list 
        return self.returnList                     

#created another class for the Activity Window that pops up when 
#the user clicks submit            
class ActivityWindow(Toplevel): 
    def __init__(self, temperature, weather, returnList):
        Toplevel.__init__(self)
        #added all the instance variables 
        self.title('Activities')
        self.grid()
        self.temperature = temperature
        self.weather = weather
        self.returnList = returnList
        
        #made the label which puts in what the user chose (as a string)
        statusLabel = Label(self, text='You chose ' + str(temperature) + ' and ' + str(weather) + '!', fg='skyblue3', font='Rockwell 20')
        #put it in the right spot 
        statusLabel.grid(row=1, column=1)
        #made the title label and changed the text, color and location
        titleLabel = Label(self, text='Your Options Include...', fg='hotpink', font='Rockwell 20')
        titleLabel.grid(row=3, column=1) 
        
        #Activities being shown in the activity window 
        for i in range(0, len(self.returnList)):
            listLabel = Label(self, text= str(self.returnList[i]), font='Rockwell 12')
            listLabel.grid(row=5+i, column=1)
            
        #quit Button
        quitButton = Button(self, text='Quit', command=self.onQuitButtonClick)
        quitButton.grid(row=len(self.returnList)+10, column=1)
        
    def onQuitButtonClick(self):
        #when the user clicks the quit button the window disappears 
        self.destroy()
            
class Temperature():
    def __init__(self):
        #all the lists of activities that pertain to the weather or temperature option
        self.tempAndWeatherDictionary = {}
        self.tempAndWeatherDictionary['Cold'] = ['ice skate at MIT', 'swing dance at MIT','drink hot chocolate at LA Burdick\'s', 'watch a movie', 'explore Boston', 'study in the Boston Public Library', 'read a book', 'order Lemon Thai', 'build a snowman', 'go skiing', 'go to the MFA' , 'go to the Isabella Stuart Gardner Museum']
        self.tempAndWeatherDictionary['Mild'] = ['swing dance at MIT', 'drink hot chocolate at LA Burdick\'s', 'watch a movie', 'explore Boston','read by Lake Waban','visit Nantucket', 'read a book', 'order Lemon Thai','go cloud watching','wear sunscreen and sunglasses', 'wear bright colors, study in the Boston Public Library', 'splash in puddles', 'sing in the rain', 'go to the MFA', 'go to the Isabella Stuart Gardner Museum', 'fly a kite']
        self.tempAndWeatherDictionary['Hot'] = ['watch a movie', 'study in the Boston Public Library', 'visit Nantucket', 'have a picnic', 'read by Lake Waban', 'read a book', 'order Lemon Thai', 'build a sandcastle', 'go cloud watching', 'wear bright colors','wear sunglasses and sunscreen', 'go swimming', 'eat ice cream', 'splash in puddles', 'sing in the rain', 'canoeing', 'kayaking', 'windsurfing', 'sailing', 'go to the MFA', 'go to the Isabella Stuart Gardner Museum', 'fly a kite']
        self.tempAndWeatherDictionary['Sunny'] = ['ice skate at MIT', 'swing dance at MIT', 'explore Boston', 'visit Nantucket', 'read by Lake Waban', 'build a sandcastle', 'build a snowman', 'go cloud watching', 'go skiing', 'wear bright colors', 'wear sunglasses and sunscreen', 'go swimming', 'eat ice cream', 'canoeing', 'kayaking']
        self.tempAndWeatherDictionary['Rainy'] = ['swing dance at MIT', 'drink hot chocolate at LA Burdick\'s', 'wear bright colors','watch a movie', 'splash in puddles', 'study in the Boston Public Library', 'order Lemon Thai', 'sing in the rain', 'go to the Isabella Stuart Gardner Museum']
        self.tempAndWeatherDictionary['Cloudy'] = ['ice skate at MIT', 'swing dance at MIT', 'drink hot chocolate at LA Burdick\'s', 'watch a movie', 'study in the Boston Public Libary', 'read a book', 'order Lemon Thai', 'build a snowman', 'go skiing']
        self.tempAndWeatherDictionary['Windy'] = ['windsurfing', 'sailing', 'watch a movie', 'study in the Boston Public Library', 'read a book', 'wear bright colors', 'go to the MFA' , 'fly a kite']
 
def run():   
    #make it run 
    gui = OurGUI()
    gui.mainloop()

run()