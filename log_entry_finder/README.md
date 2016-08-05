## Requirements:
Python 2.x
## How to use
Download the script locally and run as follow:

```python log_entry_finder.py /YOUR/LOGS/FOLDER/ StringTosearchfor```

## Usage examples:
### search for an ip address in several log files
```python log_entry_finder.py /var/logs/ 192.168.1.4```

### search for a web page in webserver logs
```python log_entry_finder.py /var/logs/ contact.html```

## Matching results
The output with matching results in written to a csv file in the current directory, where the python scrit is ran from. The output file name is ```output_matches.csv```


