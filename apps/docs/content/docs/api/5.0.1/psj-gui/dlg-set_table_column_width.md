---
id: dlg.set_table_column_width
title: dlg.set_table_column_width()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set the width of the specified column in the Table
---

## Description

Set the width of the specified column in the Table.

## Syntax

```psj
dlg.set_table_column_width(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `col`

- An _Integer_ specifying the order of the column where its width will be changed (starts from 0).
- This is a required input.

### `width`

- An _Integer_ specifying the column width.
- If not specified, a dialog is opened for user to enter a value.

## Return Code

This function does not have output value.
