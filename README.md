#  MapQuest Feature Enhancement
## CPE028/CPE41S4 - Breakout Room Activity 7.1 (Option 1)
### This is a repository for enhancement of MapQuest from Lab 4.9.2

#### Team (Agile) Members:
* Atabay, FJ Vincent
* De Guzman, Jericko

<br>Option 1: Feature Enhancements - MapQuest</br>
<br>You have on your computer the code from "Integrate a REST API in a Python Application" (lab 4.9.2). Your manager has requested:</br>
* Moving the code from your computer to a collaborative version control system
* Feature enhancements

<br>Your manager has received a request from the marketing department to add new features to the MapQuest API application. You manager has given your team the task of making feature enhancements to this application. These feature enhancements can involve UI changes such as improving the formatting output (with colors, tables, etc.), providing the user with additional options such as data using the metric system or miles, or the type of data you provide to the user. Any other improvements that you think are appropriate will differentiate your work from the work of other teams.</br>

<br>
Your manager would also like a list of other enhancements for a future revision. These are called backlog items. This backlog will be used for Project Activity 4.
</br>

<br>
Note: You will be using the final code from the lab, "Integrate a REST API in a Python Application". In this lab, you used the MapQuest directions API to retrieve JSON data, parsed the data and formatted it for the user.
</br>

## CPE028/CPE41S4 - Breakout Room Activity 9.1
###  Automated Software Testing and Deployment

#### Team (Agile) Members:
* Atabay, FJ Vincent
* De Guzman, Jericko

<br>The marketing department has received very favorable reviews and feedback about your application. Your manager has acquired funding and resources for your team to add some of the backlog features to your application.</br>

<br>As your team continues working on the code, each team member contributes to your shared application codebase on GitHub with their changes. Despite the fact that you are trying to do doing manual code reviews for each commit, or pull request, sometimes a team member’s change will break some functionality in the application. Many times, such issues are identified only when the application is deployed and running. This usually leads to long troubleshooting sessions and slows down the development.</br>

<br>To eliminate the issues from above and ease development, your team has been asked to use some of the best practices from the DevOps methodology. Design a testing process that would be triggered automatically by GitHub whenever there is a new commit to the codebase. Only if all the test cases are passed, can the committed change be merged, or further used. Your manager has recommended that, in addition to Jenkins, explore other CI/CD tools like GitHub Actions, CircleCI, etc., that might help you to build this automated CI/CD pipeline.</br>

<br>Actions Done:</br>
* Created a bash script that generates a Dockerfile containing the resources that MapQuest App needs.
* Implemented one backlog (chained dropdown options for starting and destination location for specifying the country/state).
* Created a testing script to ensure that the application is working as intended.
* Created build and test jobs in Jenkins.
* Utilized the created build and test jobs to create a pipeline in Jenkins.
* Configured the pipeline such that every change (push) in the GitHub Main Repository is reflected on the deployed application inside the Jenkins server running locally.
