# URL shortener
You know, like bit.ly.
Let's call it lin.ks!

## Requirements
* docker

### Install from source

```bash
$ git clone https://gitlab.com/hoangn.meo/url-shortenter.git <my-project-name>
$ cd <my-project-name>
$ docker-compose up
```

#### How to use
POST http://localhost:5000/ HTTP/1.1
content-type: application/json

{  
  "url":"http://anninhthudo.vn/kinh-doanh/gia-xang-tang-manh-sau-nhieu-thang-on-dinh-len-gan-19000-dong-lit/763401.antd"
}