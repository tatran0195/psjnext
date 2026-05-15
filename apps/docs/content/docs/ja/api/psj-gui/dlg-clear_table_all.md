---
title: "dlg.clear _table _all()"
description: "Clear all content of the Table"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Clear all content of the Table.

## Syntax

```psj
dlg.clear _table _all(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

## Return Code

This function does not have output value.

## Sample Code

```psj {4}
from pyjdg import *

def on _click _clear _all(dlg):
    dlg.clear _table _all(name="Table1")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _table(name="Table1",rows=14,
        columns=["Heading1","Heading2","Heading3","Heading4","Heading5"],
        layout="Window",width=560,height=260)
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
    dlg.on _command(name="Clear",callfunc=on _click _clear _all)

if __name__=='__main__':
    main()
```
