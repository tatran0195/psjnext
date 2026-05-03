---
title: "dlg.add_barpart_selector()"
description: "Add \"Bar\" to the selection list, allowing user to select bar parts and store the selected bar parts to the selection list"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add "Bar" to the selection list, allowing user to select bar parts and store the selected bar parts to the selection list.

## Syntax

```psj
dlg.add_barpart_selector(...)
```

## Inputs

### `text` @type(String) @default("Bar") @since(5.1.0)

- The title of selector.

- &#x41;_&#x53;trin&#x67;_&#x73;pecifying text which will be displayed as button label.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Mesh Count",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_barpart_selector(text="Bar 1")
    dlg.generate_window()
    
if __name__=='__main__':
    main()
```
