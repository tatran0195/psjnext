---
title: "dlg.set_groupbox_checked()"
description: "Set the initial state of the GroupBox's checkbox to enable/disable GroupBox's components."
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Set the initial state of the GroupBox's checkbox to show/hide. In case of showing, the initial state of the checkbox is checked","Set the initial state of the GroupBox's checkbox to enable/disable GroupBox's components."]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Set the initial state of the GroupBox's checkbox to enable/disable GroupBox's components.

## Syntax

```psj
dlg.set_groupbox_checked(...)
```

## Inputs

### `name` @type(String) @required

- The name of GroupBox which will be used for setting the state of its checkbox.

### `checked` @type(Boolean) @required

- The state of the GroupBox's checkbox:
  - _True_: Enable the checkbox with its state is checked (all components inside are available to use).
  - _False_: Enable the checkbox with its state is unchecked (all components inside are unavailable to use).

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.set_groupbox_checked(name="GroupBox1",checked=True)
    dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="GroupBox1")
    dlg.add_label(name="Label3",text="Label",layout="Layout2")
    dlg.add_textbox(name="TextBox4",layout="Layout2")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
