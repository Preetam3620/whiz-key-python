## File Strcuture

- In ```input.py```, log file of the product is to be given to the function ```uploadReport()```.

- ```infoUpload.py``` consists three functions: 
	- ```get_database()``` function is used to connect to the database
	- ```get_report()``` takes the log file of the report and parse it. It returns the data of all cycles and status of the product (pass or fail).
	- ```uploadReport()``` consists both these functions mentioned above. It takes the data and upload it to the database

## Log File Format

- There should be a key-value pair of the data, eg. Temp1, 75
- Status of the cycle, i.e. if cycle has failed or passed, should be mentioned in the same way. Status, Pass or Status, Fail
- End of each cycle should be given by 'END' keyword.
