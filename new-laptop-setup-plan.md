# 新电脑初始化规划

> 目标设备：机械革命蛟龙 16 Pro  
> 目标配置：Windows 11 + RTX 5070 + 24GB（12GB x 2）  
> 执行原则：新机先只装 Codex，再由 Codex 按本文件完成后续安装和配置。  
> 版本：v2，包含完整备份、驱动、软件分层、安全加固、回滚与验收协议。

---

## 零、强制执行总则（最高优先级）

以下规则优先于本文件其它所有内容，每一条都必须严格执行，不允许跳过。

1. 出现任何问题、报错、弹窗、异常、不确定项，立即停止当前任务，先向用户询问是否继续，绝不自动绕过。
2. 只从官方来源下载：软件官网、Microsoft Store、winget 官方仓库、GitHub 官方 Release。禁止第三方下载站。
3. 安装前必须完成安全检查：
   - 校验安装包发布者签名：`Get-AuthenticodeSignature`
   - 用 Windows Defender 对安装包完整扫描
   - 对高风险或非官方来源的包，先提交 VirusTotal 检查，有可疑结果就停止并询问
4. 任何带捆绑、推广、主页锁定、开机自启推广的安装器一律禁止。只能使用“自定义安装”，逐个取消所有额外项。
5. 360、小鸟壁纸、2345、金山毒霸、管家类全家桶等软件一律不安装、不自动下载、不推荐。
6. 所有下载统一放到 `C:\CodexSetup\Downloads`；安装记录写入 `C:\CodexSetup\manifest.csv`；日志写入 `C:\CodexSetup\Logs`。
7. 每执行一批安装前创建系统还原点；每个软件记录来源、版本、签名结果、病毒扫描结果、安装时间、安装路径、卸载方式。
8. 用户可以随时要求“一键清除”：
   - 立即停止所有安装任务
   - 按 manifest 反向卸载本次会话安装的软件
   - 删除 `C:\CodexSetup`
   - 清理 `%TEMP%`、winget 缓存、安装目录、AppData 残留和注册表卸载项
   - 如果用户要求彻底还原，使用安装前创建的系统还原点或整机映像还原
9. “干净、无残留”不是口号，而是以“可验证、可回滚、可审计”的方式执行。如果某一步无法保证干净回滚，必须先告诉用户风险并等待决定。
10. 每个操作前先说明“要做什么、为什么做、完成后如何清除”；用户没有确认前不执行。

---

## 一、换机前备份与数据清单（旧电脑上做）

### 1.1 必须备份的数据

- [ ] 学习项目：`Documents\New project`，确认 `.git` 目录一起带走。
- [ ] 桌面、文档、下载、图片、视频、音乐。
- [ ] 浏览器收藏夹、书签、密码和登录态，建议导出为文件。
- [ ] 微信 / QQ 聊天记录和文件目录。
- [ ] 输入法个人词库。
- [ ] Steam、WeGame、米哈游启动器等游戏存档和截图。
- [ ] Wallpaper Engine 订阅和创意工坊内容。
- [ ] 代理工具配置，例如 Clash Verge 的订阅链接和配置。
- [ ] GitHub / Gitee SSH Key，以及已登记的旧 Key 清单。

### 1.2 必须备份的配置

- Git：`C:\Users\Administrator\.gitconfig`
- Codex：`C:\Users\Administrator\.codex\config.toml`、`hooks.json`
- Codex 模型目录：`C:\Users\Administrator\.cc-switch`
- VS Code：`AppData\Roaming\Code\User\settings.json`
- PyCharm：配置、代码风格、快捷键映射
- Claude / Cline / Clawd / Copilot 等 AI 工具的配置
- PowerShell profile、终端配置、环境变量清单

> 注意：`~/.codex` 下不要整包复制。`auth.json`、日志、会话数据库要在新机重新登录生成；只迁移配置项和必要目录。

### 1.3 备份验证

