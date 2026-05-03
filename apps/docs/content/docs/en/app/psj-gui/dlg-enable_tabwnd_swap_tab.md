---
title: "dlg.enable_tabwnd_swap_tab()"
description: "Set to enable/disable swap the tab items in a tabwnd"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Set to enable/disable swap the tab items in a tabwnd.

## Syntax

```psj
dlg.dlg.set_item_visible(...)
```

## Inputs

### `name` @type(String) @required

- The name of the TabWnd.

### `enable` @type(Boolean) @required

- Whether to enable/disable swap the tab items:
  - _True_: Enable to swap.
  - _False_: Disable to swap.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_tabwnd(name="TabWnd10",width=200,height=200,layout="Window")
    dlg.enable_tabwnd_swap_tab(name="TabWnd10", enable=False)
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem11",page_text="TabItem1")
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem12",page_text="TabItem2")
    dlg.add_tabwnd_page(name="TabWnd10",page_name="TabItem13",page_text="TabItem3")
    dlg.generate_window()
if __name__=='__main__':
    main()
```
