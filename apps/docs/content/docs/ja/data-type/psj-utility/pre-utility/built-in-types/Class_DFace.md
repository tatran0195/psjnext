---
title: DFace
id: DFace
---

## Description

This is an instance of a DFace class, represents a Face inside Jupiter.

## Properties

| Attribute      | Description                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| typeID         | Type ID of the Face (ID = 6).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                 |
| id             | External ID of the Face.<br />ID can be duplicated, but not recommended.<br />ID can be changed using the renumbering function.<br />The return value is ID (int). |
| edges          | The edges belong to the Face.<br />The return value is a list of edges.                                                                                            |
| elems          | The elements belong to the Face.<br />The return value is a list of elements.                                                                                      |
| nodes          | The nodes belong to the Face.<br />The return value is a list of nodes.                                                                                            |
| color\* [^(1)] | Face color information.<br />This value can be adjusted.<br />The return value is a RGB color.                                                                     |

### Notice

[^(1)]: An asterisk symbol \* in attribute name means that attribute can be changed/assigned from the current to the new value.
