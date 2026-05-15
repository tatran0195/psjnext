---
title: "JPT.GetAllLicensesStatus()"
description: "Get all available licenses status"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all available licenses status.

## Syntax

```psj
JPT.GetAllLicensesStatus()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ stores pairs of license name and its status

## Sample Code

```psj {2}
# Check the status of all available licenses
pprint(JPT.GetAllLicensesStatus())
```
