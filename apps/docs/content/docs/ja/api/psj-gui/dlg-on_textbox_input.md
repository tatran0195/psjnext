---
title: "dlg.on _textbox _input()"
description: "Bind a created function to a textbox component when its text is changed"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Bind a created function to a textbox component when its text is changed.

## Syntax

```psj
dlg.on _textbox _input(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of the TextBox component using for binding a created def function.

<!-- @since:5.1.0 @required -->
### callfunc

- The name of function wants to be bound to.

<!-- @since:5.1.0 @required -->
### bool

- Specify whether to validate the textbox.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *
def on _input(dlg):
    text=dlg.get _item _text("TextBox2")
    if text=="1":
        return False
    else :
        print("Hello")
        return True
def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _textbox(name="TextBox2",layout="Window")
    dlg.generate _window()
    dlg.on _textbox _input("TextBox2",on _input,True)
if __name__=='__main__':
    main()
```
