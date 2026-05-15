---
title: "ExportContactPairData()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export content of show contact dialog into csv file.

## Syntax

```psj
ExportContactPairData(string strCSVFile, int iResultSet, int iTimeStep, string strResultTypeName, string strResultCompName, int iResultPosition, string[] contactPairs)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

Path of csv file to export.

<!-- @since:5.1.0 -->
### 2. int

Result set.

<!-- @since:5.1.0 -->
### 3. int

Time step.

<!-- @since:5.1.0 -->
### 4. string

Name of result type.

<!-- @since:5.1.0 -->
### 5. string

Name of component.

<!-- @since:5.1.0 -->
### 6. int

Data Location.

<!-- @since:5.1.0 -->
### 7. string\[]

Names of export contact pair.

## Return Code

Nothing.

## Sample Code

```psj
ExportContactPairData("C:/Users/Admin/Downloads/contact _f2/contact _f2/321123.csv", 1, 0, 0, ContactForceShear, Translational, 1, ["c10", "c7", "c8", "c9"])
```
