---
title: "dlg.on _table _sel _changed()"
description: "Set event when selecting a cell"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set event when selecting a cell.

## Syntax

```psj
dlg.on _table _sel _changed(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of Table.

<!-- @since:5.0.1 @type:PSJCallable @required -->
### `callfunc`

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {22}
from pyjdg import *

def on _sel _change(dlg,name,cell):
    cellvector=dlg.get _table _sel _cell(name="Table1")
    if cellvector.size() > 0:
       print("Cell's position (row) = "+str(cellvector[0].row _number))
       print("Cell's position (column) = "+str(cellvector[0].col _number))
       print("---------------------------")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _table _right _menu(name="Table1",menus=["Check cell info"])
    dlg.generate _window()
    dlg.on _table _sel _changed(name="Table1",callfunc=on _sel _change)

if __name__=='__main__':
    main()
```
