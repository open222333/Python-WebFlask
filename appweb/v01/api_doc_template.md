###  Get Token

**get authorization token**

**Request**

* Endpoint: ```GET /v1/token/<device_id>```
* Content-Type: ```application/json```

| Parameter | Type | Default/Required | Description |
|:---------:|:----:|:----------------:|-------------|
| ```device_id``` | ```String``` | Require | device unique id |
| ```key``` | ```String``` | Require | verified key |
| ```platform``` | ```android or ios``` | Require | device platform |
| ```model``` | ```String``` | Require | device model |
 ```
 key = sha256("template"+device_id+"template")
 ```
**Response**

| Parameter | Type | Description |
|:---------:|:----:|-------------|
| ```token``` | ```String``` |[JSON WEB TOKEN](https://jwt.io/) Authorization token(please bring token in header Authorization: Bearer) |



**Example**
```
curl -v "https://{domain_name}/v1/token/device_id?model=htc_a9u&platform=android&key=a420889cae3065843767dbff243693d615d74f8880ee3cad4e7c4c0b2c8baaf7"
HTTP/1.1 200 OK
Date: Mon, 08 Aug 2016 08:46:41 GMT
Content-Type: application/json
Content-Length: 177
Connection: keep-alive

Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE0NzA2NDYwMDEsImRldmljZV9pZCI6ImRldmljZV9pZCIsImF1ZCI6ImF2bmlnaHQifQ.734VfikSiwB26F84cjezniEcE5-jeR5VQ-CfmDYHkIE
```
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE0NzA2NDYwMDEsImRldmljZV9pZCI6ImRldmljZV9pZCIsImF1ZCI6ImF2bmlnaHQifQ.734VfikSiwB26F84cjezniEcE5-jeR5VQ-CfmDYHkIE"
}
```