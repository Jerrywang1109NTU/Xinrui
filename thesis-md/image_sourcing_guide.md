# 图片素材获取指南

由于部分图片属于复杂的系统架构图、原理图或实物照片，无法通过代码自动生成且必须保证中文标注的准确性，建议您按照以下清单自行查找或绘制。

## 建议获取方式
1.  **自行绘制 (Visio/PPT)**: 对于架构图和流程图，建议使用 Visio 或 PPT 绘制，这样可以完美控制中文术语。
2.  **参考文献截图**: 从您的参考文献（如文献[1]-[10]）中寻找类似的配图，截图后引用（需注明来源）。
3.  **网络素材重绘**: 在网络上找到类似图片，参考其结构重新绘制。

## 待补充图片清单

### 第一章
*   **已获取** `figs/railway_power_system.png` (城市轨道交通供电系统架构示意图)

### 第二章
*   **已获取** `figs/switchgear_structure.png` (高压开关柜结构组成示意图)
*   **figs/fault_mechanism.png**
    *   *名称*: 高压开关柜故障机理分析图
    *   *内容*: 鱼骨图或树状图，展示绝缘、机械、温升故障的成因。
    *   *建议*: 使用 XMind 或 PPT 绘制鱼骨图。
*   **figs/monitoring_requirements.png**
    *   *名称*: 在线监测系统技术需求分析
    *   *内容*: 金字塔图或列表，包含“实时性、准确性、可靠性”等指标。
*   **figs/temperature_monitoring.png**
    *   *名称*: 温度监测技术对比分析
    *   *内容*: 如红外热像仪 vs 光纤测温的示意图。
*   **已获取** `figs/pd_monitoring_methods.png` (局放监测技术方法对比)
*   **figs/mechanical_monitoring.png**
    *   *名称*: 机械特性监测系统架构
    *   *内容*: 传感器 -> 采集卡 -> PC 的连接示意图。
*   **figs/system_architecture.png**
    *   *名称*: 多参数综合监测系统架构设计
    *   *内容*: 展示“感知层-传输层-应用层”的三层架构图。
*   **figs/data_fusion_process.png**
    *   *名称*: 多源数据融合处理流程
    *   *内容*: 流程图：数据采集 -> 特征提取 -> 数据融合 -> 决策输出。

### 第三章
*   **figs/traditional_maintenance_problems.png**
    *   *名称*: 传统定期检修模式主要缺陷分析
    *   *内容*: 循环图，展示“过度维修”和“维修不足”的死循环。
*   **figs/cbm_advantages.png**
    *   *名称*: 状态检修模式优势对比分析
    *   *内容*: 对比图，展示全生命周期成本的下降曲线。
*   **figs/risk_assessment_model.png**
    *   *名称*: 风险评估模型框架结构
    *   *内容*: 矩阵图，横轴“故障概率”，纵轴“故障后果”。
*   **figs/maintenance_strategy_classification.png**
    *   *名称*: 维护策略分类体系
    *   *内容*: 决策树图：高风险->立即维修，中风险->加强监测，低风险->定期维护。
*   **figs/hybrid_maintenance_model.png**
    *   *名称*: 混合维护模式实施框架
    *   *内容*: 韦恩图或包含关系图，展示定期检修与状态检修的结合。
*   **figs/cost_benefit_analysis.png**
    *   *名称*: 维护策略成本效益分析模型
    *   *内容*: 曲线图，寻找总成本最低的最优维护点。
*   **figs/implementation_guarantee_system.png**
    *   *名称*: 维护策略实施保障体系
    *   *内容*: 房屋结构图，地基是“制度”，支柱是“技术、组织、人员”。

### 第四章
*   **figs/hardware_integration_architecture.png**
    *   *名称*: 硬件集成系统架构设计
    *   *内容*: 拓扑图，展示传感器汇聚到IED，再通过光纤到后台的连接。
*   **figs/software_integration_platform.png**
    *   *名称*: 软件集成平台功能架构
    *   *内容*: 功能模块图（数据库模块、分析模块、展示模块）。
*   **figs/system_testing_process.png**
    *   *名称*: 系统验证测试流程图
    *   *内容*: 流程图：实验室测试 -> 现场安装 -> 联调联试 -> 试运行。
*   **figs/technology_promotion_strategy.png**
    *   *名称*: 技术推广策略实施路线图
    *   *内容*: 箭头图：试点阶段 -> 示范阶段 -> 推广阶段。
*   **figs/standardization_framework.png**
    *   *名称*: 标准化建设框架体系
    *   *内容*: 框架图，包含“技术标准”、“管理标准”、“工作标准”。
*   **figs/research_achievements_summary.png**
    *   *名称*: 研究成果总结框架
    *   *内容*: 思维导图，总结论文的主要贡献。
*   **figs/future_research_directions.png**
    *   *名称*: 未来研究方向展望
    *   *内容*: 展望图，展示向“AI深度应用”和“泛在物联网”发展的趋势。

## 提示
所有图片请保存为 `png` 格式，并放置在 `figs/` 目录下，文件名需严格对应上述清单，否则论文中的图片无法显示。
