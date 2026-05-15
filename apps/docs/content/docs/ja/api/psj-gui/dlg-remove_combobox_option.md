---
title: "dlg.remove _combobox _option()"
description: "Remove a specified option in a ComboBox"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Remove a specified option in a ComboBox.

## Syntax

```psj
dlg.remove _combobox _option(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of the ComboBox component.

<!-- @since:5.1.0 @required -->
### position

- Specify the position of option in ComboBox to be removed.

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def on _button _clicked(dlg):
    option _idx=dlg.get _combobox _sel(name="ComboBox2")
    option _name=dlg.get _combobox _option(name="ComboBox2",index=option _idx)
    dlg.remove _combobox _option(name="ComboBox2",position=option _idx)
    print("The option " + option _name + " is removed")

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _combobox(name="ComboBox2",options=["item1","item2","item3","item4"],width=80,height=25,
        index=0,layout="Layout1")
    dlg.add _button(name="Button3",text="Remove Option",width=90,height=25,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _button _clicked(name="Button3",callfunc=on _button _clicked)

if __name__=='__main__':
    main()
```
