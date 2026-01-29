#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图表生成脚本 - 用于生成论文所需的4张图表
运行方法: python3 generate_thesis_charts.py
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti TC', 'STHeiti', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 确保输出目录存在
output_dir = 'thesis-md/figs'
os.makedirs(output_dir, exist_ok=True)

# ============================================================
# 图1: 温度监测效果分析 (3个子图)
# ============================================================
print("生成图1: 温度监测效果分析...")

fig, axes = plt.subplots(3, 1, figsize=(12, 10))
plt.subplots_adjust(hspace=0.35)

# 子图1: 全年趋势
ax1 = axes[0]
days = np.arange(1, 366)
temp = 35 + 10*np.sin(2*np.pi*days/365) + 3*np.sin(2*np.pi*days) + np.random.normal(0, 1, 365)
ax1.plot(days, temp, 'b-', linewidth=0.5, alpha=0.7, label='监测温度')
ax1.axhline(y=70, color='orange', linestyle='--', linewidth=1.5, label='预警阈值(70°C)')
ax1.axhline(y=90, color='red', linestyle='--', linewidth=1.5, label='告警阈值(90°C)')
ax1.fill_between(days, 0, temp, alpha=0.2, color='blue')
ax1.set_xlabel('天数', fontsize=11)
ax1.set_ylabel('触头温度(°C)', fontsize=11)
ax1.set_title('(a) 全年温度监测趋势', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left', fontsize=9)
ax1.set_ylim(20, 100)
ax1.grid(True, alpha=0.3)

# 子图2: 故障事件
ax2 = axes[1]
event_hours = np.arange(0, 48, 3)  # 16个时间点，每3小时一个
event_temp = [55, 62, 70, 78, 85, 90, 92, 90, 85, 80, 75, 70, 65, 60, 55, 52]
ax2.plot(event_hours, event_temp, 'r-o', linewidth=2, markersize=5)
ax2.axhline(y=70, color='orange', linestyle='--', label='预警阈值')
ax2.axhline(y=90, color='red', linestyle='--', label='告警阈值')
ax2.axvspan(18, 36, alpha=0.2, color='red', label='故障时段')
ax2.set_xlabel('故障发生后时间(小时)', fontsize=11)
ax2.set_ylabel('触头温度(°C)', fontsize=11)
ax2.set_title('(b) 触头发热事件演变过程(48小时)', fontsize=12, fontweight='bold')
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3)

# 子图3: 温度负荷相关性
ax3 = axes[2]
load = np.linspace(200, 600, 100)
temp_pred = 0.043 * load + 18.5
scatter_temp = 0.043 * load + 18.5 + np.random.normal(0, 3, 100)
scatter = ax3.scatter(load, scatter_temp, c=scatter_temp, cmap='RdYlBu_r', s=20, alpha=0.6)
ax3.plot(load, temp_pred, 'r--', linewidth=2, label='T = 0.043×I + 18.5')
ax3.set_xlabel('负荷电流(A)', fontsize=11)
ax3.set_ylabel('触头温度(°C)', fontsize=11)
ax3.set_title('(c) 温度-负荷相关性分析(r=0.82)', fontsize=12, fontweight='bold')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)
plt.colorbar(scatter, ax=ax3, label='温度(°C)', shrink=0.8)

plt.tight_layout()
plt.savefig(f'{output_dir}/temperature_monitoring_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("  -> 已保存: temperature_monitoring_analysis.png")

# ============================================================
# 图3: 故障预警效果分析 (3个子图)
# ============================================================
print("生成图3: 故障预警效果分析...")

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# 子图1: 预警时间分布
ax1 = axes[0]
warnings = ['OH1', 'PD', 'OH2', 'A1', 'A2', 'OH3', 'A3', 'A4', 'A5', 'A6', 'OH4', 'OH5']
hours = [0.4, 72, 0.2, 1.5, 24, 48, 0.5, 2, 12, 36, 0.3, 0.8]
colors = ['#FF5722' if h > 24 else '#4CAF50' if h > 1 else '#FFC107' for h in hours]
bars = ax1.bar(range(len(warnings)), hours, color=colors, edgecolor='white')
ax1.set_xticks(range(len(warnings)))
ax1.set_xticklabels(warnings, rotation=45, ha='right', fontsize=9)
ax1.set_xlabel('预警事件', fontsize=11)
ax1.set_ylabel('提前预警时间(小时)', fontsize=11)
ax1.set_title('(a) 预警时效性分布', fontsize=12, fontweight='bold')
ax1.axhline(y=24, color='red', linestyle='--', linewidth=1.5, label='24小时基准线')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3, axis='y')

# 子图2: 预警准确率
ax2 = axes[1]
labels = ['真实预警', '误报', '漏报']
sizes = [39, 6, 2]
colors = ['#4CAF50', '#FFC107', '#F44336']
explode = (0.05, 0, 0)
ax2.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.0f%%', startangle=90, textprops={'fontsize': 10})
ax2.set_title('(b) 预警分类统计(总计47次)', fontsize=12, fontweight='bold')

# 子图3: 响应时间
ax3 = axes[2]
response = [5, 8, 10, 6, 12, 7, 9, 8, 5, 11, 7, 8]
ax3.hist(response, bins=5, color='#2196F3', alpha=0.7, edgecolor='white')
ax3.axvline(x=np.mean(response), color='red', linestyle='--', linewidth=2, 
            label=f'平均响应时间: {np.mean(response):.1f}分钟')
