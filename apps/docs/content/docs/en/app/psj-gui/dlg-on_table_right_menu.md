---
title: "dlg.on_table_right_menu()"
description: "Set event when opening/executing context menu"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set event when opening/executing context menu.

## Syntax

```psj
dlg.on_table_right_menu(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `callfunc` @type(PSJCallable) @required

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {30}
from pyjdg import *

def on_menu(dlg,name,menu):
    print("Table name: "+ name)
    print("Clicked menu: "+ menu)
    table_cell = dlg.get_table_sel_cell(name)
    if menu == "Set Column Width":
        dlg.set_table_column_width(name,table_cell[0].col_number)
    elif menu == "Set Text Color":
        dlg.set_table_cell_text_color(name,table_cell[0])
    elif menu == "Set Cell Color":
        dlg.set_table_cell_fill_color(name)
    elif menu == "Custom Menu":
        print("You can put your function here")

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
        menus=["Set Cell Color","Set Text Color",
        "Set Column Width","Custom Menu"])
    dlg.generate_window()
    dlg.on_table_right_menu(name="Table1",callfunc=on_menu)

if __name__=='__main__':
    main()
```
