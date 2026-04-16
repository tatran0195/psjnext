---
id: dlg.is_table_cell_combobox
title: dlg.is_table_cell_combobox()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Check the input cell is a combobox cell or not
---

## Description

Check the input cell is a combobox cell or not.

## Syntax

```psj
dlg.is_table_cell_combobox(...)
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

A _Boolean_ specifying the type of inputted cell:

- _True_: The inputted cell is a combobox cell.
- _False_: The inputted cell is not a combobox cell.
