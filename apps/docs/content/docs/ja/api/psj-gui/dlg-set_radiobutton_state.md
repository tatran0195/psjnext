---
title: "dlg.set _radiobutton _state()"
description: "Set the state of the RadioButton to checked or unchecked"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set the state of the RadioButton to checked or unchecked.

## Syntax

```psj
dlg.set _radiobutton _state(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the component in which will be used for setting the state to selected/unselected.

<!-- @since:5.0.1 @required -->
### checked

- Specify the state of the checkbox:
  - _True_: The initial state of the checkbox component is checked.
  - _False_: The initial state of the checkbox component is unchecked.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
    dlg.add _radiobutton(name="RadioButton2",text="Jupiter",checked=True,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _radiobutton _state(name="RadioButton2",checked=False)
    isChecked = dlg.isbutton _checked(name="RadioButton2")
    print(isChecked)

if __name__=='__main__':
    main()
```