- [ ] 备份到移动硬盘或网盘，不要只放在旧机本地。
- [ ] 备份完成后抽查文件数量、总大小，并用哈希校验关键文件。
- [ ] 至少做一次“从备份恢复文件到临时目录”的测试，确认备份真的能用。
- [ ] API Key、Token 放进密码管理器，不要直接写进仓库或聊天文件。

---

## 二、新机第一阶段：系统、磁盘与备份底座

### 2.1 首次开机准备

1. 激活 Windows，并完成全部 Windows Update。
2. 关闭不必要的 OEM 预装推广软件，但先不删除系统关键组件。
3. 记录新机默认用户名、机器型号、BIOS 版本、硬盘型号和容量。
4. 确认网络可用；如必须代理，先处理网络再继续。

### 2.2 磁盘分区方案

新机常见为 1TB NVMe SSD，建议至少分两个区：

- `C:` 约 300GB：Windows、开发工具、系统软件。
- `D:` 约 500GB：学习项目、文档、下载、桌面数据。
- `E:` 剩余空间：游戏库、AI 模型、大型素材。

如果用户已有其它分区偏好，以用户确认为准。分区完成后：

- [ ] 把桌面、下载、文档、图片、视频默认路径迁移到数据盘。
- [ ] 明确所有软件的安装路径：开发工具装 `C:`，大型数据放 `D:` 或 `E:`。
- [ ] 把学习项目放在 `D:\Projects` 或用户指定目录，并记录路径。

### 2.3 系统备份与回滚底座

系统还原点不足以保证驱动、UWP 应用和注册表深度改动绝对可逆，因此配置软件前必须先建立更强的回滚底座：

1. 开启系统保护，并为 `C:` 创建还原点。
2. 在“干净系统”状态下创建整机系统映像到移动硬盘，或使用经过验证的第三方备份工具。
3. 每次进入新阶段前再创建一个新的还原点。
4. 正式批量安装前，先测试一次还原流程，确认映像或还原点可用。
5. 建立统一工作目录：

```text
C:\CodexSetup\
  Downloads\      所有下载的安装包
  Logs\           执行日志
  manifest.csv    安装清单
  audit-before\   安装前审计快照
  audit-after\    安装后审计快照
```

---

## 三、驱动安装矩阵

驱动必须全部来自官方来源，逐项安装并验证，不自动安装任何推广软件。

| 组件 | 来源 | 说明 | 验收 |
|---|---|---|---|
| NVIDIA 驱动 | NVIDIA 官网 | RTX 5070 Laptop GPU，Game Ready 或 Studio，需支持 Blackwell | `nvidia-smi` 显示 5070 |
| AMD 芯片组驱动 | AMD 官网 | 保证 PCIe、USB、电源管理正常 | 设备管理器无异常 |
| 核显驱动 | AMD 官网或机械革命支持页 | 与 NVIDIA 双显卡切换相关 | 设备管理器正常 |
| 声卡驱动 | 机械革命支持页或 Realtek 官网 | 外放、耳机、麦克风 | 播放测试 |
| Wi-Fi / 蓝牙 | 机械革命支持页或芯片厂商官网 | 无线网络和蓝牙 | 连接测试 |
| BIOS / 固件 | 机械革命官方支持页 | 有明确修复项且用户确认后才更新 | BIOS 版本正确 |
| 电源与散热管理 | 机械革命官方软件 | 性能模式、风扇策略、键盘灯 | 模式切换生效 |

注意事项：

- NVIDIA 驱动安装时选择“自定义安装”，执行清洁安装，不装 GeForce Experience 的推广项。
- AMD 芯片组驱动和 NVIDIA 驱动分别安装，不要同时运行多个驱动安装器。
- 所有驱动包先验签、扫描，再执行。
- BIOS 更新前必须确认电源和电池状态，并只使用官方 BIOS 文件。

---

## 四、Codex 安装与兜底方案

### 4.1 正常安装

