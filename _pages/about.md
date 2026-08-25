---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am Jianyi Zhou (周健毅), a Ph.D. student at Harbin Institute of Technology, Shenzhen.

My research interests include embodied intelligence, tactile dexterous manipulation, embodied AI security, and agent systems and code intelligence for complex software engineering tasks.


# 🔥 News
- *2026.07*: &nbsp;Our paper [TouchWorld](https://arxiv.org/abs/2607.07287) was released on arXiv!
- *2026.05*: &nbsp;Our project [TouchAnything](https://jianyi2004.github.io/TouchAnything-Website/) was released!
- *2025.12*: &nbsp;🎉🎉 Awarded National Scholarship!
- *2025.08*: &nbsp;🏆 Won First Prize in National College Student Operating System Competition
- *2025.05*: &nbsp;🎉 Nominated for Outstanding Winner (Top 1.4% globally) in MCM/ICM as Team Leader 

# 📝 Publications 
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/TouchWorld.png' alt="TouchWorld predictive and reactive tactile manipulation framework" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](https://arxiv.org/pdf/2607.07287)

**Jianyi Zhou**<sup>\*</sup>, Feiyang Hong<sup>\*</sup>, Yunhao Li<sup>\*</sup>, Yicheng Zhao, Yongjue Cen, Zirui Liu, Jiakang Huang, Zirui Chen, Ruiyang Zhang, Weizhuo Zhu, Xuhua Song, Shuo Yang<sup>†</sup>

*Harbin Institute of Technology, Shenzhen; PHANES AI* &nbsp; (<sup>\*</sup> Equal contribution; <sup>†</sup> Corresponding author)

[**Project Page**](https://phanes-lab.github.io/TouchWorld-website/) / [**Paper**](https://arxiv.org/pdf/2607.07287)
- A predictive-and-reactive tactile foundation model that combines contact-aware tactile subgoal prediction with high-frequency residual refinement for robust dexterous manipulation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Research Project</div><img src='images/TouchAnytining.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TouchAnything: A Dataset and Framework for Bimanual Tactile Estimation from Egocentric Video](https://jianyi2004.github.io/TouchAnything-Website/)

**Jianyi Zhou**, Ziteng Gao, Feiyang Hong, Zirui Liu, Guannan Zhang, Weisheng Dai, Ruichen Zhen, Chuqiao Lyu, Haotian Wu, Yinian Mao, Xushi Wang, Yuxiang Jiang, Shuo Yang

*Harbin Institute of Technology, Shenzhen; Meituan Academy of Robotics*

[**Project Page**](https://jianyi2004.github.io/TouchAnything-Website/)
- The first large-scale multi-view tactile dataset for egocentric hand-object interaction with bimanual 3D hand pose annotations and dense continuous pressure maps.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Research Project · 2025.08</div><img src='images/kfc-agent.png' alt="KFC-Agent multi-turn Linux kernel crash repair agent" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[KFC-Agent: Kernel Fault Corrector-Agent for Automated Linux Kernel Crash Repair](https://github.com/oscomp/first-prize-osf2025-LLM-based-kdump-analysis/tree/main)

**Jianyi Zhou**, Qin Yuhuai, Yue Liang

*Harbin Institute of Technology, Shenzhen*

[**Code Repository**](https://github.com/oscomp/first-prize-osf2025-LLM-based-kdump-analysis/tree/main)
- A multi-turn agent that explores crash reports, kernel source code, and execution feedback through an interactive Docker/SWE-ReX environment instead of generating a patch from a single long context.
- Combines extensible tools with trace-based call-graph retrieval, a Planner built from historical crash reports and developer discussions, and a Memory module for reusable debugging experience.
- On kbench with DeepSeek-V3 and four patches, KFC-Agent reaches 60.22% execution success, compared with 6.45% for kGym; its per-instance cost is $0.28.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2025</div><img src='images/INFUSE.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Inject Once Survive Later: Backdooring Vision-Language-Action Models to Persist Through Downstream Fine-tuning](https://arxiv.org/pdf/2602.00500)

**Jianyi Zhou**, Yujie Wei, Ruichen Zhen, Bo Zhao, Xiaobo Xia, Rui Shao, Xiu Su, Shuo Yang

*Harbin Institute of Technology, Shenzhen; Meituan Academy of Robotics; Shanghai Jiaotong University; National University of Singapore; Central South University*

[**Paper**](https://arxiv.org/pdf/2602.00500)
- Research on backdoor attacks and security vulnerabilities in vision-language-action models for embodied AI systems.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2025</div><img src='images/Conla.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[ConLA: Contrastive Latent Action Learning from Human Videos for Robotic Manipulation](https://arxiv.org/pdf/2602.00557)

Weisheng Dai, Kai Lan, **Jianyi Zhou**, Bo Zhao, Xiu Su, Junwen Tong, Weili Guan, Shuo Yang

*Harbin Institute of Technology, Shenzhen; ZTE Corporation; Shanghai Jiao Tong University; Central South University*

[**Paper**](https://arxiv.org/pdf/2602.00557)
- Contrastive latent action learning framework for robotic manipulation from human demonstration videos.
</div>
</div>

# 🎖 Honors and Awards
- *2025.12* National Scholarship (国家奖学金)
- *2025.05* Mathematical Contest in Modeling (MCM/ICM) - Nominated for Outstanding Winner (Top 1.4% globally), Team Leader
- *2025.08* National College Student Operating System Competition - First Prize (全国大学生操作系统大赛一等奖) 

# 📖 Education
- *2026.09 - 2029.06 (Expected)*, Ph.D. student at Harbin Institute of Technology, Shenzhen, advised by Prof. [Shuo Yang](https://homepage.hit.edu.cn/yangshuohit?lang=zh)
- *2022.09 - 2026.06*, B.Eng. in Computer Science and Technology, Harbin Institute of Technology, Shenzhen

# 💻 Research Experience
- *2025.01 - Present*, Research Intern in the group led by Prof. [Shuo Yang](https://homepage.hit.edu.cn/yangshuohit?lang=zh) at Harbin Institute of Technology, Shenzhen, focusing on tactile sensing and embodied AI
