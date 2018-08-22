DaPy - Enjoy the Tour in Data Mining
====
![](https://img.shields.io/badge/Version-1.3.3-green.svg)  ![](https://img.shields.io/badge/Download-PyPi-green.svg)  ![](https://img.shields.io/badge/License-GNU-blue.svg)  

![](https://github.com/JacksonWuxs/DaPy/blob/master/doc/material/logo.bmp)

As a data analysis and processing library based on the original data structures in Python, **DaPy** is not only committed to save the time of data scientists and improve the efficiency of research, but also try it best to offer you a new experience in data science.

[Installation](#installation) | [Features](#features) | [Quick Start](https://github.com/JacksonWuxs/DaPy/blob/master/Guide%20Book/English/Quick%20Start.md ) | [To Do List](#todo) | [Version Log](#version-log) | [License](#license) | [Guide Book](https://github.com/JacksonWuxs/DaPy/tree/master/Guide%20Book) | [中文版](https://github.com/JacksonWuxs/DaPy/blob/master/README_Chinese.md)

## Installation
The latest version 1.4.1 had been upload to PyPi.
```
pip install DaPy
```
Updating your last version to 1.4.1 with PyPi as follow.
```
pip install -U DaPy
```

## Features
**Convinience** and **efficiency** are the cornerstone of DaPy. 
Since the very beginning, we have designed DaPy to Python's 
native data structures as much as possible and we try to make 
it supports more Python syntax habits. Therefore you can 
adapt to DaPy quickly, if you imagine you are opearting an Excel table.
In addition, we do our best to simplify
the formulas or mathematical models in it, in order to let you 
implement your ideas fluently.  

* Here are just a few of the things that DaPy does well:  
	- [Efficiently manage diverse data with clearly perceiving approach](https://github.com/JacksonWuxs/DaPy/blob/master/Guide%20Book/English/Features.md#visibly-manage-diverse-data)
	- [Quick insert and delete a mount of new records or new variables]
	- [Make it easy to access a part of your dataset, not only by index or variable names, but also by specefic conditions]
	- [Functional IO tools for loading data from CSV files, Excel files, database and even SPSS files]
	- [Sort your records by multiple conditions]
	- [Fast verify your ideas with the built-in analysis models (e.g. `ANOVA`, `MLP`, `Linear Regression`)]
	- A variety of ways to help you easily perceive your dataset.
  
Even if it uses Python original data structures, 
DaPy still has efficiency comparable to some libraries which was wrote by C.
We have tested DaPy on the platform with
Intel i7-6560U while the Python version is 2.7.13-64Bit. The [dataset](http://www.wuxsweb.cn/Library/DaPy&Test_data/read_csv.csv)
has more than 4.5 million records and total size is 
240.2 MB. 

<table>
<tr>
	<td>Result of Testing</td>
	<td>DaPy</td>
	<td>Pandas</td>
	<td>Numpy</td> 
</tr>
<tr>
	<td>Loading Time</td>
	<td>29.3s (2.4x)</td>
	<td>12.3s (1.0x)</td>
	<td>169.0s (13.7x)</td>
</tr>
<tr>
	<td>Traverse Time</td>
	<td>0.34s (1.6x)</td>
	<td>3.10s (14.8x)</td>
	<td>0.21s (1.0x)</td>
</tr>
<tr>
	<td>Sort Time</td>
	<td>1.41s (1.65x)</td>
	<td>0.86s (1.0x)</td>
	<td>5.37s (10.1x)</td>
	</tr>
<tr>
	<td>Total Spent</td>
	<td>31.1s (1.9x)</td>
	<td>16.3s (1.0x)</td>
	<td>174.6s (10.0x)</td>
	</tr>
<tr>
	<td>Version</td>
	<td>1.3.3</td>
	<td>0.22.0</td>
	<td>1.14.0</td>
	</tr>
</table>  


## TODO  
* Descriptive Statistics
* Inferential statistics
	- Time Sequence
* Feature Engineering
	- PCA (Principal Component Analysis)
	- LDA (Linear Discriminant Analysis)
	- MIC (Maximal information coefficient)
* Algorithm
	- SVM ( Support Vector Machine)
	- K-Means
	- Lasso Regression  
	- Bayes Classification
	
If you want to follow up the latest developments, you can visit [here](https://www.teambition.com/project/5b1b7bd40b6c410019df8c41/tasks/scrum/5b1b7bd51e4661001838eb10).

## Version-Log
* V1.4.1 (2018-08-19)
	- Added `replace()` function for high-speed transering your data;
	- Fixed some bugs;
	- Optimized the speed in reading .csv file;
	- Refactored the DaPy.machine_learn.MLP, which can be form with any layers with any active functions or any cells now;
	- Refactored the DaPy.Frame and DaPy.SeriesSet in order to improve the efficiency;
	- Supported to initialize Pandas and Numpy data structures;
* V1.3.3 (2018-06-20)
	- Added more supported external data types: Excel, SPSS, SQLite3, CSV;
	- Added `Linear Regression` and `ANOVA` to DaPy.Mathematical_statistics;
	- Added `DaPy.io.encode()` for better adepting to Chinese;
	- Optimized the presentations of SeriesSet and Frame in a more beautiful way;
	- Optimized the DaPy.Matrix so that the speed in calculating is two times faster;
	- Replaced read_col(), read_frame(), read_matrix() by read();
	- Refactored the DaPy.DataSet, which can manage multiple sheets at the same time;
	- Refactored the DaPy.Frame and DaPy.SeriesSet, delete the attribute limitation of types;
	- Removed DaPy.Table;
* V1.3.2 (2018-04-26)
	- Added more useful functions for DaPy.DataSet;
	- Added a new data structure called DaPy.Matrix;
	- Added some mathematic formulas (e.g. corr, dot, exp);
	- Added `Multi-Layers Perceptrons` to DaPy.machine_learn;
	- Added some standard dataset;
	- Optimized the loading function significantly;
* V1.3.1 (2018-03-19)
	- Added the function which supports to save data as a csv file;
	- Fixed some bugs in the loading data function;
* V1.2.5 (2018-03-15)
	- First public version of DaPy!

## License
Copyright (C) 2018 Xuansheng Wu
<br>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.</br>
<br>
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.</br>
<br>
You should have received a copy of the GNU General Public License
along with this program.  If not, see https:\\www.gnu.org\licenses.# datapy
A light Python library for data processing and analysing.</br>
