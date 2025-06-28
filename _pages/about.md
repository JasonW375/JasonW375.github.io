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

I'm Four-year undergraduate student from [School of Biomedical Engineering](https://www.med.tsinghua.edu.cn/en/), [Tsinghua University](https://www.tsinghua.edu.cn/). My research interests include Medical Image Analysis, Multimodal Learning, and Foundation Models.

I am very fortunate to be advised by [Prof. Qiyuan Tian](https://www.med.tsinghua.edu.cn/info/1143/2126.htm) of [Birth Lab](https://birthlab.github.io/) from [School of Biomedical Engineering](https://bme.tsinghua.edu.cn/index.htm), Tsinghua University. 

Other related links: [Github](https://github.com/JasonW375) / [Wechat](../images/wechat.jpg) / [Google scholar](https://scholar.google.com/citations?user=n9lAi4cAAAAJ).

<a href='https://scholar.google.com.hk/citations?hl=zh-CN&user=n9lAi4cAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>

# 🔥 News
**2025.06.21:** 🌟 Awarded **Outstanding Undergraduate Graduate of Tsinghua University** (only 75 graduates awarded across the entire university). [Certificate News 1](https://mp.weixin.qq.com/s/gRv7w17NJLcrCjEdPloFDg) | [Certificate News 2](https://mp.weixin.qq.com/s/NN7nEb1bkVdsl06YXWUePw)

**2025.05.11:** 🌟 Selected as **Tsinghua University School of Medicine Annual Undergraduate Figure**. [Official News](https://mp.weixin.qq.com/s/kkYmXmvPJEN1xpuxjKlxrw)

**2025.04.28:** 🌟 My work "**Chest-OMDL: Organ-specific Multidisease Detection and Localization in Chest Computed Tomography using Weakly Supervised Deep Learning from Free-text Radiology Report**" was featured as a typical example of innovative research by Tsinghua University and shared globally via the official [X Platform](https://x.com/Tsinghua_Uni/status/1916809961021100041) / [Facebook Page](https://www.facebook.com/share/p/1BmmJHNuxG)

**2025.03.27:** 🌟 Our paper "**Chest-OMDL: Organ-specific Multidisease Detection and Localization in Chest Computed Tomography using Weakly Supervised Deep Learning from Free-text Radiology Report**" has been accepted by [MIDL 2025 (International Conference on Medical Imaging with Deep Learning)](https://2025.midl.io/) as poster.


# 📝 Publications 
<span style="color:#b02418; font-weight:bold;">#</span> co-first author | <span style="color:#b02418; font-weight:bold;">*</span> corresponding author <br> 

#### JOURNAL PAPERS
<ol reversed>
<li id="JP-Pub2"> 
    <span style="color:#000000; font-weight:bold;">Spiking-PhysFormer: Camera-Based Remote Photoplethysmography with Parallel Spike-driven Transformer</span> <br> 
    <a href="https://www.sciencedirect.com/science/article/pii/S0893608025000073">[Paper]</a> <br> 
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu#</span>, Jiankai Tang#, Chengli Yong, Haoxiang Li, Jiahao Qi, Siwei Li, Kegang Wang, Jie Gan, Yuntao Wang*, Hong Chen* <br>
    <i>Neural Networks <strong>(NN). </strong></i> 2025. 
  </li>
  
  <li id="JP-Pub1"> 
    <span style="color:#000000; font-weight:bold;">Anomaly Detection for Medical Images Using Teacher-Student Model with Skip Connections and Multi-scale Anomaly Consistency</span> <br>
    <a href="https://doi.org/10.1109/TIM.2024.3406792">[Paper]</a> <a href="https://github.com/Arktis2022/Skip-TS">[Code]</a> <br> 
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Yunrui Jiao, Jingqiao Lu, Hong Chen* <br>
    <i>IEEE Transactions on Instrumentation and Measurement <strong>(IEEE TIM). </strong></i> 2024.
  </li>
</ol>

#### CONFERENCE PAPERS
<ol reversed>
  <li id="CP-Pubx"> 
    <span style="color:#000000; font-weight:bold;">Chest-OMDL: Organ-specific Multidisease Detection and Localization in Chest Computed Tomography using Weakly Supervised Deep Learning from Free-text Radiology Report</span> <br>
    <a href="https://openreview.net/forum?id=ns6nq592HX&referrer=%5Bthe%20profile%20of%20Yifei%20Chen%5D(%2Fprofile%3Fid%3D~Yifei_Chen18">[Paper]</a> <br> 
    Xuguang Bai#, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu#</span>, Yifei Chen, Hongjia Yang, Qiyuan Tian* <br>
    <i>Medical Imaging with Deep Learning <strong>(MIDL). </strong></i> 2025. (Submitted)
  </li>

  <li id="CP-Pubx"> 
    <span style="color:#000000; font-weight:bold;">FetalCSR: Multi-input Attention Fusion Network for Neural ODE-based Fetal Cortical Surface Reconstruction</span> <br>
    <a href="https://openreview.net/forum?id=Ra0xioC3He">[Paper]</a> <br> 
    Haoxiang Li#, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu#</span>, Xuguang Bai, Yi Liao, Jialan Zheng, Hongjia Yang, Zihan Li, Haibo Qu, Qiyuan Tian* <br>
    <i>ICLR 2025 Workshop on AI for Children <strong>(ICLR Workshop). </strong></i> 2025. (Oral Paper Presentation)
  </li>
  
  <li id="CP-Pub1"> 
    <span style="color:#000000; font-weight:bold;">Spike-SLR: An Energy-efficient Parallel Spiking Transformer for Event-based Sign Language Recognition</span> <br>
    <a href="https://bmva-archive.org.uk/bmvc/2024/papers/Paper_493/paper.pdf">[Paper]</a>  <a href="https://bmvc2024.org/proceedings/493/">[Project]</a> <br> 
    Xinxu Lin#, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu#</span>, Kezhuo Liu, Hong Chen* <br>
    <i>The British Machine Vision Conference <strong>(BMVC). </strong></i> 2024. (Poster)
  </li>

  <li id="CP-Pub2"> 
    <span style="color:#000000; font-weight:bold;">SAM-Deblur: Let Segment Anything Boost Image Deblurring</span> <br>
    <a href="https://ieeexplore.ieee.org/abstract/document/10445844">[Paper]</a> <a href="https://hplqaq.github.io/projects/sam-deblur">[Project]</a>  <br> 
    Siwei Li#, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu#</span>, Yating Zhang, Shu Chen, Haoxiang Li, Hong Chen*, Zifei Dou* <br>
    <i>IEEE International Conference on Acoustics, Speech and Signal Processing <strong>(ICASSP). </strong></i> 2024. (Poster)
  </li>

  <li id="CP-Pub6"> 
    <span style="color:#000000; font-weight:bold;">Spiking-Diffusion: Vector Quantized Discrete Diffusion Model with Spiking Neural Networks</span> <br>
    <a href="https://arxiv.org/abs/2308.10187">[Paper]</a> <a href="https://github.com/Arktis2022/Spiking-Diffusion">[Code]</a> <br> 
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu#</span>, Jie Gan#, Rui Wen#, Tao Li, Yongli Chen, Hong Chen* <br>
    <i>IEEE International Conference on Computer, Big Data and Artificial Intelligence <strong>(ICCBD+AI). </strong></i> 2024. (Best Paper Award)
  </li>

  <li id="CP-Pub3"> 
    <span style="color:#000000; font-weight:bold;">Skip-ST: Anomaly Detection for Medical Images Using Student-Teacher Network with Skip Connections</span> <br>
    <a href="https://ieeexplore.ieee.org/abstract/document/10181639">[Paper]</a> <br> 
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Yunrui Jiao, Hong Chen* <br>
    <i>IEEE International Symposium on Circuits and Systems <strong>(ISCAS). </strong></i> 2023. (Oral Paper Presentation)
  </li>

  <li id="CP-Pub4"> 
    <span style="color:#000000; font-weight:bold;">PRTMTM: A Priori Regularization Method for Tooth-Marked Tongue Classification</span> <br>
    <a href="https://ieeexplore.ieee.org/abstract/document/10181870">[Paper]</a> <br> 
    Jingqiao Lu, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Hong Chen* <br>
    <i>IEEE International Symposium on Circuits and Systems <strong>(ISCAS). </strong></i> 2023. (Poster)
  </li>

  <li id="CP-Pub5"> 
    <span style="color:#000000; font-weight:bold;">Data Augmentation Using Image-to-image Translation for Tongue Coating Thickness Classification with Imbalanced Data</span> <br>
    <a href="https://ieeexplore.ieee.org/document/9948645">[Paper]</a> <br> 
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Yunrui Jiao, Hongyu Gu, Jingqiao Lu, Hong Chen* <br>
    <i>IEEE Biomedical Circuits and Systems Conference <strong>(BioCAS). </strong></i> 2022. (Oral Paper Presentation)
  </li>
</ol>
 
#### CONFERENCE ABSTRACTS
<ol reversed>
  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">Unsupervised Fetal Brain MRI Quality Assessment based on Orientation Prediction Uncertainty</span> <br>
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Haoxiang Li, Zihan Li, Hongjia Yang, Jialan Zheng, Haibo Qu, Qiyuan Tian*<br>
    <a href="https://hal.science/hal-04974115">[Paper]</a> <br> 
    <i> OHBM Annual Meeting <strong>(OHBM). </strong></i> 2025. (Poster)
  </li>

  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">Unsupervised Anomaly Detection for Fetal Brain MRI using Two-Stage Denoising Autoencoder (&#x3C9;-DAE)</span> <br>
    Yingqi Hao, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Juncheng Zhu, Hongjia Yang, Yi Liao, Haibo Qu, Qiyuan Tian*<br>
    <a href="https://hal.science/hal-04974207">[Paper]</a> <br> 
    <i> OHBM Annual Meeting <strong>(OHBM). </strong></i> 2025. (Poster)
  </li>

  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">Volume Reconstruction from Single MRI Thick-slice Stack with Deep Learning for Fetal Brain</span> <br>
    Yang H, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Liao Y, Zhu J, Li H, Li Z, Zhang J, Zheng J, Li Z, Qu H, Tian Q*<br>
    <i> OHBM Annual Meeting <strong>(OHBM). </strong></i> 2025. (Poster)
  </li>
  
  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">FreeHemoSeg: Label-Free Deep Learning Framework for Automated Segmentation of Fetal Brain Germinal Matrix and Intraventricular Hemorrhage</span> <br>
    <span style="color:#b02418; font-weight:bold;">Liu M</span>, Liao Y, Zhu J, Li H, Yang H, Zheng J, Li ZH, Li ZY, Qu H, Tian Q*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Digital Poster)
  </li>

  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">FetalSR: Super-resolving High-isotropic-resolution Image Volume from Single Thick-slice Stack with Deep Learning for Fetal Brain Morphometry</span> <br>
    Yang H, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Liao Y, Li H, Zhu J, Li Z, Zhang J, Zheng J, Li Z, Qu H, Tian Q*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Oral Presentation)
  </li>
  
  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">CortexKAN: Multi-input KAN for fetal cortical surface reconstruction</span> <br>
     Li H, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Liao Y, Zhu J, Zheng J, Yang H, Li Z, Qu H, Tian Q*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Digital Poster)
  </li>

  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">FetalSFUDA: Source-Free Unsupervised Domain Adaptation for Fetal Brain Extraction from Different Centers or MRI Sequences</span> <br>
      Li Y, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Zhu J, Yang H, Zheng J, Li Z, Liao Y, Qu H, Tian Q*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Digital Poster)
  </li>
  
  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">Negative Impacts of Germinal Matrix-Ventricular Hemorrhage on Prenatal and Postnatal Brain Development</span> <br>
     Li H, Liao Y, Zhu J, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Zheng J, Yang H, Li Z, Li Z, Tian Q, Qu H*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Digital Poster)
  </li>
  
  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">DiffKAN: Convolutional Kolmogorov-Arnold Networks for Improved Diffusion MRI Microstructural Modeling</span> <br>
    Chen Y, Li Z, Wang Y, Li Z, Zheng J, Yang H, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Tian Q*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Digital Poster)
  </li>

  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">DeepEddy: high-quality fast eddy current and bulk motion correction using deep learning-based image synthesis and co-registration</span> <br>
    Zhang J, Lange F, Andersson J, Zheng J, Jing Y, Yang H, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Li Z, Wu W, Tian Q, Li Z*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Oral Presentation)
  </li>
  
  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">DIMOND++: Improving diffusion model optimization using diffusion priors</span> <br>
    Li Z, Zheng J, Li Z, Wang Z, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Ning G, Liao H, Tian Q*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Oral Power Pitch)
  </li>

  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">High-fidelity Ultra-fast Diffusion Tensor Imaging in Stroke Patients Using Transfer Learning</span> <br>
    Jing Y, Li Z, Yu Y, Zhou J, Li Z, Zheng J, Yang H, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Wu W, Tian Q, Lu J*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Digital Poster)
  </li>

  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">Impacts of diffusion MRI spatial resolution on the short-range association fiber reconstruction and connectivity estimation</span> <br>
    Zheng J, Yang C, Zhong W, Wang Z, Li H, Li Z, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Yang H, Cao X, Liao C, Salat DH, Huang SY, Tian Q*<br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2025. (Traditional Poster)
  </li>
  
  <li id="CA-Pub0"> 
    <span style="color:#000000; font-weight:bold;">BrainSFUDA: Fetal Brain Extraction from Diffusion-weighted MR Images using Source-free Unsupervised Domain Adaption</span> <br>
    <a href="https://cds.ismrm.org/protected/Diffusion40/abstracts/Li,%20Yijin.pdf">[Paper]</a>  <br>
    Yijin Li, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Junchen Zhu, Hongjia Yang, Jialan Zheng, Ziyu Li, Yi Liao, Haibo Qu, Qiyuan Tian*<br>
    <i>ISMRM Workshop on 40 Years of Diffusion. </i> 2025. (Oral Power Pitch)
  </li>

  <li id="CA-Pub5"> 
    <span style="color:#000000; font-weight:bold;">DiffKAN3D: Efficient and Accurate 3D Diffusion MRI Parameter Estimation for Real-Time Clinical Applications</span> <br>
    <a href="https://cds.ismrm.org/protected/Diffusion40/abstracts/Chen,%20Yifei.pdf">[Paper]</a>  <br>
    Yifei Chen, Zihan Li, Shenghao Zhu, Ziyu Li, Jialan Zheng, Hongjia Yang, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Qiyuan Tian*<br>
    <i>ISMRM Workshop on 40 Years of Diffusion. </i> 2025. (Poster)
  </li>

   <li id="CA-Pub7"> 
    <span style="color:#000000; font-weight:bold;">Effect of Diffusion MRI Acquisition and Nominal Spatial Resolutions on Fiber Reconstruction and Connectivity Estimation</span> <br>
     <a href="https://cds.ismrm.org/protected/Diffusion40/abstracts/Zheng,%20Jialan.pdf">[Paper]</a>  <br>
     Zheng J, Yang C, Zhong W, Wang Z, Li H, Li Z, <span style="color:#b02418; font-weight:bold;">Liu M</span>, Yang H, Cao X, Liao C, Salat DH, Huang SY, Tian Q*<br>
    <i>ISMRM Workshop on 40 Years of Diffusion. </i> 2025. (Oral Presentation)
  </li>

  <li id="CA-Pub7"> 
    <span style="color:#000000; font-weight:bold;">DeepEddy: high-quality eddy current and bulk motion correction using deep learning-based image synthesis and co-registration</span> <br>
    <a href="https://cds.ismrm.org/protected/Diffusion40/abstracts/Zhang,%20Jize.pdf">[Paper]</a>  <br>
     Jize Zhang, Frederik Lange, Jesper Andersson, Jialan Zheng, Yi Jing, Hongjia Yang, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Zihan Li, Wenchuan Wu, Qiyuan Tian, Ziyu Li*<br>
    <i>ISMRM Workshop on 40 Years of Diffusion. </i> 2025. (Oral Presentation)
  </li>
  
  <li id="CA-Pub6"> 
    <span style="color:#000000; font-weight:bold;">DIMOND++: Improving diffusion model optimization using diffusion priors</span> <br>
    <a href="https://cds.ismrm.org/protected/Diffusion40/abstracts/Li,%20Zihan.pdf">[Paper]</a>  <br> 
     Zihan Li, Jialan Zheng, Ziyu Li, Ziang Wang, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Hongjia Yang, Guochen Ning, Hongen Liao, Qiyuan Tian*<br>
    <i>ISMRM Workshop on 40 Years of Diffusion. </i> 2025. (Poster)
  </li>
  
  <li id="CA-Pub1"> 
    <span style="color:#000000; font-weight:bold;">Detecting Fetal Germinal Matrix and Intraventricular Hemorrhage in Brain MRI Using Label-free Deep Learning</span> <br>
    <a href="https://reg.meeting.rsna.org/flow/rsna/rsna24/MeetingCentralRSNA24/page/session-catalog/session/1719506117296001dVkS">[Paper]</a>  <br>
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Haoxiang Li, Juncheng Zhu, Jialan Zheng, Hongjia Yang, Zihan Li, Ziyu Li, Qiyuan Tian*<br>
    <i>Annual Meeting of Radiological Society of North America <strong>(RSNA). </strong></i> 2024. (Oral Paper Presentation)
  </li>
  
  <li id="CA-Pub2"> 
    <span style="color:#000000; font-weight:bold;">Image Quality Assessment using an Orientation Recognition Network for Fetal MRI</span> <br>
    <a href="https://archive.ismrm.org/2024/0726.html">[Paper]</a>  <br> 
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Haoxiang Li, Zihan Li, Hongjia Yang, Jialan Zheng, Xiao Zhang, Qiyuan Tian* <br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2024. (Oral Power Pitch, Magna Cum Laude Merit Award, Top 15%)
  </li>

  <li id="CA-Pub3"> 
    <span style="color:#000000; font-weight:bold;">FetalSurfer: Automated Fetal Cortical Surface Reconstruction</span> <br>
    <a href="https://archive.ismrm.org/2024/3635.html">[Paper]</a>  <br> 
    Haoxiang Li, <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Jialan Zheng, Hongjia Yang, Zihan Li, Qiyuan Tian* <br>
    <i>ISMRM & ISMRT Annual Meeting & Exhibition <strong>(ISMRM). </strong></i> 2024. (Digital Poster)
  </li>

  <li id="CA-Pub4"> 
    <span style="color:#000000; font-weight:bold;">Label-free Image Quality Assessment of Fetal Brain MRI with Unsupervised Deep Learning</span> <br>
    <a href="https://drive.google.com/file/d/1hL0Vyr0e5Wm23xKJhQriVa_dF318Osjg/view?usp=sharing">[Paper]</a>  <br> 
    <span style="color:#b02418; font-weight:bold;">Mingxuan Liu</span>, Haoxiang Li, Haibo Qu, Qiyuan Tian* <br>
    <i>AI Health Summit. </i> 2023. (Top3 prize, Top 3%)
  </li>
