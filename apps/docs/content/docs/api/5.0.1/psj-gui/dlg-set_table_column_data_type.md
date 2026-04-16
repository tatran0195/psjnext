---
id: dlg.set_table_column_data_type
title: dlg.set_table_column_data_type()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set data type validation of cell of Table
---

## Description

Set data type validation of cell of Table.

## Syntax

```psj
dlg.set_table_column_data_type(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `col`

- An _Integer_ specifying the order of column (starts from 0).
- This is a required input.

### `data_type`

- A _String_ specifying the data type validation for the column of Table.
- Support 3 types: "String", "Integer" and "Double"
- This is a required input.

### `precision`

- An _Integer_ specifying number of digits after floating point displayed inside a Double column.
- The default value is 2.

## Return Code

This function does not have output value.
