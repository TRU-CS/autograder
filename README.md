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

[1. Python - using Jupyter Notebook](https://github.com/TRU-CS/autograder/tree/main/sample-jupyter)

2: [Python using python scripts](https://github.com/TRU-CS/autograder/tree/main/sample-py-script)

3: C/C++


## Resources:
- [Otter-grader](https://otter-grader.readthedocs.io/en/latest/otter_assign/notebook_format.html). This is a library to generate autograder zip file from a jupyter notebook.
- [Gradescope](https://gradescope-autograders.readthedocs.io/en/latest/specs/). This is a platform to host the autograder and run autotest againsts students submissions

## Training resouces:
- [Training session 1 recording](https://onetru-my.sharepoint.com/:v:/g/personal/omendezromero_tru_ca/IQBo4W3eHjNiQIxnHqN-QGwYAdfmEepqzaYh925LYVWPz_M?e=YQj85X) by Alvar (Gradescope staff)
- [Training session 2 recording](https://teams.microsoft.com/l/meetingrecap?driveId=b%21zf2_7MPqVEea23zLXiS7M_tV8lDPmb1Hrnpok85s31zmmg8_TfAcTJ96NGy6KKFO&driveItemId=01QV54V6QDBLEEISOXH5C26SCUNOYGCH3D&sitePath=https%3A%2F%2Fonetru-my.sharepoint.com%2F%3Av%3A%2Fg%2Fpersonal%2Flnguyen_tru_ca%2FIQADCshESdc_Ra9IVGuwYR9jARCUvEN6YAJrL1GImRk_QjU&fileUrl=https%3A%2F%2Fonetru-my.sharepoint.com%2Fpersonal%2Flnguyen_tru_ca%2FDocuments%2FRecordings%2FGradescope+training+session+2+by+Quan-20260219_185652UTC-Meeting+Recording.mp4%3Fweb%3D1&iCalUid=040000008200E00074C5B7101A82E008000000009DCDBA9F9F94DC010000000000000000100000008BDA6E76557AFB4D82092E320D167B95&threadId=19%3Ameeting_MThlZDNlNGQtMzEzNy00NTNlLTgzYTYtZDg1YmYyOWVlZmUw%40thread.v2&organizerId=c69c942b-f5fc-407c-914b-3a6a50d0fa5a&tenantId=eb1c9d1a-e6e8-4097-87fe-bb01690935b7&callId=ca14f375-ddd4-4186-813b-878973ee066c&threadType=Meeting&meetingType=Scheduled&subType=RecapSharingLink_RecapCore) by Quan Nguyen (TRU) 
