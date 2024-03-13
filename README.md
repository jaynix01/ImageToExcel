# ImageToExcel
ImageToExcel is a project designed to extract text from photos within a specified directory. It utilizes regular expressions to define patterns for text extraction, storing the results in an Excel spreadsheet. Users have the flexibility to customize the extraction pattern according to their specific needs or opt to save complete text excerpts from each photo. The accuracy of text extraction is dependent on the quality of the input images.


# Features
+ Scans text from JPEG and PNG photos within a chosen directory.
+ Employs regular expressions to define text extraction patterns.
+ Stores extracted text in an Excel spreadsheet.
+ Users can customize extraction patterns or opt for complete text extraction.
+ Accuracy of text extraction is dependent on image quality.

# Requirements
+ Python 3.x
+ EasyOCR
+ XlsxWriter

# Customization
```python
def text_detect(file_path):
    reader = easyocr.Reader(['en']) # Specify the language of the text in the photo.
    detected_text = reader.readtext(file_path, detail=0, paragraph=True) # The variable detected_text holds the entire text extracted from the photo
```
```python
def item_detect(detect_text):
'''
Is responsible for defining the pattern to search for specific text in the photo.
Users can modify this function according to their requirements.
The project provides an example of working with a specific photo.
'''
```

# Usage
+ Customize the text extraction pattern according to your needs and the content of your photos. (I used ***regular expressions***, but you can also use ***slices*** if preferred.)
+ Run the script by executing 'python main.py' while in the directory.
+ Specify the path to the folder containing the photos.
+ The script will process all photos in the folder.
+ The results will be saved in 'result.xlsx'.

### Please note that the script only works with JPEG and PNG files.




  
