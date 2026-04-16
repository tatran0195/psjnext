---
id: JPT-CheckLicense
title: JPT.CheckLicense()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Check whether the inputted license is activated or not
---

## Description

Check whether the inputted license is activated or not.

## Syntax

```psj
JPT.CheckLicense("Feature")
```

## Inputs

### `Feature`

- A _String_ specifying the Jupiter license's name.
- The Jupiter license's name can be found at <menuselection>Home &#187; Preference &#187; License</menuselection>.
- This is a required input.

## Return Code

A _Boolean_ specifying the status of license:

- _True_: License feature is activated.
- _False_: License feature is deactivated.
