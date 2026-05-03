---
title: "dlg.add_table_sel_option()"
description: "Set combobox cell in the Table"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Set combobox cell in the Table.

## Syntax

```psj
dlg.add_table_sel_option(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `row` @type(Integer) @required

- The position in the horizontal direction of the cell (starts from 0).

### `col` @type(Integer) @required

- The position in the vertical direction of the cell (starts from 0).

### `cell` @type(TableCellID) @required

- Object specifying the location of cell in Table. This argument is only used whe&#x6E;_&#x72;o&#x77;_&#x61;n&#x64;_&#x63;o&#x6C;_&#x61;re not specified.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row\_number returns row number of the cell
  - TableCellID.col\_number returns column number of the cell

### `index` @type(Integer) @required

- The default option to be displayed of the ComboBox.
- The starting value is 0 (first option -> index=0).

### `options` @type(List\[String]) @default(\[])

- The options of the ComboBox.

## Return Code

This function does not have output value.

## Sample Code

```psj {6-7}
from pyjdg import *
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_table(name="Table2",width=260,height=160,columns=["Heading1","Heading2"],rows=5,layout="Window")
    dlg.generate_window()
    dlg.add_table_cell_option(name="Table2",cell=TableCellID(0,0),options=["0","2"],index=1)
    dlg.add_table_cell_option(name="Table2",row=0,col=1,options=["0","2"],index=1)
if __name__=='__main__':
    main()
```
