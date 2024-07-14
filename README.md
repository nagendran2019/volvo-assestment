# My volvo-assestment
# How to run test suite-

1. Test Suite image is containerized and below command can be used to pull the docker image. (Docker file is checkedin to this repo for reference).

   **docker pull ernagendran2019/volvotest:latest**
  
2. Run docker container and bind the volume with /usr/src/app (work dir of the container). Binding volume to container's work dir will help in retaining test reports.

3. Use below commands to run the test suites (Full test suite or Feature wise run)

   **A. Full Test Suite Execution- Run below**
   
      **docker run -it ernagendran2019/volvotest /bin/bash -c "radish -b . web_shop_cart_feature.feature web_shop_login_feature.feature web_shop_logout_feature.feature --cucumber-json=<report-filename>.json"**
   
   **(OR)**
   
   **B. To run Login Feature Tests- Run below**
      
     **docker run -it ernagendran2019/volvotest /bin/bash -c "radish -b . <feature-test-file-name>.feature --cucumber-json=<report-filename>.json"**

    For Example-
   
      **docker run -it ernagendran2019/volvotest /bin/bash -c "radish -b . web_shop_login_feature.feature --cucumber-json=<report-filename>.json"**

4. In above commands, we have **"radish -b .", here "." means** the current directory. In Dockerfile, we have made workdir as the directory where all the code files are copied.

5. We can also pull test reports out of docker container by running below command.

    **docker cp <container id>:<source> <target location on host>**
   
6. You may use below command to create HTML report out of json file (generated out of bdd tests execution from Radish in docker container).
  
   **"python generateReportHTM.py -n "<NAME of the TEST REPORT>" -i <Input cucumber json report>.json -t template.html -o <output html file name>.html -c c.css"**
   
7. We have published test reports to file share in Azure (https://volvotestfeed.file.core.windows.net/report/) but we will publish it as part of the Jenkins pipelines itself for quick feedback to the developers.

<img width="706" alt="image" src="https://github.com/user-attachments/assets/719865a6-6d95-47a3-b75a-e08aea185d1c">

8. Running Test cases in parallel, below command can help in creating jobs to run tests in parallel. Will use manifests files of various feature test jobs (uploaded in same repo for reference) to create k8sjobs. Will be using k8s parallel processing approach. Command is below-

     **kubectl create -f ./jobs**

     NOTE- jobs is a folder which will have feature tests manifests yaml files as  given in below screenshot.

Reference documentation- https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/

<img width="643" alt="image" src="https://github.com/user-attachments/assets/9413f8e4-488f-4063-9229-ff4ab07d263a"> .

## CICD Flow-
![image](https://github.com/user-attachments/assets/b5345454-8eb8-4e83-aeb5-9baabd6d9db5)

**Details**-

1. **Introduction**
The purpose of this test suite is to test the user journey flow of a web shop (www.saucedemo.com) using Python and Selenium. The stakeholders for this project include the business unit and management team.

2. **Objective**
The objective is to assess the quality and stability of the user journey flow in the web shop through automated testing. This includes both browsing scenarios and purchasing flows for specific objects.

3. **Scope**
•	In Scope:
o	Automation of user journey flows including browsing and purchasing scenarios.
o	Design and implementation of test cases using Python and Selenium.
o	Parallel execution of tests.
o	Reporting of test results.
•	Out of Scope:
o	Deep integration testing with backend systems.
o	Load testing and performance testing.

4. **Testing Approach**
Tools and Technologies:
•	Python: Used for scripting test cases.
•	Selenium: Used for automating web interactions.
•	Radish-bdd: Framework for organizing and running test cases.
•	WebDriver: To interface with browsers.
•	Jenkins: For CI/CD integration.
•	K8s: For running test cases in parallel using expansion.
•	Jinja2: for creating html reports from cucumber json.
