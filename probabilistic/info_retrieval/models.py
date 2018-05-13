from django.db import models
from django.utils import timezone


import codecs
import pytesseract
from PIL import Image
from tika import parser
from bs4 import BeautifulSoup

image_types = {'png', 'jpg', 'jpeg', 'bmp'}
doc_types = {'doc', 'docx', 'pdf'}
web_types = {'html', 'htm'}


def extension(path):
    """Returns the extension of a filename"""
    tmp = str(path).split('.')
    ext = tmp[-1]
    return ext


def get_html(path):
    """Get all the HTML content"""
    html_text = BeautifulSoup(codecs.open(path, 'r').read(), 'lxml').get_text()
    return html_text


def get_image(path):
    """ example string = ocrInFile('download.jpg')"""
    img_text = pytesseract.image_to_string(Image.open(path), lang='eng')
    return img_text


def get_any(path):
    raw = parser.from_file(str(path))
    content = raw['content']
    return content

def get_content(file_path):
    ext = extension(str(file_path))

    if ext in image_types:
        content = get_image(file_path)
    elif ext in doc_types:
        content = get_any(file_path)
    elif ext in web_types:
        content = get_html(file_path)
    else:
        print('format not supported')
        content = 'null'
    return content

class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='DOCS/')
    content = 'bubu'

    def publish(self):
        self.published_date = timezone.now()
        #self.title = 'lololololo'
        self.save()