1. 从 Microsoft Store 搜索并安装 OpenAI Codex，或从 OpenAI 官网下载。
2. 登录 ChatGPT / Codex 账号，确认 Codex 能打开终端并执行 PowerShell。
3. 把本文件放到新电脑，让 Codex 读取它。

### 4.2 网络或 Store 不可用时的兜底

1. 先手动安装 Clash Verge 等代理工具，来源必须是官方 GitHub Release。
2. 验签、扫描后再安装，启动代理并记录端口。
3. 设置 PowerShell 与 Codex 的代理环境变量，例如 `HTTP_PROXY`、`HTTPS_PROXY`。
4. 再尝试从官方渠道安装 Codex。
5. 如果仍然失败，停止并向用户报告，不擅自更换下载源。

### 4.3 权限与沙箱

- 安装系统级软件、驱动、注册表组件时需要管理员权限。
- Codex 只有在用户明确确认后才使用提权模式执行。
- 普通软件安装默认使用受限权限，不主动关闭 UAC。
- 任何提权操作前都先说明原因，并记录到 manifest。

---

## 五、软件分层安装

### L1 新机必装

```powershell
winget install --id Git.Git -e
winget install --id Microsoft.PowerShell -e
winget install --id Microsoft.WindowsTerminal -e
winget install --id Microsoft.VisualStudioCode -e
winget install --id OpenJS.NodeJS.LTS -e
winget install --id astral-sh.uv -e
winget install --id MSYS2.MSYS2 -e
winget install --id 7zip.7zip -e
```

### L2 学习与开发环境

```powershell
winget install --id Microsoft.VisualStudio.2022.BuildTools -e
winget install --id JetBrains.PyCharm -e
winget install --id Docker.DockerDesktop -e
```

### L3 日常软件

- 微信、QQ、钉钉
- Firefox
- PotPlayer
- 网易云音乐
- 搜狗输入法或微软拼音
- WPS 或 Microsoft 365
- 夸克、豆包
- Steam、WeGame、米哈游启动器

### L4 按需安装

- Logitech G HUB
- Wallpaper Engine
- Windhawk / TranslucentTB
- Adobe Acrobat
- 学业工具：LaTeX、Anki、Obsidian、Typora

> 第一轮只执行 L1。L2 到 L4 逐项向用户确认，不一次性批量安装。

---

## 六、Python 环境

### 6.1 版本策略

- 默认使用 Python 3.13 做学习和 AI / GPU 项目。
- Python 3.14 仅在明确需要新特性时使用。
- 遇到旧项目或 CUDA 扩展不兼容时，再按需安装 Python 3.12。
- 每个项目单独建虚拟环境，不把包全局安装到系统 Python。

```powershell
uv python install 3.12
uv python install 3.13
uv python install 3.14
uv venv D:\Projects\venvs\ml --python 3.13
```

### 6.2 GPU / PyTorch

RTX 5070 是 Blackwell 架构，PyTorch 必须使用支持 `sm_120` 的版本，推荐 CUDA 12.8+ 的 wheel：

```powershell
uv pip install --python D:\Projects\venvs\ml\Scripts\python.exe `
  torch torchvision torchaudio `
  --index-url https://download.pytorch.org/whl/cu128
```

只有需要编译自定义 CUDA 扩展时才安装完整 CUDA Toolkit 12.8+ 和 cuDNN；普通 PyTorch 使用不需要额外安装 CUDA Toolkit。

### 6.3 Python 冒烟测试

```powershell
python --version
uv --version
uv python list
python -c "print('hello')"
```

GPU 冒烟测试：

```powershell
python -c "import torch; x=torch.randn(3,3).cuda(); print(torch.cuda.is_available(), torch.version.cuda, torch.cuda.get_device_name(0), (x@x).sum().item())"
```

---

## 七、C/C++ 环境

### 7.1 默认工具链

