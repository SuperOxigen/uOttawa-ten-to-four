# uOttawa-ten-to-four

A tool to convert your uOttawa 10 point GPA to the standard 4 point system.

## How to Use

Currently, only supports one format, a CSV file for the following form.

1.  Text cells can be anywhere.
2.  The second column can be text or an integer from 0 to 10
3.  Thats it.

| Header 1 | Header 2 |
| -------- | -------- |
| Course A |   8      |
| Course B |   5      |

Output will be a new CSV file with all values from 0 to 10 in the second
column being replaced by their 4 point system equivalent.

### Example:

The following is an example.

*my_marks10.csv*

```
Course,Mark
Year 1
ITI1100,9
MAT1340,8
Year 2
ELG2120,7
CSI2110,6
```

*on the command line*
```bash
$ ./uOttf.py -i my_marks10.csv -o my_marks4.csv
```

*my_marks4.csv*
```
Year 1
ITI1100,3.9
MAT1340,3.7
Year 2
ELG2120,3.3
CSI2110,3.0
```

## The Formula

The conversion is based on this table.

| 10 Point System | 4 Point System |
| --------------- | -------------- |
| 10              | 4.0            |
| 9               | 3.9            |
| 8               | 3.7            |
| 7               | 3.3            |
| 6               | 3.0            |
| 5               | 2.3            |
| 4               | 2.0            |
| 3               | 1.3            |
| 2               | 1.0            |
| 1               | 0.0            |
| 0               | 0.0            |

## Other Info

*   [LICENCE](LICENCE)
