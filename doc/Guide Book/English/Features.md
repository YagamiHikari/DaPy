## Features
**Convinience** and **efficiency** are the cornerstone of DaPy. 
Since the very beginning, we have designed DaPy to Python's 
native data structures as much as possible and we struggle to make 
it supports more Python syntax habits. Therefore you can 
adapt to DaPy quickly, if you imagine you are opearting an 2-dimentions table.
In addition, we do our best to simplify
the formulas or mathematical models in it, in order to let you 
implement your ideas fluently.   

#### Visually manage diverse data
Every data scientist should have at least one experience in handling the needed datas 
with multiple sources. It is inconvenient to manage or access datas with amount of 
variables names. In this section, we will simply introduce a data container, which 
represented the ideology of designing DaPy, called *DataSet*.

Both data scientist and a young kid in primary school are skillful in 
MS Office Excel software. In this software, every data should be contained in a 
*sheet* structures. We draw on ideas from Excel and proposed a data managing structure  
that is *DataSet*. 

Here is a example how does DaPy work basically to manage diverse dataset. We have prepared a [students.xlsx](http://www.wuxsweb.cn/Library/DaPy$Examples_data/students.xlsx) file as a example, which has 3 sheets insides, named "Info", "Course", and "Scholarship". Now, we will use DaPy to read this file into a DataSet object and access the data.
```Python2
>>> import DaPy as dp
>>> data = dp.read('students.xlsx')
>>> data.show()
sheet:Info
==========
   ID   |   Name  | Gender | Age 
--------+---------+--------+------
 1801.0 |  Olivia |   F    | 14.0 
 1802.0 |  James  |   M    | 14.0 
 1803.0 | Charles |   M    | 15.0 
 1804.0 |   Emma  |   F    | 16.0 
 1805.0 |   Mary  |   F    | 13.0 
 1806.0 |  Kevin  |   M    | 14.0 
 1807.0 |  Jeanne |   F    | 15.0 

sheet:Course
============
   ID   |   Course   | Score
--------+------------+-------
 1801.0 | Chemistry  |  90.0 
 1802.0 |  Biology   |  87.0 
 1803.0 |  Biology   |  88.0 
 1804.0 |  Geology   |  85.0 
 1805.0 | psychology |  92.0 
 1806.0 | Chemistry  |  93.0 
 1807.0 |  Geology   |  87.0 

sheet:Scholarship
=================
   ID   | Scholarship
--------+-------------
 1801.0 |    Third    
 1805.0 |    Second   
 1806.0 |    First    
```
And now, we have a new sheet named "tuition" that needs to be added into data and save it as "new_students.xlsx". One of the sheet structure in DaPy is *Frame*. You can initialize a new Frame object with records and column names. 
 ```Python3
>>> tuition = dp.Frame(
	[[1801, 3000],
	 [1802, 3500],
	 [1803, 3000],
	 [1804, 2500],
	 [1805, 2500],
	 [1806, 2500],
	 [1807, 3000]],
	['ID', 'Tuition'])
>>> data.add(tuition, 'Tuition')
>>> data.save("new_students.xlsx")
 ```
#### Easily insert and delete a large number of data  
As far as we are concerned, DaPy is a kind of data manage system, therefore, we learned from the thinking as 'CRUE'(Create, Retrieve, Update and Delete). We followed some of the 'list()' structure supported functions and extended them appropriately to fit the two-dimensional data structure. In this section, we would briefly review all these functions.

```DaPy.DataSet.add()``` is the hightest level data function, which is used to add a new 2-dimentional data structure into DataSet structure. With this function, DataSet can support multiple sheets inside. Following example shows how to add a new sheet.
```Python2
>>> data = dp.DataSet(obj=[[1, 1, 1], [1, 1, 1]], sheet='sheet-1')
>>> data.add(item=[[2, 2, 2], [2, 2, 2]], sheet='sheet-2')
>>> data.toframe()
>>> data
sheet:sheet-1
=============
 C_0 | C_1 | C_2
-----+-----+-----
  1  |  1  |  1  
  1  |  1  |  1  
  
sheet:sheet-2
=============
 C_0 | C_1 | C_2
-----+-----+-----
  2  |  2  |  2  
  2  |  2  |  2  
```

First of all, we are going to introduce two pairs of functions to you. 

One of the pairs of functions are ```append()``` and ```append_col()```, and which are obviously to see the meanings. ```append()``` can help you append a new record at the tail of each sheet and ```append_col()``` can support you to append a new variable at the tail of each sheet in DataSet.
```Python2
>>> from DaPy import datasets
>>> example = datasets.example()
>>> example.append([None, None, None, None])
>>> example.append_col(series=range(example.shape[0].Ln), 
		       variable_name='New_col')
>>> example.show()
sheet:sample
============
 A_col | B_col | C_col | D_col | New_col
-------+-------+-------+-------+---------
   3   |   2   |   1   |   4   |    0    
   4   |   3   |   2   |   2   |    1    
   1   |   3   |   4   |   2   |    2    
   3   |   3   |   1   |   2   |    3    
   4   |   5   |   4   |   3   |    4    
   2   |   1   |   1   |   5   |    5    
   6   |   4   |   3   |   2   |    6    
   4   |   7   |   8   |   3   |    7    
   1   |   9   |   8   |   3   |    8    
   3   |   2   |   6   |   5   |    9    
   2   |   9   |   1   |   5   |    10   
   3   |   4   |   1   |   6   |    11   
  None |  None |  None |  None |    12  
```
On the other hand, ```extend()``` and ```extend_col()``` were designed to add amount of records or amount of variables at the tail of each sheets in dataset. We added 2 new records at the same time, and especially the second record had miss values. After that, we used ```extend_col()``` function to extend the exist dataset.
```Python2
>>> example.extend([ 
	['A', 'A', 'A', 'A', 'A'],
	['C', 'C', 'C']])
>>> example.show(3)
sheet:sample
============
 A_col | B_col | C_col | D_col | New_col
-------+-------+-------+-------+---------
   3   |   2   |   1   |   4   |    0    
   4   |   3   |   2   |   2   |    1    
   1   |   3   |   4   |   2   |    2    
             .. Omit 9 Ln ..              
  None |  None |  None |  None |    12   
   A   |   A   |   A   |   A   |    A    
   C   |   C   |   C   |  None |   None  
>>> 
>>> example2 = datasets.example()
>>> example.extend_col(other=example2)
>>> example.show(4)
sheet:sample
============
 A_col | B_col | C_col | D_col | New_col | A_col_1 | B_col_1 | C_col_1 | D_col_1
-------+-------+-------+-------+---------+---------+---------+---------+---------
   3   |   2   |   1   |   4   |    0    |    3    |    2    |    1    |    4    
   4   |   3   |   2   |   2   |    1    |    4    |    3    |    2    |    2    
   1   |   3   |   4   |   2   |    2    |    1    |    3    |    4    |    2    
   3   |   3   |   1   |   2   |    3    |    3    |    3    |    1    |    2    
                                 .. Omit 7 Ln ..                                  
   3   |   4   |   1   |   6   |    11   |    3    |    4    |    1    |    6    
  None |  None |  None |  None |    12   |   None  |   None  |   None  |   None  
   A   |   A   |   A   |   A   |    A    |   None  |   None  |   None  |   None  
   C   |   C   |   C   |  None |   None  |   None  |   None  |   None  |   None  
```
 Next, let me introduce some functions for dropping the data. The normalist way is to use keyword ```del``` in Python. 
 ```Python3
 >>> del example['A_col', 'B_col', 'A_col_1', 'B_col_1', 'C_col_1']
 >>> example
sheet:sample
============
  C_col: <1, 2, 4, 1, 4, ... ,1, 1, None, A, C>
  D_col: <4, 2, 2, 2, 3, ... ,5, 6, None, A, None>
New_col: <0, 1, 2, 3, 4, ... ,10, 11, 12, A, None>
D_col_1: <4, 2, 2, 2, 3, ... ,5, 6, None, None, None>
>>> example[5]  # the 6th record in the dataset
[1, 5, 5, 5]
>>> del example[3, 4]
>>> example[5]
[8, 3, 7, 3]
>>>
 ```
Anyway, we have some other functions so that you not only can delete the data, but also catch the data. The system will return the data into a new dataset object.
```python3
>>> example.add(example.pop_col('C_col', 'D_col'))
>>> example
sheet:sample
============
New_col: <0, 1, 2, 4, 6, ... ,10, 11, 12, A, None>
D_col_1: <4, 2, 2, 3, 2, ... ,5, 6, None, None, None>

sheet:sample_1
==============
C_col: <4, 2, 2, 3, 2, ... ,5, 6, None, A, None>
D_col: <1, 2, 4, 4, 3, ... ,1, 1, None, A, C>
```
