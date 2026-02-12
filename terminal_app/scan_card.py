# Class for reading data from rfid card

from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

class ScanCard():

  def __init__(self, config: object):
    self.config = config

  def read(self) -> list:
    """Read data from rfid card. Return list with 2 elements: 
        list[0] is result code (0 - error, 1 - success), 
        list[1] is error message or text from card"""
    counter = 0
    try:
      reader = SimpleMFRC522()
      while True:
        id, text = reader.read()
        if (id and text):
          return [1, text.strip()]
        counter += 1
        # limit false scans
        if counter > self.config.max_scans:
          raise Exception("Exceeded limit of false scans")
    except Exception as e:
      return [0, e]
    finally:
      GPIO.cleanup()
