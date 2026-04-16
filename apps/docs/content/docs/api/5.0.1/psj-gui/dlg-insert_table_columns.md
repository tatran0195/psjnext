---
id: dlg.insert_table_columns
title: dlg.insert_table_columns()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Insert column(s) at a specific position in the Table
---

## Description

Insert column(s) at a specific position in the Table.

## Syntax

```psj
dlg.insert_table_columns(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `columns`

- A _[TableColumnInfoVector](/docs/cli/5.0.1/data-type/psj-gui/TableColumnInfoVector)_ object or _List of [TableColumnInfo](/docs/cli/5.0.1/data-type/psj-gui/TableColumnInfo)_ specifying the methods of columns.
- This is a required input.

### `position`

- An _Integer_ specifying the position of row to be inserted.
- This is a required input.

## Return Code

This function does not have output value.
