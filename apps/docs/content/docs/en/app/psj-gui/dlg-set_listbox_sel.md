---
title: "dlg.set_listbox_sel()"
description: "Set current selection to the ListBox component"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set current selection to the ListBox component.

## Syntax

```psj
dlg.set_listbox_sel(...)
```

## Inputs

### `name` @type(String) @required

- The name of the ListBox component.

### `option` @type(Integer) @required

- O&#x72;_&#x53;trin&#x67;_&#x73;pecifying the order of the ListBox component's values or the name of selected item.

## Return Code

This function does not have output value.

## Sample Code

```psj {14}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",margin=[0,0,0,0],orientation=orientation.horizontal,layout="Window")
    dlg.add_listbox(name="ListBox2",options=["item1","item2","item3","item4","item5"],
        width=100,height=150,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_listbox_sel(name="ListBox2",option=3)

if __name__=='__main__':
    main()
```
