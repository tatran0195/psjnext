---
title: "dlg.add_pageitem()"
description: "Add a new PageItem to the created/selected PagesCtrl"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add a new PageItem to the created/selected PagesCtrl.

## Syntax

```psj
dlg.add_pageitem(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created PagesCtrl component.

### `page_name` @type(String) @required

- The name of the created component.

### `page_header` @type(String) @required

- Text which will be displayed as PageItem header.

### `bk_color` @type(Integer) @default(16777215) @since(5.1.0)

- The background color.

### `text_color` @type(Integer) @default(0) @since(5.1.0)

- The text color.

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_pagesctrl(name="PagesCtrl4",layout="Window")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem5",page_header="Page header 1")
    dlg.add_node_selector()
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
