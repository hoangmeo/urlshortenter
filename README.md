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
```bash
curl -H "Content-Type: application/json" -X POST -d '{"url":"http://anninhthudo.vn/quan-su/163.antd"}' http://localhost:5000/
```
