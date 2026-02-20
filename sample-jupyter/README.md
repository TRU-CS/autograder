# sample-jupyter: Otter + Gradescope Template

This folder is an instructor template for building a Jupyter assignment, generating a student release, and generating a Gradescope autograder zip using Otter.

## Folder Layout

### Source files you edit
- `template.ipynb`: instructor notebook with prompts, solutions, and Otter tests.
- `requirements.txt`: Python packages required by the notebook/autograder.
- `data/`: datasets to include for both students and autograder.
- `img/`: images/assets to include for both students and autograder.

### Generated outputs (created by `otter assign`)
- `release/student/template.ipynb`: student-facing notebook (solutions stripped).
- `release/student/requirements.txt`, `release/student/data/`, `release/student/img/`: files distributed to students.
- `release/autograder/template.ipynb`: notebook used inside autograder build.
- `release/autograder/requirements.txt`, `release/autograder/data/`, `release/autograder/img/`, `release/autograder/otter_config.json`.
- `release/autograder/*-autograder_*.zip`: upload this zip to Gradescope.

## Typical Workflow

### 1) Prepare environment (once)
From repo root:
```bash
conda env create -f autograder_env.yaml
conda activate adsc4720
```

### 2) Build your assignment
Edit these files in this folder:
- `template.ipynb`
- `requirements.txt`
- `data/*`
- `img/*`

### 3) Generate student + autograder artifacts
From repo root:
```bash
conda run -n adsc4720 otter assign sample-jupyter/template.ipynb sample-jupyter/release
```

### 4) Validate generated outputs
1. Open `release/student/template.ipynb` and confirm solutions are removed.
2. Run visible tests in the student version to confirm expected behavior.
3. Confirm an autograder zip exists in `release/autograder/`.

### 5) Distribute and upload
1. Give students the contents of `release/student/`.
2. Upload the newest `release/autograder/*-autograder_*.zip` file to Gradescope.

## Notes
- If multiple autograder zip files exist, upload the newest timestamped zip.
- Re-run `otter assign` every time you change `template.ipynb`, tests, data, images, or requirements.
- Extra files such as `.OTTER_LOG` or old zip files are artifacts and can be cleaned up when needed.
