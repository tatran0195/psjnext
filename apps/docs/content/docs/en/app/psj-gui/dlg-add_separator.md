---
title: "dlg.add_separator()"
description: "Add a Separator to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add a Separator to the creating dialog.

## Syntax

```psj
dlg.add_separator(...)
```

## Inputs

### `name` @type(String) @required @since(5.1.0)

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout18",orientation=orientation.vertical,layout="Window")
    dlg.add_label(name="Label19",text="Label",text_valign="top",layout="Layout18")
    dlg.add_separator(name="Separator20",layout="Layout18")
    dlg.add_textbox(name="TextBox21",layout="Layout18")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
