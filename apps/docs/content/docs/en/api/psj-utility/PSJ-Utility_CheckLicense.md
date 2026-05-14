---
title: "JPT.CheckLicense()"
description: "Check whether the inputted license is activated or not"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Check whether the inputted license is activated or not.

## Syntax

```psj
JPT.CheckLicense("Feature")
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `Feature`

- The Jupiter license's name.
- The Jupiter license's name can be found at <menuselection>Home » Preference » License</menuselection>.

## Return Code

A _Boolean_ specifying the status of license:

- _True_: License feature is activated.
- _False_: License feature is deactivated.

## Sample Code

```psj {2}
# Get the status of the JPT _BASE feature license and print to the screen
lic = JPT.CheckLicense("JPT _BASE")
print(lic)
```
