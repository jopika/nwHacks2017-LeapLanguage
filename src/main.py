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

    def on_frame(self, controller):
        counter = 0
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        rightHand = frame.hands[0]
        rightFingers = rightHand.fingers
        extended_finger_list = frame.fingers.extended()
        
        counter = counter + 1
        if(counter == 3000):
            counter = 0

        fingers_0 = 0
        for aFinger in extended_finger_list:
          if(aFinger.type != 1):
            fingers_0 += 1
          if(aFinger.type == 1):
            fingers_0 = -1
        if(fingers_0 == 4 and rightHand.pinch_strength > 0.6):
          print "0"

    
        # Letter B
        count = 0

        fingers_B = 0

        for aFinger in extended_finger_list:
            if(aFinger.type > 0):
                fingers_B = fingers_B + 1
            if(aFinger.type == 0):
                fingers_B = -1
            count = count + 1
        if(fingers_B == 4):
            print "B"

        # Letter W
        count = 0

        fingers_W = 0
        for aFinger in extended_finger_list:
            if(aFinger.type > 0):
                fingers_W = fingers_W + 1
            if(aFinger.type == 0 or aFinger.type == 4):
                fingers_W = -1
            count = count + 1
        if(fingers_W == 3):
            print "W"

        
    #Letter N
        count = 0
        
        fingers_N = 0;
        for aFinger in extended_finger_list:
            fingers_N += 1
        if(fingers_N == 0):
            print "N"

            
        # Number 1
        count = 0

        fingers_W = 0
        for aFinger in extended_finger_list:
            if(aFinger.type > 0):
                fingers_W = fingers_W + 1
            if(aFinger.type == 0):
                fingers_W = -1
            count = count + 1
        if(fingers_W == 1):
            print "1"

        
        # Number 2
        count = 0

        fingers_W = 0
        for aFinger in extended_finger_list:
            if(aFinger.type > 0):
                fingers_W = fingers_W + 1
            if(aFinger.type == 0 or aFinger.type == 3 or aFinger.type == 4):
                fingers_W = -1
            count = count + 1
        if(fingers_W == 2):
            print "2"

        #Number 7
       
        count = 0
        fingers_0 = 0
        
           
        for aFinger in extended_finger_list:
            if(aFinger.type > 0):
                fingers_0 = fingers_0 + 1
            if(aFinger.type == 0 or aFinger.type == 3):
                fingers_0 = -1
            count +=1
            if (fingers_0 == 3 and rightHand.pinch_strength > 0.3):
                print "7"

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
