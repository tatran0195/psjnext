---
title: "EnableLicenseFeature()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Turn ON / OFF indicated license.

## Syntax

```psj
EnableLicenseFeature(String License, int Status)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

License feature shown in Home > Preference > License.

<!-- @since:5.0.1 -->
### 2. Int

- 1: Turn ON the license feature.
- 0: Turn OFF the license feature.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
EnableLicenseFeature("JPT _ANNAS", 0)
```
