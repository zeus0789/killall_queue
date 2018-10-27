import RPi.GPIO as GPIO
import time
import datetime
import sys
from lib.hx711py.hx711 import HX711
import lib.RC522.MFRC522 as MFRC522
import signal
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
import json

continue_reading = True

SECRET = '7GmEpvZULivAmWAZdJ8CN17f0kA2k0qsXSys4AKZ'
DSN = 'https://loginauth-fb69f.firebaseio.com/'
EMAIL = 'io.satyamtg@gmail.com'
authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
firebase = FirebaseApplication(DSN, authentication)
cartno = 7412350101


def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522

MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."
prevwt=0

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])

        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
            itemcode = 00000001
            reqwt = prevwt + json.loads(firebase.get('/inventory/itemcode/weight', None))
            print reqwt
            GPIO.cleanup()
            hx = HX711(5, 6)
            hx.set_reading_format("LSB", "MSB")
            hx.set_reference_unit(920)

            hx.reset()
           # hx.tare()

            scanWt = 1
            while (scanWt<5):
                try:
                    # These three lines are usefull to debug wether to use MSB or LSB in the reading formats
                    # for the first parameter of "hx.set_reading_format("LSB", "MSB")".
                    # Comment the two lines "val = hx.get_weight(5)" and "print val" and uncomment the three lines to see what it prints.
                    #np_arr8_string = hx.get_np_arr8_string()
                    #binary_string = hx.get_binary_string()
                    #print binary_string + " " + np_arr8_string

                    # Prints the weight. Comment if you're debbuging the MSB and LSB issue.
                    val = hx.get_weight(5)
                    print val
                   # if (val>=prevwt-4 and val<=prevwt+4):
                    #    timeout = timeout + 1
                   # elif (val<prevwt-4):
                    #    if (value>=removedwt-2 and value<=removedwt+2):
                            #Remove product from cart
                     #       scanWt = 0
                      #      prevwt = value
                       #     GPIO.cleanup()
                       # else:
                        #    #Notify error
                         #   scanWt = 0
                          #  GPIO.cleanup()
                   # else:
                    #    if (value>=reqwt-2 and value<=reqwt+2):
                     #       #Add product to cart
                      #      scanWt = 0
                       #     prevwt = value
                        #    GPIO.cleanup()
                      #  else:
                            #Notify Error
                       #     scanWt = 0
                        #    GPIO.cleanup()
                    hx.power_down()
                    hx.power_up()
                    time.sleep(0.5)
                    scanWt = scanWt+1
                except (KeyboardInterrupt, SystemExit):
                    GPIO.cleanup()
        else:
            print "Authentication error"
