---
title: "dlg.isbutton _checked()"
description: "Check the status of the inputted component whether it's checked or not. Currently supporting checkbox and radio button components"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Check the status of the inputted component whether it is checked or not.
Currently supporting checkbox and radio button components.

## Syntax

```psj
dlg.isbutton _checked(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the component using for checking the status of selection.

## Return Code

A _Boolean_ specifying the status of the inputted component:

- _True_: The inputted component is checked (Selected).
- _False_: The inputted component is unchecked (Unselected).

## Sample Code

```psj {4}
from pyjdg import *

def check _status(dlg):
    isChecked = dlg.isbutton _checked(name="CheckBox2")
    print(isChecked)

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
    dlg.add _checkbox(name="CheckBox2",text="Jupiter",checked=True,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _command(name="CheckBox2",callfunc=check _status)

if __name__=='__main__':
    main()
```
