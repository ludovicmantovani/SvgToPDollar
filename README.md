# SvgToPDollar

## Install
* download and install python 3 on your computer : [https://www.python.org/downloads/](https://www.python.org/downloads/)
* clone (or download) this repo
```bash
> git clone https://github.com/ludovicmantovani/SvgToPDollar.git
```
* go inside the folder and install python requirements
```bash
> cd SvgToPDollar
> pip3 install -r requirements.txt
```
## Usage
```bash
usage: svgToPDollar.py [-h] svg_file

positional arguments:
  svg_file    SVG input file

optional arguments:
  -h, --help  show this help message and exit
```
### Example
We want to convert [etoile.svg](./input/etoile.svg) file to PDollar XML file
```bash
> cd SvgToPDollar/src
> ls
svgToPDollar.py
> python3 svgToPDollar.py ../input/etoile.svg
> ls
etoile.xml  svgToPDollar.py
```
etoile.xml (generated file):
```xml
<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<Gesture Name="etoile">
  <Stroke>
    <Point X="266.07" Y="313.76" T="0" Pressure="0"/>
    <Point X="164.78" Y="260.07" T="0" Pressure="0"/>
    <Point X="63.14" Y="313.08" T="0" Pressure="0"/>
    <Point X="82.89" Y="200.16" T="0" Pressure="0"/>
    <Point X="1.07" Y="119.86" T="0" Pressure="0"/>
    <Point X="114.57" Y="103.76" T="0" Pressure="0"/>
    <Point X="165.65" Y="1.13" T="0" Pressure="0"/>
    <Point X="216.04" Y="104.1" T="0" Pressure="0"/>
    <Point X="329.43" Y="120.96" T="0" Pressure="0"/>
    <Point X="247.07" Y="200.71" T="0" Pressure="0"/>
    <Point X="266.07" Y="313.76" T="0" Pressure="0"/>
  </Stroke>
</Gesture>
```
