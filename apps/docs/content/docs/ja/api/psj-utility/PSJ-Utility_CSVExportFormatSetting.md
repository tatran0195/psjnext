---
title: "JPT.CSVExportFormatSetting()"
description: "Set export format of CSV file as with/without BOM."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set export format of CSV file as with/without BOM.

## Syntax

```psj
JPT.CSVExportFormatSetting(int Selection)
```

## Inputs

### `int`

- Selection of export format. 0: without BOM, 1: with BOM.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {1}
JPT.CSVExportFormatSetting(0)
```
