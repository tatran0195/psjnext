---
title: "dlg.clear _table _range()"
description: "Clear content of the specific range by position in the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Clear content of the specific range by position in the Table.

## Syntax

```psj
dlg.clear _table _range(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

<!-- @since:5.0.1 @required -->
### cell\_range

- Specify the information of a specific range (multi cells).

## Return Code

This function does not have output value.

## Sample Code

```psj {8-9}
from pyjdg import *

def on _click _clear(dlg):
    left=int(dlg.get _item _text(name="TextBox5"))
    top=int(dlg.get _item _text(name="TextBox7"))
    right=int(dlg.get _item _text(name="TextBox9"))
    bottom=int(dlg.get _item _text(name="TextBox11"))
    dlg.clear _table _range(name="Table1",
        cell _range=TableCellRange(left=left,top=top,right=right,bottom=bottom))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=14,
        columns=["Heading1","Heading2","Heading3","Heading4","Heading5"],
        layout="Window",width=560,height=260)
    dlg.add _groupbox(name="GroupBox2",text="Position",layout="Window")
    dlg.add _layout(name="Layout3",orientation=orientation.horizontal,
        layout="GroupBox2")
    dlg.add _label(name="Label4",text="Left",layout="Layout3")
    dlg.add _textbox(name="TextBox5",layout="Layout3")
    dlg.add _label(name="Label6",text="Top",layout="Layout3")
    dlg.add _textbox(name="TextBox7",layout="Layout3")
    dlg.add _label(name="Label8",text="Right",layout="Layout3")
    dlg.add _textbox(name="TextBox9",layout="Layout3")
    dlg.add _label(name="Label10",text="Bottom",layout="Layout3")
    dlg.add _textbox(name="TextBox11",layout="Layout3")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="Clear",text="Clear Value",
        width=80,height=30,layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    for i in range(14):
        for j in range(5):
            dlg.set _cell _value(name="Table1",row=i,col=j,value=str(i+j))
    dlg.on _command(name="Clear",callfunc=on _click _clear)

if __name__=='__main__':
    main()
```
