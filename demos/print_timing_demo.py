from time import sleep
from random import uniform
from threading import Thread

def rindex(seq, value):
    return len(seq) - 1 - seq[::-1].index(value)

class FakeWindow:

    def __init__(self):
         self.command_list = []

    def clear(self):
       self.command_list.append("clear")
        
    
    def circle(self):
        self.command_list.append("circle")
        sleep(.01)    # sleep a bit to artificially make command slow
    
    def rectangle(self):
        self.command_list.append("rectangle")
        sleep(.01)

    def triangle(self):
        self.command_list.append("triangle")
        sleep(.01)
    
    def redraw(self):
        self.command_list.append("redraw")
        
    
    def BADpaintComponent(self):
        print "*** Repainting ***"
        for s in self.command_list:
            print s
        print "------------------"
        print
        
    def GOODpaintComponent(self):
        
        print "******** Paint component called *************"
        # find the index of the last redraw command in the list
        try:
            redraw_index = rindex(self.command_list, "redraw")
            list_head = self.command_list[:redraw_index]
            print "list head", list_head
        
            # index of the clear that precedes the last redraw
            clear_index = rindex(list_head, "clear")
        
        
        
            print "*** Repainting ***"
            for s in self.command_list[clear_index:redraw_index]:
                print s
            print "------------------"
            print
        
            # trim the command list
            self.command_list = self.command_list[clear_index:]
            print "trimmed", self.command_list
    
            print "*** PC COMPLETE"
            print
        
        except ValueError:
            pass
        

def repaintLoop():
    ''' call paintComponent at random inconvenient times '''

    while True:
        delay = uniform(.5, 1.0)
        #w.BADpaintComponent()
        w.GOODpaintComponent()
        sleep(delay)  
      
    
w = FakeWindow()    

repaintThread = Thread(target = repaintLoop)
repaintThread.daemon = True
repaintThread.start()

while True:
    w.clear()
    w.circle()
    w.rectangle()
    w.triangle()
    w.redraw()
    
    sleep(.05)   
    
    



