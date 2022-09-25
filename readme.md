# 🏫我应该在校园

##  🔔使用须知

本仓库发布的文章及代码等全部内容，仅用于测试和学习研究，禁止用于商业用途，作者不保证其准确性、完整性以及合法性，请使用者依个人情况自行合理判断。

❗ 因私自用于商业或非法用途，所产生的后果由使用者自负，均与作者无关。

❗ 本仓库项目所有文章及资源，除引用第三方内容外，禁止任何自媒体进行任何形式的转载、发布。

❗ 若任何单位或个人认为该仓库内容可能存在侵犯其权力的行为，应及时通知作者并提供身份证明、所有权证明，作者在收到之后将在第一时间删除相关内容。

❗ 疫情反复均属未知，请保护好自己，健康生活，认真打卡。

⭕ 无论您以任何途径、任何方式，一旦您一经下载或使用本仓库内容，即代表您 ✅`已接受` 以上声明，请知悉。

## 📚使用教程

### 打卡账号密码

##### 1.打开我在校园，进入设置。

<img src="https://hexo-1304618721.cos.ap-chengdu.myqcloud.com/images/post/390B39EBEF36359EF2DD8DAC3266CB74.jpg" alt="img" style="zoom: 20%;" />

##### 2.修改密码

<img src="https://hexo-1304618721.cos.ap-chengdu.myqcloud.com/images/post/C94CE009C4DB20E537B3DAF5C93DC6DB.jpg" alt="img" style="zoom:20%;" />

##### 3.原密码可以随便输入，记得改两次密码，也就是第一次修改以后，再用这个密码修改一遍，可以一模一样。

<img src="https://hexo-1304618721.cos.ap-chengdu.myqcloud.com/images/post/A5F8F974FFE7CE7BFA18B8109E4418C9.jpg" alt="img" style="zoom:20%;" />

##### 4.点击头像查看个人信息就可以看到账号了

<img src="https://hexo-1304618721.cos.ap-chengdu.myqcloud.com/images/post/A9F3846A763565D0E5DBFDA65DB5CF1A.jpg" alt="img" style="zoom:25%;" />







### 代码入口

` WZXY.PY` 文件便是主入口，我已经写好了调用例子，你可以直接使用来调用打卡接口。

```python
if __name__ == '__main__':
    username="泽塔",
    password='殴斯',
    location='M78星云'
    api = WAXY(username, password, location=location)
    api.login() #首先登录
    api.getSchoolinfo() #获取batchID
    res = api.Post() #打卡
```

## ❗重要事项

- **账号密码登录**，代码有时候会报密码错误，如果出现错误，可以做一次修改密码操作，新密码与旧密码可以一样，当然，如果还是报错，**继续修改密码**，（新旧密码可以相同，这里没有检测机制 ，所以只改密码，不用改代码里的密码），直到成功为止。

- 如果**无特殊事情**尽量**不要打开**我在校园，如果打开**发现需要重新登录**，之前的密码**就是作废**了，需要**重新修改**密码**修改成一模一样**的。