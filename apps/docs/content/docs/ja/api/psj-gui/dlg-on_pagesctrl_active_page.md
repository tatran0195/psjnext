---
title: "dlg.on _pagesctrl _active _page()"
description: "Set event when selecting a PageItem"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set event when selecting a PageItem.

## Syntax

```psj
dlg.on _pagesctrl _active _page(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of PagesCtrl.

<!-- @since:5.0.1 @required -->
### callfunc

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {27}
from pyjdg import *

def on _pageitem _changed(dlg,name,old _page):
    current _page=dlg.get _pagesctrl _current _page(name="PagesCtrl1")
    current _page _name=dlg.get _pagesctrl _page _name(name="PagesCtrl1",
        page _index=current _page)
    old _page _name=dlg.get _pagesctrl _page _name(name="PagesCtrl1",
        page _index=old _page)
    print("Selected page name : "+current _page _name)
    print("Previous selected page : "+old _page _name)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _pagesctrl(name="PagesCtrl1",layout="Window")
    dlg.add _pageitem(name="PagesCtrl1",page _name="PageItem2",
        page _header="PageItem1")
    dlg.add _pageitem(name="PagesCtrl1",page _name="PageItem3",
        page _header="PageItem2")
    dlg.add _pageitem(name="PagesCtrl1",page _name="PageItem4",
        page _header="PageItem3")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="Ok",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _pagesctrl _active _page(name="PagesCtrl1",callfunc=on _pageitem _changed)

if __name__=='__main__':
    main()
```
