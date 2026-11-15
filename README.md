# CSE Python Solutions

A collection of Python practice solutions for introductory programming problems. The exercises cover number operations, string processing, and pattern printing. The problem statements are included as PDFs.

## Repository contents

| File | Description |
| --- | --- |
| `numberSolutions.py` | Number-related exercises, including arithmetic, digit properties, and comparisons. |
| `stringSolutions.py` | String manipulation and text-processing exercises. |
| `patternSolutions.py` | Exercises that print star and number patterns. |
| `NumberProblems.pdf` | Number exercise statements. |
| `StringProblems.pdf` | String exercise statements. |
| `PatternProblems.pdf` | Pattern exercise statements. |
| `input.txt` | Sample input data used by some exercises. |

## Requirements

- Python 3
- No third-party packages

## Running a solution

From the repository directory, run a Python file with:

```bash
python3 numberSolutions.py
```

The files are exercise workbooks, not a single application. Many examples are kept as comments, while some files contain active code for particular exercises. Find the exercise you want, uncomment or adapt its code if needed, and run the relevant file. Each exercise may expect different input; check its prompt or comments before providing input.

For example, the active code in `patternSolutions.py` reads an integer from standard input:

```bash
echo 4 | python3 patternSolutions.py
```

## Input data

Some exercises read from standard input, while others may read `input.txt`. When an exercise expects a file, run it from the repository directory so the relative path resolves correctly. You can edit `input.txt` to try different sample data.
