# Port checking for multiple servers/ports using Python


port_checker is a python based code and executable to check tcp port status for multiple servers and ports.


## Problem Statement
In my day to day work, I always need the check whether port access to a server is open on not. The usual way to do this is telnet. But many times, the list of server-port could gets huge, and checking each individually was taking a lot of effort. Hence this tool.


## Information

### This code is packaged into a .exe and hence can run standalone (check tools folder). 

#### Please verify if you have the following:

exe: port_checker.exe

file: input/in_server_port.csv


####  Example of input for your in_server_port.csv file. Please don't change the header name


|IP           |Port|
|-------------|----|
|10.158.102.36|3389|
|google.com   |8777|
|localhost    |80  |

####  Source Code available in src/ folder.
Please only use it if you want to change the script. The .exe is a standalone executable.

## Usage

1. Download the tools folders.

2. Change the input file as mentioned above.

3. Open command prompt and run the below command: 

```exe
port_checker.exe
```

## Output

|IP           |Port|Status                                                                                                                                                                                                                                                  |
|-------------|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|10.158.102.36|3389|Connection to 10.158.102.36 on port 3389 failed: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond|
|google.com   |8777|Connection to google.com on port 8777 failed: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond   |
|localhost    |80  |Connected to localhost on port 80                                                                                                                                                                                                                       |



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## References

[betrcode](https://gist.github.com/betrcode/0248f0fda894013382d7)

[ActiveState](http://code.activestate.com/recipes/577769-tcp-port-checker/)

## FAQ

1. Hope it is not a virus?

A: It is not. If you are worried about it, please download the src folder and use the python script. The exe is to make it easy for people without Python coding knowledge.

2. Why is the exe so big?

A: It has to do with how Python creates the package. Since the .exe should run standalone on your machine, python bundles all the dependencies into it. This includes modules like numpy, pandas, socket, etc. Hence the big file size.

3. This can be done using simple shell or bat command. Why to use Python for this?

A: There are better ways to do it ofcourse. But I am studying Python and hence this is just me solving my day-to-day problem using the language.

4. How does will it take to run?

A: Depending on the number of entries you have in the input file, tcp socket connection can take sometime. The code has timeout set (40 seconds) for each entries. Usually socket connection is established, failed long before it.

## Author

[SudhenduP](https://gist.github.com/SudhenduP)
