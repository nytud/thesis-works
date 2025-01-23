# Launcher_emagyar_huspacy (magyar)
Ez a program az e-magyar és a HuSpacy nyelvi elemzőprogramokat keretbe foglaló alkalmazás. Célja, hogy az elemzők lefuttatását megkönnyítse: képes a megadott fájlokon (vagy akár mappák teljes tartalmán) lefuttatni csak az egyik, vagy akár mindkét elemzőt, az eredményeket fájlban eltárolja, és opcionálisan a terminálra is kiírja.

## Telepítés
A program több .py fájlból áll, mindegyik letöltése szükséges a megfelelő működéshez. Telepítésnél javasolt a fájlokat egyetlen mappába letölteni, a fájlok egymáshoz képest való elmozdítása más mappákba tönkreteheti a programot. Működéshez szükséges python csomagok:
* sys
* glob
* huspacy (hu_core_news_lg)
* docker
* tarfile

A program **Linux** környezetben működik, Python 3.8 verzióval kompatibilis. A Docker miatt Windowson nem ajánlott futtatni.

Futtatás előtt kialakítandó mappaszerkezet:

_programfájlok mappája_<br/>
&emsp;&emsp;&emsp;&emsp;|<br/>
&emsp;eredmenyek<br/>
&emsp;     /   &emsp;&emsp; &emsp;    \\<br/>
huspacy &emsp;    emagyar

```
mkdir eredmenyek
cd eredmenyek
mkdir huspacy
mkdir emagyar
cd ..
```

Az e-magyar Docker alkalmazásként működik, így az alkalmazás minden elemzés előtt (szövegenként) nyit egy saját konténert, majd törli az elemzés végeztével. Ezt érdemes figyelembe venni telepítéskor is, illetve a futás hirtelen megszakítása esetén is (pl. elképzelhető, hogy a létrehozott konténer nem törlődik).

## Használat

`python3 ./launcher.py input.txt -huspacy -emagyar -oute -outh`

A parancssori argumentumok sorrendje tetszőleges lehet.

input.txt helyett vagy mellett megadható tetszőleges számú, bármilyen reguláris kifejezés, amely txt fájlokat határoz meg (pl. \*.txt, ./masikmappa/\*.txt), azonban csak a txt kiterjesztésű fájlokat értelmezi a program inputfájlként! (Kiterjesztés nélküli fájlokat nem képes értelmezni.)

### Kapcsolók:

`-huspacy`: HuSpacy elemző lefuttatása (minden megadott txt fájlra)

`-emagyar`: e-magyar elemző lefuttatása (minden megadott txt fájlra)

`-outh`: Huspacy eredményének kiírása terminálra

`-oute`: e-magyar eredményének kiírása terminálra

A program az `-outh` és az `-oute` kapcsolóktól függetlenül minden esetben fájlba is kiírja az elemzés eredményét, amelyeket a megfelelő `eredmenyek/huspacy`, illetve`eredmenyek/emagyar` könyvtárakban tárol el `ana_huspacy_eredetifajlnev.txt`, illetve `ana_emagyar_eredetifajlnev.txt` néven.

### Futtatásra példák:

`python3 ./launcher.py input.txt -huspacy`: csak HuSpacy futtatása, az eredmények fájlba íródnak

`python3 ./launcher.py input.txt -emagyar`: csak e-magyar futtatása, az eredmények fájlba íródnak

`python3 ./launcher.py input.txt -huspacy -emagyar`: mindkét elemző futtatása, az eredmények fájlba íródnak

`python3 ./launcher.py input.txt -huspacy -emagyar -oute`: mindkét elemző futtatása, a HuSpacy eredményei fájlba íródnak, az e-magyar eredményei fájlba és terminálra is kiíródnak

## Megjegyzések
A program még tesztelés alatt áll, fejlesztési javaslatokat szívesen fogadok.




# Launcher_emagyar_huspacy (English)
This program is an interface program for the language processing systems HuSpacy and e-magyar. It aims to simplify the execution of the two mentioned toolchains: it is able to process given files (or even whole directories) with only one or even both systems, storing the results in files, and optionally writing the output to the CLI.

## Installation
The program consists of several .py file, all of them are required for the application to work. When installing, it is recommended to download all of the into a single directory, because moving the files into other directories separately can cause the application to fatally crush. Required Python packages:
* sys
* glob
* huspacy (hu_core_news_lg)
* docker
* tarfile

The program works in **Linux** environment, with Python version 3.8. Due to the usage of Docker, it is not recommended to use it on Windows.


The program requires the creation of the following structure of directories:

_directory of the downloaded program_<br/>
&emsp;&emsp;&emsp;&emsp;|<br/>
&emsp;eredmenyek<br/>
&emsp;     /   &emsp;&emsp; &emsp;    \\<br/>
huspacy &emsp;    emagyar

```
mkdir eredmenyek
cd eredmenyek
mkdir huspacy
mkdir emagyar
cd ..
```

E-magyar functions as a Docker application. As a result, the program opens and runs an own Docker container, which is removed after the processing is finished. This should be considered during the installation and in case of abrupt interruption of execution as well (e.g. it is possible for the container not to be deleted).

## Usage

`python3 ./launcher.py input.txt -huspacy -emagyar -oute -outh`

The order of the commandline arguments is arbitrary.

Instead of (or even beside) input.txt, the program accepts arbitrary amount of any kind of regular expression which defines txt files (e.g. \*.txt, ./masikmappa/\*.txt). However, only files with the extension of txt can be interpreted as input files. (Files without extension are also incomprehensible for the application.)


### Mandatory arguments:

`-huspacy`: execution of HuSpacy (for all given txt files)

`-emagyar`: execution of e-magyar (for all given txt files)

`-outh`: displaying the result of HuSpacy on the commandline interface

`-oute`: displaying the result of e-magyar on the commandline interface

Regardless of the `-outh` and `-oute` mandatory arguments, the application always writes the results into files, which are located either in the directory `eredmenyek/huspacy`, or `eredmenyek/emagyar`. The naming of the files follows the pattern of `ana_huspacy_originalnameoffile.txt`, or `ana_emagyar_originalnameoffile.txt`


### Examples for executing the program:

`python3 ./launcher.py input.txt -huspacy`: executing only HuSpacy, the results are written in file

`python3 ./launcher.py input.txt -emagyar`: executing only e-magyar, the results are written in file

`python3 ./launcher.py input.txt -huspacy -emagyar`: executing both processing systems, the results are written in file

`python3 ./launcher.py input.txt -huspacy -emagyar -oute`: executing both processing systems, the results of HuSpacy are written in file, the results of e-magyar are both written in file and displayed on the terminal

## Additional remarks
The program is still in the phase of testing. Any comments and advices are appreciated.



