# Materials

All materials for students to pull each day when they arrive in class. ReadMe page includes tips for python syntax and packages, basic git commands for initialization and daily workflow, links to best practices.

---

# Python Resources

1. Built-in Data Types [https://docs.python.org/3/library/stdtypes.html]  
Video: [https://www.youtube.com/watch?v=ppsCxnNm-JI]
2. Random Module [https://docs.python.org/3/library/random.html]  
Video: [https://www.youtube.com/watch?v=KzqSDvzOFNA]
3. CMath Module [https://docs.python.org/3/library/cmath.html]
4. Complex() Function [https://docs.python.org/3/library/functions.html]
5. Git Documentation [https://git-scm.com/docs]  
Video: [https://www.youtube.com/watch?v=mVnZVw4KJnc]
6. Modular Programming [https://best-practice-and-impact.github.io/qa-of-code-guidance/modular_code.html]

# Daily Workflow

1. Change into the materials directory and pull the most recent changes:
   ```bash
    cd materials/
    git pull
2. Then move back up one level so you can see both materials and my_work directories. Copy the specific file or folder you need into your work folder:
   ```bash
    cd ..
    cp -r materials/specific_file_or_folder my_work/
3. When finished working, save your changes to your GitHub repository:
   ```bash
    git add .
    git commit -m "Some notes about your work today"
    git push origin main

# One-Time Setup (Students)

Do this **once** at the beginning of the course:

1. Open **Terminal**.
2. Clone the class materials repository:
   ```bash
   git clone https://github.com/KSantos1995/materials.git
3. Create a folder where you will do your own work and initialize git with proper steps.
    ```bash
    mkdir -p ~/my_work
    cd my_work
    git init
    git branch -m master main
    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
    git config --global credential.helper store

4. Verify the remote connection is set correctly.
    ```bash
    git remote -v

That way, by the time they get to their **first push**, the credentials are already cached.  

# Troubleshooting & Notes

## First Push Asks for Username/Password
GitHub no longer accepts account passwords for Git operations. You must use a **Personal Access Token (PAT)**.

**Steps:**
- Git will prompt you for:
  - **Username:** your GitHub username  
  - **Password:** your PAT

### How to Generate a Personal Access Token (PAT)
1. Log into GitHub.  
2. Click your profile picture → **Settings**.  
3. Select **Developer settings → Personal access tokens → Tokens (classic)**.  
4. Click **Generate new token → Generate new token (classic)**.  
5. Give the token a name (e.g., `ClassRepoToken`) and select an expiration date.  
6. Under **Select scopes**, check:
   - `repo` (access to your repositories)  
7. Click **Generate token**.  
8. Copy the token immediately — you won’t be able to see it again.  

> After pasting your PAT for the first push, Git will remember it automatically if you ran:
```bash
git config --global credential.helper store