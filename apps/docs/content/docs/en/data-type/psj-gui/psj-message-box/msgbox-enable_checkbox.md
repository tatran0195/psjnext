---
title: msgbox.enable_checkbox()
id: msgbox-enable_checkbox
---

## Description

An instance of a PSJMessageBox class, specifying a checkbox in the message box.

## Syntax

```py
msgbox.enable_checkbox(...)
```

## Input

### `text`

- A _String_ specifying the content of checkbox.
- This is a required input.

### `checked`

- A _Boolean_ specifying the default state of this component:
    - _True_: the default state of this component is checked.
    - _False_: the default state of this component is unchecked.
- The default value is _False_.

## Return Code

This function does not have output value.

## Sample Code

```py {9}
from pyjdg import *

def main():
    msgbox=PSJMessageBox()
    msgbox.set_caption(text="PSJ Message Box")
    msgbox.set_header(text="")
    msgbox.set_icon(icon_type=msgbox_icon.error)
    msgbox.set_message(text="This is an error message box")
    msgbox.enable_checkbox(text="Do not show again", checked=True)
    msgbox.set_buttons(button_type=msgbox_buttons.yes_no_cancel)
    print("clicked:"+msgbox.show())

if __name__=='__main__':
    main()
```
