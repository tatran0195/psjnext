---
title: "dlg.insert _table _columns()"
description: "Insert column(s) at a specific position in the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Insert column(s) at a specific position in the Table.

## Syntax

```psj
dlg.insert _table _columns(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of Table.

<!-- @since:5.0.1 @type:TableColumnInfoVector @required -->
### `columns`

- The object or _List of [TableColumnInfo](../data-type/psj-gui/TableColumnInfo)_ specifying the methods of columns.

<!-- @since:5.0.1 @type:Integer @required -->
### `position`

- The position of row to be inserted.

## Return Code

This function does not have output value.

## Sample Code

```psj {14-15,22-23}
from pyjdg import *

def on _click _insert _col(dlg):
    num _col=int(dlg.get _item _text(name="Col"))
    col _header _name=dlg.get _item _text(name="ColHeader")
    sel _ranges=dlg.get _table _sel _range(name="Table1")
    header _vector=TableColumnInfoVector()
    for i in range(num _col):
        if sel _ranges.size()>0:
            position=sel _ranges[0].left+i
            header _vector.append(
                TableColumnInfo(name=col _header _name+"{}".format(i+1),
                type="Double",precision=2))
            dlg.insert _table _columns(name="Table1",
                columns=header _vector,position=position)
            header _vector.clear()
        else:
            position=int(dlg.get _total _column(name="Table1"))
            header _vector.append(
            TableColumnInfo(name=col _header _name+"{}".format(i+1),
                type="Double",precision=2))
            dlg.insert _table _columns(name="Table1",
                columns=header _vector,position=position)
            header _vector.clear()

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="Insert Columns",layout="Window")
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,
        layout="GroupBox1")
    dlg.add _label(name="Label1",text="Number of Col",width=120,layout="Layout1")
    dlg.add _textbox(name="Col",layout="Layout1")
    dlg.add _layout(name="Layout9",orientation=orientation.horizontal,
        layout="GroupBox1")
    dlg.add _label(name="Col _header",text="Column header name",
        width=120,layout="Layout9")
    dlg.add _textbox(name="ColHeader",layout="Layout9")
    dlg.add _button(name="InsertCol",text="Insert Column",
        width=100,height=22,layout="GroupBox1")
    dlg.add _table(name="Table1",rows=5,
        columns=["Heading1","Heading2","Heading3"],
        layout="Window",width=600,height=260)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    for i in range(5):
        for j in range(3):
            dlg.set _cell _value(name="Table1",row=i,col=j,value=str(i+j))
    dlg.on _command(name="InsertCol",callfunc=on _click _insert _col)

if __name__=='__main__':
    main()
```
