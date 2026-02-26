from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

class Rfid():
  @staticmethod
  def read() -> None:
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
  def write() -> None:
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
  def writeIdRange() -> None:
    reader = SimpleMFRC522()
    try:
      range_from, range_to = Rfid.getIdRange()
      for id in range(range_from, range_to + 1):
        text = str(id)
        print(f"Place RFID card near reader to write ID {id}...")
        reader.write(text)
        print(f"ID {id} written successfully!")
        if id != range_to:
          input("Move card away from reader and press Enter to continue")
          print("\nSwitching to next ID...")
      print(f"\nAll IDs in range {range_from}-{range_to} written successfully!")
    except Exception as e:
      print(f"Cannot write to card: {e}")
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
  
  @staticmethod
  def getIdRange() -> tuple[int, int]:
    while True:
      range_from = input("Input ID to start with: ").strip()
      range_to = input("Input ID to end with: ").strip()
      try:
        range_from = int(range_from)
        range_to = int(range_to)
      except ValueError:
        print("Your input is not an integer! Try again...")
        continue
      if range_from > range_to:
        print("ID from is greater than ID to. Try again...")
      else:
        return (range_from, range_to)