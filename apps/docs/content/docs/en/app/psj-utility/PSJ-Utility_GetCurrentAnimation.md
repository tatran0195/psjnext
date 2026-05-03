---
title: "JPT.GetCurrentAnimation()"
description: "Get all current settings of Animation"
version_introduced: "5.1.0"
available_versions: "all"
---

## Description

Get all current settings of Animation.

## Syntax

```psj
JPT.GetCurrentAnimation()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _Dictionary_ specifying all current settings of Animation.

## Sample Code

```psj {2}
# Get all currently settings of Animation
animationDict = JPT.GetCurrentAnimation()

# Dump out result
pprint(animationDict)

# Print out the Frame number
print("Frame Number: " + str(animationDict["FrameNumber"]))
```
