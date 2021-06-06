# Final Project P4
For all documentation related to your final project. You can use it for other purposes, but you do not have to.

The wiki should introduce the code base, discuss where it comes from, its size, its relevance, its maturity, whether it is open or proprietary, professionally developed, or by volunteers.

It should furthermore present briefly the CI/CD system, including the build andversion control system. It should present the static and dynamic analysis tools that will integrated, as well as the linked management systems.

Explain how developers work with this system, and the envisioned work-flow. 


Analysis:
1 .
Code size run by LOC: cloc thefuck
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         391           3495           2208          10095
Markdown                         4            138              0            528
XML                              6              0              0             94
YAML                             2              6              0             68
INI                              1              2              0              8
Bourne Shell                     1              1              0              3
-------------------------------------------------------------------------------
SUM:                           405           3642           2208          10796
-------------------------------------------------------------------------------

* Main source code:
cloc thefuck/thefuck
     199 text files.
     199 unique files.
       4 files ignored.

github.com/AlDanial/cloc v 1.88  T=0.10 s (2044.5 files/s, 65805.1 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         199           1565            492           4348
-------------------------------------------------------------------------------
SUM:                           199           1565            492           4348
-------------------------------------------------------------------------------

* Test:
cloc thefuck/tests
     189 text files.
     189 unique files.
       6 files ignored.

github.com/AlDanial/cloc v 1.88  T=0.11 s (1697.0 files/s, 82499.0 lines/s)
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         189           1899           1664           5625
-------------------------------------------------------------------------------
SUM:                           189           1899           1664           5625
-------------------------------------------------------------------------------

Opensource developed by volunteers

2. CI/CD system

Tools for style guide enforcement: flake8

3. How developers work with system
