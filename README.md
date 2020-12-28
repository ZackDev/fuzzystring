Helper script to generate a parameterized random string.

The script takes two parameters as arguments:
- type of string to generate
  - "a" - letters from the latin alphabet a to Z
  - "n" - numeric 0 to 9
  - "s" - special characters !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

- length of string to generate
  - any non negative numerical value

Example usage to generate a alphanumerical string of length 10:
```
s = fuzzyfy("an", 10)
print(s)
```

Output:
```
G98o57r21f
```
