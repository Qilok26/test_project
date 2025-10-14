# Class Plan – Day 1 (Project Kickoff & Foundation)

## Objective:

    - Groups form and begin foundational work on their Parent’s Day project. Students will scaffold the project, assign roles, define file structure, and establish collaborative workflows in GitHub.


1. Introduction & Project Goals (10 minutes)

   * Brief overview of Parent’s Day project:
      * Target parents as users
      * Allow multiple programs to be explored (games, data-driven apps, API integrations)
      * Small presentations of code/process afterwards

   * Emphasize learning goals:
     * Working in teams
     * Proper project setup
     * Applying software engineering practices

2. Group Formation & Role Assignment (10 minutes)

   * Groups of 3–5 students
   * Assign preliminary roles (flexible, not rigid):
     * Project Lead / Manager – ensures timeline & collaboration
     * Backend / Data Lead – handles logic, API, or data handling
     * Frontend / UI Lead – handles user interface and user experience
     * Documentation / Git Lead – maintains README, GitHub updates, notes
     * Optional: QA / Tester – ensures program works, catches bugs
     * Tip: Roles can overlap depending on group size; main goal is shared understanding.

3. Project Scaffolding & File Structure (20 minutes)

   * Best Practices for Initial Setup:

     * Create a GitHub Repository
     * Name it clearly (e.g., parents_day_project_group1)
     * Initialize with README.md and .gitignore for Python
     * Decide on branching strategy (main branch, feature branches)

    ### File Structure (example template)

    ```
    project_name/
    │  
    ├── README.md             # Project overview, instructions  
    ├── requirements.txt      # Dependencies  
    ├── main.py               # Entry point  
    ├── src/                  # Core Python code  
    │   ├── __init__.py  
    │   ├── module1.py  
    │   └── module2.py  
    ├── data/                 # Any CSVs, JSON files  
    ├── assets/               # Images, sounds, UI assets  
    └── tests/                # Unit or functional tests  
        ├── test_module1.py  
        └── test_module2.py
    ```

 4. Tips for successful planning  

    * Tip: Encourage them to think modularly: each module handles a specific responsibility.

    * Function Stubs & Documentation
      * Include placeholders for all planned functions before coding.
      * Write placeholder functions with docstrings:
      ```python
      def calculate_score(user_input: str) -> int:
          """
          Calculates the score based on user input.

          Parameters:
              user_input (str): The user's response to the game prompt.

          Returns:
              int: The score earned for this response.
          """
          pass
      ```


1. Task Breakdown & Initial Work Distribution

   * Groups create a mini backlog / task list:
     * Define 3–5 major features
     * Assign initial tasks to team members
     * Prioritize tasks that build the “skeleton” of the program first

2. GitHub Workflow & Best Practices

   * Commit frequently (small, meaningful commits)
   * Branch for features; merge into main when stable
   * Update README with features, installation instructions, and group contributions
   * Example commit message: feat: add main menu UI
   * Optional: Introduce pull requests even for short projects to practice code review

3. Initial Coding / Skeleton Work

   * Each group starts implementing:
   * Skeleton functions/modules
   * Placeholder UI (if applicable)
   * Basic data structures
   * Keep Git workflow active during coding



8. Confirm at End of Class

   * Everyone has a GitHub repo
   * Initial file structure is in place
   * Initial tasks are assigned
   * Encourage communication outside class for Wednesday as a remote 'stand up' day.

