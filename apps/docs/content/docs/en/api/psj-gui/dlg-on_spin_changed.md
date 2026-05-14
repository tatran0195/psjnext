---
title: "dlg.on _spin _changed()"
description: "Run a created function after a spin value is changed"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Run a created function after a spin value is changed.

## Syntax

```psj
dlg.on _spin _changed(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the Spin component using for binding a created def function.

<!-- @since:5.1.0 @type:PSJCallable @required -->
### `callfunc`

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {3}
from pyjdg import *

def on _spin _changed(dlg,old _value,new _value):
    total _rows=dlg.get _total _row(name="Table6")
    if new _value is None:
        new _rows=int(dlg.get _item _text(name="Spin4"))
    elif new _value >= 0:
        new _rows=new _value
    if new _rows >= total _rows:
        dlg.insert _table _rows(name="Table6",row _num=int(new _rows-total _rows))
    else:
        if new _rows >= 1:
            for idx in range (new _rows, total _rows):
                dlg.delete _table _row(name="Table6",position=new _rows)
    if new _value >= 1:
        print("Current number of rows is: "+ str(new _value))
    else:
        print("Current number of rows is: "+ str(new _value+1))

def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label3",text="Number of Rows",width=80,
        text _halign="left",text _valign="top",layout="Layout2")
    dlg.add _spin(name="Spin4",min=1,max=10,pos=5,increment=1,layout="Layout2")
    dlg.add _layout(name="Layout5",orientation=orientation.vertical,layout="Window")
    dlg.add _table(name="Table6",width=350,height=300,columns=["Heading1","Heading2","Heading3"],
        rows=5,layout="Layout5")
    dlg.generate _window()
    dlg.on _spin _changed(name="Spin4",callfunc=on _spin _changed)

if __name__=='__main__':
    main()
```
