---
title: "dlg.enable_drag_table_row()"
description: "Enable to drag table rows to upward/downward"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Enable to drag table rows to upward/downward.

## Syntax

```psj
dlg.enable_drag_table_row(...)
```

## Inputs

### `name` @type(String) @required

- The name of the Table component.

### `enable` @type(Boolean) @required

- The state of dragging table row (upward/downward).
  - _True_: enable to drag the table row
  - _False_: disable to drag the table row

## Return Code

This function does not have output value.

## Sample Code

```psj {22}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=5,columns=["String","Integer","Double"],
                layout="Window",width=360,height=260)
    dlg.set_table_column_data_type(name="Table1",col=0,data_type="String")
    dlg.set_table_column_data_type(name="Table1",col=1,data_type="Integer")
    dlg.set_table_column_data_type(name="Table1",col=2,data_type="Double",precision=5)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")   
    dlg.generate_window()
    dlg.set_cell_value(name="Table1",row=0,col=0,value="Option1")
    dlg.set_cell_value(name="Table1",row=1,col=0,value=["Option2","Option3"])
    dlg.set_cell_value(name="Table1",row=0,col=1,value="1")
    dlg.set_cell_value(name="Table1",row=1,col=1,value=[2,3])
    dlg.set_cell_value(name="Table1",row=0,col=2,value="1.5")
    dlg.set_cell_value(name="Table1",row=1,col=2,value=[2.5,3.5])
    dlg.enable_drag_table_row(name="Table1",enable=True)
if __name__=='__main__':
    main()
```
