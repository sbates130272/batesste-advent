# bateste-advent: An Advent Calandar Name Generator

## Overview

Christmas can be a busy time and a random but fair allocation of
advent calandar doors is just one of billions of tasks that need to be
done.

In the spirit of Christmas here is a small Python program to offload
that task from your wearly brain. Enjoy!

## Usage

You can obtain the help for this program via
```
$ ./advent.py -h
```
An example usage might be
```
$ ./advent.py --names Alice,Bob,Charlie,Debora
```
This will generate a fair allocation of the default 24 advent calandar
doors for a single advent calandar. So an example output would be
```
$ ./advent.py --names Alice,Bob,Charlie,Debora
Door 1: Alice
Door 2: Debora
Door 3: Bob
Door 4: Charlie
Door 5: Bob
Door 6: Charlie
Door 7: Debora
Door 8: Alice
Door 9: Bob
Door 10: Debora
Door 11: Charlie
Door 12: Alice
Door 13: Alice
Door 14: Bob
Door 15: Debora
Door 16: Charlie
Door 17: Bob
Door 18: Charlie
Door 19: Debora
Door 20: Alice
Door 21: Alice
Door 22: Charlie
Door 23: Debora
Door 24: Bob

```
