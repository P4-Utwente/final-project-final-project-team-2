# Final Project P4
For all documentation related to your final project. You can use it for other purposes, but you do not have to.

The wiki should introduce the code base, discuss where it comes from, its size, its relevance, its maturity, whether it is open or proprietary, professionally developed, or by volunteers.

It should furthermore present briefly the CI/CD system, including the build and version control system. It should present the static and dynamic analysis tools that will integrated, as well as the linked management systems.

Explain how developers work with this system, and the envisioned work-flow. 


Analysis:

The source code come from the app call The Fuck, an open source app which corrects your previous console command.

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
