# TextEntry
Simple python script for automating text entry into a web form from a text file where each line is an entry.

**Dependencies: pyautogui**

```
usage: text_entry.py [-h] [--offsetX OFFSETX] [--offsetY OFFSETY] [--delay DELAY] source

Text field entry bot

positional arguments:
  source             text file containing each entry

options:
  -h, --help         show this help message and exit
  --offsetX OFFSETX  x pixel offset between text field and enter button
  --offsetY OFFSETY  y pixel offset between text field and enter button
  --delay DELAY      seconds of delay between text entry and click
```

