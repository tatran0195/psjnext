---
title: "dlg.clear _table _cell()"
description: "Clear content of a specific cell of Table"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Clear content of a specific cell of Table.

## Syntax

```psj
dlg.clear _table _cell(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of Table.

<!-- @since:5.1.0 @required -->
### row

- Specify the position in the horizontal direction of the cell (starts from 0).

<!-- @since:5.1.0 @required -->
### col

- Specify the position in the vertical direction of the cell (starts from 0).

<!-- @since:5.1.0 @optional -->
### text

- Specify the new content of the cleared cell (if needed).
- The default value is \[].

## Return Code

This function does not have output value.

## Sample Code

```psj {11-14}
from pyjdg import *

# Clear a specific cell by using right-click > Clear Cell
# The content of specific cell will be cleared
# Text Change's data will be new content of cleared cell if it is entered  
def set _table _read _from _file(dlg,name,menu):
    table _cell = dlg.get _table _sel _cell(name)
    if table _cell.size()>0:
        text _change=dlg.get _item _text(name="Textbox4")
        if menu == "Clear Cell":
            dlg.clear _table _cell(name,
                row=table _cell[0].row _number,
                col=table _cell[0].col _number,
                text=text _change)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",
        orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label3",text="Text Change",layout="Layout1")
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
    dlg.add _table _right _menu(name="Table1",
        menus=["Clear Cell"])
    dlg.generate _window()
    dlg.on _table _right _menu(name="Table1",callfunc=set _table _read _from _file)
    dlg.set _table _cell _checkbox(name="Table1",row=0,col=0,text="Checkbox",
        checked=True)
    dlg.set _cell _value(name="Table1",
        row=1,col=0,value=["Option2","Option3"])
    dlg.set _cell _value(name="Table1",row=0,col=1,value="1")
    dlg.set _cell _value(name="Table1",row=1,col=1,value=[2,3])
    dlg.set _table _cell _button(name="Table1",row=0,col=2,text="Button")
    dlg.set _cell _value(name="Table1",row=1,col=2,value=[2.5,3.5]) 

if __name__=='__main__':
    main()
```
