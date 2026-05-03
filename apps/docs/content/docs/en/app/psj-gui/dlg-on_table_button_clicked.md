---
title: "dlg.on_table_button_clicked()"
description: "Set event when selecting a button cell"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set event when selecting a button cell. This API will trigger event only if the selected cell is button cell while dlg.on\_table\_sel\_changed() will trigger event with all kinds of cell.

## Syntax

```psj
dlg.on_table_button_clicked(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `callfunc` @type(PSJCallable) @required

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {22-23}
from pyjdg import *

def on_cell_button_clicked(dlg,name,cell):
    print(name + " has button cell row = " + str(cell.row_number))
    print(name + " has button cell column = " +
        str(cell.col_number))

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
    dlg.set_table_cell_button(name="Table2",row=0,
        col=0,text="Button")
    dlg.on_table_button_clicked(name="Table2",
        callfunc=on_cell_button_clicked)

if __name__=='__main__':
    main()
```
