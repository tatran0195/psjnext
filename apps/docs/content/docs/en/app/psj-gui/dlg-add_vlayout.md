---
title: "dlg.add_vlayout()"
description: "Add a vertical Layout to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add a vertical Layout to the creating dialog.

## Syntax

```psj
dlg.add_vlayout(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `margin` @type(List) @default(\[])

- All the value defining the positions of the creating layout.
  The list of positions is defined in the order of \[left,top,right,bottom].

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_vertex_selector()
    dlg.add_vlayout(name="footer",margin=[0,0,0,20],layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
