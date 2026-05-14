---
title: "dlg.get _dlg _selector _selected _entities()"
description: "Get selected DItem in current Selection List"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get selected _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ in current Selection List.

## Syntax

```psj
dlg.get _dlg _selector _selected _entities(...)
```

## Inputs

<!-- @since:5.0.1 @type:Integer @required -->
### `selid`

- The index of the selector.

## Return Code

A _[DItemVector](../data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object specifying the list of picked items.

## Sample Code

```psj {5}
from pyjdg import *

def display _selected _entities(dlg):
    str _nodes = ""
    for n in dlg.get _dlg _selector _selected _entities(selid=0):
        str _nodes += 'Selected Node ID: ' + (str(n.id)) + ',\n'
        dlg.set _item _text(name="selected _nodes",text=str _nodes)

def main():
    dlg=JDGCreator(title="Picking Sample",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="Display all selected nodes",layout="Window")
    dlg.add _label(name="Label2",text="Please select nodes and click Display Nodes button",layout="GroupBox1")
    dlg.add _button(name="display _nodes",text="Display Nodes",layout="GroupBox1")
    dlg.add _richeditbox(name="selected _nodes",text="",width=200,height=200,layout="GroupBox1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _node _selector()
    dlg.add _node _selector()
    dlg.generate _window()
    dlg.on _command(name="display _nodes",callfunc=display _selected _entities)

if __name__=='__main__':
    main()
```
