import pandas as pd
import io

# 最新总投资金额
total_investment = 805000

# 持仓数据
data = {
    '股票': ['VOO', 'BILI', 'AMD', 'NVDA', 'BRKB', 'QQQ', 'Unity', 'Google'],
    '当前仓位%': [38, 23.6, 3.8, 6.8, 1, 1.6, 1.4, 27],
    '目标仓位%': [25, 15, 3, 5, 1, 1.6, 1.4, 27],  # 其他不动
}

df = pd.DataFrame(data)

# 计算减仓比例和金额
df['减仓%'] = df['当前仓位%'] - df['目标仓位%']
df['当前金额($)'] = df['当前仓位%'] / 100 * total_investment
df['目标金额($)'] = df['目标仓位%'] / 100 * total_investment
df['减仓金额($)'] = df['减仓%'] / 100 * total_investment

# 分4次减仓
split_count = 4
df['每次减仓金额($)'] = df['减仓金额($)'] / split_count

# 创建Excel文件
output = io.BytesIO()
with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name='减仓计划', index=False)

    # 操作说明
    instructions = pd.DataFrame({
        '操作说明': [
            '✅ 每周或每两周减仓一次，每次卖出“每次减仓金额”列金额',
            '✅ 卖出后将金额转入 SPAXX 子弹池',
            '✅ 记录每次操作日期和当时心态，可用于复盘',
            '✅ 若市场回调 >=10%，或S&P500 PE < 18，可用子弹池分批回补'
        ]
    })
    instructions.to_excel(writer, sheet_name='操作说明', index=False)

output.seek(0)
output
