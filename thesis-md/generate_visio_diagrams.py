import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
from matplotlib import font_manager

# --- Font Setup ---
# Tries multiple common Chinese fonts on macOS
font_candidates = [
    '/Library/Fonts/Arial Unicode.ttf',
    '/System/Library/Fonts/STHeiti Medium.ttc',
    '/System/Library/Fonts/PingFang.ttc',
    '/System/Library/Fonts/Hiragino Sans GB.ttc'
]

font_path = None
for f in font_candidates:
    if os.path.exists(f):
        font_path = f
        break

if font_path:
    try:
        font_manager.fontManager.addfont(font_path)
        prop = font_manager.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = prop.get_name()
        print(f"Using font: {prop.get_name()} from {font_path}")
    except Exception as e:
        print(f"Error loading font: {e}")
else:
    print("Warning: No suitable Chinese font found. Text may not render correctly.")

OUTPUT_DIR = '/Users/wangrunyan/Desktop/Xinrui/thesis-md/figs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Helper Functions ---
def create_figure(title):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(title, fontsize=16, pad=20)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    return fig, ax

def draw_box(ax, x, y, w, h, text, color='white', edgecolor='black', fontsize=12):
    rect = patches.Rectangle((x, y), w, h, linewidth=1.5, edgecolor=edgecolor, facecolor=color)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, wrap=True)
    return rect

def draw_arrow(ax, x1, y1, x2, y2, style='->'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(facecolor='black', arrowstyle=style, lw=1.5))

# --- Generators ---

def gen_traditional_maintenance_problems():
    plt.figure(figsize=(10, 6))
    x = np.linspace(0, 10, 1000)
    y = 10 - (x % 2.5) * 4 
    
    plt.plot(x, y, 'k-', linewidth=1.5)
    plt.title('传统定期检修模式缺陷分析', fontsize=16)
    plt.xlabel('时间', fontsize=12)
    plt.ylabel('设备性能状态', fontsize=12)
    plt.ylim(0, 12)
    plt.xlim(0, 10)
    plt.xticks([])
    plt.yticks([])
    
    # Zones
    plt.axhspan(7, 10, color='lightgray', alpha=0.3)
    plt.text(1.5, 8.5, '过修区域\n(状态尚好即维修)', fontsize=10, ha='center')
    
    plt.axhspan(0, 3, color='lightgray', alpha=0.3)
    plt.text(8.5, 1.5, '失修区域\n(故障发生未及时修)', fontsize=10, ha='center')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'traditional_maintenance_problems.png'))
    plt.close()

def gen_cbm_advantages():
    labels = ['定期检修 (PM)', '状态检修 (CBM)']
    cost = [80, 40]
    reliability = [60, 95]
    
    x = np.arange(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, cost, width, label='维护成本', color='gray', alpha=0.6, edgecolor='black')
    ax.bar(x + width/2, reliability, width, label='可靠性', color='white', edgecolor='black', hatch='//')
    
    ax.set_title('状态检修与定期检修效益对比', fontsize=16)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'cbm_advantages.png'))
    plt.close()

def gen_risk_assessment_model():
    fig, ax = create_figure('风险评估模型框架结构')
    draw_box(ax, 0.5, 2, 2.5, 2, '输入数据\n(Input)\n\n- 传感器数据\n- 环境参数')
    draw_box(ax, 4, 2, 2.5, 2, '风险计算矩阵\n(Processing)\n\n概率 x 后果')
    draw_box(ax, 7.5, 2, 2, 2, '风险输出\n(Output)\n\n- 高风险\n- 中风险\n- 低风险')
    draw_arrow(ax, 3, 3, 4, 3)
    draw_arrow(ax, 6.5, 3, 7.5, 3)
    plt.savefig(os.path.join(OUTPUT_DIR, 'risk_assessment_model.png'))
    plt.close()

def gen_maintenance_strategy_classification():
    fig, ax = create_figure('维护策略分类体系')
    ax.set_ylim(0, 8)
    draw_box(ax, 4, 6, 2, 1, '维护策略')
    draw_box(ax, 1, 3, 2, 1, '事后维修\n(CM)\n故障后处理')
    draw_box(ax, 4, 3, 2, 1, '预防性维修\n(PM)\n基于时间')
    draw_box(ax, 7, 3, 2, 1, '状态维修\n(CBM)\n基于状态')
    ax.plot([5, 5], [6, 5], 'k-', lw=1.5)
    ax.plot([2, 8], [5, 5], 'k-', lw=1.5)
    ax.plot([2, 2], [5, 4], 'k-', lw=1.5)
    ax.plot([5, 5], [5, 4], 'k-', lw=1.5)
    ax.plot([8, 8], [5, 4], 'k-', lw=1.5)
    plt.savefig(os.path.join(OUTPUT_DIR, 'maintenance_strategy_classification.png'))
    plt.close()

