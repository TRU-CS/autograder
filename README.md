# Autograder

Welcome to the autograder repository! This repository contains the guidelines on how to set up autograder on Gradescope with examples. 

## Documentations:
- [Otter-grader](https://otter-grader.readthedocs.io/en/latest/otter_assign/notebook_format.html). This is a library to generate autograder zip file from a jupyter notebook.
- [Gradescope](https://gradescope-autograders.readthedocs.io/en/latest/specs/). This is a platform to host the autograder and run autotest againsts students submissions

## Contents

## Generating autograded assignemnts

Autograder on Gradescope can be created using any programming languages. Please find below some examples with Python

<details>
<summary>1. Python - using Jupyter Notebook</summary>
<br>
   
1. **Clone the repository**:
   ```bash
   git clone 
2. **Set up conda environment (Do this once)**:
   ```bash
   cd autograder
   conda env create -f autograder.yaml
3. **Activate conda environment**:
   ```bash
   conda activate autograder
4. **Create your assignment using the template in `source/template` folder**:
   - `template.ipynb` is a Jupyter notebook that instructor used to create the assignment
   - `data` folder is where you can save datasets that you want students to use in the assignment
   - `img` folder is where you can save images that you want students to use in the assignment
   - `requirements.text` is where you can specify libraries that students need in this assignments, these libraries will be installed on Gradescope's Docker image
5. **Generate student's version and autograder zip files**:
   ```bash
   otter assign source/template/template.ipynb release/template

Replace the path and folder's name as appropriate. In this example, I run the command `otter assign` by retrieving the file from `source/template/template.ipynb` and the results will be exported to `release/template` folder

6. **Check your student version**:
    - You will be able to see the student's version under `release/template/student/template.ipynb`. Open this and make sure no solutions were included here
    - You can even type some answers and run the auto test cells to see if it works
    - There are two type of test cells: 
      - **visible** tests where students can see it directly in their notebook, and  
      - **hidden** tests where students cannot see it and it will only apply after they submit their work to Gradescope
    - Distribute work to students: Everything in the `release/template/student` folder including data, img, and the ipynb files will need to be shared with the students.
7. **Upload the autograder zip file to Gradescope**
    - Under `release/template/autograder` folder, you will see a `.zip` file which contains the autograder. Please upload them to Gradescope
</details>


<details>
<summary>2: Python using python scripts</summary>
<br>

Insert here

</details>

<details>
<summary>3: C</summary>
<br>

Insert here

</details>
