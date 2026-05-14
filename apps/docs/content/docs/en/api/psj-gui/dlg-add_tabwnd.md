---
title: "dlg.add _tabwnd()"
description: "Add a TabWnd (tab window) to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a TabWnd (tab window) to the creating dialog.

## Syntax

```psj
dlg.add _tabwnd(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the tab window component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:Integer @optional @default:60 -->
### `width`

- The width of the tab window.

<!-- @since:5.0.1 @type:Integer @optional @default:22 -->
### `height`

- The height of the tab window.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _tabwnd(name="TabWnd1",width=200,height=200,layout="Window")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem2",page _text="TabItem",page _orientation="horizontal")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem3",page _text="TabItem")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
