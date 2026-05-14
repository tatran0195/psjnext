---
title: "dlg.set _cell _value()"
description: "Set a value for a specific cell"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set value for a specific cell of Table.

## Syntax

```psj
dlg.set _cell _value(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the Table component.

<!-- @since:5.1.0 @type:Integer @required -->
### `row`

- The position in the horizontal direction of the cell (starts from 0).

<!-- @since:5.1.0 @type:Integer @required -->
### `col`

- The position in the vertical direction of the cell (starts from 0).

<!-- @since:5.1.0 @type:TableCellID @required -->
### `cell`

- The object specifying the location of cell in Table. This argument is only used when _row_ and _col_ are not specified.
  - TableCellID(row,col) defines a cell object
  - TableCellID.row\_number returns row number of the cell
  - TableCellID.col\_number returns column number of the cell

<!-- @since:5.1.0 @type:Integer @required -->
### `index`

- The default option to be displayed of the Combobox. The starting value is 0 (fist option > index = 0)

<!-- @since:5.0.1 @type:String @required -->
### `value`

- The or _List of String_ or _List of Integer_ or _List of Double_ specifying the content(s) which will be displayed on the selected cell.

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @required @deprecated -->
### `cell _row _id`

- The position in the horizontal direction of the cell (starts from 0).

<!-- @since:5.0.1 @type:Integer @removed:5.1.0 @required @deprecated -->
### `cell _column _id`

- The position in the vertical direction of the cell (starts from 0).

## Return Code

This function does not have output value.

## Sample Code

```psj {33-39}
from pyjdg import *

def get _table _cell _value(dlg,name,cell):
    cellvector=dlg.get _table _sel _cell(name="Table1")
    if cellvector.size()>0:
        value _cell=dlg.get _cell _value(name="Table1",
            row=cellvector[0].row _number,
            col=cellvector[0].col _number)
        dlg.set _item _text(name="Textbox4",text=value _cell)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",
        orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label3",text="Get Value",layout="Layout1")
    dlg.add _textbox(name="Textbox4",layout="Layout1")
    dlg.add _table(name="Table1",rows=5,
        columns=["String","Integer","Double"],
        layout="Window",width=360,height=260)
    dlg.set _table _column _data _type(name="Table1",
        col=0,data _type="String")
    dlg.set _table _column _data _type(name="Table1",
        col=1,data _type="Integer")
    dlg.set _table _column _data _type(name="Table1",
        col=2,data _type="Double",precision=5)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")   
    dlg.generate _window()
    dlg.on _table _sel _changed(name="Table1",callfunc=get _table _cell _value)
    dlg.set _cell _value(name="Table1",row=0,col=0,value="Option1")
    dlg.set _cell _value(name="Table1",
        row=1,col=0,value=["Option2","Option3"])
    dlg.set _cell _value(name="Table1",row=0,col=1,value="1")
    dlg.set _cell _value(name="Table1",row=1,col=1,value=[2,3])
    dlg.set _cell _value(name="Table1",row=0,col=2,value="1.5")
    dlg.set _cell _value(name="Table1",cell=TableCellID(1,2),value=[2.5,3.5,4.5], index=1) 

if __name__=='__main__':
    main()
```
