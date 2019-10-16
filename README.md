# infobeamerhosted

## Quick usage

```
pip install infobeamerhosted
python -m infobeamerhosted
```

## API

### Infobeamer()

```
from infobeamerhosted import *
InfobeamerAPI.KEY = 'your info beamer api key here'
foo = Infobeamer()
```

#### Properties

* ```.devices``` access all devices
* ```.setups``` access all devices
* ```.packages``` access all devices
* ```.assets``` access all devices
* ```.group : str``` Sets .group for all devices, setups, packages and assets.

### Common Properties for Devices(), Setups(), Packages(), Assets()

* ```.group```: the current group name used to select a subset of items. Set to '' (default) to disable.
* ```.all```: all items available.
* ```.selection```: items where the group name matches ```.group```. If this is not set the output is identitcal to ```.all```.

### Common Methods for Devices(), Setups, Packages(), Assets()

* ```getItems()```fetches all items from the Info-Beamer API. This is called upon initialization.

### Common Properties for Device(), Setup(), Package(), Asset()

* *Device()*: all properties from the [Device Object](https://info-beamer.com/doc/api#deviceobject)
* *Setup()*: all properties from the [Setup Info Object](https://info-beamer.com/doc/api#setupinfoobject)
* *Package()*: all properties from the [Package Object](https://info-beamer.com/doc/api#packageobject)
* *Asset()*: all properties from the [Package Object](https://info-beamer.com/doc/api#assetinfoobject)
* ```.group```: the current group name used to select a subset of items. Set to '' (default) to disable.

### Common Methods for Device(), Setup(), Package(), Asset()

* ```.inGroup(name: str) -> bool``` return True if the Item is in the group with the name *name*.
* ```.update([option: str, payload: dict]) -> bool```. Returns True if successfull, False otherwise.
* ```.delete() -> bool``` deletes the item. Returns True if successfull, False otherwise.

### InfobeamerAPI()

#### Static Properties

* ```InfobeamerAPI.KEY```holds our API key (required).
* ```InfobeamerAPI.USER```holds the username for the API. Default is set to ''.
* ```InfobeamerAPI.URL```holds the API URL. Default is set to https://info-beamer.com/api/v1/.

## Standalone use

```python -m infobeamerhosted```

### *API Settings*
* ```--api-key``` Key for info-beamer.com.
* ```--api-user``` User for info-beamer.com. Default is *empty*. (optional)
* ```--api-url``` Key from info-beamer.com. Default is **https://info-beamer.com/api/v1/** (optional)

You can also set environment variables for API_KEY, API_USER (optional), API_URL (optional).

```
export API_KEY = "infobeamer api key"
export API_USER = ""
export API_URL = "https://info-beamer.com/api/v1/"
```

## Ressources

* **API Documentation** [info-beamer.com/doc/api](https://info-beamer.com/doc/api)
