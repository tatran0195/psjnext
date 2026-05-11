---
title: DGroup
id: DGroup
---

## Description

This is an instance of a DGroup class, represents a Group inside Jupiter.

## Properties

| Attribute      | Description                                                                                                                                                         |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | Name of the Group.                                                                                                                                                  |
| typeID         | Type ID of the Group (ID = 79).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                |
| id             | External ID of the Group.<br />ID can be duplicated, but not recommended.<br />ID can be changed using the renumbering function.<br />The return value is ID (int). |
| targets        | Hold the contents of the Group.<br />The return value is a list of [`DItem`](DItem).                                                                                |
| color\* [^(1)] | Group color information.<br />This value can be adjusted.<br />The return value is a RGB color.                                                                     |

### Notice

[^(1)]: An asterisk symbol \* in attribute name means that attribute can be changed/assigned from the current to the new value.
