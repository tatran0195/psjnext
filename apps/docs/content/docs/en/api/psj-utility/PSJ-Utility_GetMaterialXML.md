---
title: "JPT.GetMaterialXML()"
description: "Get the information of all user material in xml format"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get the information of all user material in xml format.

## Syntax

```psj
JPT.GetMaterialXML()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _String_ containing all the created user material in XML format.

## Sample Code

```psj {6}
# Create user material data base
Properties.Material.Add("Copper _Alloy", [Density([(DENSITY, 8.3e-09)]),
                        Elastic([(YOUNGS _MODULUS, 110000.0), (POISSONS _RATIO, 0.34)])])

# Get all the created user material and store it in XML format
createdMat = JPT.GetMaterialXML()
pprint(createdMat)
```
