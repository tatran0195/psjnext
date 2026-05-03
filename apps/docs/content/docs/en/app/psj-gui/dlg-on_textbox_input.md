---
title: "dlg.on_textbox_input()"
description: "Bind a created function to a textbox component when its text is changed"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Bind a created function to a textbox component when its text is changed.

## Syntax

```psj
dlg.on_textbox_input(...)
```

## Inputs

### `name` @type(String) @required

- The name of the TextBox component using for binding a created def function.

### `callfunc` @type(PSJCallable) @required

- The name of function wants to be bound to.

### `bool` @type(Boolean) @required

- Whether to validate the textbox.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *
def on_input(dlg):
    text=dlg.get_item_text("TextBox2")
    if text=="1":
        return False
    else :
        print("Hello")
        return True
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_textbox(name="TextBox2",layout="Window")
    dlg.generate_window()
    dlg.on_textbox_input("TextBox2",on_input,True)
if __name__=='__main__':
    main()
```
