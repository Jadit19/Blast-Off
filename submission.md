# Submission Guidelines

## Setting up
Firstly, fork this repository and clone it on your local machine using `git clone`

```sh
git clone https://github.com/<your_github_username>/Blast-Off.git
```

## Structure
Create a directory in the cloned repo, the name of which should be: `<Roll_no>_<First_name>_<Surname>`. Inside your directory, your solution to the assignment must be named `Week_<week_no>`.

For now, add a `README.md` inside your respective directory, the content of which must be:

```markdown
# README

Name    : <Your_name>
Roll no.: <Your_roll_no>
```

Eventually, the directory structure should look something like this:

```
200038_Adit_Jain
│
├── README.md
├── Week_1.pdf
├── Week_2.pdf
├── Week_3.pdf
├── Week_4.ipynb
└── Week_5.ipynb
```

## Pushing

Once you have added your files in your local machine, in order to commit and push the same, follow the following set of commands:

```sh
git add .
git commit -m "<commit_message>"
git push
```

Then, click on <b>Pull Requests</b> on your forked repository and then click on <b>New pull request</b>. The heading of every pull request must be: `Added submission for week #<week_no>`

## What next?
Once your assignments have been checked, the pull request will be accepted and your files will be merged here. If some error is found during the submission process, the same will be updated via a comment on the pull request.