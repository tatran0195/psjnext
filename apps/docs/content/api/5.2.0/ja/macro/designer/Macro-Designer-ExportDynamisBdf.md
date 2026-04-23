---
id: ExportDynamisBdf
title: ExportDynamisBdf()
author: TechnoStar Co., Ltd.
authorURL: https://www.e-technostar.com/
---

## Description

Export Dynamis bdf file

## Syntax

```py
ExportDynamisBdf(String strPath, Cursor job)
```

## Inputs

### `1. String`

bdf file path

### `2. Cursor`

job cursor

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```py
ExportDynamisBdf("D:/test.dat", 135:1)
```
