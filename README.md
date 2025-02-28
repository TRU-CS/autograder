# Autograder with Gradescope

Welcome to the autograder repository! This repository contains the guidelines on how to set up autograder on Gradescope with examples. 

## Overview

[Gradescope](http://gradescope.ca) provides a **language-agnostic platform** for running autograders on its infrastructure. By leveraging Docker containers, Gradescope allows users to set up any language, compiler, library, or other dependencies required for programming assignments. 

Users provide a setup script, an autograder script, and any supporting code needed, while Gradescope handles student submissions, executes the autograder at scale, and distributes the results to students and instructors.

### Key features
- **Language agnostic**: Supports various programming languages and environments through Docker-based execution.
- **Autograded assignement**: Automatically grade programming assignments based on the autograder script provided by instructors
- **Manual Grading**: Allows instructors to override autograder results or add manual grading components.
- **Plagiarism Detection**: Automatically compare student submissions to generate similarity scores to identify potential cases of academic dishonesty.
- **Scalability**: Can hand a large number of submissions simultaneously
- **Instant feedback**: Students immediately got feedback from autograder and can attempts as many times as they want before the deadline
- **LMS integration**: Automatically sync roster and gradebook on Moodle/Canvas
- **Other admin features**: Handle regrade request, deadline extension, create custom rubric, group submission, anonymous grading, and so on.

Please check out [this video as a demo](https://www.youtube.com/watch?v=RxZxBeIp3sc) of its features. 

## Documentations:
- [Otter-grader](https://otter-grader.readthedocs.io/en/latest/otter_assign/notebook_format.html). This is a library to generate autograder zip file from a jupyter notebook.
- [Gradescope](https://gradescope-autograders.readthedocs.io/en/latest/specs/). This is a platform to host the autograder and run autotest againsts students submissions
  
## Generating autograded assignemnts

Autograder on Gradescope can be created using any programming languages. Please find below some examples with Python

<details>
<summary>1. Python - using Jupyter Notebook</summary>
<br>
   
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
