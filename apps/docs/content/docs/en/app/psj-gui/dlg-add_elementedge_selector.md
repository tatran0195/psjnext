---
title: "dlg.add_elementedge_selector()"
description: "Add \"Elem edge\" to the selection list, allowing user to select element edges and store the selected element edges to the selection list"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add "Elem edge" to the selection list, allowing user to select element edges and store the selected element edges to the selection list.

## Syntax

```psj
dlg.add_elementedge_selector(...)
```

## Inputs

### `text` @type(String) @default("Elem edge") @since(5.1.0)

- The title of selector.

## Return Code

This function does not have output value.

## Sample Code

```psj {19}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
    dlg.add_textbox(name="TextBox8",layout="Layout6")
    dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
    dlg.add_textbox(name="TextBox11",layout="Layout9")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_elementedge_selector(text = "Element edge 1")
    dlg.generate_window()
    
if __name__=='__main__':
    main()
```
