class Parents(name, age, childrenlist):
    def __init__(self)
        self.name = name 
        self.age = age
        self.childrenlist = childrenlist
                
    
    def no_of_children(self.childrenlist):
        return(len(self.childernlist))

    def good_parent(no_of_children(self.childrenlist)):
        number = no_of_children(self.childrenlist)
        if number<=2:
            print('good parent')
        else:
            print('bad parent')

sunita = Parents('sunita',45,['adi','bedi'])
no_of_children = sunita.no_of_children()
good_parent= sunita.good_parent()