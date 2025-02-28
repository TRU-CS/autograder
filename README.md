# Autograder with Gradescope

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Gradescope_logo.svg/2560px-Gradescope_logo.svg.png" width="200" />

Welcome to the autograder repository! This repository contains the guidelines on how to set up autograder on Gradescope with examples. 

## Overview

[Gradescope](http://gradescope.ca) provides a **language-agnostic platform** for running autograders on its infrastructure. By leveraging Docker containers, Gradescope allows users to set up any language, compiler, library, or other dependencies required for programming assignments. 

Users provide a setup script, an autograder script, and any supporting code needed, while Gradescope handles student submissions, executes the autograder at scale, and distributes the results to students and instructors.

### Key features
Gradescope offers several features that make it an effective platform for autograding assignments:
- **🚀 Scalability**: Handles a large number of submissions efficiently.
- **💻 Language Agnostic**: Supports various programming languages and environments through Docker-based execution.
- **✅ Autograded Assignments**: Automatically grade programming assignments based on the autograder script provided by instructors.
- **📝 Manual Grading**: Allows instructors to override autograder results or add manual grading components.
- **🔍 Plagiarism Detection**: Automatically compares student submissions to generate similarity scores and identify potential cases of academic dishonesty.
- **⚡ Instant Feedback**: Students immediately receive feedback from the autograder and can attempt submissions as many times as they want before the deadline.
- **📊 LMS Integration**: Automatically syncs roster and gradebook on Moodle/Canvas.
- **🛠️ Other Admin Features**: Handles regrade requests, deadline extensions, custom rubrics, group submissions, anonymous grading, and more.


Please check out [this video as a demo](https://www.youtube.com/watch?v=RxZxBeIp3sc) of its features. 
  
## Generating autograded assignemnts

Autograder on Gradescope can be created using any programming languages. Please find below some examples with Python:

[1. Python - using Jupyter Notebook](https://github.com/TRU-CS/autograder/blob/main/docs/1-jupyter.md)

2: Python using python scripts

3: C/C++


## Resources:
- [Otter-grader](https://otter-grader.readthedocs.io/en/latest/otter_assign/notebook_format.html). This is a library to generate autograder zip file from a jupyter notebook.
- [Gradescope](https://gradescope-autograders.readthedocs.io/en/latest/specs/). This is a platform to host the autograder and run autotest againsts students submissions