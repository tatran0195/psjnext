---
id: dlg.set_table_cell_alignment
title: dlg.set_table_cell_alignment()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set text alignment of cell
---

## Description

Set text alignment of cell.

## Syntax

```psj
dlg.set_table_cell_alignment(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `row`

- An _Integer_ specifying the order of row (starts from 0).
- This is a required input.

### `col`

- An _Integer_ specifying the order of column (starts from 0).
- This is a required input.

### `alignment`

- A _String_ specifying alignment position of content inside a cell.
    - "Left": Align content to the left
    - "Center": Center the content
    - "Right": Align content to the right
- This is a required input.

## Return Code

This function does not have output value.
