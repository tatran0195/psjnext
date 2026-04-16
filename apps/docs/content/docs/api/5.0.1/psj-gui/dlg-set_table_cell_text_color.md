---
id: dlg.set_table_cell_text_color
title: dlg.set_table_cell_text_color()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set text's color to the selected/specified cells
---

## Description

Set color to text in the selected/specified cells.

## Syntax

```psj
dlg.set_table_cell_text_color(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `cell`

- A _[TableCellID](/docs/cli/5.0.1/data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
- If not specified, all the selected cells will be used.

### `color`

- An _Integer_ specifying the color.
- If not specified, a color picker dialog is opened for user to select.

## Return Code

This function does not have output value.
