# Regular Expressions

## Description

This project focuses on building and using regular expressions (regex) with **Oniguruma**, the regex library used by Ruby by default. The goal is to practice writing regex patterns to match specific string patterns by creating Ruby scripts that accept input arguments and apply regex matching.

## Background Context

> For this project, you have to build your regular expression using Oniguruma, a regular expression library which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Each Ruby script in this project follows the same template — only the regex pattern changes:

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/YOUR_REGEX_HERE/).join
```

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on **Ubuntu 20.04 LTS**
- All files should end with a new line
- All Ruby script files must be executable
- The first line of all scripts must be exactly `#!/usr/bin/env ruby`
- All regex must be built for the **Oniguruma** library

## Tasks

### 0. Simply matching School
**File:** `0-simply_match_school.rb`

Matches the word `School` in any given string.

```bash
$ ./0-simply_match_school.rb "Best School"
School
```

---

### 1. Repetition Token #0
**File:** `1-repetition_token_0.rb`

Matches strings using a repetition token pattern (one or more occurrences).

---

### 2. Repetition Token #1
**File:** `2-repetition_token_1.rb`

Matches strings using a repetition token pattern (zero or more occurrences).

---

### 3. Repetition Token #2
**File:** `3-repetition_token_2.rb`

Matches strings using a repetition token pattern (zero or one occurrence).

---

### 4. Repetition Token #3
**File:** `4-repetition_token_3.rb`

Matches strings using a repetition token pattern. **Note:** The regex must not contain square brackets.

---

### 5. Not quite HBTN yet
**File:** `5-beginning_and_end.rb`

Matches a string that:
- Starts with `h`
- Ends with `n`
- Has **exactly one** character in between

```bash
$ ./5-beginning_and_end.rb 'hbn'
hbn
$ ./5-beginning_and_end.rb 'hn'
(empty)
```

---

### 6. Call me maybe
**File:** `6-phone_number.rb`

Matches a **10-digit phone number** only — no spaces, dashes, or extra characters allowed.

```bash
$ ./6-phone_number.rb 4155049898
4155049898
$ ./6-phone_number.rb "415 504 9898"
(empty)
```

---

### 7. OMG WHY ARE YOU SHOUTING?
**File:** `7-OMG_WHY_ARE_YOU_SHOUTING.rb`

Matches **capital letters only** from any given string.

```bash
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe"
ILO
```

---

### 8. Textme
**File:** `8-textme.rb`

Parses a TextMe SMS log line and outputs: `[SENDER],[RECEIVER],[FLAGS]`

```bash
$ ./8-textme.rb 'Feb 1 11:00:00 ... [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] ...'
Google,+16474951758,-1:0:-1:0:-1
```

---

### 9. Pass LinkedIn technical interview level0
**File:** `9-passed_linkedin_regex_challenge.jpg`

Screenshot proving completion of the [LinkedIn Regex Puzzle](https://engineering.linkedin.com/puzzle), showing the congratulations screen with date and time.

---

## Resources

- [Regular expressions - basics](https://intranet.aluswe.com/rltoken/KvagRAag_zdWeRLaktZXyA)
- [Regular expressions - advanced](https://intranet.aluswe.com/rltoken/Yb5one1viWFGAzQ9UlqfJA)
- [Rubular — Ruby regex tester](https://rubular.com)
- [Learn Regular Expressions with interactive exercises](https://regexone.com)

## Author

- **Sylvain Kalache**

## Repository

- **GitHub:** `alu-scripting`
- **Directory:** `regular_expressions`
