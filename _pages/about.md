---
permalink: /
title: ""
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

I'm first-year Master's student from [School of Biomedical Engineering](https://www.med.tsinghua.edu.cn/en/), [Tsinghua University](https://www.tsinghua.edu.cn/). My research interests include Medical Image Analysis, Multimodal Learning, and Foundation Models.

I am very fortunate to be advised by [Prof. Qiyuan Tian](https://www.med.tsinghua.edu.cn/info/1143/2126.htm) of [Birth Lab](https://birthlab.github.io/) from [School of Biomedical Engineering](https://bme.tsinghua.edu.cn/index.htm), Tsinghua University. 

Other related links: [Github](https://github.com/JasonW375) / [Wechat](../images/Wechat.jpg) / [Google scholar](https://scholar.google.com/citations?user=n9lAi4cAAAAJ).

<a href='https://scholar.google.com/citations?user=n9lAi4cAAAAJ'>
  <img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations">
</a>

# 🔥 News
**2026.07.10:** 🎉🎉 Attended the Medical Image Computing Seminar (MICS) 2026.

**2026.06.03:** 🎉🎉 Attended BME 2026 (China Biomedical Engineering Conference & Medical Innovation Summit) and received the **Excellent Paper Competition Third Prize**.

**2026.03.04:** 🎉🎉 Attended the ISMRM Workshop on Unlocking the Potential of Prenatal MRI in Washington, D.C.

**2025.12.14:** 🎉🎉 Attended the Doctoral Interdisciplinary Frontier Forum & 810th Doctoral Academic Forum (Tsinghua University) and won **Second Prize** (¥3,000). [Photo](https://www.imagehub.cc/image/MxmaAk) 

**2025.11.22:** 🎉🎉 Attended the 2nd Graduate Academic Forum (School of Biomedical Engineering & School of Clinical Medicine, Tsinghua University). [Photo](https://www.imagehub.cc/image/MxZATa) 

**2025.09.27:** 🎉🎉 Attended MICCAI 2025 in Daejeon, South Korea; won **Second Prize** in the MICCAI [VLM3D Challenge](https://vlm3dchallenge.com/) .[Photo](https://www.imagehub.cc/image/MxZ5Rd)

**2025.07.19:** 🎉🎉 Awarded **First Prize** in the **10th National Biomedical Engineering Innovation Design Competition**. [News](https://mp.weixin.qq.com/s/X08abfkwGJyQ_52iI1ipBQ)

**2025.06.21:** 🎉🎉 Awarded **Outstanding Undergraduate Graduate of Tsinghua University(Top 2%)** [News 1](https://mp.weixin.qq.com/s/gRv7w17NJLcrCjEdPloFDg) [News 2](https://mp.weixin.qq.com/s/NN7nEb1bkVdsl06YXWUePw)

**2025.05.11:** 🎉🎉 Selected as **Tsinghua University School of Medicine Annual Undergraduate Figure**. [News](https://mp.weixin.qq.com/s/kkYmXmvPJEN1xpuxjKlxrw)

**2025.04.28:** 🎉🎉 Our [Chest-OMDL](https://openreview.net/forum?id=ns6nq592HX#discussion) Project got reported by official media of Tsinghua University. [X](https://x.com/Tsinghua_Uni/status/1916809961021100041) [Facebook](https://www.facebook.com/share/p/1BmmJHNuxG)

**2025.04.28:** 🎉🎉 Our paper addressed [Multidisease Detection and Localization](https://openreview.net/forum?id=ns6nq592HX#discussion) has been accepted by [MIDL 2025](https://2025.midl.io/).

# 📝 Publications 
<span style="color:#b02418; font-weight:bold;">#</span> co-first author | <span style="color:#b02418; font-weight:bold;">*</span> corresponding author | status / venue shown in italics <br> 

#### JOURNAL PAPERS
<ol reversed>
  <li> 
    <span style="color:#000000; font-weight:bold;">EXACT: An Explainable Anomaly-aware Vision Foundation Model for Analysis of 3D Chest CT</span> <br>
    <a href="https://arxiv.org/abs/2604.24146">[Paper]</a> <br> 
    <span style="color:#b02418; font-weight:bold;">Xuguang Bai#</span>, Mingxuan Liu#*, Tongxi Song#, Yifei Chen#, Hongjia Yang, Kasidit Anmahapong, Zihan Li, Ying Zhou, Qiyuan Tian* <br>
    <i>npj Digital Medicine.</i> 2026. (Major Revision)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Towards Reliable Fetal Ultrasound Interpretation with Multi-Agent Collaboration</span> <br>
    <a href="https://arxiv.org/abs/2605.25357">[Paper]</a> <br> 
    Xiaotian Hu#, Mingxuan Liu#, Junwei Huang#, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Zihan Li, Yi Liao, Haibo Qu*, Qiyuan Tian* <br>
    <i>Medical Image Analysis <strong>(MedIA).</strong></i> 2026. (Major Revision)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Towards Generalizable and Expert-level Fetal MRI Report Impression Generation via Adaptive Fine-tuning of Large Language Models</span> <br>
    Yijin Li#, Mingxuan Liu#, X. Zhang#, Yi Liao#, W. Chen, Kasidit Anmahapong, Z. Wang, Yifei Chen, Hongjia Yang, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, D. Yue, X. Liu, N. Sun, R. Hu, M. Kang, Y. Song, H. Lai, X. Zhou, Juncheng Zhu, F. Jia, G. Ning, Haibo Qu*, Qiyuan Tian* <br>
    <i>npj Digital Medicine.</i> 2026. (Major Revision)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">A Multimodal Foundation Model for Emergency Head CT Interpretation</span> <br>
    Jingyuan Zheng#, Yifei Chen#, Beining Wu#, Yuanhan Wang#, Mingxuan Liu#, Lu Li, Shuo Jiang, Weihong Chen, Liaoman Xu, Yueyi Wu, Chang Liu, Lulu Guo, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Zihan Li, Hongjia Yang, Feiwei Qin, Jingzhe Liu, Haibo Qu, Qiang Liao, Gang Zhao, Keqin Pan, Jun Guo, Lizhou Chen, Ying Zhou, Huaiqiang Sun*, Qiyuan Tian* <br>
    <i>Science Bulletin. </i> 2026. (Major Revision, medRxiv 2026.07.07.26357429)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">A Retrospective Study of a Chinese Vision-Language Large Model for Emergency 3D Brain CT Interpretation</span> <br>
    Yifei Chen#, Jingyuan Zheng#, Yuanhan Wang#, Beining Wu, Lu Li, Mingxuan Liu, Liaoman Xu, Yueyi Wu, Chang Liu, Lulu Guo, Hongjia Yang, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Feiwei Qin, Qiang Liao, Yong Gu, Gang Zhao, Lu Ma, Keqin Pan, Jun Guo, Ying Zhou, Huaiqiang Sun*, Qiyuan Tian* <br>
    <i>medRxiv preprint. </i> 2026. (medRxiv 2026.07.11.26357421)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Preoperative CTA-based Deep Learning Model for Predicting AKI After TEVAR in Type B Aortic Dissection</span> <br>
    Mingxuan Liu#, <span style="color:#b02418; font-weight:bold;">Xuguang Bai#</span>, M. Zhang, Yifei Chen, Hongjia Yang, Z. Wang, Yitong Luo, Ying Zhou, X. Han*, Qiyuan Tian <br>
    <i>Radiology: Artificial Intelligence <strong>(Radiology: AI).</strong></i> 2026. (Under Review)
  </li>
</ol>

#### CONFERENCE PAPERS
<ol reversed>
  <li> 
    <span style="color:#000000; font-weight:bold;">FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis</span> <br>
    <a href="https://arxiv.org/abs/2603.09733">[Paper]</a> <a href="https://github.com/birthlab/FetalAgents">[Code]</a> <br> 
    Xiaotian Hu#, Junwei Huang#, Mingxuan Liu#, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Zihan Li, Yi Liao, Haibo Qu, Qiyuan Tian* <br>
    <i>International Conference on Medical Image Computing and Computer Assisted Intervention <strong>(MICCAI).</strong></i> 2026. (Early Accept, Top 9%)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">WARPNet: Scale-wise Autoregressive Cross-modal Synthesis for Accurate and Detail-preserving MRI-to-PET Generation</span> <br>
    <a href="https://ieeexplore.ieee.org/abstract/document/11356448">[Paper]</a> <a href="https://github.com/Guanyu-Zhou/WARPNet">[Code]</a> <br> 
    Guanyu Zhou#, Yifei Chen#, Gaoxiang Ying, Mingxuan Liu, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Jialan Zheng, Bixiao Cui, Qiyuan Tian*, Jie Lu*<br> 
    <i>IEEE International Conference on Bioinformatics and Biomedicine <strong>(BIBM).</strong></i> 2025. (Oral)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">FetalExtract-LLM: Structured Information Extraction in Free-Text Fetal MRI Reports Based on Privacy-Ensuring Open-weights Large Language Models</span> <br>
    <a href="https://link.springer.com/chapter/10.1007/978-3-032-05997-0_11">[Paper]</a> <br> 
    Mingxuan Liu#, Yijin Li#, Juncheng Zhu#, Hongjia Yang, Yiming Huang, Haoxiang Li, Yifei Chen, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Yi Liao, Haibo Qu, Qiyuan Tian*<br> 
    <i> MICCAI Workshop on Perinatal, Preterm and Paediatric Image Analysis <strong>(PIPPI). </strong></i> 2025. (Oral)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Chest-OMDL: Organ-specific Multidisease Detection and Localization in Chest CT Using Weakly Supervised Deep Learning from Free-text Radiology Report</span> <br>
    <a href="https://openreview.net/forum?id=ns6nq592HX">[Paper]</a> <a href="https://github.com/JasonW375/Chest-OMDL">[Code]</a> <br> 
    <span style="color:#b02418; font-weight:bold;">Xuguang Bai#</span>, Mingxuan Liu#, Yifei Chen, Hongjia Yang, Qiyuan Tian* <br>
    <i>Medical Imaging with Deep Learning <strong>(MIDL). </strong></i> 2025. (MICCAI 2025 VLM3D Challenge 2nd Place Winner)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">FetalCSR: Multi-input Attention Fusion Network for Neural ODE-based Fetal Cortical Surface Reconstruction</span> <br>
    <a href="https://openreview.net/forum?id=Ra0xioC3He">[Paper]</a> <a href="https://github.com/lhx-lhx-lhx/FetalCSR">[Code]</a> <br> 
    Haoxiang Li#, Mingxuan Liu#, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Yi Liao, Jialan Zheng, Hongjia Yang, Zihan Li, Haibo Qu, Qiyuan Tian* <br>
    <i>ICLR 2025 Workshop on AI for Children <strong>(ICLR Workshop). </strong></i> 2025. (Oral)
  </li>
</ol>

#### CONFERENCE ABSTRACTS
<ol reversed>
  <li> 
    <span style="color:#000000; font-weight:bold;">Preoperative CTA-based Deep Learning Model for Predicting AKI After TEVAR in Type B Aortic Dissection</span> <br>
    <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Mingxuan Liu, M. Zhang, Hongjia Yang, Z. Wang, Yitong Luo, Ying Zhou, X. Han, Qiyuan Tian <br>
    <i>China Biomedical Engineering Conference & Medical Innovation Summit <strong>(BME). </strong></i> 2026. (Oral, Excellent Paper Competition Third Prize)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Quality-Label-Free Stack-Level Quality Control Improves Fetal Brain Slice-to-Volume Reconstruction</span> <br>
    Mingxuan Liu, Yingqi Hao, Yi Liao, Haoxiang Li, Juncheng Zhu, Hongjia Yang, Yifei Chen, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Haibo Qu, Qiyuan Tian* <br>
    <i>ISMRM Workshop on Unlocking the Potential of Prenatal MRI. </i> 2026. (Traditional Poster)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">AlignPET: Structure-Aligned MRI-to-PET Synthesis via Variational Autoregression Model for Ischemic Brain Lesions</span> <br>
    Yifei Chen, Guanyu Zhou, Y. Wang, Mingxuan Liu, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Jialan Zheng, Bixiao Cui, Jie Lu, Qiyuan Tian* <br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2026. (Oral Power Pitch)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Automated Induction of Standardized Reporting Templates from Fetal Brain MRI Free-Text Corpora</span> <br>
    X. Zhang, Mingxuan Liu, Hongjia Yang, Yifei Chen, Juncheng Zhu, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Yiming Huang, Yingqi Hao, Zihan Li, Yi Liao, G. Ning, Haibo Qu, Qiyuan Tian* <br>
    <i>OHBM Annual Meeting <strong>(OHBM). </strong></i> 2026. (Poster)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Modality-Agnostic PET Synthesis from Single-Modality Thick-Slice MRI via Structured MRI-PET Mapping</span> <br>
    Yifei Chen, Guanyu Zhou, Y. Wang, Mingxuan Liu, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Jialan Zheng, Bixiao Cui, Jie Lu, Qiyuan Tian* <br>
    <i>OHBM Annual Meeting <strong>(OHBM). </strong></i> 2026. (Poster)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">From Free Text to Usable Labels: Privacy-Ensuring Open-weights LLM-Enhanced Clinical Report Extraction for Fetal MRI</span> <br>
    <a href="https://hal.science/hal-05330462">[Paper]</a> <br> 
    Mingxuan Liu, Yijin Li, Juncheng Zhu, Hongjia Yang, Yiming Huang, Haoxiang Li, Yifei Chen, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Yi Liao, Haibo Qu, Qiyuan Tian* <br>
    <i>Beijing-Tsinghua Health AI Summit <strong>(BEIHAI). </strong></i> 2025. (Oral, Second Prize of Oral Presentation)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Anatomy-guided Test-Time Adaptation for Automated Fetal Brain MRI Morphometry</span> <br>
    <a href="https://openreview.net/forum?id=iLBipDelQu">[Paper]</a> <br> 
    Yijin Li#, Mingxuan Liu#, Hongjia Yang, Haoxiang Li, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Yi Liao, Haibo Qu, Qiyuan Tian* <br>
    <i>Medical Imaging with Deep Learning <strong>(MIDL). </strong></i> 2025. (Poster)
  </li>

  <li> 
    <span style="color:#000000; font-weight:bold;">Comprehensive Evaluation of Unsupervised Image Enhancement for Volumetric Fetal Brain MRI</span> <br>
    <a href="https://openreview.net/forum?id=RY54DHewSk">[Paper]</a> <a href="https://github.com/yingqihao2022/FetalBrainEnhancement">[Code]</a> <br> 
    Yingqi Hao#, Mingxuan Liu#, Hongjia Yang, Haoxiang Li, <span style="color:#b02418; font-weight:bold;">Xuguang Bai</span>, Yi Liao, Haibo Qu, Qiyuan Tian* <br>
    <i>Medical Imaging with Deep Learning <strong>(MIDL). </strong></i> 2025. (Poster)
  </li>
</ol>



# 🎖 Honors and Awards
- [[Certificate]](https://www.imagehub.cc/image/Mxzg2R) *2025* **Second Prize of Oral Presentation**, 810th Doctoral Academic Forum (Doctoral Interdisciplinary Frontier Forum), Tsinghua University
- [[Certificate]](https://www.imagehub.cc/image/MxmSsB) *2025* **MICCAI [VLM3D Challenge](https://vlm3dchallenge.com/challenges/) 2nd Place Winner**
- [[Certificate]](https://www.imagehub.cc/image/ISa5ed) *2025* **First Prize in the 10th National Biomedical Engineering Innovation Design Competition**, China.
- [[Certificate]](https://www.imagehub.cc/image/IaTQmA) *2025* **Outstanding Graduate Award (Top 2%)**, Tsinghua University
- [[Certificate]](https://www.imagehub.cc/image/IaTjVR) *2025* **Tsinghua University School of Medicine Annual Undergraduate Figure**, Tsinghua University
- [[Certificate]](https://www.imagehub.cc/image/IaTVrJ) *2024* **National Scholarship, Ministry of Education**, P.R. China (Top 1 in department) <br /> &nbsp; &nbsp; &nbsp; *Top scholarship in China. 0.2% domestically*.
- [[Certificate]]() *2023* **Scholarship for Comprehensive Academic Excellence**, Tsinghua University 
- [[Certificate]](https://www.imagehub.cc/image/IaT45U) *2022* **Scholarship for Athletic Achievement**, Tsinghua University 
- [[Certificate]](https://www.imagehub.cc/image/IaVrU0) *2022* **Third Prize in the 25th Hardware Design Competition**, Tsinghua University.

# 📖 Educations
- *2025.09 - 2028.06*, Master's student: **School of Biomedical Engineering**, Tsinghua University, China. 
- *2021.09 - 2025.06*, Undergraduate student: **School of Biomedical Engineering**, Tsinghua University, China. 
  
# ⚽️ Sports Activities and Honors
- *2025.05*, Placed 5th in the Capital University Football League (Group B, non-athletic recruit), representing Tsinghua University in Beijing.
- *2025.04*, Participated in a friendly match with former Chinese National Team players Huang Bowen and Yu Dabao. [Photo A](https://www.imagehub.cc/image/IaTHRo) [Photo B](https://www.imagehub.cc/image/IaTy6a)
- *2024.11*, Placed 4th in the Capital University Football League (Group B, non-athletic recruit), representing Tsinghua University. [Photo](https://www.imagehub.cc/image/IaTPJz)
- *2024.10*,Participated in football exchange activities in Xinjiang, China, as a member of the Tsinghua University Men's Football Team. [Photo A](https://www.imagehub.cc/image/IaTLKO) [Photo B](https://www.imagehub.cc/image/IaTiAd)
- *2024.09*, Selected as a regular member (non-athletic recruit) of the Tsinghua University Men's Football Team. [Photo](https://www.imagehub.cc/image/IaThxe)
- *2024.05*, Placed 4th in the Men's 200m at the Tsinghua University Athletics Meet. [Photo](https://www.imagehub.cc/image/IaTxLq)
- *2024.05*, Placed 7th in the Men's 100m at the Tsinghua University Athletics Meet. [Photo](https://www.imagehub.cc/image/IaTttB)
- *2024.04*, As team captain, led the School of Medicine to successfully remain in Group B of the Tsinghua University Ma Yuehan Cup Football League. [Photo](https://www.imagehub.cc/image/IaTsgg)
- *2023.05*, Placed 4th in the Tsinghua University Ma Yuehan Cup Group A Football League, as a starting member of the Department of Electronic Engineering team. [Photo](https://www.imagehub.cc/image/IaTRmj) 
- *2022.05*, Won the Championship in the Tsinghua University Freshmen Cup Football Tournament. [Photo](https://www.imagehub.cc/image/IaTG60)
- *2021.10*, Won the Men's 100m Championship at the Tsinghua University Barefoot Athletics Meet. 

# 🔗 LINKS
BIRTHLab: [The lab for Brain Imaging Research at Tsinghua](https://birthlab.github.io/)<br>Mingxuan Liu:: [School of Biomedical Engineering, Tsinghua University](https://arktis2022.github.io/)<br>Haoxiang Li: [School of Biomedical Engineering, Tsinghua University](https://lihaoxiang-20.github.io/)<br>Yifei Chen: [School of Biomedical Engineering, Tsinghua University](https://justlfc03.github.io/)<br>Jianglan Zheng: [School of Biomedical Engineering, Tsinghua University](https://zjl21.github.io/)<br>Yingqi Hao: [School of Biomedical Engineering, Tsinghua University](https://yingqihao2022.github.io/)
