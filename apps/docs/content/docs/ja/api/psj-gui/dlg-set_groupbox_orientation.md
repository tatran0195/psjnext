---
title: "dlg.set _groupbox _orientation()"
description: "Set the layout of all the components inside the inputted GroupBox component to be aligned in the horizontal or vertical direction"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set the layout of all the components inside the GroupBox component to be aligned in the horizontal or vertical direction.

## Syntax

```psj
dlg.set _groupbox _orientation(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the component using for setting the orientation option.

<!-- @since:5.0.1 @required -->
### orientation

- Specify the orientation option of the GroupBox:
  - "vertical": align all the inside components in the vertical direction.
  - "horizontal": align all the inside components in the horizontal direction.

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.set _groupbox _orientation(name="GroupBox1",orientation="vertical")
    dlg.add _label(name="Label2",text="Label",layout="GroupBox1")
    dlg.add _textbox(name="TextBox3",layout="GroupBox1")
    dlg.add _label(name="Label4",text="Label",layout="GroupBox1")
    dlg.add _textbox(name="TextBox5",layout="GroupBox1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
