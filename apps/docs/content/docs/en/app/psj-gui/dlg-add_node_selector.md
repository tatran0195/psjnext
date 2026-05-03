---
title: "dlg.add_node_selector()"
description: "Add \"Node\" to the selection list, allowing user to select nodes and store the selected nodes to the selection list"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add "Node" to the selection list, allowing user to select nodes and store the selected nodes to the selection list.

## Syntax

```psj
dlg.add_node_selector(...)
```

## Inputs

### `text` @type(String) @default("") @since(5.1.0)

- The title of selector.

## Return Code

This function does not have output value.

## Sample Code

```psj {11}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_listbox(name="ListBox3",multisel=True,options=["item1","item2","item3"],width=100,height=100,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_node_selector()
    dlg.generate_window()
    
if __name__=='__main__':
    main()
```
