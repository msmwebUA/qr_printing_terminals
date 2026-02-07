from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

class Rfid():
  @staticmethod
  def read():
    reader = SimpleMFRC522()
    try:
        print("Scan your card or press Ctrl+C for exit from scan mode:")
        while True:
            id, text = reader.read()
            print(f"Card detected, UID: {id} and text: {text}")
    except KeyboardInterrupt:
        print("\nExiting from read mode...")
    finally:
        GPIO.cleanup()

  @staticmethod
  def write():
    reader = SimpleMFRC522()
    try:
      text = Rfid.getText()
      print("Place RFID card near reader to write...")
      reader.write(text)
      print("Text written successfully!")
    except Exception as e:
      print(f"Cannot write text: {e}")
    finally:
      GPIO.cleanup()

  @staticmethod
  def getText() -> str:
    while True:
      text = input("Input text to save: ").strip()
      length = len(text)
      if length > 48:
        print(f"Max 49 chars allowed. Your text is {length} chars. Try again...")
      else:
        return text