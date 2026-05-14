---
title: "dlg.get _len _listbox()"
description: "Get the size (number of items) of the ListBox"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the size (number of items) of the ListBox.

## Syntax

```psj
dlg.get _len _listbox(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ListBox component.

## Return Code

An _Integer_ specifying the size of the ListBox component.

## Sample Code

```psj {14}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
    dlg.add _listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
        width=100,height=150,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    listBoxLen=dlg.get _len _listbox(name="ListBox2")
    print(listBoxLen)

if __name__=='__main__':
    main()
```
