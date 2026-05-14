---
title: "dlg.set _groupbox _collapsed()"
description: "Set the initial state of the GroupBox's collapse to show/hide GroupBox's components"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set the initial state of the GroupBox's collapse feature to show/hide GroupBox's components.

## Syntax

```psj
dlg.set _groupbox _collapsed(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of GroupBox which will be used for setting the state of its collapse feature.

<!-- @since:5.0.1 @type:Boolean @required -->
### `collapsed`

- The state of the GroupBox's collapse feature:
  - _True_: Enable the collapse with its state is collapsed (hide all GroupBox's components).
  - _False_: Enable the collapse with its state is expanded (show all GroupBox's components).

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.set _groupbox _collapsed(name="GroupBox1",collapsed=True)
    dlg.set _groupbox _orientation(name="GroupBox1",orientation="horizontal")
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
