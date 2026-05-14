---
title: "dlg.get _cell _label()"
description: "Get label of a button cell, checkbox cell or combobox cell in the Table"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get label of a button cell, checkbox cell or combobox cell in the Table.

## Syntax

```psj
dlg.get _cell _label(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the Table component.

<!-- @since:5.1.0 @type:Integer @required -->
### `row`

- The position in the horizontal direction of the cell (starts from 0).

<!-- @since:5.1.0 @type:Integer @required -->
### `column`

- The position in the vertical direction of the cell (starts from 0).

## Return Code

- A _String_ specifying the label of the inputted cell.

## Sample Code

```psj {8-9,12-13,16-17}
from pyjdg import *

def on _cell _button _clicked(dlg,name,cell):
    JPT.ClearLog()
    cellvector=dlg.get _table _sel _cell(name="Table2")
    if cellvector.size() > 0:
        if dlg.is _table _cell _combobox(name="Table2",cell=cellvector[0]):
            combobox _label= dlg.get _cell _label(name="Table2",
                row=cellvector[0].row _number,col=cellvector[0].col _number)
            print("The label of the selected combobox is: " + combobox _label)
        elif dlg.is _table _cell _button(name="Table2",cell=cellvector[0]):
            button _label= dlg.get _cell _label(name="Table2",
                row=cellvector[0].row _number,col=cellvector[0].col _number)
            print("The label of the selected button is: " + button _label)
        elif dlg.is _table _cell _checkbox(name="Table2",cell=cellvector[0]):
            checkbox _label= dlg.get _cell _label(name="Table2",
                row=cellvector[0].row _number,col=cellvector[0].col _number)
            print("The label of the selected checkbox is: " + checkbox _label)
        else:
            print("Selected cell do not have label")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table2",width=260,height=260,
        columns=["Heading1","Heading2"],
        rows=5,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",
        layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _cell _value(name="Table2",
        row=0,col=0,
        value=["Option1","Option2","Option3"])
    dlg.set _table _cell _button(name="Table2",
        row=0,col=1,text="Button")
    dlg.set _table _cell _checkbox(name="Table2",row=1,
        col=0,text="Checkbox",checked=True)
    dlg.on _table _sel _changed(name="Table2",
        callfunc=on _cell _button _clicked)

if __name__=='__main__':
    main()
```
