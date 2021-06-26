
# Final Project P4 - The Fuck [![Version][version-badge]][version-link] [![Build Status][workflow-badge]][workflow-link] [![Coverage][coverage-badge]][coverage-link]

current host coverall result in another repo due to access deny to P4-Utwente

1. Code size

|Language                 |   files           |        blank |    comment    |  code|
|-------------------------|-------------------|--------------|---------------|------|
|Python                   |       391         |  3495        |   2208        |10095 (4348 LOC function, 5625 LOC for test)  |
|Markdown                 |       4           | 138          |   0           | 528  |
|XML                      |        6          |    0         |     0         |    94|
|YAML                     |        2          |    6         |     0         |    68|
|INI                      |        1          |    2         |     0         |     8|
|Bourne Shell             |       1           |  1           |   0           |  3   |
|SUM:                     |      405          | 3642         |  2208         | 10796|


Latest releases: 3.30, 81 releases\
Opensource developed by volunteers, 156 contributors

2. CI/CD system\
Build and version control system: Github\
CI: Using workflows of Github Actions to run test on push and pull request(It used to use travisci but then migrating to workflow from Jan)\
CD: For delivering, it uses the script in release.py to bump to new version, then upload package to Pypi\
Tools for style guide enforcement: flake8

3. How developers work with system\
  Developers will create pull request to the offical repostitory, author will review and consider to accept it

[version-badge]:   https://shields.io/github/v/release/P4-Utwente/final-project-final-project-team-2
[version-link]:    https://test.pypi.org/project/pppp/
[workflow-badge]:  https://github.com/P4-Utwente/final-project-final-project-team-2/workflows/Tests/badge.svg
[workflow-link]:   https://github.com/P4-Utwente/final-project-final-project-team-2/actions?query=workflow%3ATests
[coverage-badge]:  https://img.shields.io/coveralls/HaLe-Twente/ds-ienlp.svg  
[coverage-link]:   https://coveralls.io/github/HaLe-Twente/ds-ienlp
