### Author info

Nom complet: RAZAFINTSIALONINA Ny Anjaratiana Mahefa <br/>
Référence étudiant: STD21065 <br/>
Email: hei.mahefa@gmail.com

### Project Details
note: **this is a multithread approach**

Directory Brute Forcing (also known as Directory Bursting or Directory
Bursting) is the process of trying to find hidden or unprotected directories and files on a computer.
find hidden or unprotected directories and files on a web server using a
server using a tool or script. It is often used in
web application security tests to identify potential vulnerabilities.
vulnerabilities.
You will create a tool that will accept a list of words and attempt to
discover the directories and files accessible on the target web server.

Translated with DeepL.com (free version)

### Run the code
* download or clone project
* install python from [download site](https://www.python.org/downloads/)
* install requirements
    ```shell
    pip install -r requirements.txt
    ```
* run main (optional parameters are put between parenthesis)
  ```shell
  python main.py api_base_url word_list_path (verbose)
  ``` 
  example: <br/>

Non Verbose:
* ```shell
    python main.py http://localhost:5000 ./static/dir_list.txt
  ```

* ```shell
    python main.py http://localhost:5000 ./static/dir_list.txt False
  ```
  
Verbose
* ```shell
    python main.py http://localhost:5000 ./static/dir_list.txt True
  ```
  
* ```shell
    python main.py http://localhost:5000 ./static/dir_list.txt "random_string"
  ```
  note: **any random_string will be evaluated to True by python**