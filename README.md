<div align="center">
  <a href="https://github.com/lclty/biliTickerBuy_Dynamic_Renewable" target="_blank">
    <img width="160" src="assets/icon.ico" alt="logo">
  </a>
  <h2 id="koishi">biliTickerBuy</h1>

<p>
  <!-- GitHub Downloads -->
  <a href="https://github.com/lclty/biliTickerBuy_Dynamic_Renewable/releases">
    <img src="https://img.shields.io/github/downloads/lclty/biliTickerBuy_Dynamic_Renewable/total" alt="GitHub all releases">
  </a>
  <!-- GitHub Release Version -->
  <a href="https://github.com/lclty/biliTickerBuy_Dynamic_Renewable/releases">
    <img src="https://img.shields.io/github/v/release/lclty/biliTickerBuy_Dynamic_Renewable" alt="GitHub release (with filter)">
  </a>
  <!-- GitHub Issues -->
  <a href="https://github.com/lclty/biliTickerBuy_Dynamic_Renewable/issues">
    <img src="https://img.shields.io/github/issues/lclty/biliTickerBuy_Dynamic_Renewable" alt="GitHub issues">
  </a>
  <!-- GitHub Stars -->
  <a href="https://github.com/lclty/biliTickerBuy_Dynamic_Renewable/stargazers">
    <img src="https://img.shields.io/github/stars/lclty/biliTickerBuy_Dynamic_Renewable" alt="GitHub Repo stars">
  </a>
</p>

这是一个开源免费，简单易用的B站会员购辅助工具
</div>






## 💻 快速安装


尚在完善中，不提供快速安装方式。

## 源代码构建

开发者使用的 Python 版本为 Python 3.11.9

    git clone https://github.com/lclty/biliTickerBuy_Dynamic_Renewable
    cd ./biliTickerBuy_Dynamic_Renewable
    python -m venv ./venv_py3119

    # Linux
    ./venv_py319/bin/activate
    # Windows
    ./venv_py319/Scripts/activate

    pip install -r ./requirements

    #对于 Windows OR macOS, Chrome
    playwright install chrome
    #对于 Windows OR macOS, Edge
    playwright install msedge
    #对于 Linux, 请自行采用其它方式获取 Cookie

    python ./main.py

## ❗ 项目问题

程序使用问题： [点此链接前往discussions](https://github.com/lclty/biliTickerBuy_Dynamic_Renewable/discussions)

反馈程序BUG或者提新功能建议： [点此链接向项目提出反馈BUG](https://github.com/lclty/biliTickerBuy_Dynamic_Renewable/issues/new/choose)


## 📩 免责声明

本项目遵循 MIT License 许可协议，仅供个人学习与研究使用。请勿将本项目用于任何商业牟利行为，亦严禁用于任何形式的代抢、违法行为或违反相关平台规则的用途。由此产生的一切后果均由使用者自行承担，与本人无关。

若您 fork 或使用本项目，请务必遵守相关法律法规与目标平台规则。

## 💡 关于访问频率与并发控制
本项目在设计时严格遵循「非侵入式」原则，避免对目标服务器（如 Bilibili）造成任何干扰。

所有网络请求的时间间隔均由用户自行配置，默认值模拟正常用户的手动操作速度。程序默认单线程运行，无并发任务。遇到请求失败时，程序会进行有限次数的重试，并在重试之间加入适当的延时，避免形成高频打点。项目完全依赖平台公开接口及网页结构，不含风控规避、API劫持等破坏性手段。

## 🛡️ 平台尊重声明

本程序设计时已尽可能控制请求频率，避免对 Bilibili 服务器造成任何明显负载或影响。项目仅作为学习用途，不具备大规模、高并发的能力，亦无任何恶意行为或干扰服务的企图。

如本项目中存在侵犯 Bilibili 公司合法权益的内容，请通过邮箱 [1055069518@qq.com](mailto:1055069518@qq.com) 与我联系，我将第一时间下架相关内容并删除本仓库。对此造成的不便，我深表歉意，感谢您的理解与包容。


## ⭐️ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=lclty/biliTickerBuy_Dynamic_Renewable&type=Date)](https://www.star-history.com/#lclty/biliTickerBuy_Dynamic_Renewable&Date)