def gen_system_testing_process():
    fig, ax = create_figure('系统验证测试流程')
    draw_box(ax, 0.5, 2.5, 1.8, 1, '单元测试\n(Unit Test)')
    draw_box(ax, 3.0, 2.5, 1.8, 1, '集成测试\n(Integration)')
    draw_box(ax, 5.5, 2.5, 1.8, 1, '系统测试\n(System Test)')
    draw_box(ax, 8.0, 2.5, 1.8, 1, '验收测试\n(Acceptance)')
    draw_arrow(ax, 2.3, 3, 3.0, 3)
    draw_arrow(ax, 4.8, 3, 5.5, 3)
    draw_arrow(ax, 7.3, 3, 8.0, 3)
    plt.savefig(os.path.join(OUTPUT_DIR, 'system_testing_process.png'))
    plt.close()

def gen_research_achievements_summary():
    fig, ax = create_figure('研究成果总结')
    draw_box(ax, 1, 1, 2, 4, '1. 故障机理分析\n\n- 触头过热\n- 绝缘劣化\n- 机械卡涩')
    draw_box(ax, 4, 1, 2, 4, '2. 监测系统设计\n\n- 传感器选型\n- 组网架构\n- 软件平台')
    draw_box(ax, 7, 1, 2, 4, '3. 维护策略优化\n\n- 状态评估\n- 故障预警\n- 差异化运维')
    draw_box(ax, 0.5, 0.2, 9, 0.6, '城市轨道交通高压开关柜在线监测与智能维护技术', fontsize=14)
    plt.savefig(os.path.join(OUTPUT_DIR, 'research_achievements_summary.png'))
    plt.close()

def gen_future_research_directions():
    fig, ax = create_figure('未来研究方向展望')
    draw_box(ax, 1, 4, 2, 1, '智能感知\n(IoT)')
    draw_box(ax, 4, 2.5, 2, 1, '大数据云计算\n(Cloud)')
    draw_box(ax, 7, 1, 2, 1, 'AI智能诊断\n(AI)')
    draw_arrow(ax, 3, 4.5, 5, 3.5)
    draw_arrow(ax, 6, 3.0, 8, 2.0)
    plt.savefig(os.path.join(OUTPUT_DIR, 'future_research_directions.png'))
    plt.close()

def gen_switchgear_structure():
    fig, ax = create_figure('高压开关柜结构组成示意图')
    
    # Outer Cabinet
    rect = patches.Rectangle((2, 0.5), 6, 5, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(rect)
    
    # Compartments
    # Top Left: Instrument Room
    draw_box(ax, 2.1, 3.5, 2.8, 1.9, '仪表室\n(继电保护)', fontsize=10)
    # Top Right: Busbar Room
    draw_box(ax, 5.1, 3.5, 2.8, 1.9, '母线室\n(主母线)', fontsize=10)
    # Middle: Circuit Breaker Room
    draw_box(ax, 2.1, 2.0, 5.8, 1.3, '断路器室\n(真空断路器)', fontsize=10)
    # Bottom: Cable Room
    draw_box(ax, 2.1, 0.6, 5.8, 1.2, '电缆室\n(电缆终端 & 互感器)', fontsize=10)
    
    plt.savefig(os.path.join(OUTPUT_DIR, 'switchgear_structure.png'))
    plt.close()

def gen_pd_monitoring_methods():
    fig, ax = create_figure('局放监测技术方法对比')
    
    # Left: TEV
    draw_box(ax, 1, 1, 3.5, 4, '', color='none', edgecolor='black')
    ax.text(2.75, 4.5, 'TEV (暂态地电压)', ha='center', fontsize=12, fontweight='bold')
    draw_box(ax, 1.5, 2.5, 2.5, 1.5, '开关柜金属外壳\n(Metal Case)', color='#f0f0f0')
    draw_box(ax, 2.0, 2.2, 1.5, 0.6, 'TEV传感器\n(贴附安装)', color='white')
    ax.text(2.75, 1.5, '检测原理:\n由于趋肤效应，\n局放电磁波在外壳\n产生感应电压', ha='center', fontsize=9)
    
    # Right: Ultrasonic
    draw_box(ax, 5.5, 1, 3.5, 4, '', color='none', edgecolor='black')
    ax.text(7.25, 4.5, '超声波 (Ultrasonic)', ha='center', fontsize=12, fontweight='bold')
    draw_box(ax, 6.0, 2.5, 2.5, 1.5, '柜体缝隙 / 观察窗\n(Gap / Window)', color='#f0f0f0')
    draw_box(ax, 6.5, 2.2, 1.5, 0.6, '超声波探头\n(非接触/接触)', color='white')
    ax.text(7.25, 1.5, '检测原理:\n局放产生振动波\n通过空气传播\n被传感器接收', ha='center', fontsize=9)
    
    plt.savefig(os.path.join(OUTPUT_DIR, 'pd_monitoring_methods.png'))
    plt.close()

if __name__ == "__main__":
    func_list = [
        gen_traditional_maintenance_problems,
        gen_cbm_advantages,
        gen_risk_assessment_model,
        gen_maintenance_strategy_classification,
        gen_system_testing_process,
        gen_research_achievements_summary,
        gen_future_research_directions,
        gen_switchgear_structure,
        gen_pd_monitoring_methods
    ]
    
    for func in func_list:
        try:
            print(f"Generating {func.__name__}...")
            func()
        except Exception as e:
            print(f"Error generating {func.__name__}: {e}")
            
    print("All python-based diagrams process completed.")
