# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A documentation and template repository for Thompson Rivers University (TRU) Computer Science instructors to create auto-graded Jupyter Notebook assignments using [Otter-grader](https://otter-grader.readthedocs.io/) and [Gradescope](https://gradescope-autograders.readthedocs.io/). It is not a deployable application — the core deliverable is the workflow and the `sample-jupyter/template.ipynb` as a reference pattern.

## Environment Setup

```bash
conda env create -f autograder_env.yaml
conda activate autograder_env
```

## Key Command

The single most important command in this repo — generates the student-facing notebook and the Gradescope autograder zip from a master notebook:

```bash
otter assign sample-jupyter/template.ipynb sample-jupyter
```

This produces:
- `sample-jupyter/student/template.ipynb` — student version with solutions stripped and hidden tests removed
- `sample-jupyter/autograder/template-autograder_<timestamp>.zip` — uploaded to Gradescope

## Architecture: The One-Notebook Workflow

Everything flows from a single **master instructor notebook** (`sample-jupyter/template.ipynb`). Otter-grader uses special cell markers to split it:

| Marker | Purpose |
|---|---|
| `# BEGIN QUESTION` / `# END QUESTION` | Wraps a graded exercise |
| `# BEGIN SOLUTION` / `# END SOLUTION` | Instructor solution (stripped in student version) |
| `# BEGIN TESTS` / `# END TESTS` | Test assertions |
| `# HIDDEN` | Test visible only to the autograder, not students |
| `manual: true` | Flags a question for human grading |

## Gradescope Autograder Config

`sample-jupyter/autograder/otter_config.json` controls Gradescope behavior:
- `show_stdout: true` — students see cell output in feedback
- `show_hidden: false` — hidden test details are not revealed
- `seed: 42` / `seed_variable: "rng_seed"` — reproducible random state

## Repo Status

This is an early-stage repository. The README references future guides for Python scripts and C/C++ assignments that are not yet implemented. When adding new assignment types, follow the pattern established in `docs/1-jupyter.md` and `sample-jupyter/`.
