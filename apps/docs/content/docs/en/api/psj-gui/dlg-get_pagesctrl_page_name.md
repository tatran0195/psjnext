---
title: "dlg.get _pagesctrl _page _name()"
description: "Get name of current selected PageItem of PagesCtrl"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the name of current selected PageItem of the PagesCtrl.

## Syntax

```psj
dlg.get _pagesctrl _page _name(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of PagesCtrl.

<!-- @since:5.0.1 @type:Integer @required -->
### `page _index`

- The index order of current selected PageItem of the PagesCtrl.

## Return Code

A _String_ specifying the name of PageItem.

## Sample Code

```psj {5-6}
from pyjdg import *

def on _pageitem _changed(dlg,name,oldpage):
    current _page=dlg.get _pagesctrl _current _page(name="PagesCtrl1")
    current _page _name=dlg.get _pagesctrl _page _name(name="PagesCtrl1",
        page _index=current _page)
    print("Selected page name:"+current _page _name)

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
