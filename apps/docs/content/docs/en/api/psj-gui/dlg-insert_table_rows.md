---
title: "dlg.insert _table _rows()"
description: "Insert row(s) at a specific position in the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Insert row(s) at a specific position in the Table.

## Syntax

```psj
dlg.insert _table _rows(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of Table.

<!-- @since:5.0.1 @type:Integer @required -->
### `row _num`

- The number of rows to be inserted.

<!-- @since:5.0.1 @type:Integer @required -->
<!-- @since:5.1.0 @optional -->
### `position`

- The position of row to be inserted.
  - If specified, the row will be inserted in front of the inputted position (position-1).
  - If not specified,the row will be inserted at the end of the table.
- This is a default input.

## Return Code

This function does not have output value.

## Sample Code

```psj {10-11,14-15,17}
from pyjdg import *

def on _click _insert _row(dlg):
    num _row=int(dlg.get _item _text(name="Row"))
    sel _ranges=dlg.get _table _sel _range(name="Table1")
    position=int(dlg.get _total _row(name="Table1"))
    if sel _ranges.size()>0:
        if sel _ranges[0].top == 0:
            position=sel _ranges[0].top
            dlg.insert _table _rows(name="Table1",
                row _num=num _row,position=position)
        elif sel _ranges[0].top > 0:
            position=sel _ranges[0].top
            dlg.insert _table _rows(name="Table1",
                row _num=num _row,position=position)
    else:
        dlg.insert _table _rows(name="Table1",row _num=num _row)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="Insert Rows",layout="Window")
    dlg.add _layout(name="Layout2",orientation=orientation.horizontal,
        layout="GroupBox1")
    dlg.add _label(name="Label1",text="Number of Rows",layout="Layout2")
    dlg.add _textbox(name="Row",layout="Layout2")
    dlg.add _button(name="InsertRow",text="Insert Row",
        width=100,height=22,layout="GroupBox1")
    dlg.add _table(name="Table1",rows=5,
        columns=["Heading1","Heading2","Heading3"],
        layout="Window",width=260,height=260)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    for i in range(5):
        for j in range(3):
            dlg.set _cell _value(name="Table1",row=i,col=j,value=str(i+j))
    dlg.on _command(name="InsertRow",callfunc=on _click _insert _row)
if __name__=='__main__':
    main()
```
