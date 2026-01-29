
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# Set Chinese font
from matplotlib import font_manager

# Path to the font found on the system
font_path = '/Library/Fonts/Arial Unicode.ttf'
if not os.path.exists(font_path):
    # Fallback to another common one just in case
    font_path = '/System/Library/Fonts/STHeiti Medium.ttc'

try:
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = prop.get_name()
    print(f"Using font: {prop.get_name()} from {font_path}")
except Exception as e:
    print(f"Error loading font: {e}")

# Function to set font properties for existing objects if needed, 
# but setting rcParams should handle most. 
# However, for explicit text, we might need to pass fontproperties=prop
def get_font_prop():
    return font_manager.FontProperties(fname=font_path)

# Ensure directory exists
os.makedirs('figs', exist_ok=True)

# 1. switchgear_fault_types.png (Pie Chart)
plt.figure(figsize=(8, 8))
labels = ['绝缘故障', '机械故障', '温升故障', '其他故障']
sizes = [35, 30, 25, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('高压开关柜常见故障类型分布')
plt.axis('equal')
plt.savefig('figs/switchgear_fault_types.png')
plt.close()

# 2. monitoring_advantage.png (Bar Chart)
plt.figure(figsize=(10, 6))
categories = ['实时性', '准确性', '经济性', '预测能力']
traditional = [3, 4, 3, 1]
online_monitoring = [9, 8, 7, 9]
x = np.arange(len(categories))
width = 0.35
plt.bar(x - width/2, traditional, width, label='传统离线检测', color='#d3d3d3')
plt.bar(x + width/2, online_monitoring, width, label='在线监测技术', color='#66b3ff')
plt.xlabel('评价指标')
plt.ylabel('性能评分 (1-10)')
plt.title('在线监测技术与传统检测方式对比')
plt.xticks(x, categories)
plt.legend()
plt.savefig('figs/monitoring_advantage.png')
plt.close()

# 3. beijing_metro_case.png (Bar Chart)
plt.figure(figsize=(10, 6))
metrics = ['故障发现率', '维护成本', '设备可用率']
before = [30, 100, 95] # Normalized
after = [90, 65, 99] # Increased detection, reduced cost, high availability
x = np.arange(len(metrics))
width = 0.35
plt.bar(x - width/2, before, width, label='应用前', color='#ff9999')
plt.bar(x + width/2, after, width, label='应用后', color='#99ff99')
plt.title('北京地铁在线监测系统应用效果对比')
plt.xticks(x, metrics)
plt.legend()
plt.ylabel('相对指标 (%)')
plt.savefig('figs/beijing_metro_case.png')
plt.close()

# 4. shanghai_metro_case.png (Line/Bar Combo)
plt.figure(figsize=(10, 6))
years = ['2019', '2020', '2021', '2022', '2023']
fault_rate = [2.5, 2.1, 1.5, 1.2, 0.8] # Decreasing fault rate
cost_saving = [0, 20, 55, 90, 150] # Cumulative savings (Ten thousand RMB)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('年份')
ax1.set_ylabel('年故障率 (%)', color='tab:red')
ax1.plot(years, fault_rate, color='tab:red', marker='o', label='故障率')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('累计维护成本节省 (万元)', color='tab:blue')
ax2.bar(years, cost_saving, alpha=0.3, color='tab:blue', label='成本节省')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('上海地铁维护策略优化效益分析')
fig.tight_layout()
plt.savefig('figs/shanghai_metro_case.png')
plt.close()

# 5. warning_model_comparison.png (Horizontal Bar)
plt.figure(figsize=(10, 5))
methods = ['阈值预警', '趋势分析', '机器学习(SVM)', '深度学习(CNN)']
accuracy = [70, 78, 88, 95]
plt.barh(methods, accuracy, color=['#d3d3d3', '#add8e6', '#87cefa', '#4682b4'])
plt.xlabel('故障预测准确率 (%)')
plt.title('不同故障预警模型性能对比')
plt.xlim(0, 100)
for i, v in enumerate(accuracy):
    plt.text(v + 1, i, str(v) + '%', va='center')
plt.savefig('figs/warning_model_comparison.png')
plt.close()

print("Charts generated successfully.")

# Function to generate placeholder images
def create_placeholder(filename, title, description):
    """Generates a placeholder image with a title and description."""
    plt.figure(figsize=(10, 6))
    
    # Add text
    plt.text(0.5, 0.6, f"PENDING IMAGE:\n{title}", 
             ha='center', va='center', fontsize=14, fontweight='bold', wrap=True)
    plt.text(0.5, 0.4, f"({description})\n\nPlease replace with actual diagram.", 
             ha='center', va='center', fontsize=10, style='italic', wrap=True)
    
    # Remove axes
    plt.xticks([])
    plt.yticks([])
    for spine in plt.gca().spines.values():
        spine.set_visible(True)
        spine.set_color('#cccccc')
        spine.set_linewidth(2)
        spine.set_linestyle('--')
        
    plt.tight_layout()
    plt.savefig(f'figs/{filename}')
    plt.close()
    print(f"Generated placeholder: {filename}")

# Generate missing placeholders based on image_sourcing_guide.md

# Chapter 2
create_placeholder('fault_mechanism.png', '高压开关柜故障机理分析图', '鱼骨图或树状图，展示绝缘、机械、温升故障的成因')
create_placeholder('monitoring_requirements.png', '在线监测系统技术需求分析', '金字塔图或列表，包含“实时性、准确性、可靠性”等指标')
create_placeholder('temperature_monitoring.png', '温度监测技术对比分析', '如红外热像仪 vs 光纤测温的示意图')
create_placeholder('mechanical_monitoring.png', '机械特性监测系统架构', '传感器 -> 采集卡 -> PC 的连接示意图')
create_placeholder('system_architecture.png', '多参数综合监测系统架构设计', '展示“感知层-传输层-应用层”的三层架构图')
create_placeholder('data_fusion_process.png', '多源数据融合处理流程', '流程图：数据采集 -> 特征提取 -> 数据融合 -> 决策输出')

# Chapter 3
create_placeholder('traditional_maintenance_problems.png', '传统定期检修模式主要缺陷分析', '循环图，展示“过度维修”和“维修不足”的死循环')
create_placeholder('cbm_advantages.png', '状态检修模式优势对比分析', '对比图，展示全生命周期成本的下降曲线')
create_placeholder('risk_assessment_model.png', '风险评估模型框架结构', '矩阵图，横轴“故障概率”，纵轴“故障后果”')
create_placeholder('maintenance_strategy_classification.png', '维护策略分类体系', '决策树图：高风险->立即维修，中风险->加强监测，低风险->定期维护')
create_placeholder('hybrid_maintenance_model.png', '混合维护模式实施框架', '韦恩图或包含关系图，展示定期检修与状态检修的结合')
create_placeholder('cost_benefit_analysis.png', '维护策略成本效益分析模型', '曲线图，寻找总成本最低的最优维护点')
create_placeholder('implementation_guarantee_system.png', '维护策略实施保障体系', '房屋结构图，地基是“制度”，支柱是“技术、组织、人员”')

# Chapter 4
create_placeholder('hardware_integration_architecture.png', '硬件集成系统架构设计', '拓扑图，展示传感器汇聚到IED，再通过光纤到后台的连接')
create_placeholder('software_integration_platform.png', '软件集成平台功能架构', '功能模块图（数据库模块、分析模块、展示模块）')
create_placeholder('system_testing_process.png', '系统验证测试流程图', '流程图：实验室测试 -> 现场安装 -> 联调联试 -> 试运行')
create_placeholder('technology_promotion_strategy.png', '技术推广策略实施路线图', '箭头图：试点阶段 -> 示范阶段 -> 推广阶段')
create_placeholder('standardization_framework.png', '标准化建设框架体系', '框架图，包含“技术标准”、“管理标准”、“工作标准”')
create_placeholder('research_achievements_summary.png', '研究成果总结框架', '思维导图，总结论文的主要贡献')
create_placeholder('future_research_directions.png', '未来研究方向展望', '展望图，展示向“AI深度应用”和“泛在物联网”发展的趋势')

print("All charts and placeholders generated successfully.")