- 日常学习、算法题、轻量项目：默认 MSYS2 + MinGW-w64 的 `g++`。
- Windows 原生开发、需要 MSVC、编译 Python / CUDA 扩展：使用 Visual Studio Build Tools。
- 两个工具链不要同时混用同一个项目；用项目级 `CMakePresets.json` 区分。

### 7.2 MSYS2 + MinGW-w64

```powershell
winget install --id MSYS2.MSYS2 -e
```

首次打开 MSYS2 UCRT64 终端：

```bash
pacman -Syu
pacman -S --needed mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb mingw-w64-ucrt-x86_64-cmake mingw-w64-ucrt-x86_64-ninja mingw-w64-ucrt-x86_64-pkgconf
```

验收：

```powershell
gcc --version
g++ --version
cmake --version
ninja --version
```

### 7.3 Visual Studio Build Tools

```powershell
winget install --id Microsoft.VisualStudio.2022.BuildTools -e
```

安装后勾选“使用 C++ 的桌面开发”工作负载，需要包含 MSVC、Windows SDK、CMake 工具。

验收时在“Developer PowerShell for VS 2022”里运行：

```powershell
where cl
cl
```

### 7.4 C++ 冒烟测试

写一个最小程序并编译运行，确认工具链完整可用：

```cpp
#include <iostream>
int main() { std::cout << "hello c++" << std::endl; return 0; }
```

分别用 `g++` 和 MSVC 编译一次，确认两个工具链都正常。

---

## 八、WSL2 与 Docker

### 8.1 WSL2

```powershell
wsl --install -d Ubuntu-24.04
```

重启后进入 Ubuntu：

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git curl wget python3 python3-pip
```

### 8.2 Docker Desktop

- 安装 Docker Desktop 后，把后端设置为 WSL2。
- 选择 Ubuntu 作为 Docker 集成环境。
- 不把 Docker 数据放在系统盘，必要时配置到数据盘。

验收：

```powershell
docker --version
docker run hello-world
```

---

## 九、VS Code、Codex 与 IDE 配置

### 9.1 VS Code 扩展

- Python：`ms-python.python`、`ms-python.debugpy`、`ms-python.vscode-pylance`、`ms-python.vscode-python-envs`
- C/C++：`ms-vscode.cpptools`、`ms-vscode.cpptools-extension-pack`、`ms-vscode.cmake-tools`、`ms-vscode.cpp-devtools`
- 运行：`formulahendry.code-runner`
- LeetCode：`leetcode.vscode-leetcode`、`ccagml.vscode-leetcode-problem-rating`
- 中文：`ms-ceintl.vscode-language-pack-zh-hans`
- AI：`openai.chatgpt`、`anthropic.claude-code`、`hybridtalentcomputing.cline-chinese`、`clawd.clawd-terminal-focus`

### 9.2 Codex 配置迁移

- 新机第一次启动 Codex 并登录后，再迁移配置。
- 复制旧机 `~/.codex/config.toml` 中需要保留的部分：
  - 自定义模型提供商，例如 DeepSeek 的 `base_url`、`wire_api`、模型名
  - Codex 插件开关：browser、visualize、computer-use
  - 主题、字号、对话模式等界面设置
- 复制 `~/.cc-switch`，恢复模型目录切换。
- 不复制 `auth.json`；新机重新登录。
- 不复制 `logs_2.sqlite`、`sessions` 等运行数据。
- 插件和技能在新机安装 Codex 后自动重建；特殊自建技能再单独复制。

### 9.3 VS Code 设置迁移

- 从旧机复制 `settings.json`。
- 迁移前检查是否有绝对路径、Token、API Key 等敏感信息。
- 路径发生变化时逐项修正，不在新机沿用旧路径。

---

## 十、Git、SSH 与凭据安全

```powershell
git config --global user.name "WangZiqi0115"
git config --global user.email "wangziqi511080@163.com"
git config --global init.defaultBranch main
git config --global core.autocrlf true
```

生成 SSH Key：

```powershell
ssh-keygen -t ed25519 -C "wangziqi511080@163.com"
```

把 `~/.ssh/id_ed25519.pub` 添加到 GitHub / Gitee，然后验证：

```powershell
ssh -T git@github.com
```

### 10.1 仓库同步指令（新机 Codex 自动执行）

新机安装 Git 并配置 SSH 后，Codex 必须自动完成以下仓库同步：

```powershell
# 配置 Git 身份
git config --global user.name "WangZiqi0115"
git config --global user.email "wangziqi511080@163.com"
git config --global init.defaultBranch main
git config --global core.autocrlf true

