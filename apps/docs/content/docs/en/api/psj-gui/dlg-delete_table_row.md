---
title: "dlg.delete _table _row()"
description: "Delete row at a specific position in the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Delete row at a specific position in the Table.

## Syntax

```psj
dlg.delete _table _row(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of Table.

<!-- @since:5.0.1 @type:Integer @required -->
### `position`

- The position of row to be deleted.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def on _menu(dlg,name,menu):
    sel _ranges=dlg.get _table _sel _range(name="Table1")
    if sel _ranges.size()>0:
        position=sel _ranges[0].top
    dlg.delete _table _row(name="Table1",position=position)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=5,
        columns=["Heading1","Heading2","Heading3"],
        layout="Window",width=260,height=260)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _table _right _menu(name="Table1",menus=["Delete Row"])
    dlg.generate _window()
    dlg.on _table _right _menu(name="Table1",callfunc=on _menu)

if __name__=='__main__':
    main()
```
