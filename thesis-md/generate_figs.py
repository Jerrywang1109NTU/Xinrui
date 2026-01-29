import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
from matplotlib.font_manager import FontProperties

# 1. Setup Font
# Force load PingFang on Mac
def get_chinese_font():
    # Common paths on macOS
    paths = [
        '/System/Library/Fonts/PingFang.ttc',
        '/System/Library/Fonts/STHeiti Light.ttc',
        '/System/Library/Fonts/STHeiti Medium.ttc',
        '/Library/Fonts/Arial Unicode.ttf'
    ]
    for p in paths:
        if os.path.exists(p):
            print(f"Found font at: {p}")
            return FontProperties(fname=p)
    print("No system Chinese font found. Using default.")
    return FontProperties()

zh_font = get_chinese_font()
plt.rcParams['axes.unicode_minus'] = False

# Output Directory
output_dir = "/Users/wangrunyan/Desktop/Xinrui/thesis-md/figs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# ==========================================
# Fig 1: Traditional Maintenance Problems
# ==========================================
def plot_traditional_problems():
    print("Plotting Fig 1...")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    
    # Time axis
    x = np.linspace(0, 100, 500)
    
    # Equipment Health Curve (Simulated)
    # Drops slowly then fast
    y = 100 - 0.5 * x - 0.005 * x**2
    
    threshold = 40
    
    ax.plot(x, y, label='设备健康状态', color='#1f77b4', linewidth=2.5)
    ax.axhline(threshold, color='#d62728', linestyle='--', label='故障阈值')
    
    # Scenario 1: Over-maintenance (Too early)
    t1 = 30
    y1 = 100 - 0.5 * t1 - 0.005 * t1**2
    ax.axvline(t1, color='green', linestyle=':', linewidth=2)
    ax.scatter([t1], [y1], color='green', s=100, zorder=5)
    ax.annotate('过修点\n(状态尚好)', xy=(t1, y1), xytext=(t1+5, y1+10),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontproperties=zh_font, fontsize=12)

    # Scenario 2: Under-maintenance (Too late)
    t2 = 85
    y2 = 100 - 0.5 * t2 - 0.005 * t2**2
    ax.axvline(t2, color='orange', linestyle=':', linewidth=2)
    ax.scatter([t2], [y2], color='orange', s=100, zorder=5)
    ax.annotate('失修点\n(已发生故障)', xy=(t2, y2), xytext=(t2-25, y2-20),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontproperties=zh_font, fontsize=12)
    
    # Periodic Maintenance Intervals (Blind)
    ax.set_xticks([0, 30, 60, 90])
    ax.set_xticklabels(['T0', 'T1', 'T2', 'T3'], fontproperties=zh_font)
    ax.set_xlabel('时间 (周期性检修时刻)', fontproperties=zh_font, fontsize=12)
    ax.set_ylabel('设备健康度 / 性能', fontproperties=zh_font, fontsize=12)
    ax.set_title('传统定期检修模式的“过修”与“失修”问题示意图', fontproperties=zh_font, fontsize=14)
    ax.legend(prop=zh_font)
    ax.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'traditional_maintenance_problems.png'))
    plt.close()

# ==========================================
# Fig 2: CBM Advantages
# ==========================================
def plot_cbm_advantages():
    print("Plotting Fig 2...")
    fig, axes = plt.subplots(1, 3, figsize=(12, 5), dpi=150)
    
    # Data
    methods = ['传统检修', '状态检修']
    colors = ['#bdc3c7', '#3498db'] # Grey vs Blue
    
    # 1. Discovery Rate
    data1 = [65, 92]
    axes[0].bar(methods, data1, color=colors, width=0.5)
    axes[0].set_title('故障发现率 (%)', fontproperties=zh_font)
    axes[0].set_ylim(0, 100)
    for i, v in enumerate(data1):
        axes[0].text(i, v + 2, str(v) + '%', ha='center', fontproperties=zh_font)

    # 2. Handling Time
    data2 = [7.2, 3.5]
    axes[1].bar(methods, data2, color=colors, width=0.5)
    axes[1].set_title('平均故障处理时间 (小时)', fontproperties=zh_font)
    axes[1].set_ylim(0, 10)
    for i, v in enumerate(data2):
        axes[1].text(i, v + 0.2, str(v) + 'h', ha='center', fontproperties=zh_font)

    # 3. Maintenance Cost
    data3 = [100, 82]  # Normalized
    axes[2].bar(methods, data3, color=colors, width=0.5)
    axes[2].set_title('相对维护成本 (%)', fontproperties=zh_font)
    axes[2].set_ylim(0, 110)
    for i, v in enumerate(data3):
        axes[2].text(i, v + 2, str(v) + '%', ha='center', fontproperties=zh_font)

    for ax in axes:
        ax.set_xticklabels(methods, fontproperties=zh_font)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.suptitle('状态检修与传统检修模式应用效果对比', fontproperties=zh_font, fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'cbm_advantages.png'))
    plt.close()

