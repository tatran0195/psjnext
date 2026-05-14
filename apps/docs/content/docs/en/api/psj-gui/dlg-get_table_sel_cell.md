---
title: "dlg.get _table _sel _cell()"
description: "Get the information and attributes of the selected cells"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the information and attributes of the selected cells.

## Syntax

```psj
dlg.get _table _sel _cell(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of Table.

## Return Code

- A _[TableCellVector](../data-type/psj-gui/TableCellVector)_ object or _List of [TableCellID](../data-type/psj-gui/TableCellID)_ specifying the methods of cells.

## Sample Code

```psj {4}
from pyjdg import *

def on _context _click(dlg,name,menu):
    cellvector=dlg.get _table _sel _cell(name="Table1")
    for i in range(cellvector.size()):
        print("The cell number {} has information".format(i+1))
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
    dlg.on _table _right _menu(name="Table1",callfunc=on _context _click)

if __name__=='__main__':
    main()
```
