---
title: DPostResponse
id: DPostResponse
---

## Description

This is an instance of a DPostResponse class, represents a Post Frequency Response, Post Transient Response, Post Frequency Response (Solver), and Post Transient Response (Solver) inside Jupiter.

## Properties

| Attribute      | Description                                                                                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name           | The response name.<br />The return value is a string of name (str).                                                                                                                        |
| id             | ID of the Response.<br />The return value is ID (int).                                                                                                                                     |
| type           | Type of the response.<br />The return value is a string of response type (str).                                                                                                            |
| targetAnalysis | The target analysis.<br />The return value is a [DPostAnalysis](../../post-utility/post-built-in-types/DPostAnalysis) object stores all information of the processing target post job.     |
| resultCurve    | The information of the curve.<br />The return value is a [DPostResultCurve](../../post-utility/post-built-in-types/DPostResultCurve) object stores all information of the specified curve. |
