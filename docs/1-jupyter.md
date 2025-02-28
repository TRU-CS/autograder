# Autograder set up guideline for jupyter notebooks
  
1. **Clone the repository**:
   ```bash
   git clone https://github.com/TRU-CS/autograder.git
2. **Set up conda environment (Do this once)**:
   ```bash
   cd autograder
   conda env create -f autograder_env.yaml
3. **Activate conda environment**:
   ```bash
   conda activate autograder_env
4. **Create your assignment using the template in `sample-jupyter` folder**:
   - [`template.ipynb`](https://github.com/TRU-CS/autograder/blob/main/sample-jupyter/template.ipynb) is a Jupyter notebook that instructor use to create the assignment. You can edit this file as you wish.
   - `data` folder is where you can save datasets that you want students to use in the assignment
   - `img` folder is where you can save images that you want students to use in the assignment
   - [`requirements.txt`](https://github.com/TRU-CS/autograder/blob/main/sample-jupyter/requirements.txt) is where you can specify libraries that students need in this assignments (e.g., pandas, numpy, etc.), these libraries will be installed on Gradescope's Docker image
5. **Generate student's version and autograder zip files**:
   ```bash
   otter assign sample-jupyter/template.ipynb sample-jupyter

Replace the path and folder's name as appropriate. In this example, I run the command `otter assign` by retrieving the file from `sample-jupyter/template.ipynb` and the results will be exported to `sample-jupyter` folder

6. **Check your student version**:
    - You will be able to see the student's version under `sample-jupyter/student/template.ipynb`. Open this and make sure no solutions were included here
    - You can even type some answers and run the auto test cells to see if it works
    - There are two type of test cells: 
      - **visible** tests where students can see it directly in their notebook, and  
      - **hidden** tests where students cannot see it and it will only apply after they submit their work to Gradescope
    - Distribute work to students: Everything in the `sample-jupyter/student` folder including data, img, and the ipynb files will need to be shared with the students.
7. **Upload the autograder zip file to Gradescope**
    - Under `sample-jupyter/autograder` folder, you will see a `.zip` file which contains the autograder. Please upload them to Gradescope