---
title: "dlg.set_table_cell_fill_color()"
description: "Set color to the selected/specified cells"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set fill color to the selected/specified cells.

## Syntax

```psj
dlg.set_table_cell_fill_color(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `cell` @type(TableCellID)

- Object specifying the location of cell in Table.
- If not specified, all the selected cells will be used.

### `color` @type(Integer)

- The color.
- If not specified, a color picker dialog is opened for user to select.

## Return Code

This function does not have output value.

## Sample Code

```psj {6,8-9,11-12,14-15,17-19}
from pyjdg import *

def on_menu(dlg,name,menu):
    cellvector=dlg.get_table_sel_cell(name="Table1")
    if menu=="Set Fill Color for all selected cells using color picker":
        dlg.set_table_cell_fill_color(name="Table1")
    elif menu=="Set Fill Color only for a selected cell using color picker":
         dlg.set_table_cell_fill_color(name="Table1",
            cell=cellvector[0])
    elif menu=="Set Fill Color only for a selected cell with red color":
        dlg.set_table_cell_fill_color(name="Table1",
            cell=cellvector[0],color=7105764)
    elif menu=="Set Fill Color only for the first cell with red color":
        dlg.set_table_cell_fill_color(name="Table1",
            cell=TableCellID(row=0,col=0),color=7105764)
    elif menu=="Set Fill Color only for the first 2x2 cells with red color":
        [[dlg.set_table_cell_fill_color(name="Table1",
            cell=TableCellID(row=i,col=j),color=7105764)
            for i in (0,1)] for j in (0,1)]

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
        menus=["Set Fill Color for all selected cells using color picker",
        "Set Fill Color only for a selected cell using color picker",
        "Set Fill Color only for a selected cell with red color",
        "Set Fill Color only for the first cell with red color",
        "Set Fill Color only for the first 2x2 cells with red color"])
    dlg.generate_window()
    dlg.on_table_right_menu(name="Table1",callfunc=on_menu)

if __name__=='__main__':
    main()
```
