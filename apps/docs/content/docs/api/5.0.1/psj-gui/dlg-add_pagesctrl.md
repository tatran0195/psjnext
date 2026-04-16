---
id: dlg.add_pagesctrl
title: dlg.add_pagesctrl()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a PagesCtrl (wizard type) to the creating dialog
---

## Description

Add a PagesCtrl (wizard type) to the creating dialog.

## Syntax

```psj
dlg.add_pagesctrl(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created layout name.
  The created layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `show_header`

- A _Boolean_ specifying the state of the PageItem's header:
    - _True_: PageItem's header will be shown.
    - _False_: PageItem's header will be hidden.
- The default value is _True_.

### `current_page`

- An _Integer_ specifying the PageItem shown by default (starts from 0).
- The default value is 0.

### `width`

- An _Integer_ specifying the width of the PagesCtrl.
- The default value is 0.

### `height`

- An _Integer_ specifying the height of the PagesCtrl.
- The default value is 0.

## Return Code

This function does not have output value.
