# PSJ Sample Code Examples

This folder contains runnable PSJ sample code extracted from the documentation.  
Files mirror the docs folder structure exactly.

## Structure

```
examples/
└── cli/
    ├── 5.0.1/
    │   └── {category}/{FunctionName}.py
    └── 5.1.0/
        └── {category}/{FunctionName}.py
```

## Highlight Markers

Lines marked with `# [hl]` are highlighted in the documentation.  
Range highlights use `# [hl:start]` on the first line and `# [hl:end]` on the last.

These markers are **stripped from the rendered docs output** — they exist only in these `.py` files so that highlights stay accurate even when code is edited (the marker moves with the line).

## Running

Open any `.py` file in your PSJ environment and run it directly.  
The header comment block at the top documents the function name, version, and docs URL.
