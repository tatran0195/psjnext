---
title: "dlg.clear _combobox()"
description: "Clear all options of a specified ComboBox"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Clear all options of a specified ComboBox.

## Syntax

```psj
dlg.clear _combobox(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the ComboBox component.

## Return Code

This function does not have output value.

## Sample Code

```psj {4}
from pyjdg import *

def on _button _clicked (dlg):
    dlg.clear _combobox(name="ComboBox2")
    print("All ComboBox options are cleared")

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _combobox(name="ComboBox2",options=["item1","item2","item3","item4"],index=1,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="Button3",text="Clear ComboBox",width=100,height=30,bk _color=15790320,layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _button _clicked(name="Button3",callfunc=on _button _clicked)

if __name__=='__main__':
    main()
```
