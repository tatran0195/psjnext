---
title: "JPT.EnableScreenAnimation()"
description: "Enable screen animation effect"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Enable screen animation effect.

> This utility is used to enable the screen animation effect after using the _[JPT.DisableScreenAnimation()](JPT.DisableScreenAnimation)_ utility.

## Syntax

```psj
JPT.EnableScreenAnimation()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {9}
# Disable the screen animation
JPT.DisableScreenAnimation()

# Create a cube and check the screen animation
# The animation effect is disabled
Geometry.Part.Cube(iPartColor=7011837)

# Enable the screen animation effect after using JPT.DisableScreenAnimation()
JPT.EnableScreenAnimation()

# Create a cube and check the screen animation
# The animation effect will be enabled
Geometry.Part.Cube(iPartColor=7011837)
```
