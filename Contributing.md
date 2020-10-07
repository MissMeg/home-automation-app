# Contributing to this Project

## Contributor Covenant Code of Conduct

### Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

### Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
[https://www.contributor-covenant.org/version/2/0/code_of_conduct.html](https://www.contributor-covenant.org/version/2/0/code_of_conduct.html).

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq](https://www.contributor-covenant.org/faq). Translations are available at
[https://www.contributor-covenant.org/translations](https://www.contributor-covenant.org/translations).

## How to Contribute

Option #1: Start with the Hacktoberfest issue [here](https://github.com/MissMeg/home-automation-app/issues/2) to see a list of all current issues. When you find an issue you would like to take on, comment on the issue and say you are taking it on so other's know it is taken. If at any point you no longer want to work on the issue, make sure to comment on the issue so other's know it is available again.

Option #2: If you have found a bug or would like to add a new feature to the project, create a new issue and tag me in it for approval. Once approved, you're good to get coding! You can also submit issues for others to tackle if you do not want to code it yourself.

### Process

1. Claim an issue
2. Fork the project
3. Download the code
4. Work on the code on your machine.
5. Push your code to your forked project.
6. Create a pull request.
7. Wait to see if it's accepted.
8. Celebrate! You've just contributed to a project!
9. Now go do it again! :)

### Best Practices

* Write clean, readable code
* I'd rather have too many comments than none at all
* The goal is to help others learn how to contribute - no bug is too small
* Explain thoroughly so coders at any level can understand. KISS ;)
* Keep discussions polite and professional (See the COC above)

### Pre-commit - prerequisites

The idea for adding pre-commit is to check all python code has been formatted universally across the entire repo.

But before installing pre-commit, you need to first have [isort](https://github.com/timothycrosley/isort), [black](https://github.com/ambv/black) & [flake8](https://gitlab.com/pycqa/flake8) installed into your local machine. This is so when pre-commit warns you of unformatted code you can just run these commands separately against your code (e.g. with black the command would look like `black path/to/your/python/code.py` ) before committing changes.

To find the matching versions of these 3 dependencies, please refer to `.pre-commit-config.yaml` file and check version under `rev:`.

### Pre-commit - install
To install, please refer to [install pre-commit](https://pre-commit.com/#quick-start) to your local machine.

At the time of this writing (2020/10/01) the latest version of pre-commit is `2.7.1`. With this you install [isort](https://github.com/timothycrosley/isort), [black](https://github.com/ambv/black) & [flake8](https://gitlab.com/pycqa/flake8) as a python linter + formatter that runs everytime you commit your changes to your branch so you don't have to worry about breaking coding format from other devs :)