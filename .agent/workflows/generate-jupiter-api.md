---
description: How to generate the Jupiter Python API wrappers and build the distribution library.
---

# Workflow: Generating the Jupiter Python API

This workflow instructs you on how to trigger a full regeneration of the Python integration wrappers into `jupiterutils` whenever documentation or Jupiter installation macros change.

1. First, ensure that `MACRO_ROOT` is valid inside `packages/jupiter-cli/.env`, or that the underlying default folder exists on your filesystem.
   // turbo-all
2. Execute the generation run from `jupiter-cli`. This invokes the typescript native parsing against the `apps/docs` workspace and outputs straight into the target python folders.

```sh
cd packages/jupiter-cli
bun run build
```

3. Format, lint, and distribute the resultant Python code! This command natively runs `autopep8` formatting to ensure PEP-style spacing over the generated strings, and constructs the python packaging tarballs via setup.py.

```sh
cd ../jupiterutils
bun run build
```

_Note: Alternatively, you can just run `bun run build` at the workspace root, as Turborepo guarantees topological orchestration automatically mapping `jupiter-cli` -> `jupiterutils`._
