---
id: dlg.get_cell_value
title: dlg.get_cell_value()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get value of a specific cell of Table
---

## Description

Get value of a specific cell of Table.

## Syntax

```psj
dlg.get_cell_value(...)
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

### `option`

- An _Integer_ specifying the index number inside of combobox cell.
- The default value is -1 (get the displayed content of cell).

## Return Code

- A _String_ specifying the value of the inputted cell.
