---
title: "dlg.set_groupbox_collapsed()"
description: "Set the initial state of the GroupBox's collapse to show/hide GroupBox's components"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [frontmatter_conflict] description changed across versions
     context: {"values":["Set the initial state of the GroupBox's collapsible icon to show/hide","Set the initial state of the GroupBox's collapse to show/hide GroupBox's components"]}
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Set the initial state of the GroupBox's collapse feature to show/hide GroupBox's components.

## Syntax

```psj
dlg.set_groupbox_collapsed(...)
```

## Inputs

### `name` @type(String) @required

- The name of GroupBox which will be used for setting the state of its collapse feature.

### `collapsed` @type(Boolean) @required

- The state of the GroupBox's collapse feature:
  - _True_: Enable the collapse with its state is collapsed (hide all GroupBox's components).
  - _False_: Enable the collapse with its state is expanded (show all GroupBox's components).

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.set_groupbox_collapsed(name="GroupBox1",collapsed=True)
    dlg.set_groupbox_orientation(name="GroupBox1",orientation="horizontal")
    dlg.add_label(name="Label2",text="Label",layout="GroupBox1")
    dlg.add_textbox(name="TextBox3",layout="GroupBox1")
    dlg.add_label(name="Label4",text="Label",layout="GroupBox1")
    dlg.add_textbox(name="TextBox5",layout="GroupBox1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
