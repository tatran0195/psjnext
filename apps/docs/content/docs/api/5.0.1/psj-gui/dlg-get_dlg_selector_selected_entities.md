---
id: dlg.get_dlg_selector_selected_entities
title: dlg.get_dlg_selector_selected_entities()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Get selected DItem in current Selection List
---

## Description

Get selected _[DItem](/docs/cli/5.0.1/data-type/psj-utility/pre-utility/built-in-types/DItem)_ in current Selection List.

## Syntax

```psj
dlg.get_dlg_selector_selected_entities(...)
```

## Inputs

### `selid`

- A _Integer_ specifying the index of the selector.
- This is a required input.

## Return Code

A _[DItemVector](/docs/cli/5.0.1/data-type/psj-utility/pre-utility/built-in-types/DItemVector)_ object specifying the list of picked items.
