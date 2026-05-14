---
title: "dlg.on _dlg _ok()"
description: "Execute a created function when OK button is clicked"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute a created function when OK button is clicked.

## Syntax

```psj
dlg.on _dlg _ok(...)
```

## Inputs

<!-- @since:5.0.1 @type:PSJCallable @required -->
### `callfunc`

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {11}
from pyjdg import *

def on _button _OK _clicked(dlg):
    print("OK button is clicked")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True,include _apply=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Please click on OK button!",layout="Layout1")
    dlg.generate _window()
    dlg.on _dlg _ok(callfunc=on _button _OK _clicked)

if __name__=='__main__':
    main()
```
