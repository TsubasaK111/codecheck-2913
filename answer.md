13211321322113311213212312311211131122211213211331121321123123211231131122211211131221131112311332211213211321223112111311222112132113213221123123211231132132211231131122211311123113322112111312211312111322111213122112311311123112112322211213211321322113312211223113112221121113122113111231133221121321132132211331121321232221123123211231132132211231131122211331121321232221123113112221131112311332111213122112311311123112112322211211131221131211132221232112111312211322111312211213211312111322211231
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
