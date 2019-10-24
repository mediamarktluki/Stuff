#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

class MyRead:
 def __init__(self):
  self.text = None
  self.back = []
 def read(self):
  global back
  global running
  import RPi.GPIO as GPIO
  import MFRC522
  import signal
  running = True

  MIFAREReader = MFRC522.MFRC522()


  while running:
    # Scan for cards
   (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
   if status == MIFAREReader.MI_OK:

    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
   if status == MIFAREReader.MI_OK:


    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
	data = status
        # Check if authenticated


   if status == MIFAREReader.MI_OK:
           self.back = MIFAREReader.MFRC522_Read(8)
           MIFAREReader.MFRC522_StopCrypto1()
	   self.text = "".join(chr(x) for x in self.back)
	   return self.text
	   running = False
   else:
	  self.text = "".join(chr(x) for x in self.back)
	  running = True
  return self.text
