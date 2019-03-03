First of all you have to make some necessary changes:
1)copy all the extension file in 'Hershey'sTextExtension' and paste it in the extensions folder of Inkscape (/usr/share/inkscape/extensions/) \n
2)make necessary changes for directory locations in the python program - textShorteningandPassing.py (the comments will guide you)

The workflow is pretty simple. 

1)Copy the all the text you need as centerline text into the 'stage-text input.txt'
  (Here you can make changes to accomodate the current set of character and decide page width)
2)Run the python program - textShorteningandPassing.py
3)In Inkscape open the Hershey's text extension and click apply.

The text will appear, you can resize,rotate or align and distribute it using the tools available.