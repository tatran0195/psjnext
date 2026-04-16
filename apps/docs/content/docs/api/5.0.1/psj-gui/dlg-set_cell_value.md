---
id: dlg.set_cell_value
title: dlg.set_cell_value()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set a value for a specific cell
---

## Description

Set a value for a specific cell.

## Syntax

```psj
dlg.set_cell_value(...)
```

## Inputs

### `name`

- A _String_ specifying the name of the Table component.
- This is a required input.

### `cell_row_id`

- An _Integer_ specifying the position in the horizontal direction of the cell (starts from 0).
- This is a required input.

### `cell_column_id`

- An _Integer_ specifying the position in the vertical direction of the cell (starts from 0).
- This is a required input.

### `value`

- A _String_ or _List of String_ or _List of Integer_ or _List of Double_ specifying the content(s) which will be displayed on the selected cell.
- This is a required input.

## Return Code

This function does not have output value.
