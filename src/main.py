import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    
    counter = 0
    prevHands = [0] * 3000
    
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def readCharacter(listOfExtendedFingers, hand):
        bitSlice = 0
        for finger in listOfExtendedFingers:
            bitSlice += 2**finger.type
        if(hand.pinch_strength > 0.3):
            bitSlice += 32
        if(hand.pinch_strength > 0.6):
            bitSlice += 32
        if(bitSlice == 93):
            print "0"
        elif(bitSlice == 2):
            print "1"
        elif(bitSlice == 6):
            print "2"
        elif(bitSlice == 54):
            print "7"
        elif(bitSlice == 0):
            print "N"
        elif(bitSlice == 14):
            print "W"
        elif(bitSlice == 30):
            print "B"
        else:
            print " "


    # On every frame recieved by LeapMotion:
    def on_frame(self, controller):
        # initialize the finger count to zero
        extendedFingerCount = 0
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        if(len(frame.hands == 1)):
            detectedHand = frame.hands[0]
            extended_finger_list = frame.fingers.extended()
            readCharacter(extended_finger_list, detectedHand)
        else: 
            print " "

            
        # rightHand = frame.hands[0]
        # rightFingers = rightHand.fingers
        # extended_finger_list = frame.fingers.extended()
        
        # counter = counter + 1
        # if(counter == 3000):
        #     counter = 0

    #     # if all fingers except for 1 are extended, 
    #     # and pinch is greater than 0.6
    #     fingers_0 = 0
    #     for aFinger in extended_finger_list:
    #       if(aFinger.type != 1):
    #         fingers_0 += 1
    #       if(aFinger.type == 1):
    #         fingers_0 = -1
    #     if(fingers_0 == 4 and rightHand.pinch_strength > 0.6):
    #       print "0"

    
    #     # Letter B
    #     count = 0

    #     fingers_B = 0

    #     # if all fingers except for 0 are extended
    #     for aFinger in extended_finger_list:
    #         if(aFinger.type > 0):
    #             fingers_B = fingers_B + 1
    #         if(aFinger.type == 0):
    #             fingers_B = -1
    #         count = count + 1
    #     if(fingers_B == 4):
    #         print "B"

    #     # Letter W
    #     count = 0

    #     fingers_W = 0
    #     # If all fingers except for 0 and 4 are extended 
    #     for aFinger in extended_finger_list:
    #         if(aFinger.type > 0):
    #             fingers_W = fingers_W + 1
    #         if(aFinger.type == 0 or aFinger.type == 4):
    #             fingers_W = -1
    #         count = count + 1
    #     if(fingers_W == 3):
    #         print "W"

        
    # #Letter N
    #     count = 0
        
    #     fingers_N = 0;
    #     # if all fingers are CLOSED
    #     for aFinger in extended_finger_list:
    #         fingers_N += 1
    #     if(fingers_N == 0):
    #         print "N"

            
    #     # Number 1
    #     count = 0

    #     fingers_W = 0
    #     # only pointer finger (finger 1)
    #     for aFinger in extended_finger_list:
    #         if(aFinger.type > 0):
    #             fingers_W = fingers_W + 1
    #         if(aFinger.type == 0):
    #             fingers_W = -1
    #         count = count + 1
    #     if(fingers_W == 1):
    #         print "1"

        
    #     # Number 2
    #     count = 0

    #     # only fingers 1 and 2

    #     fingers_W = 0
    #     for aFinger in extended_finger_list:
    #         if(aFinger.type > 0):
    #             fingers_W = fingers_W + 1
    #         if(aFinger.type == 0 or aFinger.type == 3 or aFinger.type == 4):
    #             fingers_W = -1
    #         count = count + 1
    #     if(fingers_W == 2):
    #         print "2"

    #     #Number 7
       
    #     count = 0
    #     fingers_0 = 0
        
        
    #     # only fingers 2, 3, 4 are extended with pinch > 0.3 
    #     for aFinger in extended_finger_list:
    #         if(aFinger.type > 0):
    #             fingers_0 = fingers_0 + 1
    #         if(aFinger.type == 0 or aFinger.type == 3):
    #             fingers_0 = -1
    #         count +=1
    #         if (fingers_0 == 3 and rightHand.pinch_strength > 0.3):
    #             print "7"

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
