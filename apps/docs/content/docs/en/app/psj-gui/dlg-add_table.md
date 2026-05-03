---
title: "dlg.add_table()"
description: "Add a Table to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a Table to the creating dialog.

## Syntax

```psj
dlg.add_table(...)
```

## Inputs

### `rows` @type(Integer) @required

- The number of rows.

### `columns` @type(List\[String]) @required

- The number of columns and heading name of each column or &#x61;_[TableColumnInfoVector](../data-type/psj-gui/TableColumnInfoVector)_&#x6F;bject specifying the information of columns in Table.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `name` @type(String) @default("")

- The name of the created component.

### `menus` @type(List\[String]) @default(\[])

- The context menu options (right mouse click):
  - "clear": clear all the existing data.
  - "cut": cut the content of the selected cell.
  - "copy": copy the content of the selected cell.
  - "paste": paste a value/values which has been copied/cut to a selected cell/select cells.
  - "insert row": insert a single row to the bottom of the selected cell.
  - "delete row": delete a selected row/selected rows.
  - "from file": load the data from csv file into the Table.
  - "to file": export the data from the Table to a specific csv file.

### `width` @type(Integer) @default(260)

- The width of the Table.

### `height` @type(Integer) @default(260)

- The height of the Table.

### `show_grid_line` @type(Boolean) @default(True)

- The display state of grid lines:
  - _True_: show Table grid lines.
  - _False_: hide Table grid lines.

### `show_row_number` @type(Boolean) @default(True)

- The state of showing/hiding row header:
  - _True_: show row header.
  - _False_: hide row header.

### `show_col_header` @type(Boolean) @default(True)

- The state of showing/hiding column header:
  - _True_: show column header.
  - _False_: hide column header.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-11}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table2",rows=6,
        columns=["Heading1","Heading2","Heading3"],layout="Window",
        menus=["clear","cut","copy",
                "paste","insert row",
                "delete row","from file","to file"],
        width=200,height=200,
        show_grid_line=False,show_row_number=True,show_col_header=True)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
