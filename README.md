# Assignment: Day of the Week Calculator

## Objective
Implement a program to determine the day of the week for a given date in the year 2024. The program should not use any built-in date functions or libraries, relying instead on basic arithmetic and conditional statements.

## Days in Each Month

Below is a table showing the number of days in each month for the year 2024 (a leap year):

| Month      | Days in Month |
|------------|---------------|
| January    | 31            |
| February   | 29            |
| March      | 31            |
| April      | 30            |
| May        | 31            |
| June       | 30            |
| July       | 31            |
| August     | 31            |
| September  | 30            |
| October    | 31            |
| November   | 30            |
| December   | 31            |

## Days Before Given Month

To calculate the total number of days before a given month, use the following:

| Month      | Days Before |
|------------|--------------|
| January    | 0            |
| February   | 31           |
| March      | 31 + 29      |
| April      | 31 + 29 + 31 |
| May        | 31 + 29 + 31 + 30 |
| June       | 31 + 29 + 31 + 30 + 31 |
| July       | 31 + 29 + 31 + 30 + 31 + 30 |
| August     | 31 + 29 + 31 + 30 + 31 + 30 + 31 |
| September  | 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 |
| October    | 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 |
| November   | 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 |
| December   | 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 |

## Calculation Method

1. **Input Specification:**
   - Accept two integer inputs: `month` (1-12) and `day` (1 through the number of days in the specified month).

2. **Output Specification:**
   - Print the day of the week corresponding to the given date.

3. **Implementation Details:**
   - Calculate the total number of days from January 1 to the given date.
   - Use modulo 7 to determine the day of the week.

4. **Constraints:**
   - Do not use any date functions or libraries.
   - Use only `if` statements to determine the day of the week.

