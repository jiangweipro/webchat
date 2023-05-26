# 简介

**模型：**

 - [x] [ChatGPT (gpt-3.5)](https://github.com/zhayujie/bot-on-anything#1-chatgpt)

**应用：**

 
 - [x] [Web](https://github.com/zhayujie/bot-on-anything#9web)

# 快速开始

## 一、准备

### 1.运行环境

支持 Linux、MacOS、Windows 系统（Linux服务器上可长期运行)。同时需安装 Python，建议Python版本在 3.7.1~3.10 之间。

### 2.配置说明

核心配置文件为 `config.json`，在项目中提供了模板文件 `config-template.json` ，可以从模板复制生成最终生效的 `config.json` 文件：

```bash
cp config-template.json config.json
```

每一个模型和应用都有自己的配置块，最终组成完整的配置文件，整体结构如下：

```bash
{
  "model": {
    "type" : "chatgpt",             # 选用的算法模型
    "openai": {
      # openAI配置
    }
  },
  "channel": {
    "type": "wechat_mp",            # 需要接入的应用 
    "wechat": {
        # 个人微信配置
    },
    "wechat_mp": {
        # 公众号配置
    }
  }
}
```
配置文件在最外层分成 `model` 和 `channel` 两部分，model部分为模型配置，其中的 `type` 指定了选用哪个模型；channel部分包含了应用渠道的配置，`type` 字段指定了接入哪个应用。

在使用时只需要更改 model 和 channel 配置块下的 type 字段，即可在任意模型和应用间完成切换，连接不同的通路。下面将依次介绍各个 模型 及 应用 的配置和运行过程。

## 二、选择模型

### 1. ChatGPT

使用的模型是 `gpt-3.5-turbo`，详情参考[官方文档](https://platform.openai.com/docs/guides/chat)。

#### (1) 注册 OpenAI 账号

前往 [OpenAI注册页面](https://beta.openai.com/signup) 创建账号，参考这篇 [教程](https://www.cnblogs.com/damugua/p/16969508.html) 可以通过虚拟手机号来接收验证码。创建完账号则前往 [API管理页面](https://beta.openai.com/account/api-keys) 创建一个 API Key 并保存下来，后面需要在项目中配置这个key。

> 项目中使用的对话模型是 davinci，计费方式是约每 750 字 (包含请求和回复) 消耗 $0.02，图片生成是每张消耗 $0.016，账号创建有免费的 $18 额度，使用完可以更换邮箱重新注册。

#### (2) 安装依赖

```bash
pip install openai
```
> 注： openai版本需要`0.27.0`以上。如果安装失败可先升级pip，`pip3 install --upgrade pip`


#### (3) 配置项说明

```bash
{
  "model": {
    "type" : "chatgpt",
   
    "openai": {
      "api_key": "YOUR API KEY",
      "model": "gpt-3.5-turbo",                         # 模型名称
      "proxy": "http://127.0.0.1:7890",
      "character_desc": "你是ChatGPT, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。"
    }
}
```
 + `api_key`: 填入上面注册账号时创建的 `OpenAI API KEY`
 + `model`: 模型名称，目前支持填入 `gpt-3.5-turbo`, `gpt-4`, `gpt-4-32k`  (其中gpt-4 api暂未开放)
 + `proxy`: 代理客户端的地址，详情参考  [#56](https://github.com/zhayujie/bot-on-anything/issues/56)
 + `character_desc`: 配置中保存着你对chatgpt说的一段话，他会记住这段话并作为他的设定，你可以为他定制任何人格
 + `max_history_num`[optional]: 对话最大记忆长度，超过该长度则清理前面的记忆。


## 三、应用

### Web

**Contributor:** [RegimenArsenic](https://github.com/RegimenArsenic)

**依赖**

```bash
pip install PyJWT flask
```

**配置**

```bash
"channel": {
    "type": "http",
    "http": {
      "http_auth_secret_key": "6d25a684-9558-11e9-aa94-efccd7a0659b",    //jwt认证秘钥
      "http_auth_password": "6.67428e-11",        //认证密码,仅仅只是自用,最初步的防御别人扫描端口后DDOS浪费tokens
      "port": "80"       //端口
    }
  }
```

本地运行：`python3 app.py`运行后访问 `http://127.0.0.1:80`

服务器运行：部署后访问 `http://公网域名或IP:端口`


