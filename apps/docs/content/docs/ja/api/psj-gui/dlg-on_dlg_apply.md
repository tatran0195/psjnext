---
title: "dlg.on _dlg _apply()"
description: "Execute a created function when Apply button is clicked"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Execute a created function when Apply button is clicked.

## Syntax

```psj
dlg.on _dlg _apply(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### callfunc

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {11}
from pyjdg import *

def on _button _Apply _clicked(dlg):
    print("Apply button is clicked")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True,include _apply=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Please click on Apply button!",layout="Layout1")
    dlg.generate _window()
    dlg.on _dlg _apply(callfunc=on _button _Apply _clicked)

if __name__=='__main__':
    main()
```
