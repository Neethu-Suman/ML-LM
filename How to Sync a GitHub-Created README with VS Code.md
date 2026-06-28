## Part 1: Adding the README directly on GitHub

1.	Open your browser and navigate to your repository on GitHub.com.

2.	Near the top of your file list, click the Add file dropdown button and select Create new file.

3.	In the filename box, type README.md.

4.	Paste your Markdown text into the large text area below.

5.	Scroll down to the Commit changes... section at the bottom.

6.	Write a short commit message (e.g., Add README via GitHub website) and click the green Commit changes button.

Your README is now live on GitHub!

## Part 2: Reflecting the changes back to VS Code

Right now, your online GitHub repository has the README.md file, but your local VS Code folder does not. If you try to push new code from VS Code right now, GitHub will reject it because your local folder is out of date.

To sync them up, follow these steps:

1.	Open VS Code on your computer.

2.	Open the built-in terminal (Ctrl + or Cmd + ).

3.	Run the following command:

            git pull origin main

