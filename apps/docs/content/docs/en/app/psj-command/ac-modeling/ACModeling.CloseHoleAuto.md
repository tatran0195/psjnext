---
title: 'ACModeling.CloseHoleAuto()'
description: 'ACModeling CloseHoleAuto'
introduced: '5.0.1'
removed: '5.2.0'
ribbon: 'ACModeling > CloseHoleAuto'
---

## Description

ACModeling CloseHoleAuto

## Syntax

```psj
ACModeling.CloseHoleAuto(...)
```

## Inputs

### `crlClosedHoleParts` @type(List\[Cursor]) @required

- The closed hole parts.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ACModeling.CloseHoleAuto(crlClosedHoleParts)
```
