---
title: "dlg.enable_table_cell()"
description: "Set to enable/disable the cell in the table"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Set to enable/disable the cell in the table.

## Syntax

```psj
dlg.enable_table_cell(...)
```

## Inputs

### `name` @type(String) @required

- The name of the Table.

### `row` @type(Integer) @required

- The position in the horizontal direction of the cell (starts from 0).

### `col` @type(Integer) @required

- The position in the vertical direction of the cell (starts from 0).

### `cell` @type(TableCellID) @required

- Object specifying the location of cell in Table. This argument is only used whe&#x6E;_&#x72;o&#x77;_&#x61;n&#x64;_&#x63;o&#x6C;_&#x61;re not specified.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row\_number returns row number of the cell
  - TableCellID.col\_number returns column number of the cell

### `enable` @type(Boolean) @required

- Whether to enable/disable cell:
  - _True_: Enable to cell.
  - _False_: Disable to cell.

## Return Code

This function does not have output value.

## Sample Code

```psj {7,10}
from pyjdg import *

def on_menu(dlg,name,menu):
    table_cell = dlg.get_table_sel_cell(name)
    if menu == "Disable Cells":
        for cell in table_cell:
            dlg.enable_table_cell(name="Table1",cell=cell,enable=False)
    elif menu == "Enable Cells":
        for cell in table_cell:
            dlg.enable_table_cell(name="Table1",cell=cell,enable=True)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=260,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_table_right_menu(name="Table1",
        menus=["Disable Cells","Enable Cells"])
    dlg.generate_window()
    dlg.on_table_right_menu(name="Table1",callfunc=on_menu)

if __name__=='__main__':
    main()
```
