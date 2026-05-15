---
title: "dlg.add _table _sel _option()"
description: "Set combobox cell in the Table"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set combobox cell in the Table.

## Syntax

```psj
dlg.add _table _sel _option(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of Table.

<!-- @since:5.1.0 @required -->
### row

- Specify the position in the horizontal direction of the cell (starts from 0).

<!-- @since:5.1.0 @required -->
### col

- Specify the position in the vertical direction of the cell (starts from 0).

<!-- @since:5.1.0 @required -->
### cell

- Specify the location of cell in Table. This argument is only used when _row_ and _col_ are not specified.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row\_number returns row number of the cell
  - TableCellID.col\_number returns column number of the cell

<!-- @since:5.1.0 @required -->
### index

- Specify the default option to be displayed of the ComboBox.
- The starting value is 0 (first option -> index=0).

<!-- @since:5.1.0 @optional -->
### options

- Specify the options of the ComboBox.
- The default value is \[].

## Return Code

This function does not have output value.

## Sample Code

```psj {6-7}
from pyjdg import *
def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _table(name="Table2",width=260,height=160,columns=["Heading1","Heading2"],rows=5,layout="Window")
    dlg.generate _window()
    dlg.add _table _cell _option(name="Table2",cell=TableCellID(0,0),options=["0","2"],index=1)
    dlg.add _table _cell _option(name="Table2",row=0,col=1,options=["0","2"],index=1)
if __name__=='__main__':
    main()
```