</ol>


# 🎖 Honors and Awards
- [[Certificate]](https://arktis2022.github.io/) *2025* **2025 ISMRM: Educational Stipend Award**
- [[Certificate]](https://img.erpweb.eu.org/imgs/2025/03/735b20353752c284.jpg) *2024* **National Scholarship, Ministry of Education**, P.R. China <br /> &nbsp; &nbsp; &nbsp; *Top scholarship in China. 0.2% domestically*.
- [[Certificate]](https://drive.google.com/file/d/1VYlwtxd4h-leijUuAW2cbnBj9PjgIWrQ/view?usp=sharing) *2024* **First Prize at 9th National Biomedical Engineering Innovation Design Competition for College Students (Top 5%)** <br /> &nbsp; &nbsp; &nbsp; *A Deep Learning-Enabled Framework for Anomaly Detection in Fetal Brain MRI*
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/07/6cac5893381c31d0.jpg) *2024* **Outstanding Graduate of Beijing**
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/07/b8f175077893bf72.jpg) *2024* **Outstanding Graduate Award (Top 2%)**, Tsinghua University
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/06/f5785a7f202d1499.jpg) *2024* **2024 ISMRM Magna Cum Laude Merit Award (Top 15%)**
- [[Certificate]](https://mp.weixin.qq.com/s/Oy85Q203XVaCIvwvRs9wfA) *2024* **Second Prize at the 42nd "Challenge Cup" of Tsinghua University** <br /> &nbsp; &nbsp; &nbsp; *Image Deblurring System Driven by Multimodal Data Augmentation*
- [[Certificate]](https://mp.weixin.qq.com/s/Oy85Q203XVaCIvwvRs9wfA) *2024* **Third Prize at the 42nd "Challenge Cup" of Tsinghua University** <br /> &nbsp; &nbsp; &nbsp; *Automated Fetal MRI Image Processing and Anomaly Detection*
- [[Certificate]](https://arktis2022.github.io/) *2024* **2024 ISMRM: Educational Stipend Award**
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/12/0b64f5dd23685207.jpg) *2024* **2024 ICCBD+AI Best Paper Award**
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/02/207b20e0e675d4fa.jpg) *2023* **Top3 Prize in [Al Health Summit 2023 Poster Competition](https://healthsummit.ai/main/abstracts/)**, Singapore
- [[Certificate]](https://img.erpweb.eu.org/imgs/2025/03/1646fe4986f106aa.jpg) *2023* **National Scholarship, Ministry of Education**, P.R. China (Top 1 in department) <br /> &nbsp; &nbsp; &nbsp; *Top scholarship in China. 0.2% domestically*.
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/06/3725764c812767de.jpg) *2022* **Scholarship for Academic Excellence**, Tsinghua University 
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/06/fa3e12191add4d53.jpg) *2022* **Scholarship for Science and Technology Innovation Excellence**, Tsinghua University 
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/06/de4438e28228284b.jpg) *2022* **Second Prize for Outstanding Projects of the Students Research Training Program**, Tsinghua University <br /> &nbsp; &nbsp; &nbsp; *Supported by a National College Student Innovation and Entrepreneurship Project*
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/06/8593b53040f7c593.jpg) *2020* **Scholarship for Academic Excellence**, Tsinghua University 

