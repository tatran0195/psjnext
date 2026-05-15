---
title: "dlg.add _table()"
description: "Add a Table to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a Table to the creating dialog.

## Syntax

```psj
dlg.add _table(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### rows

- Specify the number of rows.

<!-- @since:5.0.1 @required -->
### columns

- Specify the number of columns and heading name of each column or a_[TableColumnInfoVector](../data-type/psj-gui/TableColumnInfoVector)_ object specifying the information of columns in Table.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### name

- Specify the name of the created component.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### menus

- Specify the context menu options (right mouse click):
  - "clear": clear all the existing data.
  - "cut": cut the content of the selected cell.
  - "copy": copy the content of the selected cell.
  - "paste": paste a value/values which has been copied/cut to a selected cell/select cells.
  - "insert row": insert a single row to the bottom of the selected cell.
  - "delete row": delete a selected row/selected rows.
  - "from file": load the data from csv file into the Table.
  - "to file": export the data from the Table to a specific csv file.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the Table.
- The default value is 260.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the Table.
- The default value is 260.

<!-- @since:5.0.1 @optional -->
### show\_grid\_line

- Specify the display state of grid lines:
  - _True_: show Table grid lines.
  - _False_: hide Table grid lines.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### show\_row\_number

- Specify the state of showing/hiding row header:
  - _True_: show row header.
  - _False_: hide row header.
- The default value is _True_.

<!-- @since:5.0.1 @optional -->
### show\_col\_header

- Specify the state of showing/hiding column header:
  - _True_: show column header.
  - _False_: hide column header.
- The default value is _True_.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-11}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table2",rows=6,
        columns=["Heading1","Heading2","Heading3"],layout="Window",
        menus=["clear","cut","copy",
                "paste","insert row",
                "delete row","from file","to file"],
        width=200,height=200,
        show _grid _line=False,show _row _number=True,show _col _header=True)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
