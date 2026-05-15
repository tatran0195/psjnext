---
title: "dlg.set _groupbox _checked()"
description: "Set the initial state of the GroupBox's checkbox to enable/disable GroupBox's components."
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set the initial state of the GroupBox's checkbox to enable/disable GroupBox's components.

## Syntax

```psj
dlg.set _groupbox _checked(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of GroupBox which will be used for setting the state of its checkbox.

<!-- @since:5.0.1 @required -->
### checked

- Specify the state of the GroupBox's checkbox:
  - _True_: Enable the checkbox with its state is checked (all components inside are available to use).
  - _False_: Enable the checkbox with its state is unchecked (all components inside are unavailable to use).

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.set _groupbox _checked(name="GroupBox1",checked=True)
    dlg.add _layout(name="Layout2",orientation=orientation.horizontal,layout="GroupBox1")
    dlg.add _label(name="Label3",text="Label",layout="Layout2")
    dlg.add _textbox(name="TextBox4",layout="Layout2")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
