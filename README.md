## Calculate the Day of the Week for Any Date in 2024

จงเขียนโปรแกรมเพื่อคำนวณหาวันในสัปดาห์ โดยรับ input ดังนี้
* เดือนในปี 2024 มีค่าที่ถูกต้องในช่วง (1-12)
* วันที่ในเดือนดังกล่าว มีค่าที่ถูกต้องตามตารางด้านล่าง
  
นักศึกษาสามารถสมมติได้ว่าผู้ใช้จะ input เป็นตัวเลข อย่างไรก็ตามต้วเลขอาจไม่อยู่ในช่วงที่ถูกต้อง
จงเขียนโปรแกรมเพื่อคำนวณหาวันในสัปดาห์ 

โดยกำหนดให้ วันที่ 1 January 2024 เป็นวันจันทร์ (Day Number=1, Day Name=Monday)   

## จำนวนวันในแต่ละเดือน
ตารางด้านล่างแสดงจำนวนในแต่ละเดือนของปี 2024 และจำนวนวันที่ผ่านมาจนถึงวันที่ 1 ของเดือนนั้น (Days Before)

|Month Number| Month      | Days in Month | Days Before |
|------------|------------|---------------|---------------|
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


**Output:**
* แสดงข้อความ Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday หรือ Invalid Date
  
|Day Number| Day Name      | 
|------------|------------|
|0 | Sunday       | 
|1 | Monday    | 
|2 | Tuesday   | 
|3 | Wednesday      |
|4 | Thursday      | 
|5 | Friday       |
|6 | Saturday       | 

**Hint:**
คำนวณหาจำนวนวันจาก 1 January 2024 และทำการใช้ modulo 7

**ตัวอย่างที่ 1:**

**Input:** `month=8`,  `day=4` โดยโปรแกรมจะถาม `month`, `day`  ตามลำดับ
```
8
14
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Wednesday
```

**ตัวอย่างที่ 2:**

**Input:** `month=2`,  `day=30` โดยโปรแกรมจะถาม `month`, `day`  ตามลำดับ
```
2
30
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Invalid Date
```

**ตัวอย่างที่ 3:**

**Input:** `month=14`,  `day=5` โดยโปรแกรมจะถาม `month`, `day`  ตามลำดับ
```
14
5
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Invalid Date
```

**ตัวอย่างที่ 4:**

**Input:** `month=2`,  `day=29` โดยโปรแกรมจะถาม `month`, `day`  ตามลำดับ
```
2
29
```
**Expected output:** หลังจากโปรแกรมคำนวณแล้ว โปรแกรมควรแสดงผลลัพธ์เป็น
```
Thursday
```
