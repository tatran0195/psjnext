---
title: "JPT.DisableScreenUpdate()"
description: "Disable updating data render on the display window"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Disable updating data render on the display window.

:::note

The data render will be enabled after finishing executing the PSJ code.

:::

## Syntax

```psj
JPT.DisableScreenUpdate()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2}
# Disable data render on the display window
JPT.DisableScreenUpdate()

# Create a cube and check the data render
# The data render is disabled
Geometry.Part.Cube(iPartColor=7011837)
```
