import logging


try:
    import RPi.GPIO as GPIO

except ImportError:
    logging.warning("RPi GPIO module is not installed. Falling back to dummy GPIO...")
    import dpl.connections.gpio_dummy as GPIO

except RuntimeError:
    logging.warning("RPi GPIO module can't be loaded on this system. "
                    "Falling back to dummy GPIO...")
    import dpl.connections.gpio_dummy as GPIO