# ==========================================
# Fig 3: Risk Assessment Model
# ==========================================
def plot_risk_model():
    print("Plotting Fig 3...")
    fig, ax = plt.subplots(figsize=(8, 8), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    def draw_box(x, y, w, h, text, color='#ecf0f1'):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", 
                                      linewidth=1, edgecolor='black', facecolor=color)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', 
                fontproperties=zh_font, fontsize=12)

    # Pyramid structure
    # Level 1: Sensing (Bottom)
    draw_box(1, 1, 8, 1.5, "状态感知层\n(温度 / 局部放电 / 机械特性)", color='#d6eaf8')
    
    # Arrow
    ax.arrow(5, 2.9, 0, 0.6, head_width=0.3, head_length=0.3, fc='black', ec='black')
    
    # Level 2: Analysis (Middle)
    draw_box(2, 4, 6, 1.5, "数据分析层\n(趋势分析 / 频谱诊断 / 阈值对比)", color='#aed6f1')
    
    # Arrow
    ax.arrow(5, 5.9, 0, 0.6, head_width=0.3, head_length=0.3, fc='black', ec='black')
    
    # Level 3: Decision (Top)
    draw_box(3, 7, 4, 1.5, "风险决策层\n(正常 / 注意 / 报警)", color='#5dade2')
    
    ax.set_title('高压开关柜运行风险评估模型框架', fontproperties=zh_font, fontsize=15)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'risk_assessment_model.png'))
    plt.close()

# ==========================================
# Fig 4: Maintenance Strategy Classification
# ==========================================
def plot_strategy_classification():
    print("Plotting Fig 4...")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    def draw_node(x, y, w, h, text, color='white', edge='black', bold=False):
        rect = patches.FancyBboxPatch((x-w/2, y-h/2), w, h, boxstyle="round,pad=0.1", 
                                      linewidth=1.5 if bold else 1, edgecolor=edge, facecolor=color)
        ax.add_patch(rect)
        weight = 'bold' if bold else 'normal'
        ax.text(x, y, text, ha='center', va='center', 
                fontproperties=zh_font, fontsize=12, fontweight=weight)
        return (x, y - h/2 - 0.1) # Return bottom anchor

    # Root
    root_x, root_y = 5, 5
    root_bottom = draw_node(root_x, root_y, 3, 0.8, "维修策略体系", color='#ecf0f1')

    # Branches
    # 1. Corrective
    c_x, c_y = 2, 3
    c_top = (c_x, c_y + 0.5)
    draw_node(c_x, c_y, 2.5, 0.8, "事后维修\n(故障后处理)", color='#f2f4f4')
    
    # 2. Preventive
    p_x, p_y = 5, 3
    p_top = (p_x, p_y + 0.5)
    draw_node(p_x, p_y, 2.5, 0.8, "定期检修\n(基于时间周期)", color='#f2f4f4')
    
    # 3. Predictive (Highlight)
    pd_x, pd_y = 8, 3
    pd_top = (pd_x, pd_y + 0.5)
    draw_node(pd_x, pd_y, 2.5, 0.8, "状态检修\n(基于在线监测)", color='#a9dfbf', edge='#196f3d', bold=True)

    # Connections
    ax.plot([root_x, c_x], [root_bottom[1], c_top[1]], 'k-', lw=1)
    ax.plot([root_x, p_x], [root_bottom[1], p_top[1]], 'k-', lw=1)
    ax.plot([root_x, pd_x], [root_bottom[1], pd_top[1]], 'k-', lw=1)

    ax.text(5, 1, "本研究重点推荐推广应用“状态检修”模式", ha='center', 
            fontproperties=zh_font, fontsize=12, style='italic', color='#555')

    ax.set_title('维修策略分类体系架构图', fontproperties=zh_font, fontsize=15)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'maintenance_strategy_classification.png'))
    plt.close()

