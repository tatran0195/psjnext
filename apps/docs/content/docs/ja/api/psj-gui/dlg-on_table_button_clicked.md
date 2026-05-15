---
title: "dlg.on _table _button _clicked()"
description: "Set event when selecting a button cell"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set event when selecting a button cell. This API will trigger event only if the selected cell is button cell while dlg.on\_table\_sel\_changed() will trigger event with all kinds of cell.

## Syntax

```psj
dlg.on _table _button _clicked(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of Table.

<!-- @since:5.0.1 @required -->
### callfunc

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {22-23}
from pyjdg import *

def on _cell _button _clicked(dlg,name,cell):
    print(name + " has button cell row = " + str(cell.row _number))
    print(name + " has button cell column = " +
        str(cell.col _number))

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
    dlg.set _table _cell _button(name="Table2",row=0,
        col=0,text="Button")
    dlg.on _table _button _clicked(name="Table2",
        callfunc=on _cell _button _clicked)

if __name__=='__main__':
    main()
```
