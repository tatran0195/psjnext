---
id: dlg.is_table_cell_checked
title: dlg.is_table_cell_checked()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Check the state of checkbox cell
---

## Description

Check the state of checkbox cell.

## Syntax

```psj
dlg.is_table_cell_checked(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `cell`

- A _[TableCellID](/docs/cli/5.0.1/data-type/psj-gui/TableCellID)_ object specifying the location of cell in Table.
    - TableCellID(row,col) defines a cell object
    - TableCellID.row_number returns row number of the cell
    - TableCellID.col_number returns column number of the cell
- This is a required input.

## Return Code

A _Boolean_ specifying the state of checkbox cell:

- _True_: The checkbox cell is checked.
- _False_: The checkbox cell is unchecked.
