import os

# App initialization
from . import main # from the __init__ file

port_number = os.getenv("PORT_NUMBER")
application = main(os.getenv("CONFIG_MODE"))

if __name__ == "__main__":
  application.run(host="0.0.0.0", port=port_number)
