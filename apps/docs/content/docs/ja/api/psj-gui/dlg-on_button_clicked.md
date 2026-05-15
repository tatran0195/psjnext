---
title: "dlg.on _button _clicked()"
description: "Bind a created def function to a Button/RadioButton/CheckBox"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Bind a created function to a Button/RadioButton/CheckBox.

## Syntax

```psj
dlg.on _button _clicked(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the Button/RadioButton/CheckBox using for binding a created def function.

<!-- @since:5.0.1 @required -->
### callfunc

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {29-31}
from pyjdg import *

def on _button _clicked(dlg):
    JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube _1", 5357649, 0:0)')
    print("--- Cube created! ---")

def on _checkbox _clicked(dlg):
    print("You clicked on Checkbox!")

def on _radio _buton _clicked(dlg):
    print("You clicked on Radio Button!")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox2",text="GroupBox",layout="Window")
    dlg.add _layout(name="Layout4",orientation=orientation.vertical,layout="GroupBox2")
    dlg.add _label(name="Label8",text="Click on Button!",text _halign="left",text _valign="top",layout="Layout4")
    dlg.add _button(name="Button5",text="Button",width=60,height=22,layout="Layout4")
    dlg.add _label(name="Label9",text="Click on Checkbox!",text _halign="left",text _valign="top",layout="Layout4")
    dlg.add _checkbox(name="CheckBox6",text="CheckBox",layout="Layout4")
    dlg.add _label(name="Label10",text="Click on Radio Button!",text _halign="left",text _valign="top",layout="Layout4")
    dlg.add _radiobutton(name="RadioButton7",text="RadioButton",layout="Layout4")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _button _clicked(name="Button5",callfunc=on _button _clicked)
    dlg.on _button _clicked(name="CheckBox6",callfunc=on _checkbox _clicked)
    dlg.on _button _clicked(name="RadioButton7",callfunc=on _radio _buton _clicked)

if __name__=='__main__':
    main()
```
