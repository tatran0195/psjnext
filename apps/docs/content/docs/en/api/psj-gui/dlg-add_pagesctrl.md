---
title: "dlg.add _pagesctrl()"
description: "Add a PagesCtrl (wizard type) to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a PagesCtrl (wizard type) to the creating dialog.

## Syntax

```psj
dlg.add _pagesctrl(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created layout name.
  The created layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:Boolean @optional @default:True -->
### `show _header`

- The state of the PageItem's header:
  - _True_: PageItem's header will be shown.
  - _False_: PageItem's header will be hidden.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `current _page`

- The PageItem shown by default (starts from 0).

<!-- @since:5.1.0 @type:Integer @optional @default:13158460 -->
### `sel _color`

- The highlight color when selecting a PageItem.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `show _separator`

- The stage of separator:
  - _True_: Show the separate border.
  - _False_: Do not show the separate border.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `width`

- The width of the PagesCtrl.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `height`

- The height of the PagesCtrl.

<!-- @since:5.1.0 @type:String @optional @default:"center" -->
### `text _align`

- The text alignment type (left-center-right) set for PageItem.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _pagesctrl(name="PagesCtrl4",current _page=2,width=300,height=300,text _align="right",layout="Window")
    dlg.add _pageitem(name="PagesCtrl4",page _name="PageItem5",page _header="PageItem 1")
    dlg.add _pageitem(name="PagesCtrl4",page _name="PageItem6",page _header="PageItem 2")
    dlg.add _pageitem(name="PagesCtrl4",page _name="PageItem7",page _header="PageItem 3")
    dlg.add _pageitem(name="PagesCtrl4",page _name="PageItem8",page _header="PageItem 4")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
