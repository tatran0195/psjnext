---
title: "dlg.set _pagesctrl _current _page()"
description: "Set current displayed PageItem in PagesCtrl"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set current displayed PageItem in PagesCtrl.

## Syntax

```psj
dlg.set _pagesctrl _current _page(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name the PagesCtrl.

<!-- @since:5.0.1 @type:Integer @required -->
### `page _index`

- The index position of the PageItem (starts from 0).

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def switch _page(dlg):
    page = dlg.get _combobox _sel(name="switcher")
    dlg.set _pagesctrl _current _page(name='PagesCtrl2',page _index=page)

def main():

    dlg=JDGCreator(title="Switch page sample",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="Set current page from combobox",layout="Window")
    dlg.set _groupbox _orientation("GroupBox1","horizontal")
    dlg.add _label(name="Label2",text="Select current page",layout="GroupBox1")
    dlg.add _combobox(name="switcher",options=["First page","Second page","Third page"],layout="GroupBox1")
    dlg.add _groupbox(name="GroupBox2",text="Current page display",layout="Window")
    dlg.set _groupbox _orientation("GroupBox2","horizontal")
    dlg.add _pagesctrl(name="PagesCtrl2",width=260,height=160,layout="GroupBox2")
    dlg.add _pageitem(name="PagesCtrl2",page _name="PageItem3",page _header="First page")
    dlg.add _pageitem(name="PagesCtrl2",page _name="PageItem4",page _header="Second page")
    dlg.add _pageitem(name="PagesCtrl2",page _name="PageItem5",page _header="Third page")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _combobox _sel(name="switcher",callfunc=switch _page)

if __name__=='__main__':
    main()
```
