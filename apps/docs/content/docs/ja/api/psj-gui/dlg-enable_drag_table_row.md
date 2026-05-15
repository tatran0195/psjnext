---
title: "dlg.enable _drag _table _row()"
description: "Enable to drag table rows to upward/downward"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Enable to drag table rows to upward/downward.

## Syntax

```psj
dlg.enable _drag _table _row(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of the Table component.

<!-- @since:5.1.0 @required -->
### enable

- Specify the state of dragging table row (upward/downward).
  - _True_: enable to drag the table row
  - _False_: disable to drag the table row

## Return Code

This function does not have output value.

## Sample Code

```psj {22}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=5,columns=["String","Integer","Double"],
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
    dlg.set _cell _value(name="Table1",row=0,col=0,value="Option1")
    dlg.set _cell _value(name="Table1",row=1,col=0,value=["Option2","Option3"])
    dlg.set _cell _value(name="Table1",row=0,col=1,value="1")
    dlg.set _cell _value(name="Table1",row=1,col=1,value=[2,3])
    dlg.set _cell _value(name="Table1",row=0,col=2,value="1.5")
    dlg.set _cell _value(name="Table1",row=1,col=2,value=[2.5,3.5])
    dlg.enable _drag _table _row(name="Table1",enable=True)
if __name__=='__main__':
    main()
```
