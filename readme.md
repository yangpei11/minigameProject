# minigame后段协议
## 获取验证码
URL：/login/GetVerifyCode

+ 输入格式：

```json
{
	parma:"parma"  
}

parma
{
	phoneNumber:"110"  //手机号
}
```
___


+ 输出格式：

```json
{	
	code: 0, //0为成功，-1为错误
	msg: "手机号码为空" //反馈的消息
}
```
## 验证码登陆
URL：/login/Login

```json
{
	parma:"parma"  
}

parma
{
	
	phoneNumber:"110",  //手机号
	verifyCode: "973920", //验证码
	deviceID: "FE231Y" //设备ID
}
```
___


+ 输出格式：

```json
{	
	code: 0, //0为成功，-1为错误
	msg: "验证码错误" //反馈的消息
	data: "存档数据，当第一次登陆时为空"
	
}
```

## 存档
URL：/login/SaveData

```json
{
	parma:"parma"  
}

parma
{
	username"110",  //手机号或者设备ID
}
```
___


+ 输出格式：

```json
{	
	code: 0, //0为成功，-1为错误
	msg: "验证码错误" //反馈的消息
}
```