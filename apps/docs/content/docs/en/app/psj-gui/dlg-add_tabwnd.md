---
title: "dlg.add_tabwnd()"
description: "Add a TabWnd (tab window) to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a TabWnd (tab window) to the creating dialog.

## Syntax

```psj
dlg.add_tabwnd(...)
```

## Inputs

### `name` @type(String) @required

- The name of the tab window component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `width` @type(Integer) @default(60)

- The width of the tab window.

### `height` @type(Integer) @default(22)

- The height of the tab window.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_tabwnd(name="TabWnd1",width=200,height=200,layout="Window")
    dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem2",page_text="TabItem",page_orientation="horizontal")
    dlg.add_tabwnd_page(name="TabWnd1",page_name="TabItem3",page_text="TabItem")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
