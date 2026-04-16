---
id: dlg.add_listbox
title: dlg.add_listbox()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a ListBox to the creating dialog
---

## Description

Add a ListBox to the creating dialog.

## Syntax

```psj
dlg.add_listbox(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `layout`

- A _String_ specifying the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.
- This is a required input.

### `multisel`

- A _Boolean_ specifying the permission that allow user to select multiple values at the same time:
    - _True_: user can select multiple values.
    - _False_: user can select only one value per time.
- The default value is False.

### `options`

- A _List of String_ specifying all the options of the ListBox component.
- The default value is [].

### `width`

- An _Integer_ specifying the width of the ListBox.
- The default value is 0.

### `height`

- An _Integer_ specifying the height of the ListBox.
- The default value is 0.

## Return Code

This function does not have output value.
