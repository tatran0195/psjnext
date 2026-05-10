---
title: msgbox.add_button()
id: msgbox-add_button
---

## Description

An instance of a PSJMessageBox class, adding a button whose button name can be defined by user.

## Syntax

```psj
msgbox.add_button(...)
```

## Input

### `pos`

- An _Enum_ specifying the [`msgbox_position`](msgbox-position-types) of the button to be added.
- This is a required input.

### `text`

- A _String_ specifying the name of the added button.
- This is a required input.

## Return Code

This function does not have output value.

## Sample Code

```psj {9-11}
from pyjdg import *

def main():
    msgbox=PSJMessageBox()
    msgbox.set_caption(text="PSJ Message Box")
    msgbox.set_header(text="")
    msgbox.set_icon(icon_type=msgbox_icon.error)
    msgbox.set_message(text="This is an error message box")
    msgbox.add_button(pos=msgbox_position.first, text="First")
    msgbox.add_button(pos=msgbox_position.second, text="Second")
    msgbox.add_button(pos=msgbox_position.third, text="Third")
    print("clicked:"+msgbox.show())

if __name__=='__main__':
    main()
```
