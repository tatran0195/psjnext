---
title: "dlg.on _activate _selector()"
description: "Run a created function after a selector is activated."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Run a created function after a selector is activated.

## Syntax

```psj
dlg.activate _selector(...)
```

## Inputs

<!-- @since:5.1.0 @type:PSJCallable @required -->
### `callfunc`

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {33}
from pyjdg import *

def on _node _selector _clicked(dlg):
    dlg.activate _selector(0)

def on _part _selector _clicked(dlg):
    dlg.activate _selector(1)

def on _activate _selector(dlg,selector _id):
    if selector _id==0:
       dlg.set _radiobutton _state("RadioButton3",True)
       dlg.set _radiobutton _state("RadioButton4",False)
    else :
       dlg.set _radiobutton _state("RadioButton4",True)
       dlg.set _radiobutton _state("RadioButton3",False)

def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _label(
            name="Label2",width=200,height=80,
            text="Open the selection list.\n" 
                 "Confirm that selector focus changes when radio buttons are selected,"
                 "and conversely, that radio button selection changes when selectors are focused.",
            text _halign="left",text _valign="top",layout="Window")
    dlg.add _node _selector()
    dlg.add _part _selector()
    dlg.add _layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
    dlg.add _radiobutton(name="RadioButton3",text="Node",layout="Layout2",checked=True)
    dlg.add _radiobutton(name="RadioButton4",text="Part",layout="Layout2")
    dlg.generate _window()
    dlg.on _button _clicked("RadioButton3",on _node _selector _clicked)
    dlg.on _button _clicked("RadioButton4",on _part _selector _clicked)
    dlg.on _activate _selector(on _activate _selector)

if __name__=='__main__':
    main()
```
