# killall_queue

## Idea

Hey there mate! Look at that shopping cart.. somebody's been busy shopping it seems :) Ah! I see flour, biscuits, deodorant (You sure need it) and oh! Is that Nutella. Looks nice. Great actually, but do you know what.. something's missing from your Cart - 
**SMARTNESS**
You sure are going to need it in your cart if you wish to avoid the long and tiresome queues at your favorite shopping mall on the day of the sale that everybody's been waiting for.

killall_queue brings to you an Internet of Things(IoT) based smart and secure shopping system which aims to -  
1. Improve the end user experience by "killing all queues" (please appreciate the linux reference) thereby saving customer's time, energy and effort that would have been wasted otherwise.
2. Increasing the revenue generated by the enterpize/shopping mall by :
* Increasing the number of people who may want to visit the mall and increasing the number of people who 
* Reducing the money spent on cashiers' salary every month. 
3. Providing assistance with inventory management by dynamically updating the database.

killall_queue's device consists of an RFID Scanner which reads data from RFID tags attached to each item kept in the shopping mall(hence creating an IoT system of carts and items) and sends it to the database. The android app which runs on the consumer's mobile device reads the data from this database(after logging in using the barcode on each cart), prepares the virtual cart including the items that the customer wants to buy and provides facilty to pay online using payment gateways. As a dual check, a weight sensor has also been deployed to keep a check on frauds and cheats who might swap RFID tags.

After checkout (which is allowed only when the user shows )the inventory is updated and the shopping mall owner can stay aware of the items that are running out.

## Tech Stack
1. Raspberry Pi 3B+
2. RFID (RC522)
3. Weight Sensor (hx711py)
4. Android Studio
5. Firebase REST API

## Instructions to run the application -
1. Connect the RFID (RC522) with Raspberry Pi 3B+
2. SSH to the Pi
3. git clone https://github.com/hackabit18/killall_queue/
4. cd killall_queue/iot-backend
5. python main.py
6. Scan the qr code by the app
7. You are ready to go!

Find more about the project here : http://killallqueue.tech/

## Future Prospects

Applications that the smart shopping system can perform have already been discussed right in the beginning.

The possibilities in which this humble effort to realize an awesome idea might grow into are umpteen. Some which we can easily think of are :

1. The inventory management system can be modified and the user can be provided with the location of the items that they are looking for using a chatbot
2. The dual check that was being done using a weight sensor can also be done using image processing which may give better results.

## Copyright Information
1. [RC522](https://github.com/hackabit18/killall_queue/blob/master/iot-backend/lib/RC522/LICENSE.txt)
2. [hx711py](https://github.com/hackabit18/killall_queue/blob/master/iot-backend/lib/hx711py/LICENSE)
