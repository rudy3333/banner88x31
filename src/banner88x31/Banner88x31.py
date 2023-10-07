import requests
import bs4
from PIL import Image
from urllib.request import urlopen


class Banner88x31:
    """
    Create an instance of the `Banner88x31` class.
    ```python
    scraper = Banner88x31()
    ```
    | Methods            | Details                                                  |
    | ------------------ | -------------------------------------------------------- |
    | `get_all()`        | Returns the list of all available 88x31 banners          |
    """

    def __init__(self):
        self.urls_to_scrape = [
            "https://cyber.dabamos.de/88x31/index.html",
            "https://cyber.dabamos.de/88x31/index2.html",
            "https://cyber.dabamos.de/88x31/index3.html",
            "https://cyber.dabamos.de/88x31/index4.html",
            "https://cyber.dabamos.de/88x31/index5.html",
        ]

    def get_all(self, url=True):
        """
        Returns the list of all available 88x31 banners
        Class: Banner88x31

        | Properties  | Details                                                                  |
        | ----------- | ------------------------------------------------------------------------ |
        | `url`       | If False, returns only tags. Defaults to `True. Takes `False` or `True`  |
        
        Example:
        ```python
        banners = Banner88x31()
        result = banners.get_all()
        ```

        Returns:
        ```json
        ["https://cyber.dabamos.de/88x31/000010.gif", "https://cyber.dabamos.de/88x31/007button.gif", "..."]
        ```
        """
        
        img_alt = []
        for url in self.urls_to_scrape:
            try:
                response = requests.get(url)
                response.raise_for_status()
                source = response.content
                soup = bs4.BeautifulSoup(source, "lxml")
                for img_tag in soup.find_all("img"):
                    if url == True:
                        img_alt.append(
                            "https://cyber.dabamos.de/88x31/" + img_tag.get("alt") + ".gif"
                        )
                    else:
                        img_alt.append(img_tag.get("alt"))
                return img_alt
            except:
                return None

    def get_wh(self, tag):
        """
        Returns the width and height of the given tag
        Class: Banner88x31

        | Properties  | Details                                                                  |
        | ----------- | ------------------------------------------------------------------------ |
        | `tag`       | Tag of requested image. Takes a string.                                  |
        
        Example:
        ```python
        banners = Banner88x31()
        wh = banners.get_wh("amd_powered")
        ```

        Returns:
        ```json
        (85, 30)```
        """
        
        url = "https://cyber.dabamos.de/88x31/" + tag + ".gif"
        try:
            img = Image.open(urlopen(url))
            size = img.size
            return size
        except:
            return None
