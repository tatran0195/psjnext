---
title: "JPT.EnableLicenseFeature()"
description: "Enable or disable an inputted license feature"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Enable/Disable a license feature which is existing in the current Jupiter.

## Syntax

```psj
JPT.EnableLicenseFeature("licenseFeatureName", BoolType)
```

## Inputs

<!-- @since:5.0.1 @required -->
### licenseFeatureName

- Specify the name of Jupiter license which is existing in the current Jupiter.
- The Jupiter license's name can be found at <menuselection>Home » Preference » License</menuselection>.

<!-- @since:5.0.1 @required -->
### BoolType

- Specify the_[BoolType](../data-type/psj-utility/pre-utility/enumeration-types/bool-types)_ describing the enable state of license:
  - _True_: Enable the license.
  - _False_: Disable the license.

:::tip
You also can input **1** instead of inputting JPT.BoolType.TRUE\_VAL,
or input **0** instead of inputting JPT.BoolType.FALSE\_VAL.
:::

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2,3,5,8,9,11}
# Disable license JPT _BASE
JPT.EnableLicenseFeature("JPT _BASE",
                         JPT.BoolType.FALSE _VAL)
# Or
# JPT.EnableLicenseFeature("JPT _BASE", 0)

# Enable license JPT _BASE
JPT.EnableLicenseFeature("JPT _BASE",
                         JPT.BoolType.TRUE _VAL)
# Or
# JPT.EnableLicenseFeature("JPT _BASE", 1)
```
