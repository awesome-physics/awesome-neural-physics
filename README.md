# Awesome Neural Physics

A curated list of papers on the seamless fusion of neural models and physics simulation. It follows the field from injecting neural capabilities into classical solvers to embedding physical simulators directly within neural architectures.

> Best browsing experience: use the [interactive index](https://awesome-physics.github.io/awesome-neural-physics/) for search, filtering, and tag-based lookup.

[Interactive Index](https://awesome-physics.github.io/awesome-neural-physics/) | [BibTeX](main.bib) | [Tag Guide](#tag-guide) | [Citation](#citation)

## Contents

- [Fluid (80)](#fluid)
- [Cloth (53)](#cloth)
- [Softbody (63)](#softbody)
- [Rigidbody (38)](#rigidbody)
- [Multiphys (13)](#multiphys)
- [Tag Guide](#tag-guide)
- [Citation](#citation)

<a id="fluid"></a>
## Fluid (80)

Neural physics papers on fluid simulation, reconstruction, control, and differentiable methods.

* **A Neural Particle Level Set Method for Dynamic Interface Tracking** | TOG 2025  
  *Duowen Chen, Junwei Zhou, Bo Zhu*  
  [[DOI]](https://doi.org/10.1145/3730399) [[Project]](https://cdwj.github.io/projects/neural-pls-project-page/index.html)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square)

<br>

* **A Pioneering Neural Network Method for Efficient and Robust Fuel Sloshing Simulation in Aircraft** | AAAI 2025  
  *Chen Yu, Shuai Zheng, Nianyi Wang, Menglong Jin, et al.*  
  [[DOI]](https://doi.org/10.1609/aaai.v39i15.33752) [[Code]](https://github.com/chenyu-xjtu/A-Pioneering-Neural-Network-Method-for-Efficient-and-Robust-Fuel-Sloshing-Simulation-in-Aircraft)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **AMR-Transformer: Enabling Efficient Long-range Interaction for Complex Neural Fluid Simulation** | CVPR 2025  
  *Zeyi Xu, Jinfan Liu, Kuangxu Chen, Ye Chen, et al.*  
  [[DOI]](https://doi.org/10.1109/cvpr52734.2025.00545) [[Code]](https://github.com/JfanLiu/AMR_Transformer)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Transformer](https://img.shields.io/badge/-Transformer-bc6c25.svg?style=flat-square)

<br>

* **An Adjoint Method for Differentiable Fluid Simulation on Flow Maps** | Siggraph Asia 2025  
  *Zhiqi Li, Jinjin He, Barnab\'as B\"orcs\"ok, Taiyuan Zhang, et al.*  
  [[Paper]](https://arxiv.org/abs/2511.01259) [[Project]](https://pearseven.github.io/DiffFMProject/) [[DOI]](https://doi.org/10.1145/3757377.3763903)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **FlowCapX: Physics-Grounded Flow Capture with Long-Term Consistency** | CGF 2025  
  *N. Tao, L. Zhang, Xingyu Ni, Mengyu Chu, et al.*  
  [[DOI]](https://doi.org/10.1111/cgf.70274) [[Code]](https://github.com/taoningxiao/FlowCapX)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Learning an Implicit Physical Model for Image-based Fluid Simulation** | ICCV 2025  
  *Emily Yue-ting Jia, Jiageng Mao, Zhiyuan Gao, Yajie Zhao, et al.*  
  [[Paper]](https://arxiv.org/abs/2508.08254) [[Project]](https://physfluid.github.io/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Neural Kinematic Bases for Fluids** | Siggraph Asia 2025  
  *Yibo Liu, Zhixin Fang, Sune Darkner, Noam Aigerman, et al.*  
  [[Paper]](https://arxiv.org/abs/2504.15657) [[DOI]](https://doi.org/10.1145/3757377.3763925)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square)

<br>

* **Representing Flow Fields with Divergence-Free Kernels for Reconstruction** | PACMCGIT 2025  
  *Xingyu Ni, Jingrui Xing, X. Li, Bin Wang, et al.*  
  [[DOI]](https://doi.org/10.1145/3747872) [[Project]](https://www.physicsbasedanimation.com/2025/08/10/representing-flow-fields-with-divergence-free-kernels-for-reconstruction)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square) ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square)

<br>

* **UniPhy: Learning a Unified Constitutive Model for Inverse Physics Simulation** | CVPR 2025  
  *Himangi Mittal, Peiye Zhuang, Hsin-Ying Lee, Shubham Tulsiani*  
  [[DOI]](https://doi.org/10.1109/cvpr52734.2025.01511) [[Project]](https://himangim.github.io/UniPhy)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square) ![Neural Material](https://img.shields.io/badge/-Neural%20Material-6d597a.svg?style=flat-square)

<br>

* **A Real-Time and Interactive Fluid Modeling System for Mixed Reality** | TVCG 2024  
  *Yunchi Cen, Hanchen Deng, Yue Ma, Xiaohui Liang*  
  [[DOI]](https://doi.org/10.1109/tvcg.2024.3456140) [[Code]](https://github.com/cenyc/Interactive-Fluid-Modeling)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square)

<br>

* **Dynamic ocean inverse modeling based on differentiable rendering** | CVM 2024  
  *Xie, Xueguang, Gao, Yang, Hou, Fei, Hao, Aimin, et al.*  
  [[Paper]](https://link.springer.com/article/10.1007/s41095-023-0338-4)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Fluid Inverse Volumetric Modeling and Applications from Surface Motion** | TVCG 2024  
  *Xie, Xueguang, Gao, Yang, Hou, Fei, Cheng, Tianwei, et al.*  
  [[Paper]](https://www.computer.org/csdl/journal/tg/5555/01/10452823/1UUuVAIPShy)  
  ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square) ![CNN](https://img.shields.io/badge/-CNN-e76f51.svg?style=flat-square)

<br>

* **Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting** | Arxiv 2024  
  *Yutao Feng, Xiang Feng, Yintong Shang, Ying Jiang, et al.*  
  [[Project]](https://amysteriouscat.github.io/GaussianSplashing/)  
  ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square) ![3DGS](https://img.shields.io/badge/-3DGS-bc6c25.svg?style=flat-square)

<br>

* **Laplacian Projection Based Global Physical Prior Smoke Reconstruction** | TVCG 2024  
  *Xiao, Shibang, Tong, Chao, Zhang, Qifan, Cen, Yunchi, et al.*  
  [[Paper]](https://www.computer.org/csdl/journal/tg/5555/01/10414126/1TZIJbrBNo4)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Learning Reduced Fluid Dynamics** | AAAI 2024  
  *Pan, Zherong, Gao, Xifeng, Wu, Kui*  
  [[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/29367)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Neural Implicit Reduced Fluid Simulation** | Siggraph Asia 2024  
  *Yuanyuan Tao, Ivan Puhachov, Derek Nowrouzezahrai, Paul Kry*  
  [[DOI]](https://doi.org/10.1145/3680528.3687628) [[Project]](https://yuanyuantao.github.io/Neural-Implicit-Reduced-Fluid-Simulation/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **Neural Monte Carlo Fluid Simulation** | Siggraph 2024  
  *Pranav Jain, Ziyin Qu, Peter Yichen Chen, Oded Stein*  
  [[DOI]](https://doi.org/10.1145/3641519.3657438) [[Code]](https://github.com/Pranav-Jain/Neural-Monte-Carlo-Fluid-Simulation)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **Neural Physical Simulation with Multi-Resolution Hash Grid Encoding** | AAAI 2024  
  *Wang, Haoxiang, Yu, Tao, Yang, Tianwei, Qiao, Hui, et al.*  
  [[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/28349)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **NeuralFluid: Neural Fluidic System Design and Control with Differentiable Simulation** | NeurIPS 2024  
  *Li, Yifei, Sun, Yuchen, Ma, Pingchuan, Sifakis, Eftychios, et al.*  
  [[Paper]](https://papers.nips.cc/paper_files/paper/2024/hash/9a379c1b05793d1c42dc832269834515-Abstract-Conference.html) [[Project]](https://people.csail.mit.edu/liyifei/publication/neuralfluid/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square)

<br>

* **NeuSmoke: Efficient Smoke Reconstruction and View Synthesis with Neural Transportation Fields** | Siggraph Asia 2024  
  *Jiaxiong Qiu, Ruihong Cen, Zhong Li, Han Yan, et al.*  
  [[DOI]](https://doi.org/10.1145/3680528.3687667) [[Code]](https://github.com/JiaxiongQ/NeuSmoke)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Physics-Informed Learning of Characteristic Trajectories for Smoke Reconstruction** | Siggraph 2024  
  *Yiming Wang, Siyu Tang, Mengyu Chu*  
  [[DOI]](https://doi.org/10.1145/3641519.3657483) [[Code]](https://github.com/19reborn/PICT_smoke)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square) ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square)

<br>

* **Reconstruction of implicit surfaces from fluid particles using convolutional neural networks** | CGF 2024  
  *Chunming Zhao, Tamar Shinar, Craig Schroeder*  
  [[DOI]](https://doi.org/10.1111/cgf.15181) [[Project]](https://www.cs.ucr.edu/~craigs/research.html)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square) ![CNN](https://img.shields.io/badge/-CNN-e76f51.svg?style=flat-square)

<br>

* **SNN-PDE: Learning Dynamic PDEs from Data with Simplicial Neural Networks** | AAAI 2024  
  *Jae Woong Choi, Yuzhou Chen, Huikyo Lee, Hyun Kim, et al.*  
  [[DOI]](http://dx.doi.org/10.1609/aaai.v38i10.29038) [[DOI]](https://doi.org/10.1609/aaai.v38i10.29038)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Symmetric Basis Convolutions for Learning Lagrangian Fluid Mechanics** | ICLR 2024  
  *Rene Winchenbach, Nils Thuerey*  
  [[Code]](https://github.com/tum-pbs/SFBC)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **A generalized constitutive model for versatile mpm simulation and inverse learning with differentiable physics** | PACMCGIT 2023  
  *Su, Haozhe, Li, Xuan, Xue, Tao, Jiang, Chenfanfu, et al.*  
  [[Project]](https://xuan-li.github.io/publication/su2023generalized/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **Boundary Graph Neural Networks for 3D Simulations** | AAAI 2023  
  *Andreas Mayr, Sebastian Lehner, Arno Mayrhofer, Christoph Kloss, et al.*  
  [[DOI]](https://doi.org/10.1609/aaai.v37i8.26092) [[Project]](https://ml-jku.github.io/bgnn)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Fast fluid simulation via dynamic multi-scale gridding** | AAAI 2023  
  *Liu, Jinxian, Chen, Ye, Ni, Bingbing, Ren, Wei, et al.*  
  [[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/25255)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Fluid Simulation on Neural Flow Maps** | TOG 2023  
  *Deng, Yitong, Yu, Hong-Xing, Zhang, Diyang, Wu, Jiajun, et al.*  
  [[Project]](https://yitongdeng-projects.github.io/neural_flow_maps_webpage/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **FluidLab: A Differentiable Environment for Benchmarking Complex Fluid Manipulation** | ICLR 2023  
  *Xian, Zhou, Zhu, Bo, Xu, Zhenjia, Tung, Hsiao-Yu, et al.*  
  [[Project]](https://fluidlab2023.github.io/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Inferring Hybrid Neural Fluid Fields from Videos** | NeurIPS 2023  
  *Yu, Hong-Xing, Zheng, Yang, Gao, Yuan, Deng, Yitong, et al.*  
  [[Paper]](https://papers.nips.cc/paper_files/paper/2023/hash/00feea0d4eea58fdda7151f7e7f76c72-Abstract-Conference.html) [[Project]](https://kovenyu.com/hyfluid/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Interactive design of 2D car profiles with aerodynamic feedback** | CGF 2023  
  *Nicolas Rosset, Guillaume Cordonnier, Régis Duvigneau, Adrien Bousseau*  
  [[DOI]](https://doi.org/10.1111/cgf.14772) [[Project]](https://hal.science/hal-03975369)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Shape Design](https://img.shields.io/badge/-Shape%20Design-8ab17d.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square)

<br>

* **Learning to Estimate Single-View Volumetric Flow Motions without 3D Supervision** | ICLR 2023  
  *Erik Franz, Barbara Solenthaler, Nils Thuerey*  
  [[Project]](https://ge.in.tum.de/publications/2023-franz-neuralglobtrans/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Learning Vortex Dynamics for Fluid Inference and Prediction** | ICLR 2023  
  *Yitong Deng, Hong-Xing Yu, Jiajun Wu, Bo Zhu*  
  [[Code]](https://github.com/yitongdeng-projects/learning_vortex_dynamics_code)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Neural Stress Fields for Reduced-order Elastoplasticity and Fracture** | Siggraph Asia 2023  
  *Zong, Zeshun, Li, Xuan, Li, Minchen, Chiaramonte, Maurizio M, et al.*  
  [[Project]](https://zeshunzong.github.io/reduced-order-mpm/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Fracture](https://img.shields.io/badge/-Fracture-3a86b8.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **Neural vortex method: From finite Lagrangian particles to infinite dimensional Eulerian dynamics** | Comput. Fluids 2023  
  *Shiying Xiong, Xingzhe He, Yunjin Tong, Yitong Deng, et al.*  
  [[Paper]](https://arxiv.org/abs/2006.04178) [[DOI]](https://doi.org/10.1016/j.compfluid.2023.105811)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification** | ICLR 2023  
  *Xuan Li, Yi-Ling Qiao, Peter Yichen Chen, Krishna Murthy Jatavallabhula, et al.*  
  [[Project]](https://sites.google.com/view/PAC-NeRF)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square) ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square)

<br>

* **PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics** | Arxiv 2023  
  *Xie, Tianyi, Zong, Zeshun, Qiu, Yuxing, Li, Xuan, et al.*  
  [[Project]](https://xpandora.github.io/PhysGaussian/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![3DGS](https://img.shields.io/badge/-3DGS-bc6c25.svg?style=flat-square)

<br>

* **Physics-Informed Neural Corrector for Deformation-based Fluid Control** | CGF 2023  
  *Tang, Jingwei, Kim, Byungsoo, Azevedo, Vinicius C., Solenthaler, Barbara*  
  [[Project]](https://studios.disneyresearch.com/2023/05/07/physics-informed-neural-corrector-for-deformation-based-fluid-control/) [[DOI]](https://doi.org/10.1111/cgf.14751)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square)

<br>

* **Solving Inverse Physics Problems with Score Matching** | NeurIPS 2023  
  *Holzschuh, Benjamin, Vegetti, Simona, Thuerey, Nils*  
  [[Code]](https://github.com/tum-pbs/SMDP)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Optimization](https://img.shields.io/badge/-Optimization-457b9d.svg?style=flat-square)

<br>

* **SurfsUp: Learning Fluid Simulation for Novel Surfaces** | ICCV 2023  
  *Arjun Mani, Ishaan Preetam Chandratreya, Elliot Creager, Carl Vondrick, et al.*  
  [[DOI]](https://doi.org/10.1109/ICCV51070.2023.01308) [[Project]](https://surfsup.cs.columbia.edu/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **ACID: Action-Conditional Implicit Visual Dynamics for Deformable Object Manipulation** | RSS 2022  
  *Bokui Shen, Zhenyu Jiang, Christopher Choy, Silvio Savarese, et al.*  
  [[DOI]](https://doi.org/10.15607/rss.2022.xviii.001)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Deep Reconstruction of 3D Smoke Densities from Artist Sketches** | CGF 2022  
  *Kim, Byungsoo, Huang, Xingchang, Wuelfroth, Laura, Tang, Jingwei, et al.*  
  [[Paper]](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14461) [[DOI]](https://doi.org/10.1111/cgf.14461)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square) ![CNN](https://img.shields.io/badge/-CNN-e76f51.svg?style=flat-square)

<br>

* **Efficient Neural Style Transfer for Volumetric Simulations** | TOG 2022  
  *Aurand, Joshua, Ortiz, Raphael, Nauer, Silvia, Azevedo, Vinicius C.*  
  [[Project]](https://studios.disneyresearch.com/2022/11/30/efficient-neural-style-transfer-for-volumetric-simulations/) [[DOI]](https://doi.org/10.1145/3550454.3555517)  
  ![Style Transfer](https://img.shields.io/badge/-Style%20Transfer-e76f51.svg?style=flat-square)

<br>

* **Fluidic Topology Optimization with an Anisotropic Mixture Model** | TOG 2022  
  *Yifei Li, Tao Du, Sangeetha Srinivasan, Kui Wu, et al.*  
  [[DOI]](https://doi.org/10.1145/3550454.3555429) [[Project]](https://people.csail.mit.edu/liyifei/publication/anisotropicstokes)  
  ![Optimization](https://img.shields.io/badge/-Optimization-457b9d.svg?style=flat-square) ![Shape Design](https://img.shields.io/badge/-Shape%20Design-8ab17d.svg?style=flat-square)

<br>

* **Guaranteed conservation of momentum for learning particle-based fluid dynamics** | NeurIPS 2022  
  *Prantl, Lukas, Ummenhofer, Benjamin, Koltun, Vladlen, Thuerey, Nils*  
  [[Code]](https://github.com/tum-pbs/DMCF)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Half-Inverse Gradients for Physical Deep Learning** | ICLR 2022  
  *Patrick Schnell, Philipp Holl, Nils Thuerey*  
  [[Paper]](https://arxiv.org/abs/2203.10131)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Neurofluid: Fluid dynamics grounding with particle-driven neural radiance fields** | ICML 2022  
  *Guan, Shanyan, Deng, Huayu, Wang, Yunbo, Yang, Xiaokang*  
  [[Project]](https://syguan96.github.io/NeuroFluid/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Physics informed neural fields for smoke reconstruction with sparse data** | TOG 2022  
  *Chu, Mengyu, Liu, Lingjie, Zheng, Quan, Franz, Erik, et al.*  
  [[Project]](https://rachelcmy.github.io/pinf_smoke/) [[DOI]](https://doi.org/10.1145/3528223.3530169)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square) ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square)

<br>

* **Transformer with implicit edges for particle-based physics simulation** | ECCV 2022  
  *Shao, Yidi, Loy, Chen Change, Dai, Bo*  
  [[Project]](https://www.mmlab-ntu.com/project/tie/index.html)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square) ![Transformer](https://img.shields.io/badge/-Transformer-bc6c25.svg?style=flat-square)

<br>

* **Versatile Control of Fluid-directed Solid Objects Using Multi-task Reinforcement Learning** | TOG 2022  
  *Ren, Bo, Ye, Xiaohan, Pan, Zherong, Zhang, Taiyuan*  
  [[Paper]](https://dl.acm.org/doi/10.1145/3554731) [[DOI]](https://doi.org/10.1145/3554731)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Data-driven simulation in fluids animation: A survey** | VRIH 2021  
  *Chen, Qian, Wang, Yue, Wang, Hui, Yang, Xubo*  
  [[Paper]](https://www.sciencedirect.com/science/article/pii/S2096579621000139)  
  ![Survey](https://img.shields.io/badge/-Survey-3a86b8.svg?style=flat-square)

<br>

* **Global transport for fluid reconstruction with learned self-supervision** | CVPR 2021  
  *Franz, Erik, Solenthaler, Barbara, Thuerey, Nils*  
  [[Project]](https://ge.in.tum.de/publications/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Learning meaningful controls for fluids** | TOG 2021  
  *Chu, Mengyu, Thuerey, Nils, Seidel, Hans-Peter, Theobalt, Christian, et al.*  
  [[Project]](https://rachelcmy.github.io/den2vel/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square) ![GAN](https://img.shields.io/badge/-GAN-8ab17d.svg?style=flat-square)

<br>

* **Model-Predictive Control of Blood Suction for Surgical Hemostasis using Differentiable Fluid Simulations** | ICRA 2021  
  *Jing-bin Huang, Fei Liu, Florian Richter, Michael C. Yip*  
  [[DOI]](https://doi.org/10.1109/icra48506.2021.9561624) [[Project]](https://ucsdarclab.com/autopublication/model-predictive-control-of-blood-suction-for-surgical-hemostasis-using-differentiable-fluid-simulations)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square)

<br>

* **Neural upflow: A scene flow learning approach to increase the apparent resolution of particle-based liquids** | PACMCGIT 2021  
  *Roy, Bruno, Poulin, Pierre, Paquette, Eric*  
  [[Paper]](https://dl.acm.org/doi/abs/10.1145/3480147)  
  ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square)

<br>

* **Predicting high-resolution turbulence details in space and time** | TOG 2021  
  *Bai, Kai, Wang, Chunhao, Desbrun, Mathieu, Liu, Xiaopei*  
  [[Paper]](https://dl.acm.org/doi/abs/10.1145/3478513.3480492)  
  ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square)

<br>

* **Two-step Temporal Interpolation Network Using Forward Advection for Efficient Smoke Simulation** | CGF 2021  
  *Oh, Young Jin, Lee, In-Kwon*  
  [[Project]](https://onlinelibrary.wiley.com/doi/10.1111/cgf.142638)  
  ![Temporal Interpolation](https://img.shields.io/badge/-Temporal%20Interpolation-bc6c25.svg?style=flat-square)

<br>

* **Volumetric appearance stylization with stylizing kernel prediction network** | TOG 2021  
  *Guo, Jie, Li, Mengtian, Zong, Zijing, Liu, Yuntao, et al.*  
  [[Paper]](https://dl.acm.org/doi/abs/10.1145/3450626.3459799) [[DOI]](https://doi.org/10.1145/3450626.3459799)  
  ![Style Transfer](https://img.shields.io/badge/-Style%20Transfer-e76f51.svg?style=flat-square)

<br>

* **A Novel CNN-Based Poisson Solver for Fluid Simulation** | TVCG 2020  
  *Xiao, Xiangyun, Zhou, Yanqing, Wang, Hui, Yang, Xubo*  
  [[Project]](http://dalab.se.sjtu.edu.cn/www/home/?page_id=790) [[DOI]](https://doi.org/10.1109/TVCG.2018.2873375)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![CNN](https://img.shields.io/badge/-CNN-e76f51.svg?style=flat-square)

<br>

* **Dynamic fluid surface reconstruction using deep neural network** | CVPR 2020  
  *Thapa, Simron, Li, Nianyi, Ye, Jinwei*  
  [[Project]](https://ivlab.cse.lsu.edu/FSRN_CVPR20.html)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Dynamic Upsampling of Smoke through Dictionary-based Learning** | TOG 2020  
  *Bai, Kai, Li, Wei, Desbrun, Mathieu, Liu, Xiaopei*  
  [[Project]](https://faculty.sist.shanghaitech.edu.cn/faculty/liuxp/projects/ss_dbnn/index.htm) [[DOI]](https://doi.org/10.1145/3412360)  
  ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square)

<br>

* **Interactive liquid splash modeling by user sketches** | TOG 2020  
  *Yan, Guowei, Chen, Zhili, Yang, Jimei, Wang, Huamin*  
  [[Paper]](https://dl.acm.org/doi/abs/10.1145/3414685.3417832)  
  ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square) ![GAN](https://img.shields.io/badge/-GAN-8ab17d.svg?style=flat-square)

<br>

* **Lagrangian neural style transfer for fluids** | TOG 2020  
  *Kim, Byungsoo, Azevedo, Vinicius C., Gross, Markus, Solenthaler, Barbara*  
  [[Code]](https://github.com/byungsook/neural-flow-style) [[DOI]](https://doi.org/10.1145/3386569.3392473)  
  ![Style Transfer](https://img.shields.io/badge/-Style%20Transfer-e76f51.svg?style=flat-square)

<br>

* **Latent space subdivision: stable and controllable time predictions for fluid flow** | CGF 2020  
  *Wiewel, Steffen, Kim, Byungsoo, Azevedo, Vinicius C, Solenthaler, Barbara, et al.*  
  [[Project]](https://ge.in.tum.de/publications/2020-lssubdiv-wiewel/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![CNN](https://img.shields.io/badge/-CNN-e76f51.svg?style=flat-square)

<br>

* **Learning to Control PDEs with Differentiable Physics** | ICLR 2020  
  *Philipp Holl, Vladlen Koltun, Nils Thuerey*  
  [[Paper]](http://arxiv.org/abs/2001.07457) [[Code]](https://github.com/p-holl/PDE-Control) [[DOI]](https://doi.org/10.48550/arxiv.2001.07457)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square)

<br>

* **Learning to manipulate amorphous materials** | TOG 2020  
  *Zhang, Yunbo, Yu, Wenhao, Liu, C. Karen, Kemp, Charlie, et al.*  
  [[Project]](https://tml.stanford.edu/publications/2020/learning-manipulate-amorphous-materials) [[DOI]](https://doi.org/10.1145/3414685.3417868)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Machine learning for fluid mechanics** | ARFM 2020  
  *Brunton, Steven L, Noack, Bernd R, Koumoutsakos, Petros*  
  [[Project]](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-010719-060214)  
  ![Survey](https://img.shields.io/badge/-Survey-3a86b8.svg?style=flat-square)

<br>

* **Tomofluid: Reconstructing dynamic fluid from sparse view videos** | CVPR 2020  
  *Zang, Guangming, Idoughi, Ramzi, Wang, Congli, Bennett, Anthony, et al.*  
  [[Paper]](https://openaccess.thecvf.com/content_CVPR_2020/html/Zang_TomoFluid_Reconstructing_Dynamic_Fluid_From_Sparse_View_Videos_CVPR_2020_paper.html)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **A CNN-based Flow Correction Method for Fast Preview** | CGF 2019  
  *Xiao, Xiangyun, Wang, Hui, Yang, Xubo*  
  [[Project]](http://dalab.se.sjtu.edu.cn/www/home/?page_id=763)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![CNN](https://img.shields.io/badge/-CNN-e76f51.svg?style=flat-square)

<br>

* **Lagrangian fluid simulation with continuous convolutions** | ICLR 2019  
  *Ummenhofer, Benjamin, Prantl, Lukas, Thuerey, Nils, Koltun, Vladlen*  
  [[Project]](https://ge.in.tum.de/publications/2020-ummenhofer-iclr/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **ScalarFlow: a large-scale volumetric data set of real-world scalar transport flows for computer animation and machine learning** | TOG 2019  
  *Eckert, Marie-Lena, Um, Kiwon, Thuerey, Nils*  
  [[Project]](https://ge.in.tum.de/publications/2019-scalarflow-eckert/) [[DOI]](https://doi.org/10.1145/3355089.3356545)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Transport-based neural style transfer for smoke simulations** | TOG 2019  
  *Kim, Byungsoo, Azevedo, Vinicius C., Gross, Markus, Solenthaler, Barbara*  
  [[Paper]](https://dl.acm.org/doi/10.1145/3355089.3356560) [[DOI]](https://doi.org/10.1145/3355089.3356560)  
  ![Style Transfer](https://img.shields.io/badge/-Style%20Transfer-e76f51.svg?style=flat-square)

<br>

* **Video-guided real-to-virtual parameter transfer for viscous fluids** | TOG 2019  
  *Takahashi, Tetsuya, Lin, Ming C.*  
  [[Project]](https://gamma.cs.unc.edu/ParameterTransfer/) [[DOI]](https://doi.org/10.1145/3355089.3356551)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Deep dynamical modeling and control of unsteady fluid flows** | NeurIPS 2018  
  *Morton, Jeremy, Jameson, Antony, Kochenderfer, Mykel J, Witherden, Freddie*  
  [[Code]](https://github.com/sisl/deep_flow_control)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square)

<br>

* **Fluid directed rigid body control using deep reinforcement learning** | TOG 2018  
  *Ma, Pingchuan, Tian, Yunsheng, Pan, Zherong, Ren, Bo, et al.*  
  [[Project]](https://gamma.cs.unc.edu/DRL_FluidRigid/) [[DOI]](https://doi.org/10.1145/3197517.3201334)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Fluid Control](https://img.shields.io/badge/-Fluid%20Control-8ab17d.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **tempoGAN: A temporally coherent, volumetric GAN for super-resolution fluid flow** | TOG 2018  
  *Xie, You, Franz, Erik, Chu, Mengyu, Thuerey, Nils*  
  [[Project]](https://ge.in.tum.de/publications/tempogan/)  
  ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square) ![GAN](https://img.shields.io/badge/-GAN-8ab17d.svg?style=flat-square)

<br>

* **Accelerating eulerian fluid simulation with convolutional networks** | ICML 2017  
  *Tompson, Jonathan, Schlachter, Kristofer, Sprechmann, Pablo, Perlin, Ken*  
  [[Code]](https://github.com/google/FluidNet)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Data-driven synthesis of smoke flows with CNN-based feature descriptors** | TOG 2017  
  *Chu, Mengyu, Thuerey, Nils*  
  [[Project]](https://ge.in.tum.de/publications/2017-sig-chu/) [[DOI]](https://doi.org/10.1145/3072959.3073643)  
  ![CNN](https://img.shields.io/badge/-CNN-e76f51.svg?style=flat-square) ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square)

<br>

* **Data-driven projection method in fluid simulation** | CAVW 2016  
  *Yang, Cheng, Yang, Xubo, Xiao, Xiangyun*  
  [[Project]](http://dalab.se.sjtu.edu.cn/www/home/?page_id=911) [[DOI]](https://doi.org/10.1002/cav.1695)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Data-driven fluid simulations using regression forests** | TOG 2015  
  *Ladick\'y, L'ubor, Jeong, SoHyeon, Solenthaler, Barbara, Pollefeys, Marc, et al.*  
  [[Paper]](https://dl.acm.org/doi/10.1145/2816795.2818129) [[DOI]](https://doi.org/10.1145/2816795.2818129)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Fluid Reconstruction](https://img.shields.io/badge/-Fluid%20Reconstruction-6d597a.svg?style=flat-square)
<a id="cloth"></a>
## Cloth (53)

Papers on cloth, garments, and apparel-related dynamics, reconstruction, and avatar-centric modeling.

* **Dress Anyone : Automatic Physically-Based Garment Pattern Refitting 56** | PACMCGIT 2025  
  *Hsiao-yu Chen, Egor Larionov, Ladislav Kavan, Gene Wei-Chin Lin, et al.*  
  [[DOI]](https://doi.org/10.1145/3747858) [[Project]](https://igl.ethz.ch/projects/dress_anyone)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Optimization](https://img.shields.io/badge/-Optimization-457b9d.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square)

<br>

* **Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics** | TOG 2025  
  *Xuan Li, Chang Yu, Wenxin Du, Ying Jiang, et al.*  
  [[DOI]](https://doi.org/10.1145/3731177) [[Project]](https://dress-1-to-3.github.io/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square)

<br>

* **Frequency-Divided Learning of Fine-Grained Clothing Behavior via Flexible Dynamic Graphs** | TVCG 2025  
  *Tianxing Li, Rui Shi, Takashi Kanai, Qing Zhu*  
  [[DOI]](https://doi.org/10.1109/tvcg.2025.3591816) [[Project]](https://shirui-homepage.com/publication/2025-freq-div-TVCG)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos** | ICCV 2025  
  *Jiang, Hanxiao, Hsu, Hao-Yu, Zhang, Kaifeng, Yu, Hsin-Ni, et al.*  
  [[Project]](https://jianghanxiao.github.io/phystwin-web/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **PICA: Physics-Integrated Clothed Avatar** | TVCG 2025  
  *Bo Peng, Yunfan Tao, Haoyu Zhan, Yudong Guo, et al.*  
  [[DOI]](https://doi.org/10.1109/tvcg.2025.3560241) [[Project]](https://ustc3dv.github.io/PICA) [[DOI]](https://doi.org/10.1109/tvcg.2025.3614642)  
  ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![3DGS](https://img.shields.io/badge/-3DGS-bc6c25.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Self-Supervised Humidity-Controllable Garment Simulation via Capillary Bridge Modeling** | CGF 2025  
  *Min Shi, Xinyuan Wang, J. Zhang, Lin Gao, et al.*  
  [[DOI]](https://doi.org/10.1111/cgf.70236)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Bayesian Differentiable Physics for Cloth Digitalization** | CVPR 2024  
  *Deshan Gong, Ningtao Mao, He Wang*  
  [[Code]](https://github.com/realcrane/Bayesian-Differentiable-Physics-for-Cloth-Digitalization)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square)

<br>

* **ContourCraft: Learning to Resolve Intersections in Neural Multi-Garment Simulations** | Siggraph 2024  
  *Artur Grigorev, Giorgio Becherini, Michael J. Black, Otmar Hilliges, et al.*  
  [[DOI]](https://doi.org/10.1145/3641519.3657408)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **DiffAvatar: Simulation-Ready Garment Optimization with Differentiable Simulation** | CVPR 2024  
  *Li, Yifei, Chen, Hsiao-yu, Larionov, Egor, Sarafianos, Nikolaos, et al.*  
  [[Paper]](https://people.csail.mit.edu/liyifei/publication/diffavatar/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Optimization](https://img.shields.io/badge/-Optimization-457b9d.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square)

<br>

* **Efficient Deformation Learning of Varied Garments with a Structure-Preserving Multilevel Framework** | PACMCGIT 2024  
  *Tianxing Li, Rui Shi, Zihui Li, Takashi Kanai, et al.*  
  [[DOI]](https://doi.org/10.1145/3651286) [[Project]](https://li-tianxing.github.io/publication/psdunet)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Estimating Cloth Simulation Parameters From Tag Information and Cusick Drape Test** | CGF 2024  
  *Eunjung Ju, Kwang-yun Kim, S. W. Yoon, Eungjune Shim, et al.*  
  [[DOI]](https://doi.org/10.1111/cgf.15027) [[Project]](https://mingry.github.io/Fabrics5k)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Garment Animation NeRF with Color Editing** | CGF 2024  
  *Renke Wang, Meng Zhang, Jun Li, Jian Yang*  
  [[DOI]](https://doi.org/10.1111/cgf.15178) [[Project]](https://mengzephyr.com/Garment-Animation-NeRF-With-Color-Editing)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square) ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square)

<br>

* **GarmentDreamer: 3DGS Guided Garment Synthesis with Diverse Geometry and Texture Details** | Arxiv 2024  
  *Li, Boqian, Li, Xuan, Jiang, Ying, Xie, Tianyi, et al.*  
  [[Paper]](https://arxiv.org/abs/2405.12420)  
  ![3DGS](https://img.shields.io/badge/-3DGS-bc6c25.svg?style=flat-square)

<br>

* **Inverse Garment and Pattern Modeling with a Differentiable Simulator** | CGF 2024  
  *Boyang Yu, Frédéric Cordier, Hyewon Seo*  
  [[DOI]](https://doi.org/10.1111/cgf.15249)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Neural Garment Dynamic Super-Resolution** | Siggraph Asia 2024  
  *Meng Zhang, Jun Li*  
  [[DOI]](https://doi.org/10.1145/3680528.3687610) [[Project]](https://mengzephyr.com/Neural-Garment-Dynamic-Super-Reslution)  
  ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square)

<br>

* **Neural Garment Dynamics via Manifold-Aware Transformers** | CGF 2024  
  *Peizhuo Li, Tuanfeng Y. Wang, Timur Levent Kesdogan, Duygu Ceylan, et al.*  
  [[DOI]](https://doi.org/10.1111/cgf.15028) [[Code]](https://github.com/PeizhuoLi/manifold-aware-transformers)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![Transformer](https://img.shields.io/badge/-Transformer-bc6c25.svg?style=flat-square)

<br>

* **NeuralClothSim: Neural Deformation Fields Meet the Thin Shell Theory** | NeurIPS 2024  
  *Navami Kairanda, Marc Habermann, Christian Theobalt, Vladislav Golyanik*  
  [[Paper]](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c7649eeb93d2fad0ced9a3b974260710-Abstract-Conference.html) [[Project]](https://4dqv.mpi-inf.mpg.de/NeuralClothSim/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **Parametric Linear Blend Skinning Model for Multiple-Shape 3D Garments** | TVCG 2024  
  *X. Chen, Guangrun Wang, Xiaogang Xu, Philip H. S. Torr, et al.*  
  [[DOI]](https://doi.org/10.1109/tvcg.2024.3478852) [[Project]](https://www.sysu-hcp.net/projects/cv/126.html)  
  ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square)

<br>

* **Physics-guided Shape-from-Template: Monocular Video Perception through Neural Surrogate Models** | CVPR 2024  
  *David Stotko, Nils Wandel, Reinhard Klein*  
  [[DOI]](https://doi.org/10.1109/cvpr52733.2024.01130) [[Code]](https://github.com/vc-bonn/Physics-guided-Shape-from-Template)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Real-Time Neural Cloth Deformation Using a Compact Latent Space and a Latent Vector Predictor** | ECCV 2024  
  *Chanhaeng Lee, Maksym Perepichka, Saeed Ghorbani, Sudhir Mudur, et al.*  
  [[DOI]](https://doi.org/10.1007/978-3-031-92387-6_25)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Super-Resolution Cloth Animation with Spatial and Temporal Coherence** | TOG 2024  
  *Jiawang Yu, Zhendong Wang*  
  [[DOI]](https://doi.org/10.1145/3658143) [[Project]](https://www.physicsbasedanimation.com/2024/07/09/super-resolution-cloth-animation-with-spatial-and-temporal-coherence)  
  ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square)

<br>

* **ClothCombo: Modeling Inter-Cloth Interaction for Draping Multi-Layered Clothes** | TOG 2023  
  *Lee, Dohae, Kang, Hyun, Lee, In-Kwon*  
  [[Paper]](https://dl.acm.org/doi/10.1145/3618376)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **D-Cloth: Skinning-based Cloth Dynamic Prediction with a Three-stage Network** | CGF 2023  
  *Li, Yu Di, Tang, Min, Chen, Xiao Rui, Yang, Yun, et al.*  
  [[Project]](https://min-tang.github.io/home/DCloth/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Data-Free Learning of Reduced-Order Kinematics** | Siggraph 2023  
  *Sharp, Nicholas, Romero, Cristian, Jacobson, Alec, Vouga, Etienne, et al.*  
  [[Project]](https://nmwsharp.com/research/neural-physics-subspaces/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Detail-Aware Deep Clothing Animations Infused with Multi-Source Attributes** | CGF 2023  
  *Li, Tianxing, Shi, Rui, Kanai, Takashi*  
  [[Paper]](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14651)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **DiffXPBD: Differentiable Position-Based Simulation of Compliant Constraint Dynamics** | PACMCGIT 2023  
  *Stuyck, Tuur, Chen, Hsiao-yu*  
  [[DOI]](https://doi.org/10.1145/3606923)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Dynamic mesh-aware radiance fields** | ICCV 2023  
  *Qiao, Yi-Ling, Gao, Alexander, Xu, Yiran, Feng, Yue, et al.*  
  [[Project]](https://mesh-aware-rf.github.io/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square) ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square)

<br>

* **HOOD: Hierarchical Graphs for Generalized Modelling of Clothing Dynamics** | CVPR 2023  
  *Artur Grigorev, Michael J. Black, Otmar Hilliges*  
  [[DOI]](https://doi.org/10.1109/cvpr52729.2023.01627) [[Project]](https://dolorousrtur.github.io/hood/?trk=public_post_comment-text)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **How Will It Drape Like? Capturing Fabric Mechanics from Depth Images** | CGF 2023  
  *Carlos Rodríguez-Pardo, Melania Prieto-Martín, Dan Casas, Elena Garcés*  
  [[DOI]](http://dx.doi.org/10.1111/cgf.14750) [[Project]](https://carlosrodriguezpardo.es/projects/MechFromDepth) [[DOI]](https://doi.org/10.1111/cgf.14750)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Learning Anchor Transformations for 3D Garment Animation** | CVPR 2023  
  *Fang Zhao, Zekun Li, Shaoli Huang, Junwu Weng, et al.*  
  [[DOI]](https://doi.org/10.1109/cvpr52729.2023.00055) [[Project]](https://semanticdh.github.io/AnchorDEF)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square)

<br>

* **SwinGar: Spectrum-Inspired Neural Dynamic Deformation for Free-Swinging Garments** | TVCG 2023  
  *Tianxing Li, Rui Shi, Qing Zhu, Takashi Kanai*  
  [[DOI]](https://doi.org/10.1109/tvcg.2023.3346055)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Towards Multi-Layered 3D Garments Animation** | ICCV 2023  
  *Yidi Shao, Chen Change Loy, Bo Dai*  
  [[DOI]](https://doi.org/10.1109/iccv51070.2023.01321) [[Project]](https://mmlab-ntu.github.io/project/layersnet)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **DiffCloth: Differentiable Cloth Simulation with Dry Frictional Contact** | TOG 2022  
  *Li, Yifei, Du, Tao, Wu, Kui, Xu, Jie, et al.*  
  [[Paper]](https://people.csail.mit.edu/liyifei/publication/diffcloth/) [[DOI]](https://doi.org/10.1145/3527660)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Shape Design](https://img.shields.io/badge/-Shape%20Design-8ab17d.svg?style=flat-square)

<br>

* **Dressing avatars: Deep photorealistic appearance for physically simulated clothing** | TOG 2022  
  *Xiang, Donglai, Bagautdinov, Timur, Stuyck, Tuur, Prada, Fabian, et al.*  
  [[Project]](https://research.facebook.com/publications/dressing-avatars-deep-photorealistic-appearance-for-physically-simulated-clothing/)  
  ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square)

<br>

* **Learning Latent Graph Dynamics for Visual Manipulation of Deformable Objects** | ICRA 2022  
  *Xiao Ma, David Hsu, Wee Sun Lee*  
  [[DOI]](https://doi.org/10.1109/icra46639.2022.9811597)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Learning-based bending stiffness parameter estimation by a drape tester** | TOG 2022  
  *Feng, Xudong, Huang, Wenchao, Xu, Weiwei, Wang, Huamin*  
  [[Code]](https://github.com/DrapeTester/ClothDrapeTester)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Mesh-based Dynamics with Occlusion Reasoning for Cloth Manipulation** | RSS 2022  
  *Zixuan Huang, Xingyu Lin, David Held*  
  [[DOI]](https://doi.org/10.15607/rss.2022.xviii.011)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Neural cloth simulation** | TOG 2022  
  *Bertiche, Hugo, Madadi, Meysam, Escalera, Sergio*  
  [[Project]](https://hbertiche.github.io/NeuralClothSim/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Pattern-based cloth registration and sparse-view animation** | TOG 2022  
  *Halimi, Oshri, Stuyck, Tuur, Xiang, Donglai, Bagautdinov, Timur, et al.*  
  [[Paper]](https://dl.acm.org/doi/abs/10.1145/3550454.3555448)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Predicting loose-fitting garment deformations using bone-driven motion networks** | Siggraph 2022  
  *Pan, Xiaoyu, Mai, Jiaming, Jiang, Xinwei, Tang, Dongxue, et al.*  
  [[Project]](http://www.cad.zju.edu.cn/home/jin/SigCloth2022/SigCloth2022.htm)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Snug: Self-supervised neural dynamic garments** | CVPR 2022  
  *Santesteban, Igor, Otaduy, Miguel A, Casas, Dan*  
  [[Project]](http://mslab.es/projects/SNUG/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Dynamic neural garments** | TOG 2021  
  *Zhang, Meng, Wang, Tuanfeng Y., Ceylan, Duygu, Mitra, Niloy J.*  
  [[Project]](https://geometry.cs.ucl.ac.uk/projects/2021/DynamicNeuralGarments/) [[DOI]](https://doi.org/10.1145/3478513.3480497)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **gradSim: Differentiable Simulation for System Identification and Visuomotor Control** | ICLR 2021  
  *Krishna Murthy Jatavallabhula, Miles Macklin, Florian Golemo, Vikram Voleti, et al.*  
  [[Paper]](https://openreview.net/forum?id=c_E8kFWfhp0) [[Project]](https://gradsim.github.io/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Inverse Simulation: Reconstructing Dynamic Geometry of Clothed Humans via Optimal Control** | CVPR 2021  
  *Jingfan Guo, Jie Li, Rahul Narain, Hyun Soo Park*  
  [[DOI]](https://doi.org/10.1109/cvpr46437.2021.01446)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Cloth Reconstruction](https://img.shields.io/badge/-Cloth%20Reconstruction-6d597a.svg?style=flat-square)

<br>

* **Neural Implicit Surfaces for Efficient and Accurate Collisions in Physically Based Simulations** | Arxiv 2021  
  *Bertiche, Hugo, Madadi, Meysam, Escalera, Sergio*  
  [[Paper]](https://arxiv.org/abs/2110.01614) [[Project]](https://hbertiche.github.io/NeuralColliders/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **PBNS: physically based neural simulation for unsupervised garment pose space deformation** | TOG 2021  
  *Bertiche, Hugo, Madadi, Meysam, Escalera, Sergio*  
  [[Project]](https://hbertiche.github.io/PBNS/) [[DOI]](https://doi.org/10.1145/3478513.3480479)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Self-supervised collision handling via generative 3d garment models for virtual try-on** | CVPR 2021  
  *Santesteban, Igor, Thuerey, Nils, Otaduy, Miguel A, Casas, Dan*  
  [[Project]](http://mslab.es/projects/SelfSupervisedGarmentCollisions/)  
  ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square)

<br>

* **Cloth in the wind: A case study of physical measurement through simulation** | CVPR 2020  
  *Runia, Tom FH, Gavrilyuk, Kirill, Snoek, Cees GM, Smeulders, Arnold WM*  
  [[Paper]](https://arxiv.org/abs/2003.05065)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Learning Mesh-Based Simulation with Graph Networks** | ICLR 2020  
  *Tobias Pfaff, Meire Fortunato, Álvaro Sánchez-González, Peter Battaglia*  
  [[Paper]](http://arxiv.org/abs/2010.03409) [[Project]](https://sites.google.com/view/meshgraphnets) [[DOI]](https://doi.org/10.48550/arxiv.2010.03409)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Learning to measure the static friction coefficient in cloth contact** | CVPR 2020  
  *Rasheed, Abdullah Haroon, Romero, Victor, Bertails-Descoubes, Florence, Wuhrer, Stefanie, et al.*  
  [[Paper]](https://openaccess.thecvf.com/content_CVPR_2020/html/Rasheed_Learning_to_Measure_the_Static_Friction_Coefficient_in_Cloth_Contact_CVPR_2020_paper.html)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Projective dynamics with dry frictional contact** | TOG 2020  
  *Ly, Micka\"el, Jouve, Jean, Boissieux, Laurence, Bertails-Descoubes, Florence*  
  [[Project]](https://astcort.github.io/) [[DOI]](https://doi.org/10.1145/3386569.3392396)  
  ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Differentiable Cloth Simulation for Inverse Problems** | NeurIPS 2019  
  *Liang, Junbang, Lin, Ming, Koltun, Vladlen*  
  [[Project]](https://gamma.umd.edu/researchdirections/virtualtryon/differentiablecloth)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square)

<br>

* **Learning an intrinsic garment space for interactive authoring of garment animation** | TOG 2019  
  *Wang, Tuanfeng Y., Shao, Tianjia, Fu, Kai, Mitra, Niloy J.*  
  [[Project]](https://geometry.cs.ucl.ac.uk/projects/2019/garment_authoring/) [[DOI]](https://doi.org/10.1145/3355089.3356512)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square)
<a id="softbody"></a>
## Softbody (63)

Work on deformable objects, elasticity, fracture, soft robots, and learned physical models for soft materials.

* **Neuralocks: Real-Time Dynamic Neural Hair Simulation** | CGF 2026  
  *Gene Wei-Chin Lin, Egor Larionov, Hsiao-yu Chen, Doug Roble, et al.*  
  [[DOI]](https://doi.org/10.1111/cgf.70407)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![Hair](https://img.shields.io/badge/-Hair-ff7f0e.svg?style=flat-square)

<br>

* **A Differentiable Material Point Method Framework for Shape Morphing** | TVCG 2025  
  *Min Xu, Chongmin Song, David I. W. Levin, David Hyde*  
  [[DOI]](https://doi.org/10.1109/tvcg.2025.3591729) [[Project]](https://chayo.oopy.io/1e7e3760-68e9-808e-b30a-f89ba08d6193)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)

<br>

* **DeepFracture: A Generative Approach for Predicting Brittle Fractures with Neural Discrete Representation Learning** | CGF 2025  
  *Huang, Yuhang, Kanai, Takashi*  
  [[Project]](https://nikoloside.graphics/deepfracture/) [[DOI]](https://doi.org/10.1111/cgf.70002)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Fracture](https://img.shields.io/badge/-Fracture-3a86b8.svg?style=flat-square)

<br>

* **Differentiable Simulation of Soft Robots with Frictional Contacts** | IEEE 8th International Conference on Soft Robotics (RoboSoft) 2025  
  *Etienne Ménager, Louis Montaut, Quentin Le Lidec, Justin Carpentier*  
  [[DOI]](https://doi.org/10.1109/ROBOSOFT63089.2025.11020844) [[Project]](https://simple-robotics.github.io/publications/differentiable-soft-robotics/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Elastic Locomotion with Mixed Second-order Differentiation** | Siggraph 2025  
  *Siyuan Shen, Tianjia Shao, Kun Zhou, Chenfanfu Jiang, et al.*  
  [[DOI]](https://doi.org/10.1145/3721238.3730685)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Inverse Design of Discrete Interlocking Materials with Desired Mechanical Behavior** | Siggraph 2025  
  *Pengbin Tang, Bernhard Thomaszewski, Stelian Coros, Bernd Bickel*  
  [[DOI]](https://doi.org/10.1145/3721238.3730675) [[Project]](https://tangpengbin.github.io/publications/InverseDIM/index.html)  
  ![Optimization](https://img.shields.io/badge/-Optimization-457b9d.svg?style=flat-square) ![Shape Design](https://img.shields.io/badge/-Shape%20Design-8ab17d.svg?style=flat-square)

<br>

* **Learning Object Properties Using Robot Proprioception via Differentiable Robot-Object Interaction** | ICRA 2025  
  *Peter Yichen Chen, Lijun Liu, Pingchuan Ma, J. J. Eastman, et al.*  
  [[DOI]](https://doi.org/10.1109/icra55743.2025.11127955) [[Project]](https://warpdiffrobot.github.io/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Neural Modular Physics for Elastic Simulation** | Arxiv 2025  
  *Li, Yifei, Wu, Haixu, Xu, Zeyi, Stuyck, Tuur, et al.*  
  [[Paper]](https://arxiv.org/abs/2512.15083) [[Project]](https://people.csail.mit.edu/liyifei/publication/nmp)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Neurally Integrated Finite Elements for Differentiable Elasticity on Evolving Domains** | TOG 2025  
  *Gilles Daviet, Tianchang Shen, Nicholas Sharp, David I. W. Levin*  
  [[DOI]](https://doi.org/10.1145/3727874) [[Project]](https://research.nvidia.com/labs/toronto-ai/flexisim/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square)

<br>

* **Precise Gradient Discontinuities in Neural Fields for Subspace Physics** | Siggraph Asia 2025  
  *Mengfei Liu, Yue Chang, Zhecheng Wang, Peter Yichen Chen, et al.*  
  [[DOI]](https://doi.org/10.1145/3757377.3763810) [[Project]](https://www.dgp.toronto.edu/projects/discont_grad)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **Quaffure: Real-Time Quasi-Static Neural Hair Simulation** | CVPR 2025  
  *Tuur Stuyck, Gene Wei-Chin Lin, Egor Larionov, Hsiao-yu Chen, et al.*  
  [[DOI]](https://doi.org/10.1109/cvpr52734.2025.00031) [[Project]](https://tuurstuyck.github.io/quaffure/quaffure.html)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![Hair](https://img.shields.io/badge/-Hair-ff7f0e.svg?style=flat-square)

<br>

* **Self-supervised Learning of Latent Space Dynamics** | PACMCGIT 2025  
  *Yue Li, Gene Wei-Chin Lin, Egor Larionov, Aljaž Božič, et al.*  
  [[DOI]](https://doi.org/10.1145/3747854)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square)

<br>

* **Shape Space Spectra** | TOG 2025  
  *Chang Yue, Otman Benchekroun, Maurizio M. Chiaramonte, Peter Yichen Chen, et al.*  
  [[DOI]](https://doi.org/10.1145/3731148) [[Project]](https://www.dgp.toronto.edu/projects/sss)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Sound](https://img.shields.io/badge/-Sound-2f6db3.svg?style=flat-square) ![Shape Design](https://img.shields.io/badge/-Shape%20Design-8ab17d.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **Structure from Collision** | CVPR 2025  
  *Takuhiro Kaneko*  
  [[DOI]](https://doi.org/10.1109/cvpr52734.2025.01521)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square) ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square) ![3DGS](https://img.shields.io/badge/-3DGS-bc6c25.svg?style=flat-square)

<br>

* **Differentiable solver for time-dependent deformation problems with contact** | TOG 2024  
  *Huang, Zizhou, Tozoni, Davi Colli, Gjoka, Arvi, Ferguson, Zachary, et al.*  
  [[Paper]](https://dl.acm.org/doi/10.1145/3657648)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square) ![Shape Design](https://img.shields.io/badge/-Shape%20Design-8ab17d.svg?style=flat-square)

<br>

* **Differentiable Voronoi Diagrams for Simulation of Cell-Based Mechanical Systems** | TOG 2024  
  *Numerow, Logan, Li, Yue, Coros, Stelian, Thomaszewski, Bernhard*  
  [[Code]](https://github.com/lnumerow-ethz/VoronoiCellSim)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **DiffSound: Differentiable Modal Sound Rendering and Inverse Rendering for Diverse Inference Tasks** | Siggraph 2024  
  *Xutong Jin, Chenxi Xu, Ruohan Gao, Jiajun Wu, et al.*  
  [[DOI]](https://doi.org/10.1145/3641519.3657493) [[Project]](https://hellojxt.github.io/DiffSound/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Sound](https://img.shields.io/badge/-Sound-2f6db3.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square)

<br>

* **ElastoGen: 4D Generative Elastodynamics** | Arxiv 2024  
  *Feng, Yutao, Shang, Yintong, Feng, Xiang, Lan, Lei, et al.*  
  [[Paper]](https://arxiv.org/abs/2405.15056)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing** | Arxiv 2024  
  *Qiu, Ri-Zhao, Yang, Ge, Zeng, Weijia, Wang, Xiaolong*  
  [[Project]](https://feature-splatting.github.io/)  
  ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square) ![3DGS](https://img.shields.io/badge/-3DGS-bc6c25.svg?style=flat-square)

<br>

* **Improving Physics-Augmented Continuum Neural Radiance Field-Based Geometry-Agnostic System Identification with Lagrangian Particle Optimization** | CVPR 2024  
  *Takuhiro Kaneko*  
  [[DOI]](https://doi.org/10.1109/cvpr52733.2024.00523)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Parameter Estimation](https://img.shields.io/badge/-Parameter%20Estimation-6d597a.svg?style=flat-square) ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square)

<br>

* **Near-realtime Facial Animation by Deep 3D Simulation Super-Resolution** | TOG 2024  
  *Hyojoon Park, Sangeetha Grama Srinivasan, Matthew Cong, Doyub Kim, et al.*  
  [[DOI]](https://doi.org/10.1145/3670687) [[Code]](https://github.com/hjoonpark/3d-sim-super-res)  
  ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![Super Resolution](https://img.shields.io/badge/-Super%20Resolution-8ab17d.svg?style=flat-square)

<br>

* **Neural Modes: Self-supervised Learning of Nonlinear Modal Subspaces** | CVPR 2024  
  *Jiahong Wang, Yinwei Du, Stelian Coros, Bernhard Thomaszewski*  
  [[DOI]](https://doi.org/10.1109/cvpr52733.2024.02185) [[Code]](https://github.com/jiahong-w/neural-modes)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square)

<br>

* **PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation** | Arxiv 2024  
  *Tianyuan Zhang, Hong-Xing Yu, Rundi Wu, Brandon Y. Feng, et al.*  
  [[Project]](https://physdreamer.github.io/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Pie-nerf: Physics-based interactive elastodynamics with nerf** | CVPR 2024  
  *Feng, Yutao, Shang, Yintong, Li, Xuan, Shao, Tianjia, et al.*  
  [[Project]](https://fytalon.github.io/pienerf/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square) ![NeRF](https://img.shields.io/badge/-NeRF-e76f51.svg?style=flat-square)

<br>

* **Real-time Wing Deformation Simulations for Flying Insects** | Siggraph 2024  
  *Qiang Chen, Zhigang Deng, Feng Li, Yuming Fang, et al.*  
  [[DOI]](https://doi.org/10.1145/3641519.3657434) [[Project]](https://graphics.cs.uh.edu/article/2024/2640/2024-siggraph-insectwingdeformation/)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square)

<br>

* **VR-GS: A Physical Dynamics-Aware Interactive Gaussian Splatting System in Virtual Reality** | Arxiv 2024  
  *Jiang, Ying, Yu, Chang, Xie, Tianyi, Li, Xuan, et al.*  
  [[Project]](https://yingjiang96.github.io/VR-GS/)  
  ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square) ![3DGS](https://img.shields.io/badge/-3DGS-bc6c25.svg?style=flat-square)

<br>

* **Beyond Chainmail: Computational Modeling of Discrete Interlocking Materials** | TOG 2023  
  *Pengbin Tang, Stelian Coros, Bernhard Thomaszewski*  
  [[DOI]](https://doi.org/10.1145/3592112)  
  ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **DefGraspNets: Grasp Planning on 3D Fields with Graph Neural Nets** | ICRA 2023  
  *Isabella Huang, Yashraj Narang, Růžena Bajcsy, Fábio Ramos, et al.*  
  [[DOI]](https://doi.org/10.1109/icra48891.2023.10160986) [[Project]](https://research.nvidia.com/publication/2023-05_defgraspnets-grasp-planning-3d-fields-graph-neural-nets)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **DiffVL: Scaling Up Soft Body Manipulation using Vision-Language Driven Differentiable Physics** | NeurIPS 2023  
  *Huang, Zhiao, Chen, Feng, Pu, Yewen, Lin, Chunru, et al.*  
  [[Paper]](https://arxiv.org/abs/2312.06408)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Elastic Context: Encoding Elasticity for Data-driven Models of Textiles Elastic Context: Encoding Elasticity for Data-driven Models of Textiles** | ICRA 2023  
  *Alberta Longhini, Marco Moletta, Alfredo Reichlin, Michael C. Welle, et al.*  
  [[DOI]](https://doi.org/10.1109/icra48891.2023.10160740)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Learning Contact Deformations with General Collider Descriptors** | Siggraph Asia 2023  
  *Romero, Cristian, Casas, Dan, Chiaramonte, Maurizio, Otaduy, Miguel A*  
  [[Project]](https://dancasas.github.io/)  
  ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **LiCROM: Linear-Subspace Continuous Reduced Order Modeling with Neural Fields** | Siggraph Asia 2023  
  *Chang, Yue, Chen, Peter Yichen, Wang, Zhecheng, Chiaramonte, Maurizio M., et al.*  
  [[Paper]](https://arxiv.org/abs/2310.15907) [[DOI]](https://doi.org/10.1145/3610548.3618158)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **Neural Metamaterial Networks for Nonlinear Material Design** | TOG 2023  
  *Li, Yue, Coros, Stelian, Thomaszewski, Bernhard*  
  [[Code]](https://github.com/liyuesolo/NeuralMetamaterialNetwork) [[DOI]](https://doi.org/10.1145/3618325)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Optimization](https://img.shields.io/badge/-Optimization-457b9d.svg?style=flat-square)

<br>

* **Neuwigs: A neural dynamic model for volumetric hair capture and animation** | CVPR 2023  
  *Wang, Ziyan, Nam, Giljoo, Stuyck, Tuur, Lombardi, Stephen, et al.*  
  [[Project]](https://ziyanw1.github.io/neuwigs/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Hair](https://img.shields.io/badge/-Hair-ff7f0e.svg?style=flat-square)

<br>

* **SAM-RL: Sensing-Aware Model-Based Reinforcement Learning via Differentiable Physics-Based Simulation and Rendering** | RSS 2023  
  *Jun Lv, Yunhai Feng, Cheng Zhang, Shuang Zhao, et al.*  
  [[DOI]](https://doi.org/10.15607/rss.2023.xix.040)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Contact-centric deformation learning** | TOG 2022  
  *Romero, Cristian, Casas, Dan, Chiaramonte, Maurizio M, Otaduy, Miguel A*  
  [[Project]](http://mslab.es/projects/ContactCentricLearning/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Differentiable Depth for Real2Sim Calibration of Soft Body Simulations** | CGF 2022  
  *Kasra Arnavaz, Mads Nielsen, Paul G. Kry, Miles Macklin, et al.*  
  [[DOI]](https://doi.org/10.1111/cgf.14720) [[Project]](https://researchprofiles.ku.dk/en/publications/differentiable-depth-for-real2sim-calibration-of-soft-body-simula)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square)

<br>

* **Differentiable simulation of inertial musculotendons** | TOG 2022  
  *Wang, Ying, Verheul, Jasper, Yeo, Sang-Hoon, Kalantari, Nima Khademi, et al.*  
  [[Paper]](https://dl.acm.org/doi/abs/10.1145/3550454.3555490)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools** | ICLR 2022  
  *Xingyu Lin, Zhiao Huang, Yunzhu Li, Joshua B. Tenenbaum, et al.*  
  [[Paper]](https://arxiv.org/abs/2203.17275) [[Project]](https://xingyu-lin.github.io/diffskill/) [[DOI]](https://doi.org/10.48550/arXiv.2203.17275)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Implicit neural representation for physics-driven actuated soft bodies** | TOG 2022  
  *Yang, Lingchen, Kim, Byungsoo, Zoss, Gaspard, G\"ozc\"u, Baran, et al.*  
  [[Paper]](https://people.inf.ethz.ch/zossg/publication/yang-2022/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **Learning to Synthesize Volumetric Meshes from Vision-based Tactile Imprints** | ICRA 2022  
  *Xinghao Zhu, Siddarth Jain, Masayoshi Tomizuka, Jeroen van Baar*  
  [[DOI]](https://doi.org/10.1109/icra46639.2022.9812092)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Neuphysics: Editable neural geometry and physics from monocular videos** | NeurIPS 2022  
  *Qiao, Yi-Ling, Gao, Alexander, Lin, Ming*  
  [[Project]](https://sites.google.com/view/neuphysics/home)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **RoboCraft: Learning to See, Simulate, and Shape Elasto-Plastic Objects with Graph Networks** | RSS 2022  
  *Haochen Shi, Huazhe Xu, Zhiao Huang, Yunzhu Li, et al.*  
  [[DOI]](https://doi.org/10.15607/rss.2022.xviii.008)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Soft Robots Learn to Crawl: Jointly Optimizing Design and Control with Sim-to-Real Transfer** | RSS 2022  
  *Charles Schaff, Audrey Sedal, Matthew R. Walter*  
  [[DOI]](https://doi.org/10.15607/rss.2022.xviii.062)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Soft Robot](https://img.shields.io/badge/-Soft%20Robot-bc6c25.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Tracking Fast Trajectories with a Deformable Object using a Learned Model** | ICRA 2022  
  *James A. Preiss, David Millard, Tao Yao, Gaurav S. Sukhatme*  
  [[DOI]](https://doi.org/10.1109/icra46639.2022.9812189) [[Project]](https://uscresl.org/publication/tracking-fast-trajectories-with-a-deformable-object-using-a-learned-model)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Virtual Elastic Objects** | CVPR 2022  
  *Hsiao-yu Chen, Edith Tretschk, Tuur Stuyck, Petr Kadleček, et al.*  
  [[DOI]](https://doi.org/10.1109/cvpr52688.2022.01537) [[Project]](https://hsiaoyu.github.io/VEO)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square)

<br>

* **A Deep Emulator for Secondary Motion of 3D Characters** | CVPR 2021  
  *Mianlun Zheng, Yi Zhou, Duygu Ceylan, Jernej Barbič*  
  [[DOI]](https://doi.org/10.1109/cvpr46437.2021.00587) [[Code]](https://github.com/ZhengMianlun/deep_emulator)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square)

<br>

* **Accurately Solving Rod Dynamics with Graph Learning** | NeurIPS 2021  
  *Han Shao, Tassilo Kugelstadt, Torsten Hädrich, Wojtek Pałubicki, et al.*  
  [[Project]](http://hdl.handle.net/10754/679142) [[Project]](https://computationalsciences.org/publications/shao-2021-physical-systems-graph-learning.html)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **DiffAqua** | TOG 2021  
  *Pingchuan Ma, Tao Du, John Z. Zhang, Kui Wu, et al.*  
  [[DOI]](https://doi.org/10.1145/3450626.3459832) [[Project]](https://diffaqua.csail.mit.edu/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Optimization](https://img.shields.io/badge/-Optimization-457b9d.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Soft Robot](https://img.shields.io/badge/-Soft%20Robot-bc6c25.svg?style=flat-square) ![Underwater Robot](https://img.shields.io/badge/-Underwater%20Robot-ff7f0e.svg?style=flat-square) ![Robot Control](https://img.shields.io/badge/-Robot%20Control-8ab17d.svg?style=flat-square)

<br>

* **Differentiable simulation of soft multi-body systems** | NeurIPS 2021  
  *Qiao, Yiling, Liang, Junbang, Koltun, Vladlen, Lin, Ming*  
  [[Code]](https://github.com/YilingQiao/diff_fem)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **Diffpd: Differentiable projective dynamics** | TOG 2021  
  *Du, Tao, Wu, Kui, Ma, Pingchuan, Wah, Sebastien, et al.*  
  [[Project]](https://people.iiis.tsinghua.edu.cn/~taodu/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **Fast and Feature-Complete Differentiable Physics Engine for Articulated Rigid Bodies with Contact Constraints** | RSS 2021  
  *Keenon Werling AND Dalton Omens AND Jeongseok Lee AND Ioannis Exarchos AND C. Karen Liu*  
  [[Paper]](https://arxiv.org/abs/2103.16021) [[DOI]](https://doi.org/10.15607/RSS.2021.XVII.034)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **High-order differentiable autoencoder for nonlinear model reduction** | TOG 2021  
  *Shen, Siyuan, Yang, Yin, Shao, Tianjia, Wang, He, et al.*  
  [[Paper]](https://dl.acm.org/doi/10.1145/3450626.3459754) [[DOI]](https://doi.org/10.1145/3450626.3459754)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square)

<br>

* **Learning active quasistatic physics-based models from data** | TOG 2021  
  *Srinivasan, Sangeetha Grama, Wang, Qisi, Rojas, Junior, Kl\'ar, Gergely, et al.*  
  [[Project]](https://pages.cs.wisc.edu/~qisiw/SIG.html)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Avatar](https://img.shields.io/badge/-Avatar-4c78a8.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square)

<br>

* **Learning contact corrections for handle-based subspace dynamics** | TOG 2021  
  *Romero, Cristian, Casas, Dan, P\'erez, Jes\'us, Otaduy, Miguel*  
  [[Project]](http://mslab.es/projects/LearningContactCorrections/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Learning to Propagate Interaction Effects for Modeling Deformable Linear Objects Dynamics** | ICRA 2021  
  *Yuxuan Yang, Johannes A. Stork, Todor Stoyanov*  
  [[DOI]](https://doi.org/10.1109/icra48506.2021.9561636) [[Project]](https://amm.aass.oru.se/icra2021-learning-dlo)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **ADD: analytically differentiable dynamics for multi-body systems with frictional contact** | TOG 2020  
  *Geilinger, Moritz, Hahn, David, Zehnder, Jonas, B\"acher, Moritz, et al.*  
  [[Paper]](https://arxiv.org/abs/2007.00987) [[DOI]](https://doi.org/10.1145/3414685.3417766)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Correspondence-Free Material Reconstruction using Sparse Surface Constraints** | CVPR 2020  
  *Sebastian Weiß, Robert Maier, Daniel Cremers, Rüdiger Westermann, et al.*  
  [[DOI]](https://doi.org/10.1109/cvpr42600.2020.00474) [[Project]](https://ge.in.tum.de/publications/2020-cvpr-weiss)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Real-time hair simulation with neural interpolation** | TVCG 2020  
  *Lyu, Qing, Chai, Menglei, Chen, Xiang, Zhou, Kun*  
  [[Paper]](https://www.mlchai.com/publication/lyu2020real/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![CNN](https://img.shields.io/badge/-CNN-e76f51.svg?style=flat-square) ![Hair](https://img.shields.io/badge/-Hair-ff7f0e.svg?style=flat-square)

<br>

* **ChainQueen: A Real-Time Differentiable Physical Simulator for Soft Robotics** | ICRA 2019  
  *Hu, Yuanming, Liu, Jiancheng, Spielberg, Andrew, Tenenbaum, Joshua B., et al.*  
  [[Code]](https://github.com/yuanming-hu/ChainQueen) [[DOI]](https://doi.org/10.1109/ICRA.2019.8794333)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Latent-space dynamics for reduced deformable simulation** | CGF 2019  
  *Fulton, Lawson, Modi, Vismay, Duvenaud, David, Levin, David IW, et al.*  
  [[Project]](https://www.dgp.toronto.edu/projects/latent-space-dynamics/)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square)

<br>

* **Real2Sim: visco-elastic parameter estimation from dynamic motion** | TOG 2019  
  *Hahn, David, Banzet, Pol, Bern, James M., Coros, Stelian*  
  [[Paper]](https://dl.acm.org/doi/10.1145/3355089.3356548) [[DOI]](https://doi.org/10.1145/3355089.3356548)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square)

<br>

* **SoftCon: simulation and control of soft-bodied animals with biomimetic actuators** | TOG 2019  
  *Min, Sehee, Won, Jungdam, Lee, Seunghwan, Park, Jungnam, et al.*  
  [[Project]](https://mrl.snu.ac.kr/publications/ProjectSoftCon/SoftCon.html?utm_campaign=Artificial%2BIntelligence%2BWeekly&utm_medium=rss&utm_source=Artificial_Intelligence_Weekly_153) [[DOI]](https://doi.org/10.1145/3355089.3356497)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)
<a id="rigidbody"></a>
## Rigidbody (38)

Methods for articulated rigid bodies, robotics, contact-rich motion, and rigid object dynamics.

* **Efficient Differentiable Contact Model with Long-range Influence** | ICLR 2026  
  *Xiaohan Ye, Kui Wu, Zherong Pan, Taku Komura*  
  [[Paper]](https://arxiv.org/abs/2509.20917) [[DOI]](https://doi.org/10.48550/arXiv.2509.20917)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Newton: An Open-Source, GPU-Accelerated Physics Simulation Engine Built upon NVIDIA Warp** | 2025  
  *newton-physics contributors*  
  [[Code]](https://github.com/newton-physics/newton)  
  ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)

<br>

* **Painless Differentiable Rotation Dynamics** | TOG 2025  
  *Magí Romanyà-Serrasolsas, Juan J. Casafranca, Miguel Á. Otaduy*  
  [[DOI]](https://doi.org/10.1145/3730944) [[Project]](https://mslab.es/projects/Painless/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions** | CVPR 2025  
  *Qi Ruan, Jiabao Lei, Wenhao Yuan, Yanglin Zhang, et al.*  
  [[DOI]](https://doi.org/10.1109/cvpr52734.2025.02101)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Estimating Material Properties of Interacting Objects Using Sum-GP-UCB** | ICRA 2024  
  *M. Yunus Seker, Oliver Kroemer*  
  [[DOI]](https://doi.org/10.1109/icra57147.2024.10610129) [[Project]](https://myunusseker.github.io/SumGP)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square) ![Material Estimation](https://img.shields.io/badge/-Material%20Estimation-6d597a.svg?style=flat-square)

<br>

* **Jade: A Differentiable Physics Engine for Articulated Rigid Bodies with Intersection-Free Frictional Contact** | ICRA 2024  
  *Yang, Gang, Luo, Siyuan, Feng, Yunhai, Sun, Zhixin, et al.*  
  [[Project]](https://sites.google.com/view/diffsim/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Soft Pneumatic Actuator Design using Differentiable Simulation** | Siggraph 2024  
  *Arvi Gjoka, Espen Knoop, Moritz Bächer, Denis Zorin, et al.*  
  [[DOI]](https://doi.org/10.1145/3641519.3657467) [[Project]](https://la.disneyresearch.com/publication/soft-pneumatic-actuator-design-using-differentiable-simulation)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Optimization](https://img.shields.io/badge/-Optimization-457b9d.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Shape Design](https://img.shields.io/badge/-Shape%20Design-8ab17d.svg?style=flat-square)

<br>

* **An Extensible, Data-Oriented Architecture for High-Performance, Many-World Simulation** | TOG 2023  
  *Shacklett, Brennan, Rosenzweig, Luc Guy, Xie, Zhiqiang, Sarkar, Bidipta, et al.*  
  [[Project]](https://madrona-engine.github.io/) [[DOI]](https://doi.org/10.1145/3592427)  
  ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)

<br>

* **Differentiable Dynamics Simulation Using Invariant Contact Mapping and Damped Contact Force** | ICRA 2023  
  *Minji Lee, Jeong Min Lee, Dongjun Lee*  
  [[DOI]](https://doi.org/10.1109/icra48891.2023.10161519)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Differentiable Physics Simulation of Dynamics-Augmented Neural Objects** | RA-L 2023  
  *Le Cleac'h, Simon, Yu, Hong-Xing, Guo, Michelle, Howell, Taylor A., et al.*  
  [[DOI]](https://doi.org/10.1109/LRA.2023.3257707)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square)

<br>

* **DOC: Differentiable Optimal Control for Retargeting Motions onto Legged Robots** | TOG 2023  
  *Grandia, Ruben, Farshidian, Farbod, Knoop, Espen, Schumacher, Christian, et al.*  
  [[Paper]](https://la.disneyresearch.com/publication/doc-differentiable-optimal-control-for-retargeting-motions-onto-legged-robots/) [[DOI]](https://doi.org/10.1145/3592454)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Robot Control](https://img.shields.io/badge/-Robot%20Control-8ab17d.svg?style=flat-square)

<br>

* **Dynamic-Resolution Model Learning for Object Pile Manipulation** | RSS 2023  
  *Yixuan Wang, Yunzhu Li, Katherine Driggs-Campbell, Li Fei-Fei, et al.*  
  [[DOI]](https://doi.org/10.15607/rss.2023.xix.047) [[Code]](https://github.com/WangYixuan12/dyn-res-pile-manip)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Robot Control](https://img.shields.io/badge/-Robot%20Control-8ab17d.svg?style=flat-square)

<br>

* **Fast-Grasp'D: Dexterous Multi-finger Grasp Generation Through Differentiable Simulation** | ICRA 2023  
  *Dylan Turpin, Tao Zhong, Shutong Zhang, Guanglei Zhu, et al.*  
  [[DOI]](https://doi.org/10.1109/icra48891.2023.10160314)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Neural Collision Fields for Triangle Primitives** | Siggraph Asia 2023  
  *Zesch, Ryan S., Modi, Vismay, Sueda, Shinjiro, Levin, David I.W.*  
  [[Paper]](https://research.nvidia.com/labs/prl/publication/zesch2023ncf/) [[DOI]](https://doi.org/10.1145/3610548.3618225)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Neural Field](https://img.shields.io/badge/-Neural%20Field-8ab17d.svg?style=flat-square)

<br>

* **RoboNinja: Learning an Adaptive Cutting Policy for Multi-Material Objects** | RSS 2023  
  *Zhenjia Xu, Xian Zhou, Xingyu Lin, Cheng Chi, et al.*  
  [[DOI]](https://doi.org/10.15607/rss.2023.xix.046)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square)

<br>

* **Vr-handnet: A visually and physically plausible hand manipulation system in virtual reality** | TVCG 2023  
  *Han, DongHeun, Lee, RoUn, Kim, KyeongMin, Kang, HyeongYeop*  
  [[Paper]](https://ieeexplore.ieee.org/abstract/document/10066837)  
  ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![User Interaction](https://img.shields.io/badge/-User%20Interaction-8ab17d.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Accelerated Policy Learning with Parallel Differentiable Simulation** | Conference on Robot Learning (CoRL) 2022  
  *Jie Xu, Viktor Makoviychuk, Yashraj Narang, Fábio Ramos, et al.*  
  [[Paper]](https://arxiv.org/abs/2204.07137) [[Project]](https://short-horizon-actor-critic.github.io/) [[DOI]](https://doi.org/10.48550/arXiv.2204.07137)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square) ![Robot Control](https://img.shields.io/badge/-Robot%20Control-8ab17d.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Dojo: A Differentiable Physics Engine for Robotics** | Arxiv 2022  
  *Howell, Taylor, Le Cleac'h, Simon, Bruedigam, Jan, Kolter, Zico, et al.*  
  [[Project]](https://sites.google.com/view/dojo-sim)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)

<br>

* **Learning Object Relations with Graph Neural Networks for Target-Driven Grasping in Dense Clutter** | ICRA 2022  
  *Xibai Lou, Yang Yang, Changhyun Choi*  
  [[DOI]](https://doi.org/10.1109/icra46639.2022.9811601)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square) ![Robot Control](https://img.shields.io/badge/-Robot%20Control-8ab17d.svg?style=flat-square)

<br>

* **Learning physical dynamics with subequivariant graph neural networks** | NeurIPS 2022  
  *Han, Jiaqi, Huang, Wenbing, Ma, Hengbo, Li, Jiachen, et al.*  
  [[Project]](https://hanjq17.github.io/SGNN/)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)

<br>

* **Learning physics constrained dynamics using autoencoders** | NeurIPS 2022  
  *Yang, Tsung-Yen, Rosca, Justinian, Narasimhan, Karthik, Ramadge, Peter J*  
  [[Paper]](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6d5e035724687454549b97d6c805dc84-Abstract-Conference.html)  
  ![Neural Representation](https://img.shields.io/badge/-Neural%20Representation-4c78a8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **Physical Simulation Layer for Accurate 3D Modeling** | CVPR 2022  
  *Mariem Mezghanni, Théo Bodrito, Malika Boulkenafed, Maks Ovsjanikov*  
  [[DOI]](https://doi.org/10.1109/cvpr52688.2022.01315)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square)

<br>

* **Probabilistic Inference of Simulation Parameters via Parallel Differentiable Simulation** | ICRA 2022  
  *Eric Heiden, Christopher E. Denniston, David Millard, Fábio Ramos, et al.*  
  [[DOI]](https://doi.org/10.1109/icra46639.2022.9812293) [[Project]](https://uscresl.github.io/prob-diff-sim)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **SAGCI-System: Towards Sample-Efficient, Generalizable, Compositional, and Incremental Robot Learning** | ICRA 2022  
  *Jun Lv, Qiaojun Yu, Lin Shao, Wenhai Liu, et al.*  
  [[DOI]](https://doi.org/10.1109/icra46639.2022.9811859)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Brax - A Differentiable Physics Engine for Large Scale Rigid Body Simulation** | NeurIPS 2021  
  *C. Daniel Freeman, Erik Frey, Anton Raichuk, Sertan Girgin, et al.*  
  [[Code]](https://github.com/google/brax)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **DiSECt: A Differentiable Simulation Engine for Autonomous Robotic Cutting** | RSS 2021  
  *Eric Heiden, Miles Macklin, Yashraj Narang, Dieter Fox, et al.*  
  [[DOI]](https://doi.org/10.15607/rss.2021.xvii.067) [[Project]](https://eric-heiden.com/publication/2021-disect-rss)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)

<br>

* **Efficient Differentiable Simulation of Articulated Bodies** | ICML 2021  
  *Qiao, Yi-Ling, Liang, Junbang, Koltun, Vladlen, Lin, Ming C.*  
  [[Code]](https://github.com/YilingQiao/diffarticulated)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **NeuralSim: Augmenting Differentiable Simulators with Neural Networks** | ICRA 2021  
  *Heiden, Eric, Millard, David, Coumans, Erwin, Sheng, Yizhou, et al.*  
  [[Code]](https://github.com/erwincoumans/tiny-differentiable-simulator)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **NeuralSim: Augmenting Differentiable Simulators with Neural Networks** | ICRA 2021  
  *Eric Heiden, David Millard, Erwin Coumans, Yizhou Sheng, et al.*  
  [[DOI]](https://doi.org/10.1109/icra48506.2021.9560935) [[Project]](https://uscresl.org/publication/neuralsim-augmenting-differentiable-simulators-with-neural-networks)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square)

<br>

* **PyBullet, a Python module for physics simulation for games, robotics and machine learning** | 2016--2021  
  *Erwin Coumans, Yunfei Bai*  
  [[Project]](http://pybullet.org)  
  ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)

<br>

* **Single-view robot pose and joint angle estimation via render & compare** | CVPR 2021  
  *Labb\'e, Yann, Carpentier, Justin, Aubry, Mathieu, Sivic, Josef*  
  [[Project]](https://www.di.ens.fr/willow/research/robopose/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square)

<br>

* **The Role of Physics-Based Simulators in Robotics** | ARCRAS 2021  
  *Liu, C. Karen, Negrut, Dan*  
  [[DOI]](https://doi.org/10.1146/annurev-control-072220-093055)  
  ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Survey](https://img.shields.io/badge/-Survey-3a86b8.svg?style=flat-square)

<br>

* **Rl-cyclegan: Reinforcement learning aware simulation-to-real** | CVPR 2020  
  *Rao, Kanishka, Harris, Chris, Irpan, Alex, Levine, Sergey, et al.*  
  [[Paper]](https://arxiv.org/abs/2006.09001)  
  ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Scalable Differentiable Physics for Learning and Control** | ICML 2020  
  *Qiao, Yi-Ling, Liang, Junbang, Koltun, Vladlen, Lin, Ming C.*  
  [[Code]](https://github.com/YilingQiao/diffsim)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square)

<br>

* **Use the force, luke! learning to predict physical forces by simulating effects** | CVPR 2020  
  *Ehsani, Kiana, Tulsiani, Shubham, Gupta, Saurabh, Farhadi, Ali, et al.*  
  [[Project]](https://ehsanik.github.io/forcecvpr2020/)  
  ![Reconstruction](https://img.shields.io/badge/-Reconstruction-3a86b8.svg?style=flat-square) ![Real2Sim](https://img.shields.io/badge/-Real2Sim-e76f51.svg?style=flat-square)

<br>

* **Drake: Model-based design and verification for robotics** | 2019  
  *Russ Tedrake, the Drake Development Team*  
  [[Project]](https://drake.mit.edu)  
  ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square)

<br>

* **Learning to fly: computational controller design for hybrid UAVs with reinforcement learning** | TOG 2019  
  *Xu, Jie, Du, Tao, Foshey, Michael, Li, Beichen, et al.*  
  [[Project]](https://people.csail.mit.edu/jiex/papers/LearningToFly/index.html) [[DOI]](https://doi.org/10.1145/3306346.3322940)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **MuJoCo: A physics engine for model-based control** | IROS 2012  
  *Todorov, Emanuel, Erez, Tom, Tassa, Yuval*  
  [[Project]](https://mujoco.org/) [[DOI]](https://doi.org/10.1109/IROS.2012.6386109)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)
<a id="multiphys"></a>
## Multiphys (13)

Papers that span multiple physical domains or focus on coupled systems and general simulation frameworks.

* **Multiphysics Simulation Methods in Computer Graphics** | CGF 2025  
  *Daniel Holz, Stefan Rhys Jeske, Fabian Löschner, Jan Bender, et al.*  
  [[DOI]](https://doi.org/10.1111/cgf.70082) [[Project]](https://multi.physics-simulation.org/)  
  ![Survey](https://img.shields.io/badge/-Survey-3a86b8.svg?style=flat-square)

<br>

* **Stabilizing Reinforcement Learning in Differentiable Multiphysics Simulation** | ICLR 2025  
  *Eliot Xing, Vernon Luk, Jean Oh*  
  [[Paper]](https://arxiv.org/abs/2412.12089) [[Project]](https://rewarped.github.io/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **A Review of Differentiable Simulators** | IEEE Access 2024  
  *R. Newbury, Jack Collins, Kerry He, Jiahe Pan, et al.*  
  [[DOI]](https://doi.org/10.1109/ACCESS.2024.3425448) [[Project]](https://rhys-newbury.github.io/projects/DiffSim)  
  ![Survey](https://img.shields.io/badge/-Survey-3a86b8.svg?style=flat-square)

<br>

* **SoftMAC: Differentiable Soft Body Simulation with Forecast-based Contact Model and Two-way Coupling with Articulated Rigid Bodies and Clothes** | IROS 2024  
  *Min Liu, Gang Yang, Siyuan Luo, Lin Shao*  
  [[DOI]](https://doi.org/10.1109/IROS58592.2024.10801308) [[Project]](https://minliu01.github.io/SoftMAC/)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **Aquarium: A Fully Differentiable Fluid-Structure Interaction Solver for Robotics Applications** | ICRA 2023  
  *Jeong Hun Lee, Mike Y. Michelis, Robert K. Katzschmann, Zachary Manchester*  
  [[DOI]](https://doi.org/10.1109/icra48891.2023.10161494) [[Code]](https://github.com/RoboticExplorationLab/Aquarium.jl)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Underwater Robot](https://img.shields.io/badge/-Underwater%20Robot-ff7f0e.svg?style=flat-square)

<br>

* **DiffFR: Differentiable SPH-Based Fluid-Rigid Coupling for Rigid Body Control** | TOG 2023  
  *Li, Zhehao, Xu, Qingyu, Ye, Xiaohan, Ren, Bo, et al.*  
  [[Project]](https://zhehaoli1999.github.io/DiffFR/) [[DOI]](https://doi.org/10.1145/3618318)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Shape Design](https://img.shields.io/badge/-Shape%20Design-8ab17d.svg?style=flat-square)

<br>

* **Learning neural constitutive laws from motion observations for generalizable pde dynamics** | ICML 2023  
  *Ma, Pingchuan, Chen, Peter Yichen, Deng, Bolei, Tenenbaum, Joshua B, et al.*  
  [[Project]](https://sites.google.com/view/nclaw)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Neural Material](https://img.shields.io/badge/-Neural%20Material-6d597a.svg?style=flat-square)

<br>

* **MPMNet: A data-driven MPM framework for dynamic fluid-solid interaction** | TVCG 2023  
  *Li, Jin, Gao, Yang, Dai, Ju, Li, Shuai, et al.*  
  [[Paper]](https://ieeexplore.ieee.org/document/10113697)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)

<br>

* **FishGym: A High-Performance Physics-based Simulation Framework for Underwater Robot Learning** | ICRA 2022  
  *Wenji Liu, Kai Bai, Xuming He, Shuran Song, et al.*  
  [[DOI]](https://doi.org/10.1109/ICRA46639.2022.9812066) [[Code]](https://github.com/fish-gym/gym-fish)  
  ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Embodied AI](https://img.shields.io/badge/-Embodied%20AI-1f77b4.svg?style=flat-square) ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square) ![Underwater Robot](https://img.shields.io/badge/-Underwater%20Robot-ff7f0e.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Differentiable Fluids with Solid Coupling for Learning and Control** | AAAI 2021  
  *Takahashi, Tetsuya, Liang, Junbang, Qiao, Yi-Ling, Lin, Ming C.*  
  [[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/16764) [[DOI]](https://doi.org/10.1609/aaai.v35i7.16764)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![Control](https://img.shields.io/badge/-Control-2f6db3.svg?style=flat-square) ![Reinforcement Learning](https://img.shields.io/badge/-Reinforcement%20Learning-8ab17d.svg?style=flat-square)

<br>

* **Differentiable Simulation** | Siggraph Asia 2021  
  *Stelian Coros, Miles Macklin, Bernhard Thomaszewski, Nils Th\"urey*  
  [[DOI]](https://doi.org/10.1145/3476117.3483433)  
  ![Differentiable Simulation](https://img.shields.io/badge/-Differentiable%20Simulation-3a86b8.svg?style=flat-square) ![Contact](https://img.shields.io/badge/-Contact-2a9d8f.svg?style=flat-square)

<br>

* **NVIDIA SimNetTM: An AI-Accelerated Multi-Physics Simulation Framework** | ICCS 2021  
  *Hennigh, Oliver, Narasimhan, Susheela, Nabian, Mohammad Amin, Subramaniam, Akshay, et al.*  
  [[Paper]](https://arxiv.org/abs/2012.07938)  
  ![Engine](https://img.shields.io/badge/-Engine-1f77b4.svg?style=flat-square)

<br>

* **Learning to simulate complex physics with graph networks** | ICML 2020  
  *Sanchez-Gonzalez, Alvaro, Godwin, Jonathan, Pfaff, Tobias, Ying, Rex, et al.*  
  [[Project]](https://sites.google.com/view/learning-to-simulate)  
  ![Neural Solver](https://img.shields.io/badge/-Neural%20Solver-457b9d.svg?style=flat-square) ![GNN](https://img.shields.io/badge/-GNN-6d597a.svg?style=flat-square)
<a id="tag-guide"></a>
## Tag Guide

Reader-facing tags used in the list for quick scanning and search.

| Tag | Count |
| --- | --- |
| Real2Sim | 39 |
| Fluid Reconstruction | 22 |
| GNN | 21 |
| Reinforcement Learning | 18 |
| Cloth Reconstruction | 14 |
| Neural Field | 11 |
| Parameter Estimation | 11 |
| User Interaction | 11 |
| Fluid Control | 10 |
| Material Estimation | 9 |
| NeRF | 9 |
| Super Resolution | 9 |
| CNN | 8 |
| Shape Design | 8 |
| 3DGS | 7 |
| Robot Control | 5 |
| Hair | 4 |
| Style Transfer | 4 |
| GAN | 3 |
| Transformer | 3 |
| Underwater Robot | 3 |
| Neural Material | 2 |
| Soft Robot | 2 |
| Temporal Interpolation | 1 |
## Citation

If you find this repository helpful, please consider citing it!

```
@misc{wang2024awesomelist,
  title = {Awesome Neural Physics - A Curated List of Papers on AI Techniques for Physics Simulation in Computer Graphics},
  author = {Hui Wang},
  journal = {GitHub repository},
  url = {https://github.com/awesome-physics/awesome-neural-physics},
  year = {2026},
}
```
