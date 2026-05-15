---
title: "dlg.remove _listbox _option()"
description: "Remove a specified option in a ListBox"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Remove a specified option in a ListBox.

## Syntax

```psj
dlg.remove _listbox _option(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of the ComboBox component.

<!-- @since:5.1.0 @required -->
### position

- Specify the position of option in ListBox to be removed.

## Return Code

This function does not have output value.

## Sample Code

```psj {8}
from pyjdg import *

def on _button _clicked (dlg):
# It is possible to remove options one by one or multiple options at the same time
    options _idx=list(dlg.get _listbox _sels(name="ListBox2"))
    for idx in options _idx:
        option _name=dlg.get _listbox _option(name="ListBox2",option _index=options _idx[0])
        dlg.remove _listbox _option(name="ListBox2",position=options _idx[0])
        print("The option " + option _name + " is removed")


def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _listbox(name="ListBox2",multisel=True,
      options=["item1","item2","item3"],width=100,height=150,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="Button3",text="Remove Option",width=100,height=30,bk _color=15790320,layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _button _clicked(name="Button3",callfunc=on _button _clicked)

if __name__=='__main__':
    main()
```
