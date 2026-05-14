---
title: "dlg.enable _tabwnd _swap _tab()"
description: "Set to enable/disable swap the tab items in a tabwnd"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set to enable/disable swap the tab items in a tabwnd.

## Syntax

```psj
dlg.dlg.set _item _visible(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the TabWnd.

<!-- @since:5.1.0 @type:Boolean @required -->
### `enable`

- Whether to enable/disable swap the tab items:
  - _True_: Enable to swap.
  - _False_: Disable to swap.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *
def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _tabwnd(name="TabWnd10",width=200,height=200,layout="Window")
    dlg.enable _tabwnd _swap _tab(name="TabWnd10", enable=False)
    dlg.add _tabwnd _page(name="TabWnd10",page _name="TabItem11",page _text="TabItem1")
    dlg.add _tabwnd _page(name="TabWnd10",page _name="TabItem12",page _text="TabItem2")
    dlg.add _tabwnd _page(name="TabWnd10",page _name="TabItem13",page _text="TabItem3")
    dlg.generate _window()
if __name__=='__main__':
    main()
```
