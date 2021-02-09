from guizero import App
app = App(title="Hello world")
app.display()
#on run, the program opens a note window with the hello world title

from guizero import App, Text, Picture

#exit function
def exitGUI():
    if app.yesno("close", "would you like to close the program?"):
        app.destroy()
        print("closing...")

app = App("destroy!")
app.bg = "#A0B0D0" 
wanted_text = Text(app, "Damn drones")
wanted_text.text_size = 50
wanted_text.font = "Times New Roman"
cat = Picture(app, image="drone.jpeg")
app.display()



#5
from guizero import App, Text, Box, PushButton
def do_nothing():
 return 0
app = App(title="lab 7 app", height=300, width=300, layout="grid")
text = Text(app, text="bla bla bla", grid=[0,0])
box = Box(app, layout="grid", grid=[1,0])
button1 = PushButton(box, command=do_nothing, text="1", grid=[0,0])
button2 = PushButton(box, command=do_nothing, text="2", grid=[1,0])
button3 = PushButton(box, command=do_nothing, text="3", grid=[2,0])
button4 = PushButton(box, command=do_nothing, text="4", grid=[0,1])
button5 = PushButton(box, command=do_nothing, text="5", grid=[1,1])
button6 = PushButton(box, command=do_nothing, text="6", grid=[2,1])
app.display()



#6a
from guizero import App, PushButton
from gpiozero import LED
led17 = LED(17)
def GPIO_17():
    if button1.text == "GPIO17_ON ":
        button1.text ="GPIO17_OFF"
        led17.on()
        else:
            button1.text="GPIO17_ON "
            led17.off()
if __name__ == '__main__':
    app = App("Activation GPIO")
    button1 = PushButton(app, command=GPIO_17, text="GPIO17_ON ")
    app.display()
    led17.off()
    


#6b
from guizero import App, Text
from gpiozero import Button
from gpiozero import LED

button = Button(2)
led = LED(17)

def scanInput():
    if button.is_pressed:
        text.value = 1 #"GPIO2 ON "
        led.on()
    else:
        text.value = 0 #"GPIO2 OFF"
        led.off()
            
def exitGUI():
    text.destroy()
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        print("Adios")
        
if __name__ == '__main__':
    app = App("Reading GPIO")
    text = Text(app, text="1")
    text.repeat(10, scanInput)  # Schedule call to scan GPIO input every
    app.when_closed = exitGUI
    app.display()
    
    
#