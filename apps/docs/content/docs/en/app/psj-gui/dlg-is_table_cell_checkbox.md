---
title: "dlg.is_table_cell_checkbox()"
description: "Check the input cell is a checkbox cell or not"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Check the input cell is a checkbox cell or not.

## Syntax

```psj
dlg.is_table_cell_checkbox(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `cell` @type(TableCellID) @required

- Object specifying the location of cell in Table.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row\_number returns row number of the cell
  - TableCellID.col\_number returns column number of the cell

## Return Code

A _Boolean_ specifying the type of inputted cell:

- _True_: The inputted cell is a checkbox cell.
- _False_: The inputted cell is not a checkbox cell.

## Sample Code

```psj {7-9}
from pyjdg import *

def on_cell_button_clicked(dlg,name,cell):
    JPT.ClearLog()
    cellvector=dlg.get_table_sel_cell(name="Table2")
    if cellvector.size() > 0:
       check_cell_checkbox = \
            dlg.is_table_cell_checkbox(name="Table2",
                cell=cellvector[0])
       print("Is checkbox cell: " + str(check_cell_checkbox))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table2",width=260,height=260,
        columns=["Heading1","Heading2"],
        rows=5,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",
        layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_table_cell_checkbox(name="Table2",row=0,
        col=0,text="Checkbox",checked=True)
    dlg.on_table_sel_changed(name="Table2",
        callfunc=on_cell_button_clicked)

if __name__=='__main__':
    main()
```
