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

<!-- @since:5.0.1 @type:Integer @required -->
### `rows`

- The number of rows.

<!-- @since:5.0.1 @type:List[String] @required -->
### `columns`

- The number of columns and heading name of each column or a_[TableColumnInfoVector](../data-type/psj-gui/TableColumnInfoVector)_ object specifying the information of columns in Table.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:List[String] @optional @default:[] -->
### `menus`

- The context menu options (right mouse click):
  - "clear": clear all the existing data.
  - "cut": cut the content of the selected cell.
  - "copy": copy the content of the selected cell.
  - "paste": paste a value/values which has been copied/cut to a selected cell/select cells.
  - "insert row": insert a single row to the bottom of the selected cell.
  - "delete row": delete a selected row/selected rows.
  - "from file": load the data from csv file into the Table.
  - "to file": export the data from the Table to a specific csv file.

<!-- @since:5.0.1 @type:Integer @optional @default:260 -->
### `width`

- The width of the Table.

<!-- @since:5.0.1 @type:Integer @optional @default:260 -->
### `height`

- The height of the Table.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `show _grid _line`

- The display state of grid lines:
  - _True_: show Table grid lines.
  - _False_: hide Table grid lines.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `show _row _number`

- The state of showing/hiding row header:
  - _True_: show row header.
  - _False_: hide row header.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `show _col _header`

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
