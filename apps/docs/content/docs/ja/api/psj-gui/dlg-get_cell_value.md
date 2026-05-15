---
title: "dlg.get _cell _value()"
description: "Get value of a specific cell of Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get value of a specific cell of Table.

## Syntax

```psj
dlg.get _cell _value(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the Table component.

<!-- @since:5.1.0 @required -->
### row

- Specify the position in the horizontal direction of the cell (starts from 0).

<!-- @since:5.1.0 @required -->
### col

- Specify the position in the vertical direction of the cell (starts from 0).

<!-- @since:5.0.1 @optional -->
### option

- Specify the index number inside of combobox cell.
- The default value is -1 (get the displayed content of cell).

<!-- @since:5.0.1 @removed:5.1.0 @required @deprecated -->
### cell\_row\_id

- Specify the position in the horizontal direction of the cell (starts from 0).

<!-- @since:5.0.1 @removed:5.1.0 @required @deprecated -->
### cell\_column\_id

- Specify the position in the vertical direction of the cell (starts from 0).

## Return Code

- A _String_ specifying the value of the inputted cell.

## Sample Code

```psj {6-8,10-12,14-16}
from pyjdg import *

def get _table _cell _value(dlg,name,cell):
    cellvector=dlg.get _table _sel _cell(name="Table1")
    if cellvector.size()>0:
        value _cell=dlg.get _cell _value(name="Table1",
            row=cellvector[0].row _number,
            col=cellvector[0].col _number)
        dlg.set _item _text(name="Textbox4",text=value _cell)
        value _cell=dlg.get _cell _value(name="Table1",
            row=cellvector[0].row _number,
            col=cellvector[0].col _number,option=1)
        dlg.set _item _text(name="Textbox5",text=value _cell)
        value _cell=dlg.get _cell _value(name="Table1",
            row=cellvector[0].row _number,
            col=cellvector[0].col _number,option=2)
        dlg.set _item _text(name="Textbox6",text=value _cell)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",margin=[0,0,200,0],
        orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label3",text="Get Displayed Value",width=100,layout="Layout1")
    dlg.add _textbox(name="Textbox4",layout="Layout1")
    dlg.add _layout(name="Layout2",margin=[0,0,200,0],
        orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label4",text="Get Value option=1",width=100,layout="Layout2")
    dlg.add _textbox(name="Textbox5",layout="Layout2")
    dlg.add _layout(name="Layout3",margin=[0,0,200,0],
        orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label5",text="Get Value option=2",width=100,layout="Layout3")
    dlg.add _textbox(name="Textbox6",layout="Layout3")
    dlg.add _table(name="Table1",rows=5,
        columns=["String","Integer","Double"],
        layout="Window",width=360,height=260)
    dlg.set _table _column _data _type(name="Table1",col=0,data _type="String")
    dlg.set _table _column _data _type(name="Table1",col=1,data _type="Integer")
    dlg.set _table _column _data _type(name="Table1",col=2,data _type="Double",precision=5)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _table _sel _changed(name="Table1",callfunc=get _table _cell _value)
    dlg.set _cell _value(name="Table1",row=0,col=0,
        value=["Option1","Option2","Option3"])

if __name__=='__main__':
    main()
```
