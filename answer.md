1321132132211331121321231231121113112221121321133112132112312321123113112221121113122113111231133221121321132122311211131122211213211321322112312321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331221122311311222112111312211311123113322112132113213221133112132123222112312321123113213221123113112221133112132123222112311311222113111231133211121312211231131112311211232221121113122113121113222123211211131221132211131221121321131211132221123
----
# Look-And-Say Solution [Python]
This is my solution for Codecheck's <a href="https://app.code-check.io/orgs/codecheck_official/challenges/177">Look-And-Say challenge</a> in Python.

## Methodology
* The basic 'secret method' of the Look-And-Say sequence can be found on [wikipedia](https://en.wikipedia.org/wiki/Look-and-say_sequence).
* This is a fairly straightforward recursive task, with no backtracking.
* For convenience, numbers are for the most part treated as strings.  
  This is due to the nature of the sequence.
* The `say_number`method reads out an input in the look-and-say manner.
* The `main` method calls the `say_number` recursively, starting with "1".

## Installation:
1. **Install all requirements!**
2. Download the contents of this repo to a directory of your choice.
3. Open command prompt.
4. Enter `cd [directory of your choice] && codecheck`
5. Some tests should print to console, ending with:
```
codecheck: tests  : 7
codecheck: success: 7
codecheck: failure: 0
```
6. This means that I'm purty awesome. (And so are you!)

## Requirements:
* <a href="https://www.python.org/downloads/">Python2</a>
* <a href="https://docs.npmjs.com/getting-started/installing-node">Node.js/npm</a>
* <a href="https://github.com/code-check/codecheck">Codecheck</a> (`npm install codecheck -g`)
