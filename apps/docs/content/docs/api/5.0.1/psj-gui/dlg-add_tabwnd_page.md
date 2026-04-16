---
id: dlg.add_tabwnd_page
title: dlg.add_tabwnd_page()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Add a TabItem (page) to the TabWnd component
---

## Description

Add a TabItem (page) to the TabWnd component.

## Syntax

```psj
dlg.add_tabwnd_page(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the TabWnd component in which the creating TabItem will be put added to.
- This is a required input.

### `page_name`

- A _String_ specifying the name of the created component.
- This is a required input.

### `page_text`

- A _String_ specifying text which will be displayed as a title.
- The default value is "".

### `page_orientation`

- A _String_ specifying the orientation of the creating tab page. It has 2 options:
    - "vertical": aligning all the inside components in the vertical direction.
    - "horizontal": aligning all the inside components in the horizontal direction.
- The default value is "vertical".

## Return Code

This function does not have output value.