# ==========================================
# Chapter 2 Figures
# ==========================================
def plot_fault_mechanism():
    print("Plotting Fig 2.2...")
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    ax.axis('off')
    
    # Venn diagram style or separate bubbles
    circle1 = patches.Circle((3, 6), 2, color='#f1948a', alpha=0.7) # Overheat
    circle2 = patches.Circle((7, 6), 2, color='#85c1e9', alpha=0.7) # Insulation
    circle3 = patches.Circle((5, 3), 2, color='#f7dc6f', alpha=0.7) # Mechanical
    
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)
    
    ax.text(3, 6, "导电回路过热\n(38%)\n\n接触不良/过负荷", ha='center', va='center', fontproperties=zh_font)
    ax.text(7, 6, "绝缘故障\n(35%)\n\n受潮/老化/爬电", ha='center', va='center', fontproperties=zh_font)
    ax.text(5, 3, "机械故障\n(27%)\n\n卡涩/拒动", ha='center', va='center', fontproperties=zh_font)
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 9)
    ax.set_title('高压开关柜常见故障类型及占比', fontproperties=zh_font, fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fault_mechanism.png'))
    plt.close()

def plot_pd_methods():
    print("Plotting Fig 2.4...")
    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    ax.axis('off')
    
    # Table like structure
    col_labels = ['检测技术', '检测对象', '安装位置']
    rows = [
        ['TEV (暂态地电压)', '设备内部放电\n(电磁波信号)', '开关柜金属外壳\n(磁吸附)'],
        ['Ultrasonic (超声波)', '表面/悬浮放电\n(声波信号)', '柜体缝隙/观察窗\n(非接触)'],
        ['UHF (特高频)', '内部绝缘缺陷\n(高频电磁波)', '内置传感器\n(需改造)']
    ]
    
    cell_colors = [['#e8f8f5']*3, ['#eaeded']*3, ['#fef9e7']*3]
    
    table = ax.table(cellText=rows, colLabels=col_labels, loc='center', cellLoc='center',
                     cellColours=cell_colors, colColours=['#d4e6f1']*3)
    
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2) # Height scale
    
    # Set font for table
    for (row, col), cell in table.get_celld().items():
        cell.set_text_props(fontproperties=zh_font)

    ax.set_title('常用局部放电监测技术对比', fontproperties=zh_font, fontsize=14, pad=10)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'pd_monitoring_methods.png'))
    plt.close()

def plot_mechanical_monitor():
    print("Plotting Fig 2.5...")
    fig, ax = plt.subplots(figsize=(10, 4), dpi=150)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')
    
    # Blocks
    ax.add_patch(patches.FancyBboxPatch((0.5, 1.5), 2, 1, facecolor='#d7bde2', edgecolor='black', boxstyle="round,pad=0.1"))
    ax.text(1.5, 2, "传感器\n(霍尔/角度)", ha='center', va='center', fontproperties=zh_font)
    
    ax.arrow(2.6, 2, 0.8, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
    
    ax.add_patch(patches.FancyBboxPatch((3.5, 1.5), 2, 1, facecolor='#a9cce3', edgecolor='black', boxstyle="round,pad=0.1"))
    ax.text(4.5, 2, "数据采集\n单元(IED)", ha='center', va='center', fontproperties=zh_font)
    
    ax.arrow(5.6, 2, 0.8, 0, head_width=0.1, head_length=0.1, fc='k', ec='k')
    
    ax.add_patch(patches.FancyBboxPatch((6.5, 1.5), 2, 1, facecolor='#a3e4d7', edgecolor='black', boxstyle="round,pad=0.1"))
    ax.text(7.5, 2, "后台分析\n(行程/速度)", ha='center', va='center', fontproperties=zh_font)

    ax.set_title('机械特性监测系统数据流向示意', fontproperties=zh_font, fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'mechanical_monitoring.png'))
    plt.close()

# ==========================================
# Chapter 4 Figures
# ==========================================
def plot_pd_analysis():
    print("Plotting Fig 4.2...")
    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)
    
    days = np.arange(0, 150)
    # Background noise and normal fluctuation
    pd_level = np.random.normal(5, 2, size=len(days))
    pd_level = np.abs(pd_level) # Positive only
    
    # Fault starts at day 117
    fault_start = 117
    pd_level[fault_start:] += np.linspace(0, 30, len(days)-fault_start) + np.random.normal(0, 2, len(days)-fault_start)
    
    ax.plot(days, pd_level, label='局部放电幅值(dB)', color='#8e44ad')
    ax.axhline(20, color='orange', linestyle='--', label='预警阈值(20dB)')
    ax.axhline(35, color='red', linestyle='--', label='告警阈值(35dB)')
    
    # Arrow for early warning
    ax.annotate('早期预警\n(第117天)', xy=(117, 20), xytext=(90, 25),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontproperties=zh_font)
    
    ax.set_xlabel('监测时间 (天)', fontproperties=zh_font)
    ax.set_ylabel('放电幅值 (dB)', fontproperties=zh_font)
    ax.set_title('局部放电故障发展趋势模拟', fontproperties=zh_font, fontsize=14)
    ax.legend(prop=zh_font)
    ax.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'pd_monitoring_analysis.png')) # Note the filename in json was pd_monitoring_analysis maybe
    plt.close()
    
