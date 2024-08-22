# Assignment: Day of the Week 2024 Calculator

## Objective
จงเขียนโปรแกรมเพื่อคำนวณหาวันในสัปดาห์ โดยรับ input ดังนี้
* เดือนในปี 2024 มีค่าที่ถูกต้องในช่วง (1-12)
* วันที่ในเดือนดังกล่าว มีค่าที่ถูกต้องตามตารางด้านล่าง
  
นักศึกษาสามารถสมมติได้ว่าผู้ใช้จะ input เป็นตัวเลข อย่างไรก็ตามต้วเลขอาจไม่อยู่ในช่วงที่ถูกต้อง
จงเขียนโปรแกรมเพื่อคำนวณหาวันในสัปดาห์ 


## จำนวนวันใ

Below is a table showing the number of days in each month for the year 2024 (a leap year):

|Month Number| Month      | Days in Month | Days Before |
|------------|---------------|---------------|
|1 | January    | 31            | 0            |
|2 | February   | 29            | 31            |
|3 | March      | 31            | 60            |
|4 | April      | 30            | 91            |
|5 | May        | 31            | 121            |
|6 | June       | 30            | 152            |
|7 | July       | 31            | 182            |
|8 | August     | 31            | 213             |
|9 | September  | 30            | 244             |
|10 | October    | 31            | 274            |
|11 | November   | 30            | 305             |
|12 | December   | 31            | 335            |


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

