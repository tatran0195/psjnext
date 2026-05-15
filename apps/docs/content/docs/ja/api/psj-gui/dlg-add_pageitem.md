---
title: "dlg.add _pageitem()"
description: "Add a new PageItem to the created/selected PagesCtrl"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a new PageItem to the created/selected PagesCtrl.

## Syntax

```psj
dlg.add _pageitem(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created PagesCtrl component.

<!-- @since:5.0.1 @required -->
### page\_name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### page\_header

- Specify text which will be displayed as PageItem header.

<!-- @since:5.1.0 @optional -->
### bk\_color

- Specify the background color.
- The default value is 16777215.

<!-- @since:5.1.0 @optional -->
### text\_color

- Specify the text color.
- The default value is 0.

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _pagesctrl(name="PagesCtrl4",layout="Window")
    dlg.add _pageitem(name="PagesCtrl4",page _name="PageItem5",page _header="Page header 1")
    dlg.add _node _selector()
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
