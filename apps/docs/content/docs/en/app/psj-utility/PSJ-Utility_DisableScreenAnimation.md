---
title: "JPT.DisableScreenAnimation()"
description: "Disable screen animation effect"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Disable screen animation effect.

> The screen animation effect will be enabled after finishing executing the PSJ code.
> Or using _[JPT.EnableScreenAnimation()](JPT.EnableScreenAnimation)_ to turn it on again.

## Syntax

```psj
JPT.DisableScreenAnimation()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {2}
# Disable the screen animation
JPT.DisableScreenAnimation()

# Create a cube and check the screen animation
# The animation effect is disabled
Geometry.Part.Cube(iPartColor=7011837)
```
