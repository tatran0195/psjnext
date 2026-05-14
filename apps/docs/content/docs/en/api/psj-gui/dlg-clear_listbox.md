---
title: "dlg.clear _listbox()"
description: "Clear all options of a specified ListBox"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Clear all options of a specified ListBox.

## Syntax

```psj
dlg.clear _listbox(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the ListBox component.

## Return Code

This function does not have output value.

## Sample Code

```psj {4}
from pyjdg import *

def on _button _clicked (dlg):
    dlg.clear _listbox(name="ListBox2")
    print("All ListBox options are cleared")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _listbox(name="ListBox2",multisel=True,
      options=["item1","item2","item3"],width=100,height=150,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="Button3",text="Clear ListBox",width=100,height=30,bk _color=15790320,layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _button _clicked(name="Button3",callfunc=on _button _clicked)

if __name__=='__main__':
    main()
```
