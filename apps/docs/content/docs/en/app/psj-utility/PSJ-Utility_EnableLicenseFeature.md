---
title: "JPT.EnableLicenseFeature()"
description: "Enable or disable an inputted license feature"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Enable/Disable a license feature which is existing in the current Jupiter.

## Syntax

```psj
JPT.EnableLicenseFeature("licenseFeatureName", BoolType)
```

## Inputs

### `licenseFeatureName` @type(String) @required

- The name of Jupiter license which is existing in the current Jupiter.
- The Jupiter license's name can be found at<menuselection>Home » Preference » License</menuselection>.

### `BoolType` @type(Enum) @required

- Th&#x65;_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_&#x64;escribing the enable state of license:
  - _True_: Enable the license.
  - _False_: Disable the license.

:::tip
You also can input**1**instead of inputting JPT.BoolType.TRUE\_VAL,
or input**0**instead of inputting JPT.BoolType.FALSE\_VAL.
:::

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,3,5,8,9,11}
# Disable license JPT_BASE
JPT.EnableLicenseFeature("JPT_BASE",
                         JPT.BoolType.FALSE_VAL)
# Or
# JPT.EnableLicenseFeature("JPT_BASE", 0)

# Enable license JPT_BASE
JPT.EnableLicenseFeature("JPT_BASE",
                         JPT.BoolType.TRUE_VAL)
# Or
# JPT.EnableLicenseFeature("JPT_BASE", 1)
```