ax3.set_xlabel('响应时间(分钟)', fontsize=11)
ax3.set_ylabel('频次', fontsize=11)
ax3.set_title('(c) 预警响应时间分布', fontsize=12, fontweight='bold')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(f'{output_dir}/fault_warning_effect.png', dpi=150, bbox_inches='tight')
plt.close()
print("  -> 已保存: fault_warning_effect.png")

# ============================================================
# 图4: 维护效率对比 (3个子图)
# ============================================================
print("生成图4: 维护效率对比...")

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# 子图1: 巡检时间
ax1 = axes[0]
x = [0, 1]
time_data = [30, 5]
bars = ax1.bar(x, time_data, color=['#F44336', '#4CAF50'], width=0.5, edgecolor='white')
ax1.set_xticks(x)
ax1.set_xticklabels(['传统模式', '在线监测'], fontsize=11)
ax1.set_ylabel('单站巡检时间(分钟)', fontsize=11)
ax1.set_title('(a) 巡检时间对比\n(效率提升83%)', fontsize=12, fontweight='bold')
ax1.bar_label(bars, fmt='%d分钟', padding=3, fontsize=11)
ax1.set_ylim(0, 40)
ax1.grid(True, alpha=0.3, axis='y')
ax1.annotate('+83%', xy=(0.5, 28), fontsize=12, ha='center', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# 子图2: 故障发现率
ax2 = axes[1]
detection = [65, 92]
bars = ax2.bar(x, detection, color=['#F44336', '#4CAF50'], width=0.5, edgecolor='white')
ax2.set_xticks(x)
ax2.set_xticklabels(['传统模式', '在线监测'], fontsize=11)
ax2.set_ylabel('故障发现率(%)', fontsize=11)
ax2.set_title('(b) 故障发现率对比\n(65%→92%)', fontsize=12, fontweight='bold')
ax2.bar_label(bars, fmt='%d%%', padding=3, fontsize=11)
ax2.set_ylim(0, 110)
ax2.grid(True, alpha=0.3, axis='y')
ax2.annotate('+27%', xy=(0.5, 80), fontsize=12, ha='center', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# 子图3: 处理时间
ax3 = axes[2]
faults = ['触头发热', '局部放电', '机械故障', '平均']
trad = [8.5, 12.3, 6.2, 7.2]
online = [4.2, 5.8, 3.1, 3.5]
x_pos = np.arange(len(faults))
width = 0.35
bars1 = ax3.bar(x_pos - width/2, trad, width, label='传统模式', color='#F44336', edgecolor='white')
bars2 = ax3.bar(x_pos + width/2, online, width, label='在线监测', color='#4CAF50', edgecolor='white')
ax3.set_xticks(x_pos)
ax3.set_xticklabels(faults, fontsize=10)
ax3.set_ylabel('故障处理时间(小时)', fontsize=11)
ax3.set_title('(c) 故障处理时间对比', fontsize=12, fontweight='bold')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(f'{output_dir}/maintenance_efficiency_comparison.png', dpi=150, bbox_inches='tight')
plt.close()
print("  -> 已保存: maintenance_efficiency_comparison.png")

# ============================================================
# 图5: 综合效益分析 (3个子图)
# ============================================================
print("生成图5: 综合效益分析...")

fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

# 子图1: 年度成本对比
ax1 = axes[0]
years = ['第1年', '第2年', '第3年', '第4年', '第5年']
trad_cost = [45, 45, 45, 45, 45]
online_cost = [88, 53, 53, 53, 53]
x_pos = np.arange(len(years))
width = 0.35
ax1.bar(x_pos - width/2, trad_cost, width, label='传统模式', color='#F44336', edgecolor='white')
ax1.bar(x_pos + width/2, online_cost, width, label='在线监测(含投资)', color='#4CAF50', edgecolor='white')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(years, fontsize=10)
ax1.set_ylabel('年度成本(万元)', fontsize=11)
ax1.set_title('(a) 年度维护成本对比', fontsize=12, fontweight='bold')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3, axis='y')

# 子图2: ROI分析
ax2 = axes[1]
labels = ['系统投资', '累计节约', '净收益']
values = [80, 207, 127]
colors = ['#2196F3', '#4CAF50', '#FF9800']
bars = ax2.bar(labels, values, color=colors, edgecolor='white')
ax2.set_ylabel('金额(万元)', fontsize=11)
ax2.set_title('(b) 5年投资回报分析\n(投资回收期5.6年)', fontsize=12, fontweight='bold')
ax2.bar_label(bars, fmt='%d万', padding=3, fontsize=11)
ax2.grid(True, alpha=0.3, axis='y')

# 子图3: 雷达图
ax3 = axes[2]
categories = ['故障预防', '运维效率', '供电可靠性', '设备寿命', '数据价值', '管理水平']
N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]
values = [85, 92, 88, 75, 80, 78]
values += values[:1]
ax3 = plt.subplot(1, 3, 3, polar=True)
ax3.plot(angles, values, 'o-', linewidth=2, color='#2196F3')
ax3.fill(angles, values, alpha=0.25, color='#2196F3')
ax3.set_xticks(angles[:-1])
ax3.set_xticklabels(categories, fontsize=9)
ax3.set_ylim(0, 100)
ax3.set_title('(c) 多维度综合效益评估', fontsize=12, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig(f'{output_dir}/comprehensive_benefit_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("  -> 已保存: comprehensive_benefit_analysis.png")

# ============================================================
# 完成
# ============================================================
print("\n" + "="*60)
print("所有图表生成完成!")
print(f"输出目录: {output_dir}/")
print("生成的图表文件:")
print("  1. temperature_monitoring_analysis.png")
print("  2. fault_warning_effect.png")
print("  3. maintenance_efficiency_comparison.png")
print("  4. comprehensive_benefit_analysis.png")
print("="*60)
