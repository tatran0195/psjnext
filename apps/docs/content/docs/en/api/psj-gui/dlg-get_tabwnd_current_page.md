---
title: "dlg.get _tabwnd _current _page()"
description: "Get the selecting page of the inputted TabWnd"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the selecting page of the inputted TabWnd.

## Syntax

```psj
dlg.get _tabwnd _current _page(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the TabWnd component using for getting selected page order.

## Return Code

An _Integer_ specifying the order of the selected page of the inputted TabWnd.

## Sample Code

```psj {4}
from pyjdg import *

def get _current _tab(dlg):
    selected _page = dlg.get _tabwnd _current _page(name="TabWnd1")
    JPT.Debugger(selected _page)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _tabwnd(name="TabWnd1",width=400,height=200,layout="Window")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem2",page _text="TabItem")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem3",page _text="TabItem")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem4",page _text="TabItem")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem5",page _text="TabItem")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem6",page _text="TabItem")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _command(name="ButtonApply",callfunc=get _current _tab)

if __name__=='__main__':
    main()
```
