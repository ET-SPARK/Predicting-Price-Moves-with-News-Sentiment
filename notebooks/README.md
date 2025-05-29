```
sudo ln -s /usr/lib/libta_lib.so /usr/lib/libta-lib.so && sudo ldconfig && pip install ta-lib

```

```
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && tar -xzf ta-lib-0.4.0-src.tar.gz && cd ta-lib && ./configure --prefix=/usr && make && sudo make install && cd .. && pip install ta-lib
```
