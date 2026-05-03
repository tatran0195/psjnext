---
title: "dlg.add_pagesctrl()"
description: "Add a PagesCtrl (wizard type) to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add a PagesCtrl (wizard type) to the creating dialog.

## Syntax

```psj
dlg.add_pagesctrl(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created layout name.
  The created layout can be a GroupBox component, Layout component, etc.

### `show_header` @type(Boolean) @default(True)

- The state of the PageItem's header:
  - _True_: PageItem's header will be shown.
  - _False_: PageItem's header will be hidden.

### `current_page` @type(Integer) @default(0)

- The PageItem shown by default (starts from 0).

### `sel_color` @type(Integer) @default(13158460) @since(5.1.0)

- The highlight color when selecting a PageItem.

### `show_separator` @type(Boolean) @default(True) @since(5.1.0)

- The stage of separator:
  - _True_: Show the separate border.
  - _False_: Do not show the separate border.

### `width` @type(Integer) @default(0)

- The width of the PagesCtrl.

### `height` @type(Integer) @default(0)

- The height of the PagesCtrl.

### `text_align` @type(String) @default("center") @since(5.1.0)

- The text alignment type (left-center-right) set for PageItem.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_pagesctrl(name="PagesCtrl4",current_page=2,width=300,height=300,text_align="right",layout="Window")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem5",page_header="PageItem 1")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem6",page_header="PageItem 2")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem7",page_header="PageItem 3")
    dlg.add_pageitem(name="PagesCtrl4",page_name="PageItem8",page_header="PageItem 4")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
