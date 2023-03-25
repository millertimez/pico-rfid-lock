from mfrc522 import MFRC522
from machine import Pin
import utime
              
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
reader2 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=1,rst=22)
reader3 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=13,rst=22)
reader4 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=10,rst=22)

lock =Pin(16,Pin.OUT)

print("")
print("Place card into reader")
print("")

pin = Pin("LED", Pin.OUT)

try:
    
    # make the LED blink 3 times... just for fun
    pin.value(1)
    utime.sleep_ms(500)
    pin.value(0)
    utime.sleep_ms(500)
    pin.value(1)
    utime.sleep_ms(500)
    pin.value(0)
    utime.sleep_ms(500)
    pin.value(1)
    utime.sleep_ms(500)
    pin.value(0)
    
    # main loop
    while True:

        step1 = 0
        step2 = 0
        step3 = 0
        step4 = 0

        # Reader 1
        reader.init()
        # read card ud
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            # get the uid
            (stat, uid) = reader.SelectTagSN()
            # debug print the uid in order to hard code it for the next step
            print("Card detected {}  uid={}".format(hex(int.from_bytes(bytes(uid),"little",False)).upper(),reader.tohexstring(uid)))
            
            # hard coded uid check... much easier than setting and reading the keys....
            if uid == [0x61, 0xE7, 0xCE, 0x1C] or uid == [0xB3, 0x85, 0xF7, 0x93]:
                # uid matches, so set pass for this reader
                step1 = 1

        reader2.init()
        (stat2, tag_type2) = reader2.request(reader2.REQIDL)
        if stat2 == reader2.OK:
            (stat2, uid2) = reader2.SelectTagSN()
            print("Card2 detected {}  uid={}".format(hex(int.from_bytes(bytes(uid2),"little",False)).upper(),reader2.tohexstring(uid2)))
            
            if uid2 == [0x2C, 0x25, 0x59, 0x49] or uid2 == [0x80, 0x61, 0x22, 0x53]:
                step2 = 1

        reader3.init()
        (stat3, tag_type3) = reader3.request(reader3.REQIDL)
        if stat3 == reader3.OK:
            (stat3, uid3) = reader3.SelectTagSN()
            print("Card3 detected {}  uid={}".format(hex(int.from_bytes(bytes(uid3),"little",False)).upper(),reader3.tohexstring(uid3)))
            
            if uid3 == [0x90, 0xD0, 0x43, 0x25] or uid3 == [0x59, 0xD9, 0x74, 0x54]:
                step3 = 1

        reader4.init()
        (stat4, tag_type4) = reader4.request(reader4.REQIDL)
        if stat4 == reader4.OK:
            (stat4, uid4) = reader4.SelectTagSN()
            print("Card detected {}  uid={}".format(hex(int.from_bytes(bytes(uid4),"little",False)).upper(),reader4.tohexstring(uid4)))
            
            if uid4 == [0x71, 0xC3, 0x42, 0x1C] or uid4 == [0x99, 0x2C, 0x48, 0x54]:
                step4 = 1

        # if all have matches open the lock and turn on the LED
        if step1==1 and step2==1 and step3==1 and step4==1:
            pin.value(1)
            lock.value(1)
        else:
            pin.value(0)
            lock.value(0)
        utime.sleep_ms(50)                

except KeyboardInterrupt:
    print("Bye")

