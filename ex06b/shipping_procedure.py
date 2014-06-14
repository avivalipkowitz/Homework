#!/usr/bin/env python
import robots
from sys import argv


class FoodThing(object):

    def __init__(self, melon_type):
        self.melon_type = melon_type
        self.weight = 0.0
        self.color = None
        self.stickers = []

    def prep(self):
        robots.cleanerbot.clean(self) # clean is method of cleanerbot defined in robots.py file
        robots.stickerbot.apply_logo(self)
    
    def __str__(self):
        if self.weight <= 0:
            return self.melon_type
        else:
            return "%s %0.2fLB %s" % (self.color, self.weight, self.melon_type)


class WinterSquash(FoodThing):

    def prep(self):
        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)
        robots.painterbot.paint(self)

class Melon(FoodThing):
    pass    # Is this an appropriate move? I don't want it to do anything different than 
            # the parent class...

    

def main():

    # read in files. Added this for-loop so that when new melons/squashes
    # become available, user can just call an additional script in the 
    # command line.

    for i in range(1, len(argv)):
        myfile = open(argv[-1])
        
        for line in myfile: 
            (melon_type, quantity) = line.rstrip().split(':')
            quantity = int(quantity)
            
            count = 0
            melons = []
            while len(melons) < quantity:
                if count > 200:
                    print "\nALL MELONS HAVE BEEN PICKED"
                    print "ORDERS FAILED TO BE FULFILLED!"
                    sys.exit()
                
                if melon_type == "Winter Squash":
                    m = WinterSquash(melon_type)
                else:
                    m = Melon(melon_type)

                robots.pickerbot.pick(m)
                count += 1
                
                m.prep()
                
                # paint all yellow melons (should only be winter squash) green
                robots.painterbot.paint(m)

                # evaluate melon
                presentable = robots.inspectorbot.evaluate(m)
                if presentable:
                    melons.append(m)
                else:
                    robots.trashbot.trash(m)
                    continue


        print "------"
        print "Robots Picked %d %s for order of %d" % (count, melon_type, quantity)

        # Pack the melons for shipping
        boxes = robots.packerbot.pack(melons)
        # Ship the boxes
        robots.shipperbot.ship(boxes)
        print "------\n"


if __name__ == "__main__":
    main()