---
title: "dlg.enable _table _cell()"
description: "Set to enable/disable the cell in the table"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set to enable/disable the cell in the table.

## Syntax

```psj
dlg.enable _table _cell(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the Table.

<!-- @since:5.1.0 @type:Integer @required -->
### `row`

- The position in the horizontal direction of the cell (starts from 0).

<!-- @since:5.1.0 @type:Integer @required -->
### `col`

- The position in the vertical direction of the cell (starts from 0).

<!-- @since:5.1.0 @type:TableCellID @required -->
### `cell`

- The object specifying the location of cell in Table. This argument is only used when _row_ and _col_ are not specified.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row\_number returns row number of the cell
  - TableCellID.col\_number returns column number of the cell

<!-- @since:5.1.0 @type:Boolean @required -->
### `enable`

- Whether to enable/disable cell:
  - _True_: Enable to cell.
  - _False_: Disable to cell.

## Return Code

This function does not have output value.

## Sample Code

```psj {7,10}
from pyjdg import *

def on _menu(dlg,name,menu):
    table _cell = dlg.get _table _sel _cell(name)
    if menu == "Disable Cells":
        for cell in table _cell:
            dlg.enable _table _cell(name="Table1",cell=cell,enable=False)
    elif menu == "Enable Cells":
        for cell in table _cell:
            dlg.enable _table _cell(name="Table1",cell=cell,enable=True)

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
    dlg.add _table _right _menu(name="Table1",
        menus=["Disable Cells","Enable Cells"])
    dlg.generate _window()
    dlg.on _table _right _menu(name="Table1",callfunc=on _menu)

if __name__=='__main__':
    main()
```
