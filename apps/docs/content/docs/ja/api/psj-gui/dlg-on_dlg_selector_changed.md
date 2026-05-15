---
title: "dlg.on _dlg _selector _changed()"
description: "Run a created function after an item is selected"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Run a created function after an item is selected.

## Syntax

```psj
dlg.on _dlg _selector _changed(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### callfunc

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {26}
from pyjdg import *

def display _selected _entities(dlg,sel _list):
    str _node=''
    for n in sel _list:
        str _node += 'Node:' + str(n.id) + ', '
    dlg.set _item _text(name="node",text=str _node)

def main():
    dlg=JDGCreator(title="Picking Sample",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.add _label(name="infor1",text="This sample illustrates that when you pick an item,",layout="GroupBox1")
    dlg.add _label(name="infor2",text="you can receive it right after that by your own function.",layout="GroupBox1")
    dlg.add _label(name="infor3",text="The function must have 2 parameters, "\
        "one is dlg and another is a list that returned by selection; ",layout="GroupBox1")
    dlg.add _label(name="infor4",text="such as : def displaySelectedEntity(dlg,selList):",layout="GroupBox1")
    dlg.add _groupbox(name="GroupBox2",text="Selected node will be shown here",layout="Window")
    dlg.add _richeditbox(name="node",width=100,height=200,layout="GroupBox2")
    dlg.add _node _selector()
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _dlg _selector _changed(callfunc=display _selected _entities)

if __name__=='__main__':
    main()
```
