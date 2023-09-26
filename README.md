
## OPIGPIO: A Python Package for GPIO on Orange Pi

OPIGPIO is a Python package designed to simplify GPIO (General Purpose Input/Output) operations on Orange Pi. The package offers an Arduino-like API and is designed for ease of use.

### Features

- Easy-to-use API similar to Arduino.
- Automatic permission handling for non-root users.
- Comprehensive logging for debugging.

### Installation

#### Installation from PyPI

```bash
pip install OPIGPIO
```

### Usage

Here's a quick example that shows how to make an LED blink connected to pin 12:

```python
import time
import logging
from OPIGPIO.opi_gpio import OPIGPIO

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the GPIO class
gpio = OPIGPIO()

# Run any setup code
gpio.setup()

# Set the mode of pin 12 as output
gpio.pinMode(12, "out")

# Loop to make the LED blink
while True:
    gpio.digitalWrite(12, 1)  # Turn the LED on
    time.sleep(1)             # Wait for 1 second
    gpio.digitalWrite(12, 0)  # Turn the LED off
    time.sleep(1)             # Wait for 1 second
```

### Security Note

This package includes the ability to change file permissions to allow GPIO operations for non-root users. Please be aware that this has security implications and should only be used in trusted environments.
