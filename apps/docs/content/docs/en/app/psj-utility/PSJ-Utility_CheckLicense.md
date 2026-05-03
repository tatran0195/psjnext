---
title: "JPT.CheckLicense()"
description: "Check whether the inputted license is activated or not"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Check whether the inputted license is activated or not.

## Syntax

```psj
JPT.CheckLicense("Feature")
```

## Inputs

### `Feature` @type(String) @required

- The Jupiter license's name.
- The Jupiter license's name can be found at<menuselection>Home » Preference » License</menuselection>.

## Return Code

A _Boolean_ specifying the status of license:

- _True_: License feature is activated.
- _False_: License feature is deactivated.

## Sample Code

```psj {2}
# Get the status of the JPT_BASE feature license and print to the screen
lic = JPT.CheckLicense("JPT_BASE")
print(lic)
```
