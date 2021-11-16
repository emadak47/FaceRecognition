# Face Recognition

Face recognition using Python and MySQL, using Flask as a web framework

*******

## Usage

### Source files
1. Download and unzip the source files
2. Launch terminal and change directory into the new folder

### MySQL Database setup
3. Access mySQL database locally (using `mysql -u root -p`)
4. Enter the password
5. Enter the following commands:
```
CREATE DATABASE facerecognition;
USE facerecognition;
source facerecognition.sql
```
### .env File
5. Duplicate the .env.template file
6. Enter this new file and fill in the all of the details. 

Note: `MYSQL_HOST` is likely to be `'localhost'` and `MYSQL_DB` must be `'facerecognition'`

7. Rename this file to `.env`

### Environment
8. Enter the following commands. Note that the `x` must be replaced in `python=3.x`
```
conda create -n face python=3.x
conda activate face
pip install -r requirements.txt
```
### Run
9. Enter `python backend.py`