# Some files were named differently in previous messages, I'll stick to the names needed by the thesis text (or what I will insert)
# Checking referenced names: 
# Ch 4 text mentions: pd_monitoring_analysis.png (inferred 4.2)
# fault_warning_effect.png (4.3)
# maintenance_efficiency_comparison.png (4.4)
# comprehensive_benefit_analysis.png (4.5)

def plot_warning_stats():
    print("Plotting Fig 4.3...")
    fig, ax = plt.subplots(figsize=(8, 6), dpi=150)
    
    labels = ['真实故障 (39次)', '误报 (6次)', '漏报 (2次)']
    sizes = [39, 6, 2]
    colors = ['#58d68d', '#f5b041', '#ec7063']
    explode = (0.1, 0, 0)
    
    patches, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
           autopct='%1.1f%%', shadow=True, startangle=140)
    
    for text in texts + autotexts:
        text.set_fontproperties(zh_font)
    
    ax.set_title('故障预警准确性统计分析', fontproperties=zh_font, fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'fault_warning_effect.png'))
    plt.close()

def plot_maintenance_efficiency():
    print("Plotting Fig 4.4...")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    
    categories = ['单站巡检耗时', '故障处理耗时']
    traditional = [30, 7.2*60] # Minutes
    monitoring = [5, 3.5*60]   # Minutes
    
    # Scale issue, maybe normalize or double axis. Let's stick to bar chart of Improvement %
    
    # Better: Efficiency Improvement Chart
    items = ['巡检效率', '故障处理速度', '人员配置优化']
    improvement = [83, 51, 50] # Percent
    
    bars = ax.barh(items, improvement, color='#2874a6')
    ax.set_xlim(0, 100)
    ax.set_xlabel('提升比例 (%)', fontproperties=zh_font)
    
    for i, v in enumerate(improvement):
        ax.text(v + 1, i, f"+{v}%", va='center', fontproperties=zh_font, fontweight='bold')
        
    ax.set_yticks(range(len(items)))
    ax.set_yticklabels(items, fontproperties=zh_font, fontsize=12)
    ax.set_title('在线监测系统带来的运维效率提升', fontproperties=zh_font, fontsize=14)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'maintenance_efficiency_comparison.png'))
    plt.close()

def plot_benefit_analysis():
    print("Plotting Fig 4.5...")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=150)
    
    years = np.arange(1, 11)
    # Unit: 10k RMB
    cost_traditional = np.cumsum([45] * 10)
    
    # Monitoring: Year 1 invest 80+8=88, then 8/year
    cost_monitoring = []
    current = 0
    for y in years:
        if y == 1:
            current += (80 + 8)
        else:
            current += 8
        cost_monitoring.append(current)
    
    ax.plot(years, cost_traditional, 'o--', label='传统模式累计成本', color='gray')
    ax.plot(years, cost_monitoring, 's-', label='在线监测模式累计成本', color='#2ecc71', linewidth=2)
    
    # Junction point approx year 6
    ax.annotate('投资回收点\n(约5.6年)', xy=(5.6, 45*5.6), xytext=(6, 150),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontproperties=zh_font)
    
    ax.set_xlabel('运行年份', fontproperties=zh_font)
    ax.set_ylabel('累计投入成本 (万元)', fontproperties=zh_font)
    ax.set_title('系统全生命周期成本效益分析', fontproperties=zh_font, fontsize=14)
    ax.legend(prop=zh_font)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'comprehensive_benefit_analysis.png'))
    plt.close()

if __name__ == "__main__":
    print("Generating diagrams...")
    try:
        # Ch 3 Originals
        plot_traditional_problems()
        print("Generated: traditional_maintenance_problems.png")
        plot_cbm_advantages()
        print("Generated: cbm_advantages.png")
        plot_risk_model()
        print("Generated: risk_assessment_model.png")
        plot_strategy_classification()
        print("Generated: maintenance_strategy_classification.png")
        
        # Ch 2 New
        plot_fault_mechanism()
        print("Generated: fault_mechanism.png")
        plot_pd_methods()
        print("Generated: pd_monitoring_methods.png")
        plot_mechanical_monitor()
        print("Generated: mechanical_monitoring.png")
        
        # Ch 4 New
        plot_pd_analysis()
        print("Generated: pd_monitoring_analysis.png") # Warning: name check
        plot_warning_stats()
        print("Generated: fault_warning_effect.png")
        plot_maintenance_efficiency()
        print("Generated: maintenance_efficiency_comparison.png")
        plot_benefit_analysis()
        print("Generated: comprehensive_benefit_analysis.png")
        
        print("All Done.")
    except Exception as e:
        print(f"Error: {e}")

