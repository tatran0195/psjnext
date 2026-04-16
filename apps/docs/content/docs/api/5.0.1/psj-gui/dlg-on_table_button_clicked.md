---
id: dlg.on_table_button_clicked
title: dlg.on_table_button_clicked()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set event when selecting a button cell
---

## Description

Set event when selecting a button cell. This API will trigger event only if the selected cell is button cell while dlg.on_table_sel_changed() will trigger event with all kinds of cell.

## Syntax

```psj
dlg.on_table_button_clicked(...)
```

## Inputs

### `name`

- A _String_ specifying the name of Table.
- This is a required input.

### `callfunc`

- The name of function wants to be bound to.
- This is a required input.

## Return Code

This function does not have output value.
