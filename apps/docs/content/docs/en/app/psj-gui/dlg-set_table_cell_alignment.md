---
title: "dlg.set_table_cell_alignment()"
description: "Set text alignment of cell"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Set text alignment of cell.

## Syntax

```psj
dlg.set_table_cell_alignment(...)
```

## Inputs

### `name` @type(String) @required

- The name of Table.

### `row` @type(Integer) @required

- The order of row (starts from 0).

### `col` @type(Integer) @required

- The order of column (starts from 0).

### `alignment` @type(String) @required

- Alignment position of content inside a cell.
  - "Left": Align content to the left
  - "Center": Center the content
  - "Right": Align content to the right

## Return Code

This function does not have output value.

## Sample Code

```psj {4-9}
from pyjdg import *

def on_click_set_alignment(dlg):
    dlg.set_table_cell_alignment(name="Table1",row=0,col=0,
        alignment="Left")
    dlg.set_table_cell_alignment(name="Table1",row=1,col=0,
        alignment="Center")
    dlg.set_table_cell_alignment(name="Table1",row=2,col=0,
        alignment="Right")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=5,
        columns=["Heading1","Heading2"],
        layout="Window",width=360,height=260)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonSetAlignment",width=70,height=30,
        text="Set Alignment",layout="footer")
    dlg.add_button(name="Ok",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_table_column_width(name="Table1",col=0,width=200)
    dlg.set_cell_value(name="Table1",row=0,col=0,
        value="Left Alignment")
    dlg.set_cell_value(name="Table1",row=1,col=0,
        value="Center Alignment")
    dlg.set_cell_value(name="Table1",row=2,col=0,
        value="Right Alignment")
    dlg.on_command(name="ButtonSetAlignment",callfunc=on_click_set_alignment)

if __name__=='__main__':
    main()
```
