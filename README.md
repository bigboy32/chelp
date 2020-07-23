# chelp
A Quick Script to help you search a question on stackoverflow from cmd

## INSTALLATION FOR LINUX

```bash
git clone https://www.github.com/bigboy32/chelp.git
cd chelp
# install python3 with yor package manager
sudo cp chelp /usr/bin
```

and then....

```bash
chelp
```

It will redirect you to an empty stackoverflow site.

## INSTALATION FOR WINDOWS AND MAC

Ok this process isn't that much more complicated.

First :

- Option 1 Instal git and git clone it
 
 OR
 
 - Option 2 clone it from github by clicking the clone button
 
 THEN:
 
- If you choose option 2: Unzip it and open terminal at that location
- For the people with option 1: than just go in tho the chelp folder.

THEN:

First install python and put it in to the path, then:
```bash
pip install pyinstaller
python -m pyinstaller chelp.py --onefile 

# If you encounter an error with python -m pytinstaller : use : pyinstaller --onefile chelp.py
```

And then copy it in to the path


## Usage:

in terminal/cmd: ```bash
chelp YOUR ERROR IN ONE LINE
```
Enjoy!
