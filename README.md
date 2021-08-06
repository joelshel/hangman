# hangman

Contributors:
* joelshel

# Description

Hangman game made in python and with the tkinter library. The game was tested in **Ubuntu 20.04.2 LTS** and with **Python 3.8.10**. Also the game depends of **PIL** (**Pillow**) library and it was tested with **8.3.1** version.

# How to play
If you don't have Python installed install it and next run `pip3 install -r requirements.txt` or `pip install -r requirements.txt`.
To play the game execute the **frontend.py** file. If you don't want an interface for the game execute the **backend.py** file instead.
If you don't want to install python you have a compiled version of the game in **comphangman/dist** dir but is only available for ubuntu.
You still have the file used to compile the game if you want to do it by yourself. It was used pyinstaller to compile it with version 4.5. To compile the game by yourself run<br>
```
cd
cd my_dir/hangman
./comphangman.sh
cp img/ src/ -r comphangman/dist/
```
on ubuntu. Don't forget to install pyinstaller before execute this. 
Execute **my_dir/hangman/comphangman/dist/hangman** for play the compiled version.
# References
The backend.py file is based in a [vídeo](https://www.youtube.com/watch?v=8ext9G7xspg&t=1465s) from [freeCodeCamp.org](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) and you can find a similar code in hangman.py file.<br>
The words used for the game can be found [here](https://github.com/Xethron/Hangman/blob/master/words.txt).
