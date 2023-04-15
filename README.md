# dorksearch

Google dorklarını kullanarak arama yapmaya yarayan bir araçtır.

## Gereksinimler

dorksearch aşağıdaki kütüphaneleri kullanır.

* Colorama
* Requests
* BeautifulSoup4

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/dorksearch.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

```bash
usage: dorksearch.py [-h] [--site SITE] [--ext EXT] [--intitle INTITLE] [--cache CACHE] [--related RELATED]
                     [--inpostauthor INPOSTAUTHOR] [--inanchor INANCHOR] [--intext INTEXT] [--inurl INURL]
                     [--link LINK] [--out OUT]

options:
  -h, --help            show this help message and exit
  --site SITE
  --ext EXT
  --intitle INTITLE
  --cache CACHE
  --related RELATED
  --inpostauthor INPOSTAUTHOR
  --inanchor INANCHOR
  --intext INTEXT
  --inurl INURL
  --link LINK
  --out OUT

```

## Örnekler

```python
python3 dorksearch.py --site example --intitle "admin"
python3 dorksearch.py --site example --inurl "Python" --ext "pdf"
```