# 📖 Educations
- *2024.08 - present*, PhD student: **School of Biomedical Engineering**, Tsinghua University, China.
- *2021.09 - 2024.06*, Undergraduate student: **School of Biomedical Engineering**, Tsinghua University, China. 
- *2019.09 – 2021.08*, Undergraduate student: **Department of Chemical Engineering**, Tsinghua University, China.

# 🦜 Invited Talks
- *2024* **2024 ISMRM & ISMRT Annual Meeting & Exhibition**
- *2023* **AI Health Summit 2023**
- *2023* **2023 IEEE International Symposium on Circuits and Systems**
- *2022* **2022 IEEE Biomedical Circuits and Systems Conference**

# 💰 Funding
- *2023-2024* **Beijing Natural Science Foundation Undergraduate "Qiyan" Program**
- *2022-2023* **National College Student Innovation and Entrepreneurship Project**

# 🎓 Academic Service
+ Co-organizer of [OCSMRM 2024](http://www.ocsmrm.org/)
+ *Journal Reviewer*, IEEE TCDS; IEEE TCAS-I; IEEE TCAS-II; IEEE TIP; Applied Intelligence.
+ *Conference Reviewer*, ACM MobileHCI 2024; AAAI-25 UC; IEEE ISBI 2025; ISMRM 2025; IJCNN 2025; CHIL 2025; MICCAI 2025; ICLR 2025 Workshop (AI4CHL, XAI4Science).
  
# 🎣 Activities
- *2025.02.16*, Attended the ISMRM Workshop on 40 Years of Diffusion: Past, Present & Future Perspectives in Kyoto, Japan. [Photo](https://drive.google.com/file/d/1PB_3NYgY80Eziv8DedZvkEdgrSYU49aY/view?usp=sharing)
- *2024.11.24*, Attended the 2024 British Machine Vision Conference (BMVC) in Glasgow, UK. [Photo](https://img.erpweb.eu.org/imgs/2024/11/cb1c15b029cec4e7.jpg)
- *2024.09.22*, Attended the 2024 Annual Meeting of the Neuroimaging Committee of Chinese Psychological Society, held in Nanjing. [Photo](https://img.erpweb.eu.org/imgs/2024/09/67e9ff106746c091.jpg)
- *2024.07.20*, Attended the 9th National Biomedical Engineering Innovation Design Competition for College Students, held in Sanya. [Photo](https://img.erpweb.eu.org/imgs/2024/07/aed77c3330a9ef9c.jpg)
- *2024.07.14*, Attended the Medical Imaging Computing Seminar 2024 (MICS 2024), held in Xiamen. [Photo](https://img.erpweb.eu.org/imgs/2024/07/a4d7a1923b39dfa2.jpg)
- *2024.07.04*, Attended the ADVANCED IMAGING AND MICROSCOPY (AIM 2024), held in Huairou District. [Photo](https://img.erpweb.eu.org/imgs/2024/07/05c57542c5d7591a.jpg)
- *2024.05.10*, Attended the ISMRM-Endorsed Global Outreach Workshop in Thailand 2024. [Photo](https://img.erpweb.eu.org/imgs/2024/05/20292d7def1ae7b0.jpg)
- *2024.05.08*, Attended the OCSMRM 2024 as one of the organizers, held in Singapore. [Photo](https://img.erpweb.eu.org/imgs/2024/05/0bb68e1150ae04be.png)
- *2024.05.07*, Attended the ISMRM 2024, held in Singapore. [Photo A](https://img.erpweb.eu.org/imgs/2024/05/0bf1c7f9ac829f10.jpg) [Photo B](https://img.erpweb.eu.org/imgs/2024/05/a2646308883e4385.jpg)
- *2023.04.17*, Attended the ICASSP 2024, held in Seoul. [Photo](https://img.erpweb.eu.org/imgs/2024/04/0a91be3331527e5d.jpg)
- *2023.11.24*, Won the top3 Prize in Al Health Summit 2023 Poster Competition. [Photo](https://img.erpweb.eu.org/imgs/2024/02/207b20e0e675d4fa.jpg) (First row: Competition judges; Left one: Editor-in-chief of The Lancet Digital Health; Left two: Prof Catherine R Lucey; Left three: Editor-in-chief of Nature Medicine; Left four: Editor-in-chief of Nature Biomedical Engineering)
- *2023.11.24*, Top 5 poster competition in AI health summit 2023. [Photo](https://img.erpweb.eu.org/imgs/2024/02/2547ed7aa1423a38.jpg)
- *2023.11.22*, BIRTHLab members visited Nanyang Technological University. [Photo](https://img.erpweb.eu.org/imgs/2024/02/0cb68379b33a36d5.png)
- *2023.10.02*, Attended the NUS-THU Joint Workshop on Biomedical Engineering 2023, held in Singapore. [Photo](https://img.erpweb.eu.org/imgs/2024/02/5514cfe5a7abca58.png)
- *2023.07.26*, Attended the IEEE ASYNC 2023 held in Beijing, China. [Photo](https://img.erpweb.eu.org/imgs/2024/02/28f5198102433c57.png)
  
# 💌 Social Event
- *2024.11.11*, Visited the Universal Beijing Resort (环球影城) with my girlfriend. [Photo](https://img.erpweb.eu.org/imgs/2024/11/0bf79f13a48a3433.jpg)
- *2024.11.08*, Visited the Forbidden City (故宫) with my girlfriend, in Beijing. [Photo](https://img.erpweb.eu.org/imgs/2024/11/59aa6f9f72433bac.jpg)
- *2024.09.17*, Celebrating the Moon Festival at Huazhong University of Science and Technology (HUST) with my girlfriend, in Wuhan. [Photo](https://img.erpweb.eu.org/imgs/2024/09/648d5b55b079db83.jpg)
- *2024.07.26*, 🎂 Celebrating girlfriend's birthday 🎂. [Photo](https://img.erpweb.eu.org/imgs/2024/08/5078c45c4becf74c.jpg)
- *2024.06.28*, Graduated with a bachelor's degree from Tsinghua University. [Photo](https://img.erpweb.eu.org/imgs/2024/07/51b1f1467d9be574.jpg)
- *2024.05.02*, Visited the Tientsin Eye (天津之眼) with my girlfriend, in Tianjing. [Photo](https://img.erpweb.eu.org/imgs/2024/05/231e58636bd80878.jpg)
- *2024.03.20*, Watched the stage play "Count Wulong Mountain" (《乌龙山伯爵》) at the Happy Twist Theater (开心麻花剧场) with my girlfriend, in Beijing. [Photo](https://img.erpweb.eu.org/imgs/2024/03/f1eec2640d6e2ded.jpg)
- *2024.03.19*, Visited the Happy Valley Beijing (欢乐谷) with my girlfriend, in Beijing. [Photo A](https://img.erpweb.eu.org/imgs/2024/03/8ddc3c7236876ab4.jpg) [Photo B](https://img.erpweb.eu.org/imgs/2024/03/6302a2dab7c7ff69.jpg)
- *2024.02.28*, Visited the Juzizhou Island (橘子洲) with my girlfriend, in Changsha. [Photo](https://ibb.co/mDLzGyS)
- *2023.10.22*, Visited the National Museum of China (国家博物馆) with my girlfriend, in Beijing. [Photo](https://img.erpweb.eu.org/imgs/2024/02/b0b5af6405497e7d.png)
- *2023.06.14*, Visited the Yuewang Pavilion (岳王亭) with my girlfriend, in Changsha. [Photo](https://img.erpweb.eu.org/imgs/2024/03/b621eaab184bcea3.jpg)

# 🫶 Other
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/06/379f54cbbf11e115.jpg) *2024* **United Nations Children's Fund (unicef) Second Anniversary Commemorative Certificate**
- [[Certificate]](https://img.erpweb.eu.org/imgs/2024/06/577a0ba3ae662a03.jpg) *2023* **United Nations Children's Fund (unicef) First Anniversary Commemorative Certificate**

# 🔗 LINKS
BIRTHLab: [The lab for Brain Imaging Research at Tsinghua](https://birthlab.github.io/)<br>Haoxiang Li: [School of Biomedical Engineering, Tsinghua University](https://lihaoxiang-20.github.io/)<br>Jack Tang: [Xinya College, Tsinghua University](https://mcjacktang.github.io/)<br>Yunkang Cao: [Huazhong University of Science and Technology](https://caoyunkang.github.io/)<br>Yiming Huang: [Microsoft Research Asia](https://yiyihum.github.io/)<br>Siwei Li: [Department of Electronic Engineering of Tsinghua University](https://hplqaq.github.io/)<br>Yifei Chen: [School of Biomedical Engineering, Tsinghua University](https://justlfc03.github.io/)