# 创建项目目录
New-Item -ItemType Directory -Force -Path "D:\Projects" | Out-Null

# 第一次同步：克隆仓库
if (!(Test-Path "D:\Projects\New project\.git")) {
    git clone https://github.com/WangZiqi0115/Python-.git "D:\Projects\New project"
} else {
    # 已存在时只拉取最新
    git -C "D:\Projects\New project" pull --rebase
}

# 改为 SSH 远程地址，方便以后免密 push
git -C "D:\Projects\New project" remote set-url origin git@github.com:WangZiqi0115/Python-.git

# 检查同步结果
git -C "D:\Projects\New project" status
git -C "D:\Projects\New project" remote -v
```

同步完成后必须确认以下文件存在：

```text
D:\Projects\New project\README.md
D:\Projects\New project\Codex每日必读.md
D:\Projects\New project\new-laptop-setup-plan.md
```

确认后，Codex 必须先读取 `Codex每日必读.md`，再按其中的 Git 工作流继续后续学习任务。

如果使用 Clash 等本地代理：

```powershell
git config --global http.proxy http://127.0.0.1:7897
```

凭据安全要求：

- 开启 BitLocker 后再保存敏感配置。
- UAC 保持默认或更高，不关闭。
- Windows Defender 实时保护保持开启。
- API Key、Token 使用 Windows 凭据管理器或密码管理器保存，不写进普通配置文件。
- `.codex`、`.claude.json`、`.env` 等敏感文件不进 Git 仓库。

---

## 十一、学业与科研工具

针对当前学习方向，建议增加：

- LaTeX：TeX Live 或 MiKTeX，用于数学作业、论文、建模报告。
- Obsidian 或 Typora：笔记和知识管理。
- Anki：408、数学、英语背诵。
- Python 数学库：NumPy、SciPy、Pandas、Matplotlib、SymPy。
- 数学建模相关：Scipy、PuLP / OR-Tools、可视化库。
- Office：WPS 或 Microsoft 365，Excel / Word / PPT。

学业工具同样放入 L2 / L4 分层，按需安装。

---

## 十二、Windows 基础设置

- 开启开发人员模式。
- 开启存储感知，自动清理临时文件。
- 关闭不必要的开机自启，保留 Codex、Clash Verge、输入法。
- 外接电源时使用高性能模式，电池下使用平衡模式。
- 设置默认终端为 Windows Terminal。
- 文件资源管理器默认打开“此电脑”。
- 重要文件同步到 OneDrive / 网盘。
- 开启 BitLocker 和 Windows Hello。
- 定期检查 Windows Update，但驱动更新只接受官方渠道。

---

## 十三、审计、一键清除与回滚协议

### 13.1 安装前审计

每轮安装前执行：

```powershell
winget export -o C:\CodexSetup\audit-before\winget.json
Get-AppxPackage | Export-Csv C:\CodexSetup\audit-before\appx.csv
reg export "HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall" C:\CodexSetup\audit-before\uninstall.reg /y
```

记录关键目录和文件的基线：

```powershell
Get-ChildItem "C:\Program Files","C:\Program Files (x86)","$env:LOCALAPPDATA\Programs" -ErrorAction SilentlyContinue | Select-Object FullName,Length | Export-Csv C:\CodexSetup\audit-before\programs.csv
```

### 13.2 每个安装包的检查流程

1. 确认来源为官方渠道。
2. 下载到 `C:\CodexSetup\Downloads`。
3. 计算 SHA256 并记录。
4. 校验 Authenticode 签名。
5. Windows Defender 扫描安装包。
6. 高风险包提交 VirusTotal。
7. 全部通过后，向用户展示结果并等待确认。
8. 安装时选择自定义，取消所有捆绑项。
9. 安装完成后把结果写入 manifest。

### 13.3 一键清除

用户要求“一键清除”时按以下顺序执行：

1. 立即停止所有下载、安装、配置任务。
2. 根据 manifest 反向卸载本次会话安装的软件。
3. 删除 `C:\CodexSetup` 及所有下载内容。
4. 清理 `%TEMP%`、winget 缓存、安装目录、AppData 残留和注册表卸载项。
5. 再次导出 winget、Appx、注册表和程序目录快照，与 `audit-before` 对比。
6. 若发现无法自动清除的残留，先报告用户，不强行删除系统文件。
7. 如果用户要求彻底还原，使用安装前的系统还原点或整机映像还原。

### 13.4 回滚验证

正式大规模安装前，先做一次小规模回滚测试：

1. 安装一个 7-Zip 或同类小工具。
2. 按一键清除流程卸载并清理。
3. 对比前后快照，确认没有残留。
4. 测试通过后才开始 L1 批量安装。

---

## 十四、新机验收清单

### 基础环境

- [ ] `winget --version` 正常
- [ ] `git --version`、`git config --list` 正常
- [ ] `ssh -T git@github.com` 连接成功
- [ ] `node -v`、`npm -v` 正常
- [ ] `uv --version` 正常，Python 虚拟环境可创建
- [ ] Python 冒烟测试输出正常
- [ ] `nvidia-smi` 能识别 RTX 5070
- [ ] PyTorch 张量计算在 GPU 上运行成功
- [ ] `gcc`、`g++`、`cmake`、`ninja` 可用
- [ ] MSVC `cl` 可用
- [ ] C++ Hello World 编译运行成功
- [ ] `wsl --status`、`wsl -l -v` 正常
- [ ] `docker run hello-world` 成功
- [ ] VS Code 扩展恢复完成
- [ ] Codex 能打开终端并执行命令

### 数据与安全

- [ ] 学习项目克隆到新机并能正常 `git pull` / `git push`
- [ ] `README.md`、`Codex每日必读.md`、`new-laptop-setup-plan.md` 都存在于项目目录
- [ ] 文档、桌面、下载路径已迁移到数据盘
- [ ] 浏览器、微信、QQ 等登录态和数据迁移完成
- [ ] BitLocker 已开启
- [ ] Windows Defender 实时保护开启
- [ ] API Key / Token 已存入凭据管理器或密码管理器
- [ ] 一键清除协议测试通过
- [ ] 系统还原点或整机映像验证可用

### 日常使用

- [ ] 微信、QQ、钉钉、浏览器、游戏等日常软件可启动
- [ ] 输入法、代理、音乐播放器、截图工具正常
- [ ] 外放、耳机、麦克风、Wi-Fi、蓝牙正常
- [ ] 电源模式、风扇、键盘灯等笔记本功能正常

> 验收过程中遇到任何一项不通过，立即停止并询问用户，不修改测试结果，不继续下一项。

---

## 附录：旧电脑上值得继续保留的软件清单

从旧电脑检测到的软件中，建议新机按需恢复：

- Git、Node.js、Python、MSYS2、VS Code、PyCharm
- CC Switch、Clash Verge、Codex Dream Skin
- Claude、Clawd on Desk、Cline Chinese
- Firefox、PotPlayer、微信、QQ、钉钉、网易云音乐、夸克、豆包
- Steam、WeGame、米哈游启动器、Wallpaper Engine、Windhawk
- 搜狗输入法、WinRAR、Adobe Acrobat、Logitech G HUB

旧机上的 Office 2007、DirectX 老运行时、XNA 等不必迁移，新机用新版 Office 和现代运行时即可。
