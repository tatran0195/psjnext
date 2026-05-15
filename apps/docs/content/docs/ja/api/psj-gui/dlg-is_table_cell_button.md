---
title: "dlg.is _table _cell _button()"
description: "Check the input cell is a button cell or not"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Check the input cell is a button cell or not.

## Syntax

```psj
dlg.is _table _cell _button(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

<!-- @since:5.0.1 @required -->
### cell

- Specify the location of cell in Table.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row\_number returns row number of the cell
  - TableCellID.col\_number returns column number of the cell

## Return Code

A _Boolean_ specifying the type of inputted cell:

- _True_: The inputted cell is a button cell.
- _False_: The inputted cell is not a button cell.

## Sample Code

```psj {7-9}
from pyjdg import *

def on _cell _button _clicked(dlg,name,cell):
    JPT.ClearLog()
    cellvector=dlg.get _table _sel _cell(name="Table2")
    if cellvector.size() > 0:
       check _cell _button = \
            dlg.is _table _cell _button(name="Table2",
                cell=cellvector[0])
       print("Is button cell: " + str(check _cell _button))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table2",width=260,height=260,
        columns=["Heading1","Heading2"],
        rows=5,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",
        layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _table _cell _button(name="Table2",row=0,
        col=0,text="Button")
    dlg.on _table _sel _changed(name="Table2",
        callfunc=on _cell _button _clicked)

if __name__=='__main__':
    main()
```
