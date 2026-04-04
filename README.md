# Awesome Neural Physics

A curated list of papers on  the seamless fusion of neural models and physics simulation. It follows the field from injecting neural capabilities into classical solvers to embedding physical simulators directly within neural architectures.

> **Best browsing experience:** use the [interactive index](https://awesome-physics.github.io/awesome-neural-physics/) for search, filtering, category browsing, and tag lookup.

<a id="categories"></a>
## Categories

[Fluid (76)](#fluid) | [Cloth (45)](#cloth) | [Softbody (62)](#softbody) | [Rigidbody (40)](#rigidbody) | [Multiphys (17)](#multiphys)

<a id="keywords"></a>
## Keywords

[Reinforcement Learning (11)](#keyword-guide) | [3DGS (8)](#keyword-guide) | [User Interaction (8)](#keyword-guide) | [NeRF (6)](#keyword-guide) | [Super Resolution (6)](#keyword-guide) | [Neural Material (4)](#keyword-guide) | [Style Transfer (4)](#keyword-guide) | [Real2Sim (3)](#keyword-guide)

<a id="fluid"></a>
<details open>
<summary><strong>Fluid (76)</strong></summary>

- [A Neural Particle Level Set Method for Dynamic Interface Tracking](https://doi.org/10.1145/3730399) *TOG 2025* categories: `Neural Representation` [project](https://cdwj.github.io/projects/neural-pls-project-page/index.html) [doi](https://doi.org/10.1145/3730399)
- [A Pioneering Neural Network Method for Efficient and Robust Fuel Sloshing Simulation in Aircraft](https://doi.org/10.1609/aaai.v39i15.33752) *AAAI 2025* [project](https://github.com/chenyu-xjtu/A-Pioneering-Neural-Network-Method-for-Efficient-and-Robust-Fuel-Sloshing-Simulation-in-Aircraft) [doi](https://doi.org/10.1609/aaai.v39i15.33752)
- [AMR-Transformer: Enabling Efficient Long-range Interaction for Complex Neural Fluid Simulation](https://doi.org/10.1109/cvpr52734.2025.00545) *CVPR 2025* categories: `Neural Solver` [project](https://github.com/JfanLiu/AMR_Transformer) [doi](https://doi.org/10.1109/cvpr52734.2025.00545)
- [An Adjoint Method for Differentiable Fluid Simulation on Flow Maps](https://arxiv.org/abs/2511.01259) *Siggraph Asia 2025* categories: `Differentiable Simulation` [project](https://pearseven.github.io/DiffFMProject/) [doi](https://doi.org/10.1145/3757377.3763903)
- [Learning an Implicit Physical Model for Image-based Fluid Simulation](https://arxiv.org/abs/2508.08254) *ICCV 2025* categories: `Reconstruction` tags: `3DGS` [project](https://physfluid.github.io/) [paper](https://arxiv.org/abs/2508.08254)
- [Neural Kinematic Bases for Fluids](https://arxiv.org/abs/2504.15657) *Siggraph Asia 2025* categories: `Neural Representation` [doi](https://doi.org/10.1145/3757377.3763925)
- [Representing Flow Fields with Divergence-Free Kernels for Reconstruction](https://doi.org/10.1145/3747872) *PACMCGIT 2025* categories: `Neural Representation` `Reconstruction` [project](https://www.physicsbasedanimation.com/2025/08/10/representing-flow-fields-with-divergence-free-kernels-for-reconstruction) [doi](https://doi.org/10.1145/3747872)
- [A Real-Time and Interactive Fluid Modeling System for Mixed Reality](https://doi.org/10.1109/tvcg.2024.3456140) *TVCG 2024* categories: `Reconstruction` tags: `User Interaction` [project](https://github.com/cenyc/Interactive-Fluid-Modeling) [doi](https://doi.org/10.1109/tvcg.2024.3456140)
- [Differentiable Voronoi Diagrams for Simulation of Cell-Based Mechanical Systems](https://github.com/lnumerow-ethz/VoronoiCellSim) *TOG 2024* [paper](https://github.com/lnumerow-ethz/VoronoiCellSim)
- [Dynamic ocean inverse modeling based on differentiable rendering](https://link.springer.com/article/10.1007/s41095-023-0338-4) *CVM 2024* [paper](https://link.springer.com/article/10.1007/s41095-023-0338-4)
- [Fluid Inverse Volumetric Modeling and Applications from Surface Motion](https://www.computer.org/csdl/journal/tg/5555/01/10452823/1UUuVAIPShy) *TVCG 2024* [paper](https://www.computer.org/csdl/journal/tg/5555/01/10452823/1UUuVAIPShy)
- [Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting](https://amysteriouscat.github.io/GaussianSplashing/) *Arxiv 2024* tags: `3DGS` [paper](https://amysteriouscat.github.io/GaussianSplashing/)
- [Laplacian Projection Based Global Physical Prior Smoke Reconstruction](https://www.computer.org/csdl/journal/tg/5555/01/10414126/1TZIJbrBNo4) *TVCG 2024* categories: `Differentiable Simulation` `Reconstruction` [paper](https://www.computer.org/csdl/journal/tg/5555/01/10414126/1TZIJbrBNo4)
- [Learning Reduced Fluid Dynamics](https://ojs.aaai.org/index.php/AAAI/article/view/29367) *AAAI 2024* [paper](https://ojs.aaai.org/index.php/AAAI/article/view/29367)
- [Neural Implicit Reduced Fluid Simulation](https://doi.org/10.1145/3680528.3687628) *Siggraph Asia 2024* categories: `Neural Solver` `Neural Representation` [project](https://yuanyuantao.github.io/Neural-Implicit-Reduced-Fluid-Simulation/) [doi](https://doi.org/10.1145/3680528.3687628)
- [Neural Monte Carlo Fluid Simulation](https://doi.org/10.1145/3641519.3657438) *Siggraph 2024* categories: `Neural Representation` [project](https://github.com/Pranav-Jain/Neural-Monte-Carlo-Fluid-Simulation) [doi](https://doi.org/10.1145/3641519.3657438)
- [NeuralFluid: Neural Fluidic System Design and Control with Differentiable Simulation](https://papers.nips.cc/paper_files/paper/2024/hash/9a379c1b05793d1c42dc832269834515-Abstract-Conference.html) *NeurIPS 2024* categories: `Differentiable Simulation` `Control` [project](https://people.csail.mit.edu/liyifei/publication/neuralfluid/) [paper](https://papers.nips.cc/paper_files/paper/2024/hash/9a379c1b05793d1c42dc832269834515-Abstract-Conference.html)
- [NeuSmoke: Efficient Smoke Reconstruction and View Synthesis with Neural Transportation Fields](https://doi.org/10.1145/3680528.3687667) *Siggraph Asia 2024* categories: `Reconstruction` [project](https://github.com/JiaxiongQ/NeuSmoke) [doi](https://doi.org/10.1145/3680528.3687667)
- [Physics-Informed Learning of Characteristic Trajectories for Smoke Reconstruction](https://doi.org/10.1145/3641519.3657483) *Siggraph 2024* categories: `Reconstruction` tags: `NeRF` [project](https://github.com/19reborn/PICT_smoke) [doi](https://doi.org/10.1145/3641519.3657483)
- [Reconstruction of implicit surfaces from fluid particles using convolutional neural networks](https://doi.org/10.1111/cgf.15181) *CGF 2024* categories: `Reconstruction` [project](https://www.cs.ucr.edu/~craigs/research.html) [doi](https://doi.org/10.1111/cgf.15181)
- [SNN-PDE: Learning Dynamic PDEs from Data with Simplicial Neural Networks](http://dx.doi.org/10.1609/aaai.v38i10.29038) *AAAI 2024* categories: `Neural Solver` [doi](https://doi.org/10.1609/aaai.v38i10.29038)
- [Symmetric Basis Convolutions for Learning Lagrangian Fluid Mechanics](https://github.com/tum-pbs/SFBC) *ICLR 2024* [paper](https://github.com/tum-pbs/SFBC)
- [Aquarium: A Fully Differentiable Fluid-Structure Interaction Solver for Robotics Applications](https://doi.org/10.1109/icra48891.2023.10161494) *ICRA 2023* categories: `Differentiable Simulation` `Embodied AI` [project](https://github.com/RoboticExplorationLab/Aquarium.jl) [doi](https://doi.org/10.1109/icra48891.2023.10161494)
- [Boundary Graph Neural Networks for 3D Simulations](https://doi.org/10.1609/aaai.v37i8.26092) *AAAI 2023* categories: `Neural Solver` [project](https://ml-jku.github.io/bgnn) [doi](https://doi.org/10.1609/aaai.v37i8.26092)
- [DiffFR: Differentiable SPH-Based Fluid-Rigid Coupling for Rigid Body Control](https://zhehaoli1999.github.io/DiffFR/) *TOG 2023* categories: `Differentiable Simulation` `Control` [doi](https://doi.org/10.1145/3618318)
- [Fast fluid simulation via dynamic multi-scale gridding](https://ojs.aaai.org/index.php/AAAI/article/view/25255) *AAAI 2023* [paper](https://ojs.aaai.org/index.php/AAAI/article/view/25255)
- [Fluid Simulation on Neural Flow Maps](https://yitongdeng-projects.github.io/neural_flow_maps_webpage/) *TOG 2023* [paper](https://yitongdeng-projects.github.io/neural_flow_maps_webpage/)
- [FluidLab: A Differentiable Environment for Benchmarking Complex Fluid Manipulation](https://fluidlab2023.github.io/) *ICLR 2023* categories: `Differentiable Simulation` [paper](https://fluidlab2023.github.io/)
- [Inferring Hybrid Neural Fluid Fields from Videos](https://papers.nips.cc/paper_files/paper/2023/hash/00feea0d4eea58fdda7151f7e7f76c72-Abstract-Conference.html) *NeurIPS 2023* categories: `Reconstruction` `Neural Representation` [project](https://kovenyu.com/hyfluid/) [paper](https://papers.nips.cc/paper_files/paper/2023/hash/00feea0d4eea58fdda7151f7e7f76c72-Abstract-Conference.html)
- [Interactive design of 2D car profiles with aerodynamic feedback](https://doi.org/10.1111/cgf.14772) *CGF 2023* categories: `Neural Solver` `Neural Representation` [project](https://hal.science/hal-03975369) [doi](https://doi.org/10.1111/cgf.14772)
- [Learning to Estimate Single-View Volumetric Flow Motions without 3D Supervision](https://ge.in.tum.de/publications/2023-franz-neuralglobtrans/) *ICLR 2023* [paper](https://ge.in.tum.de/publications/2023-franz-neuralglobtrans/)
- [Learning Vortex Dynamics for Fluid Inference and Prediction](https://github.com/yitongdeng-projects/learning_vortex_dynamics_code) *ICLR 2023* [paper](https://github.com/yitongdeng-projects/learning_vortex_dynamics_code)
- [Neural vortex method: From finite Lagrangian particles to infinite dimensional Eulerian dynamics](https://arxiv.org/abs/2006.04178) *Comput. Fluids 2023* [doi](https://doi.org/10.1016/j.compfluid.2023.105811)
- [Physics-Informed Neural Corrector for Deformation-based Fluid Control](https://studios.disneyresearch.com/2023/05/07/physics-informed-neural-corrector-for-deformation-based-fluid-control/) *CGF 2023* categories: `Control` [doi](https://doi.org/10.1111/cgf.14751)
- [Solving Inverse Physics Problems with Score Matching](https://github.com/tum-pbs/SMDP) *NeurIPS 2023* [paper](https://github.com/tum-pbs/SMDP)
- [SurfsUp: Learning Fluid Simulation for Novel Surfaces](https://doi.org/10.1109/ICCV51070.2023.01308) *ICCV 2023* categories: `Neural Solver` [project](https://surfsup.cs.columbia.edu/) [doi](https://doi.org/10.1109/ICCV51070.2023.01308)
- [Deep Reconstruction of 3D Smoke Densities from Artist Sketches](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14461) *CGF 2022* [doi](https://doi.org/10.1111/cgf.14461)
- [Efficient Neural Style Transfer for Volumetric Simulations](https://studios.disneyresearch.com/2022/11/30/efficient-neural-style-transfer-for-volumetric-simulations/) *TOG 2022* tags: `Style Transfer` [doi](https://doi.org/10.1145/3550454.3555517)
- [FishGym: A High-Performance Physics-based Simulation Framework for Underwater Robot Learning](https://doi.org/10.1109/ICRA46639.2022.9812066) *ICRA 2022* categories: `Engine` tags: `Reinforcement Learning` [project](https://github.com/fish-gym/gym-fish) [doi](https://doi.org/10.1109/ICRA46639.2022.9812066)
- [Fluidic Topology Optimization with an Anisotropic Mixture Model](https://doi.org/10.1145/3550454.3555429) *TOG 2022* categories: `Differentiable Simulation` [project](https://people.csail.mit.edu/liyifei/publication/anisotropicstokes) [doi](https://doi.org/10.1145/3550454.3555429)
- [Guaranteed conservation of momentum for learning particle-based fluid dynamics](https://github.com/tum-pbs/DMCF) *NeurIPS 2022* [paper](https://github.com/tum-pbs/DMCF)
- [Half-Inverse Gradients for Physical Deep Learning](https://arxiv.org/abs/2203.10131) *ICLR 2022* [paper](https://arxiv.org/abs/2203.10131)
- [Neurofluid: Fluid dynamics grounding with particle-driven neural radiance fields](https://syguan96.github.io/NeuroFluid/) *ICML 2022* [paper](https://syguan96.github.io/NeuroFluid/)
- [Physics informed neural fields for smoke reconstruction with sparse data](https://rachelcmy.github.io/pinf_smoke/) *TOG 2022* categories: `Reconstruction` tags: `NeRF` [doi](https://doi.org/10.1145/3528223.3530169)
- [Transformer with implicit edges for particle-based physics simulation](https://www.mmlab-ntu.com/project/tie/index.html) *ECCV 2022* [paper](https://www.mmlab-ntu.com/project/tie/index.html)
- [Versatile Control of Fluid-directed Solid Objects Using Multi-task Reinforcement Learning](https://dl.acm.org/doi/10.1145/3554731) *TOG 2022* categories: `Control` tags: `Reinforcement Learning` [doi](https://doi.org/10.1145/3554731)
- [Data-driven simulation in fluids animation: A survey](https://www.sciencedirect.com/science/article/pii/S2096579621000139) *VRIH 2021* categories: `Survey` [paper](https://www.sciencedirect.com/science/article/pii/S2096579621000139)
- [Differentiable Fluids with Solid Coupling for Learning and Control](https://ojs.aaai.org/index.php/AAAI/article/view/16764) *AAAI 2021* categories: `Differentiable Simulation` `Control` [doi](https://doi.org/10.1609/aaai.v35i7.16764)
- [Global transport for fluid reconstruction with learned self-supervision](https://ge.in.tum.de/publications/) *CVPR 2021* [paper](https://ge.in.tum.de/publications/)
- [Learning meaningful controls for fluids](https://rachelcmy.github.io/den2vel/) *TOG 2021* categories: `Control` [paper](https://rachelcmy.github.io/den2vel/)
- [Model-Predictive Control of Blood Suction for Surgical Hemostasis using Differentiable Fluid Simulations](https://doi.org/10.1109/icra48506.2021.9561624) *ICRA 2021* categories: `Control` `Embodied AI` [project](https://ucsdarclab.com/autopublication/model-predictive-control-of-blood-suction-for-surgical-hemostasis-using-differentiable-fluid-simulations) [doi](https://doi.org/10.1109/icra48506.2021.9561624)
- [Neural upflow: A scene flow learning approach to increase the apparent resolution of particle-based liquids](https://dl.acm.org/doi/abs/10.1145/3480147) *PACMCGIT 2021* [paper](https://dl.acm.org/doi/abs/10.1145/3480147)
- [Predicting high-resolution turbulence details in space and time](https://dl.acm.org/doi/abs/10.1145/3478513.3480492) *TOG 2021* tags: `Super Resolution` [paper](https://dl.acm.org/doi/abs/10.1145/3478513.3480492)
- [Two-step Temporal Interpolation Network Using Forward Advection for Efficient Smoke Simulation](https://onlinelibrary.wiley.com/doi/10.1111/cgf.142638) *CGF 2021* [paper](https://onlinelibrary.wiley.com/doi/10.1111/cgf.142638)
- [Volumetric appearance stylization with stylizing kernel prediction network](https://dl.acm.org/doi/abs/10.1145/3450626.3459799) *TOG 2021* tags: `Style Transfer` [doi](https://doi.org/10.1145/3450626.3459799)
- [A Novel CNN-Based Poisson Solver for Fluid Simulation](http://dalab.se.sjtu.edu.cn/www/home/?page_id=790) *TVCG 2020* [doi](https://doi.org/10.1109/TVCG.2018.2873375)
- [Dynamic fluid surface reconstruction using deep neural network](https://ivlab.cse.lsu.edu/FSRN_CVPR20.html) *CVPR 2020* categories: `Reconstruction` [paper](https://ivlab.cse.lsu.edu/FSRN_CVPR20.html)
- [Dynamic Upsampling of Smoke through Dictionary-based Learning](https://faculty.sist.shanghaitech.edu.cn/faculty/liuxp/projects/ss_dbnn/index.htm) *TOG 2020* tags: `Super Resolution` [doi](https://doi.org/10.1145/3412360)
- [Interactive liquid splash modeling by user sketches](https://dl.acm.org/doi/abs/10.1145/3414685.3417832) *TOG 2020* tags: `User Interaction` [paper](https://dl.acm.org/doi/abs/10.1145/3414685.3417832)
- [Lagrangian neural style transfer for fluids](https://github.com/byungsook/neural-flow-style) *TOG 2020* tags: `Style Transfer` [doi](https://doi.org/10.1145/3386569.3392473)
- [Latent space subdivision: stable and controllable time predictions for fluid flow](https://ge.in.tum.de/publications/2020-lssubdiv-wiewel/) *CGF 2020* [paper](https://ge.in.tum.de/publications/2020-lssubdiv-wiewel/)
- [Learning to Control PDEs with Differentiable Physics](http://arxiv.org/abs/2001.07457) *ICLR 2020* categories: `Differentiable Simulation` tags: `User Interaction` [project](https://github.com/p-holl/PDE-Control) [doi](https://doi.org/10.48550/arxiv.2001.07457)
- [Machine learning for fluid mechanics](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-010719-060214) *ARFM 2020* categories: `Survey` [paper](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-010719-060214)
- [Tomofluid: Reconstructing dynamic fluid from sparse view videos](https://openaccess.thecvf.com/content_CVPR_2020/html/Zang_TomoFluid_Reconstructing_Dynamic_Fluid_From_Sparse_View_Videos_CVPR_2020_paper.html) *CVPR 2020* categories: `Reconstruction` [paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Zang_TomoFluid_Reconstructing_Dynamic_Fluid_From_Sparse_View_Videos_CVPR_2020_paper.html)
- [A CNN-based Flow Correction Method for Fast Preview](http://dalab.se.sjtu.edu.cn/www/home/?page_id=763) *CGF 2019* tags: `Super Resolution` [paper](http://dalab.se.sjtu.edu.cn/www/home/?page_id=763)
- [Lagrangian fluid simulation with continuous convolutions](https://ge.in.tum.de/publications/2020-ummenhofer-iclr/) *ICLR 2019* [paper](https://ge.in.tum.de/publications/2020-ummenhofer-iclr/)
- [ScalarFlow: a large-scale volumetric data set of real-world scalar transport flows for computer animation and machine learning](https://ge.in.tum.de/publications/2019-scalarflow-eckert/) *TOG 2019* [doi](https://doi.org/10.1145/3355089.3356545)
- [Transport-based neural style transfer for smoke simulations](https://dl.acm.org/doi/10.1145/3355089.3356560) *TOG 2019* tags: `Style Transfer` [doi](https://doi.org/10.1145/3355089.3356560)
- [Video-guided real-to-virtual parameter transfer for viscous fluids](https://gamma.cs.unc.edu/ParameterTransfer/) *TOG 2019* [doi](https://doi.org/10.1145/3355089.3356551)
- [Deep dynamical modeling and control of unsteady fluid flows](https://github.com/sisl/deep_flow_control) *NeurIPS 2018* categories: `Control` [paper](https://github.com/sisl/deep_flow_control)
- [Fluid directed rigid body control using deep reinforcement learning](https://gamma.cs.unc.edu/DRL_FluidRigid/) *TOG 2018* categories: `Control` tags: `Reinforcement Learning` [doi](https://doi.org/10.1145/3197517.3201334)
- [tempoGAN: A temporally coherent, volumetric GAN for super-resolution fluid flow](https://ge.in.tum.de/publications/tempogan/) *TOG 2018* tags: `Super Resolution` [paper](https://ge.in.tum.de/publications/tempogan/)
- [Accelerating eulerian fluid simulation with convolutional networks](https://github.com/google/FluidNet) *ICML 2017* [paper](https://github.com/google/FluidNet)
- [Data-driven synthesis of smoke flows with CNN-based feature descriptors](https://ge.in.tum.de/publications/2017-sig-chu/) *TOG 2017* [doi](https://doi.org/10.1145/3072959.3073643)
- [Data-driven projection method in fluid simulation](http://dalab.se.sjtu.edu.cn/www/home/?page_id=911) *CAVW 2016* [doi](https://doi.org/10.1002/cav.1695)
- [Data-driven fluid simulations using regression forests](https://dl.acm.org/doi/10.1145/2816795.2818129) *TOG 2015* [doi](https://doi.org/10.1145/2816795.2818129)

</details>
<a id="cloth"></a>
<details>
<summary><strong>Cloth (45)</strong></summary>

- [Dress Anyone : Automatic Physically-Based Garment Pattern Refitting 56](https://doi.org/10.1145/3747858) *PACMCGIT 2025* categories: `Differentiable Simulation` [project](https://igl.ethz.ch/projects/dress_anyone) [doi](https://doi.org/10.1145/3747858)
- [Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics](https://doi.org/10.1145/3731177) *TOG 2025* categories: `Differentiable Simulation` `Reconstruction` [project](https://dress-1-to-3.github.io/) [doi](https://doi.org/10.1145/3731177)
- [Frequency-Divided Learning of Fine-Grained Clothing Behavior via Flexible Dynamic Graphs](https://doi.org/10.1109/tvcg.2025.3591816) *TVCG 2025* categories: `Neural Solver` `Avatar` [project](https://shirui-homepage.com/publication/2025-freq-div-TVCG) [doi](https://doi.org/10.1109/tvcg.2025.3591816)
- [PICA: Physics-Integrated Clothed Avatar](https://doi.org/10.1109/tvcg.2025.3560241) *TVCG 2025* categories: `Avatar` tags: `3DGS` [project](https://ustc3dv.github.io/PICA) [doi](https://doi.org/10.1109/tvcg.2025.3614642)
- [Self-Supervised Humidity-Controllable Garment Simulation via Capillary Bridge Modeling](https://doi.org/10.1111/cgf.70236) *CGF 2025* [doi](https://doi.org/10.1111/cgf.70236)
- [Bayesian Differentiable Physics for Cloth Digitalization](https://github.com/realcrane/Bayesian-Differentiable-Physics-for-Cloth-Digitalization) *CVPR 2024* categories: `Differentiable Simulation` [paper](https://github.com/realcrane/Bayesian-Differentiable-Physics-for-Cloth-Digitalization)
- [ContourCraft: Learning to Resolve Intersections in Neural Multi-Garment Simulations](https://doi.org/10.1145/3641519.3657408) *Siggraph 2024* categories: `Neural Solver` [doi](https://doi.org/10.1145/3641519.3657408)
- [DiffAvatar: Simulation-Ready Garment Optimization with Differentiable Simulation](https://people.csail.mit.edu/liyifei/publication/diffavatar/) *CVPR 2024* categories: `Differentiable Simulation` `Avatar` [paper](https://people.csail.mit.edu/liyifei/publication/diffavatar/)
- [Efficient Deformation Learning of Varied Garments with a Structure-Preserving Multilevel Framework](https://doi.org/10.1145/3651286) *PACMCGIT 2024* categories: `Neural Solver` [project](https://li-tianxing.github.io/publication/psdunet) [doi](https://doi.org/10.1145/3651286)
- [Estimating Cloth Simulation Parameters From Tag Information and Cusick Drape Test](https://doi.org/10.1111/cgf.15027) *CGF 2024* [project](https://mingry.github.io/Fabrics5k) [doi](https://doi.org/10.1111/cgf.15027)
- [Garment Animation NeRF with Color Editing](https://doi.org/10.1111/cgf.15178) *CGF 2024* categories: `Avatar` tags: `NeRF` [project](https://mengzephyr.com/Garment-Animation-NeRF-With-Color-Editing) [doi](https://doi.org/10.1111/cgf.15178)
- [GarmentDreamer: 3DGS Guided Garment Synthesis with Diverse Geometry and Texture Details](https://arxiv.org/abs/2405.12420) *Arxiv 2024* tags: `3DGS` [paper](https://arxiv.org/abs/2405.12420)
- [Neural Garment Dynamic Super-Resolution](https://doi.org/10.1145/3680528.3687610) *Siggraph Asia 2024* tags: `Super Resolution` [project](https://mengzephyr.com/Neural-Garment-Dynamic-Super-Reslution) [doi](https://doi.org/10.1145/3680528.3687610)
- [Neural Garment Dynamics via Manifold-Aware Transformers](https://doi.org/10.1111/cgf.15028) *CGF 2024* categories: `Neural Solver` `Avatar` [project](https://github.com/PeizhuoLi/manifold-aware-transformers) [doi](https://doi.org/10.1111/cgf.15028)
- [NeuralClothSim: Neural Deformation Fields Meet the Thin Shell Theory](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c7649eeb93d2fad0ced9a3b974260710-Abstract-Conference.html) *NeurIPS 2024* categories: `Neural Solver` `Neural Representation` [project](https://4dqv.mpi-inf.mpg.de/NeuralClothSim/) [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c7649eeb93d2fad0ced9a3b974260710-Abstract-Conference.html)
- [Parametric Linear Blend Skinning Model for Multiple-Shape 3D Garments](https://doi.org/10.1109/tvcg.2024.3478852) *TVCG 2024* categories: `Avatar` [project](https://www.sysu-hcp.net/projects/cv/126.html) [doi](https://doi.org/10.1109/tvcg.2024.3478852)
- [Physics-guided Shape-from-Template: Monocular Video Perception through Neural Surrogate Models](https://doi.org/10.1109/cvpr52733.2024.01130) *CVPR 2024* categories: `Neural Solver` `Reconstruction` [project](https://github.com/vc-bonn/Physics-guided-Shape-from-Template) [doi](https://doi.org/10.1109/cvpr52733.2024.01130)
- [Real-Time Neural Cloth Deformation Using a Compact Latent Space and a Latent Vector Predictor](https://doi.org/10.1007/978-3-031-92387-6_25) *ECCV 2024* categories: `Neural Solver` [doi](https://doi.org/10.1007/978-3-031-92387-6_25)
- [ClothCombo: Modeling Inter-Cloth Interaction for Draping Multi-Layered Clothes](https://dl.acm.org/doi/10.1145/3618376) *TOG 2023* [paper](https://dl.acm.org/doi/10.1145/3618376)
- [D-Cloth: Skinning-based Cloth Dynamic Prediction with a Three-stage Network](https://min-tang.github.io/home/DCloth/) *CGF 2023* categories: `Neural Solver` [paper](https://min-tang.github.io/home/DCloth/)
- [Detail-Aware Deep Clothing Animations Infused with Multi-Source Attributes](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14651) *CGF 2023* categories: `Avatar` [paper](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14651)
- [DiffXPBD: Differentiable Position-Based Simulation of Compliant Constraint Dynamics](https://doi.org/10.1145/3606923) *PACMCGIT 2023* categories: `Differentiable Simulation` [doi](https://doi.org/10.1145/3606923)
- [Elastic Context: Encoding Elasticity for Data-driven Models of Textiles Elastic Context: Encoding Elasticity for Data-driven Models of Textiles](https://doi.org/10.1109/icra48891.2023.10160740) *ICRA 2023* categories: `Embodied AI` tags: `Neural Material` [doi](https://doi.org/10.1109/icra48891.2023.10160740)
- [HOOD: Hierarchical Graphs for Generalized Modelling of Clothing Dynamics](https://doi.org/10.1109/cvpr52729.2023.01627) *CVPR 2023* categories: `Neural Solver` [project](https://dolorousrtur.github.io/hood/?trk=public_post_comment-text) [doi](https://doi.org/10.1109/cvpr52729.2023.01627)
- [How Will It Drape Like? Capturing Fabric Mechanics from Depth Images](http://dx.doi.org/10.1111/cgf.14750) *CGF 2023* [project](https://carlosrodriguezpardo.es/projects/MechFromDepth) [doi](https://doi.org/10.1111/cgf.14750)
- [Learning Anchor Transformations for 3D Garment Animation](https://doi.org/10.1109/cvpr52729.2023.00055) *CVPR 2023* categories: `Avatar` [project](https://semanticdh.github.io/AnchorDEF) [doi](https://doi.org/10.1109/cvpr52729.2023.00055)
- [SwinGar: Spectrum-Inspired Neural Dynamic Deformation for Free-Swinging Garments](https://doi.org/10.1109/tvcg.2023.3346055) *TVCG 2023* [doi](https://doi.org/10.1109/tvcg.2023.3346055)
- [Towards Multi-Layered 3D Garments Animation](https://doi.org/10.1109/iccv51070.2023.01321) *ICCV 2023* [project](https://mmlab-ntu.github.io/project/layersnet) [doi](https://doi.org/10.1109/iccv51070.2023.01321)
- [DiffCloth: Differentiable Cloth Simulation with Dry Frictional Contact](https://people.csail.mit.edu/liyifei/publication/diffcloth/) *TOG 2022* categories: `Differentiable Simulation` [doi](https://doi.org/10.1145/3527660)
- [Dressing avatars: Deep photorealistic appearance for physically simulated clothing](https://research.facebook.com/publications/dressing-avatars-deep-photorealistic-appearance-for-physically-simulated-clothing/) *TOG 2022* categories: `Avatar` [paper](https://research.facebook.com/publications/dressing-avatars-deep-photorealistic-appearance-for-physically-simulated-clothing/)
- [Learning Latent Graph Dynamics for Visual Manipulation of Deformable Objects](https://doi.org/10.1109/icra46639.2022.9811597) *ICRA 2022* categories: `Neural Representation` `Embodied AI` [doi](https://doi.org/10.1109/icra46639.2022.9811597)
- [Learning-based bending stiffness parameter estimation by a drape tester](https://github.com/DrapeTester/ClothDrapeTester) *TOG 2022* [paper](https://github.com/DrapeTester/ClothDrapeTester)
- [Neural cloth simulation](https://hbertiche.github.io/NeuralClothSim/) *TOG 2022* [paper](https://hbertiche.github.io/NeuralClothSim/)
- [Pattern-based cloth registration and sparse-view animation](https://dl.acm.org/doi/abs/10.1145/3550454.3555448) *TOG 2022* [paper](https://dl.acm.org/doi/abs/10.1145/3550454.3555448)
- [Predicting loose-fitting garment deformations using bone-driven motion networks](http://www.cad.zju.edu.cn/home/jin/SigCloth2022/SigCloth2022.htm) *Siggraph 2022* categories: `Neural Solver` `Avatar` [paper](http://www.cad.zju.edu.cn/home/jin/SigCloth2022/SigCloth2022.htm)
- [Snug: Self-supervised neural dynamic garments](http://mslab.es/projects/SNUG/) *CVPR 2022* categories: `Neural Solver` `Avatar` [paper](http://mslab.es/projects/SNUG/)
- [Dynamic neural garments](https://geometry.cs.ucl.ac.uk/projects/2021/DynamicNeuralGarments/) *TOG 2021* categories: `Neural Solver` `Avatar` [doi](https://doi.org/10.1145/3478513.3480497)
- [Neural Implicit Surfaces for Efficient and Accurate Collisions in Physically Based Simulations](https://arxiv.org/abs/2110.01614) *Arxiv 2021* categories: `Neural Representation` [project](https://hbertiche.github.io/NeuralColliders/) [paper](https://arxiv.org/abs/2110.01614)
- [PBNS: physically based neural simulation for unsupervised garment pose space deformation](https://hbertiche.github.io/PBNS/) *TOG 2021* categories: `Neural Solver` `Avatar` [doi](https://doi.org/10.1145/3478513.3480479)
- [Self-supervised collision handling via generative 3d garment models for virtual try-on](http://mslab.es/projects/SelfSupervisedGarmentCollisions/) *CVPR 2021* [paper](http://mslab.es/projects/SelfSupervisedGarmentCollisions/)
- [Cloth in the wind: A case study of physical measurement through simulation](https://arxiv.org/abs/2003.05065) *CVPR 2020* [paper](https://arxiv.org/abs/2003.05065)
- [Learning to measure the static friction coefficient in cloth contact](https://openaccess.thecvf.com/content_CVPR_2020/html/Rasheed_Learning_to_Measure_the_Static_Friction_Coefficient_in_Cloth_Contact_CVPR_2020_paper.html) *CVPR 2020* [paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Rasheed_Learning_to_Measure_the_Static_Friction_Coefficient_in_Cloth_Contact_CVPR_2020_paper.html)
- [Projective dynamics with dry frictional contact](https://astcort.github.io/) *TOG 2020* [doi](https://doi.org/10.1145/3386569.3392396)
- [Differentiable Cloth Simulation for Inverse Problems](https://gamma.umd.edu/researchdirections/virtualtryon/differentiablecloth) *NeurIPS 2019* categories: `Differentiable Simulation` [paper](https://gamma.umd.edu/researchdirections/virtualtryon/differentiablecloth)
- [Learning an intrinsic garment space for interactive authoring of garment animation](https://geometry.cs.ucl.ac.uk/projects/2019/garment_authoring/) *TOG 2019* categories: `Avatar` tags: `User Interaction` [doi](https://doi.org/10.1145/3355089.3356512)

</details>
<a id="softbody"></a>
<details>
<summary><strong>Softbody (62)</strong></summary>

- [Neuralocks: Real-Time Dynamic Neural Hair Simulation](https://doi.org/10.1111/cgf.70407) *CGF 2026* categories: `Neural Solver` `Avatar` [doi](https://doi.org/10.1111/cgf.70407)
- [A Differentiable Material Point Method Framework for Shape Morphing](https://doi.org/10.1109/tvcg.2025.3591729) *TVCG 2025* categories: `Differentiable Simulation` [project](https://chayo.oopy.io/1e7e3760-68e9-808e-b30a-f89ba08d6193) [doi](https://doi.org/10.1109/tvcg.2025.3591729)
- [DeepFracture: A Generative Approach for Predicting Brittle Fractures with Neural Discrete Representation Learning](https://nikoloside.graphics/deepfracture/) *CGF 2025* categories: `Neural Representation` `Fracture` [doi](https://doi.org/10.1111/cgf.70002)
- [Differentiable Simulation of Soft Robots with Frictional Contacts](https://doi.org/10.1109/ROBOSOFT63089.2025.11020844) *IEEE 8th International Conference on Soft Robotics (RoboSoft) 2025* categories: `Differentiable Simulation` `Embodied AI` [project](https://simple-robotics.github.io/publications/differentiable-soft-robotics/) [doi](https://doi.org/10.1109/ROBOSOFT63089.2025.11020844)
- [Elastic Locomotion with Mixed Second-order Differentiation](https://doi.org/10.1145/3721238.3730685) *Siggraph 2025* categories: `Differentiable Simulation` [doi](https://doi.org/10.1145/3721238.3730685)
- [Inverse Design of Discrete Interlocking Materials with Desired Mechanical Behavior](https://doi.org/10.1145/3721238.3730675) *Siggraph 2025* categories: `Differentiable Simulation` [project](https://tangpengbin.github.io/publications/InverseDIM/index.html) [doi](https://doi.org/10.1145/3721238.3730675)
- [Neural Modular Physics for Elastic Simulation](https://arxiv.org/abs/2512.15083) *Arxiv 2025* categories: `Neural Solver` [project](https://people.csail.mit.edu/liyifei/publication/nmp) [paper](https://arxiv.org/abs/2512.15083)
- [Neurally Integrated Finite Elements for Differentiable Elasticity on Evolving Domains](https://doi.org/10.1145/3727874) *TOG 2025* categories: `Differentiable Simulation` `Neural Representation` [project](https://research.nvidia.com/labs/toronto-ai/flexisim/) [doi](https://doi.org/10.1145/3727874)
- [PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](https://jianghanxiao.github.io/phystwin-web/) *ICCV 2025* tags: `Real2Sim` `3DGS` [paper](https://jianghanxiao.github.io/phystwin-web/)
- [Precise Gradient Discontinuities in Neural Fields for Subspace Physics](https://doi.org/10.1145/3757377.3763810) *Siggraph Asia 2025* categories: `Neural Representation` [project](https://www.dgp.toronto.edu/projects/discont_grad) [doi](https://doi.org/10.1145/3757377.3763810)
- [Quaffure: Real-Time Quasi-Static Neural Hair Simulation](https://doi.org/10.1109/cvpr52734.2025.00031) *CVPR 2025* categories: `Neural Solver` `Avatar` [project](https://tuurstuyck.github.io/quaffure/quaffure.html) [doi](https://doi.org/10.1109/cvpr52734.2025.00031)
- [Self-supervised Learning of Latent Space Dynamics](https://doi.org/10.1145/3747854) *PACMCGIT 2025* categories: `Neural Representation` [doi](https://doi.org/10.1145/3747854)
- [Shape Space Spectra](https://doi.org/10.1145/3731148) *TOG 2025* categories: `Neural Representation` [project](https://www.dgp.toronto.edu/projects/sss) [doi](https://doi.org/10.1145/3731148)
- [UniPhy: Learning a Unified Constitutive Model for Inverse Physics Simulation](https://doi.org/10.1109/cvpr52734.2025.01511) *CVPR 2025* categories: `Differentiable Simulation` tags: `Neural Material` [project](https://himangim.github.io/UniPhy) [doi](https://doi.org/10.1109/cvpr52734.2025.01511)
- [Differentiable solver for time-dependent deformation problems with contact](https://dl.acm.org/doi/10.1145/3657648) *TOG 2024* categories: `Differentiable Simulation` [paper](https://dl.acm.org/doi/10.1145/3657648)
- [DiffSound: Differentiable Modal Sound Rendering and Inverse Rendering for Diverse Inference Tasks](https://doi.org/10.1145/3641519.3657493) *Siggraph 2024* categories: `Differentiable Simulation` `Reconstruction` [project](https://hellojxt.github.io/DiffSound/) [doi](https://doi.org/10.1145/3641519.3657493)
- [ElastoGen: 4D Generative Elastodynamics](https://arxiv.org/abs/2405.15056) *Arxiv 2024* [paper](https://arxiv.org/abs/2405.15056)
- [Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing](https://feature-splatting.github.io/) *Arxiv 2024* tags: `User Interaction` `3DGS` [paper](https://feature-splatting.github.io/)
- [Near-realtime Facial Animation by Deep 3D Simulation Super-Resolution](https://doi.org/10.1145/3670687) *TOG 2024* categories: `Avatar` tags: `Super Resolution` [project](https://github.com/hjoonpark/3d-sim-super-res) [doi](https://doi.org/10.1145/3670687)
- [Neural Modes: Self-supervised Learning of Nonlinear Modal Subspaces](https://doi.org/10.1109/cvpr52733.2024.02185) *CVPR 2024* categories: `Neural Representation` [project](https://github.com/jiahong-w/neural-modes) [doi](https://doi.org/10.1109/cvpr52733.2024.02185)
- [PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation](https://physdreamer.github.io/) *Arxiv 2024* [paper](https://physdreamer.github.io/)
- [Pie-nerf: Physics-based interactive elastodynamics with nerf](https://fytalon.github.io/pienerf/) *CVPR 2024* tags: `User Interaction` `NeRF` [paper](https://fytalon.github.io/pienerf/)
- [Real-time Wing Deformation Simulations for Flying Insects](https://doi.org/10.1145/3641519.3657434) *Siggraph 2024* [project](https://graphics.cs.uh.edu/article/2024/2640/2024-siggraph-insectwingdeformation/) [doi](https://doi.org/10.1145/3641519.3657434)
- [Soft Pneumatic Actuator Design using Differentiable Simulation](https://doi.org/10.1145/3641519.3657467) *Siggraph 2024* categories: `Differentiable Simulation` `Embodied AI` [project](https://la.disneyresearch.com/publication/soft-pneumatic-actuator-design-using-differentiable-simulation) [doi](https://doi.org/10.1145/3641519.3657467)
- [VR-GS: A Physical Dynamics-Aware Interactive Gaussian Splatting System in Virtual Reality](https://yingjiang96.github.io/VR-GS/) *Arxiv 2024* tags: `User Interaction` `3DGS` [paper](https://yingjiang96.github.io/VR-GS/)
- [Beyond Chainmail: Computational Modeling of Discrete Interlocking Materials](https://doi.org/10.1145/3592112) *TOG 2023* [doi](https://doi.org/10.1145/3592112)
- [Data-Free Learning of Reduced-Order Kinematics](https://nmwsharp.com/research/neural-physics-subspaces/) *Siggraph 2023* [paper](https://nmwsharp.com/research/neural-physics-subspaces/)
- [DiffVL: Scaling Up Soft Body Manipulation using Vision-Language Driven Differentiable Physics](https://arxiv.org/abs/2312.06408) *NeurIPS 2023* categories: `Differentiable Simulation` [paper](https://arxiv.org/abs/2312.06408)
- [Learning Contact Deformations with General Collider Descriptors](https://dancasas.github.io/) *Siggraph Asia 2023* [paper](https://dancasas.github.io/)
- [LiCROM: Linear-Subspace Continuous Reduced Order Modeling with Neural Fields](https://arxiv.org/abs/2310.15907) *Siggraph Asia 2023* [doi](https://doi.org/10.1145/3610548.3618158)
- [Neural Metamaterial Networks for Nonlinear Material Design](https://github.com/liyuesolo/NeuralMetamaterialNetwork) *TOG 2023* tags: `Neural Material` [doi](https://doi.org/10.1145/3618325)
- [Neural Stress Fields for Reduced-order Elastoplasticity and Fracture](https://zeshunzong.github.io/reduced-order-mpm/) *Siggraph Asia 2023* categories: `Neural Representation` `Fracture` [paper](https://zeshunzong.github.io/reduced-order-mpm/)
- [Neuwigs: A neural dynamic model for volumetric hair capture and animation](https://ziyanw1.github.io/neuwigs/) *CVPR 2023* categories: `Neural Solver` `Avatar` [paper](https://ziyanw1.github.io/neuwigs/)
- [RoboNinja: Learning an Adaptive Cutting Policy for Multi-Material Objects](https://doi.org/10.15607/rss.2023.xix.046) *RSS 2023* categories: `Control` `Embodied AI` [doi](https://doi.org/10.15607/rss.2023.xix.046)
- [ACID: Action-Conditional Implicit Visual Dynamics for Deformable Object Manipulation](https://doi.org/10.15607/rss.2022.xviii.001) *RSS 2022* categories: `Neural Representation` `Embodied AI` [doi](https://doi.org/10.15607/rss.2022.xviii.001)
- [Contact-centric deformation learning](http://mslab.es/projects/ContactCentricLearning/) *TOG 2022* [paper](http://mslab.es/projects/ContactCentricLearning/)
- [Differentiable Depth for Real2Sim Calibration of Soft Body Simulations](https://doi.org/10.1111/cgf.14720) *CGF 2022* categories: `Differentiable Simulation` tags: `Real2Sim` [project](https://researchprofiles.ku.dk/en/publications/differentiable-depth-for-real2sim-calibration-of-soft-body-simula) [doi](https://doi.org/10.1111/cgf.14720)
- [Differentiable simulation of inertial musculotendons](https://dl.acm.org/doi/abs/10.1145/3550454.3555490) *TOG 2022* categories: `Differentiable Simulation` [paper](https://dl.acm.org/doi/abs/10.1145/3550454.3555490)
- [DiffSkill: Skill Abstraction from Differentiable Physics for Deformable Object Manipulations with Tools](https://arxiv.org/abs/2203.17275) *ICLR 2022* categories: `Differentiable Simulation` `Embodied AI` [project](https://xingyu-lin.github.io/diffskill/) [doi](https://doi.org/10.48550/arXiv.2203.17275)
- [Implicit neural representation for physics-driven actuated soft bodies](https://people.inf.ethz.ch/zossg/publication/yang-2022/) *TOG 2022* categories: `Differentiable Simulation` [paper](https://people.inf.ethz.ch/zossg/publication/yang-2022/)
- [Learning to Synthesize Volumetric Meshes from Vision-based Tactile Imprints](https://doi.org/10.1109/icra46639.2022.9812092) *ICRA 2022* categories: `Reconstruction` `Embodied AI` [doi](https://doi.org/10.1109/icra46639.2022.9812092)
- [Neuphysics: Editable neural geometry and physics from monocular videos](https://sites.google.com/view/neuphysics/home) *NeurIPS 2022* categories: `Differentiable Simulation` [paper](https://sites.google.com/view/neuphysics/home)
- [RoboCraft: Learning to See, Simulate, and Shape Elasto-Plastic Objects with Graph Networks](https://doi.org/10.15607/rss.2022.xviii.008) *RSS 2022* categories: `Neural Solver` `Embodied AI` [doi](https://doi.org/10.15607/rss.2022.xviii.008)
- [Soft Robots Learn to Crawl: Jointly Optimizing Design and Control with Sim-to-Real Transfer](https://doi.org/10.15607/rss.2022.xviii.062) *RSS 2022* categories: `Control` [doi](https://doi.org/10.15607/rss.2022.xviii.062)
- [Tracking Fast Trajectories with a Deformable Object using a Learned Model](https://doi.org/10.1109/icra46639.2022.9812189) *ICRA 2022* categories: `Neural Solver` `Embodied AI` [project](https://uscresl.org/publication/tracking-fast-trajectories-with-a-deformable-object-using-a-learned-model) [doi](https://doi.org/10.1109/icra46639.2022.9812189)
- [Virtual Elastic Objects](https://doi.org/10.1109/cvpr52688.2022.01537) *CVPR 2022* categories: `Differentiable Simulation` [project](https://hsiaoyu.github.io/VEO) [doi](https://doi.org/10.1109/cvpr52688.2022.01537)
- [A Deep Emulator for Secondary Motion of 3D Characters](https://doi.org/10.1109/cvpr46437.2021.00587) *CVPR 2021* categories: `Neural Solver` `Avatar` [project](https://github.com/ZhengMianlun/deep_emulator) [doi](https://doi.org/10.1109/cvpr46437.2021.00587)
- [Accurately Solving Rod Dynamics with Graph Learning](http://hdl.handle.net/10754/679142) *NeurIPS 2021* categories: `Neural Solver` [project](https://computationalsciences.org/publications/shao-2021-physical-systems-graph-learning.html) [paper](http://hdl.handle.net/10754/679142)
- [DiffAqua](https://doi.org/10.1145/3450626.3459832) *TOG 2021* categories: `Differentiable Simulation` [project](https://diffaqua.csail.mit.edu/) [doi](https://doi.org/10.1145/3450626.3459832)
- [Differentiable simulation of soft multi-body systems](https://github.com/YilingQiao/diff_fem) *NeurIPS 2021* categories: `Differentiable Simulation` [paper](https://github.com/YilingQiao/diff_fem)
- [Diffpd: Differentiable projective dynamics](https://people.iiis.tsinghua.edu.cn/~taodu/) *TOG 2021* categories: `Differentiable Simulation` [paper](https://people.iiis.tsinghua.edu.cn/~taodu/)
- [DiSECt: A Differentiable Simulation Engine for Autonomous Robotic Cutting](https://doi.org/10.15607/rss.2021.xvii.067) *RSS 2021* categories: `Differentiable Simulation` `Embodied AI` [project](https://eric-heiden.com/publication/2021-disect-rss) [doi](https://doi.org/10.15607/rss.2021.xvii.067)
- [Efficient deformable shape correspondence via multiscale spectral manifold wavelets preservation](https://ieeexplore.ieee.org/document/9578652) *CVPR 2021* [paper](https://ieeexplore.ieee.org/document/9578652)
- [High-order differentiable autoencoder for nonlinear model reduction](https://dl.acm.org/doi/10.1145/3450626.3459754) *TOG 2021* [doi](https://doi.org/10.1145/3450626.3459754)
- [Learning active quasistatic physics-based models from data](https://pages.cs.wisc.edu/~qisiw/SIG.html) *TOG 2021* categories: `Differentiable Simulation` [paper](https://pages.cs.wisc.edu/~qisiw/SIG.html)
- [Learning contact corrections for handle-based subspace dynamics](http://mslab.es/projects/LearningContactCorrections/) *TOG 2021* [paper](http://mslab.es/projects/LearningContactCorrections/)
- [Learning to manipulate amorphous materials](https://tml.stanford.edu/publications/2020/learning-manipulate-amorphous-materials) *TOG 2020* tags: `Reinforcement Learning` [doi](https://doi.org/10.1145/3414685.3417868)
- [Real-time hair simulation with neural interpolation](https://www.mlchai.com/publication/lyu2020real/) *TVCG 2020* categories: `Neural Solver` `Avatar` [paper](https://www.mlchai.com/publication/lyu2020real/)
- [ChainQueen: A Real-Time Differentiable Physical Simulator for Soft Robotics](https://github.com/yuanming-hu/ChainQueen) *ICRA 2019* categories: `Differentiable Simulation` [doi](https://doi.org/10.1109/ICRA.2019.8794333)
- [Latent-space dynamics for reduced deformable simulation](https://www.dgp.toronto.edu/projects/latent-space-dynamics/) *CGF 2019* [paper](https://www.dgp.toronto.edu/projects/latent-space-dynamics/)
- [Real2Sim: visco-elastic parameter estimation from dynamic motion](https://dl.acm.org/doi/10.1145/3355089.3356548) *TOG 2019* categories: `Differentiable Simulation` tags: `Real2Sim` [doi](https://doi.org/10.1145/3355089.3356548)
- [SoftCon: simulation and control of soft-bodied animals with biomimetic actuators](https://mrl.snu.ac.kr/publications/ProjectSoftCon/SoftCon.html?utm_campaign=Artificial%2BIntelligence%2BWeekly&utm_medium=rss&utm_source=Artificial_Intelligence_Weekly_153) *TOG 2019* categories: `Control` tags: `Reinforcement Learning` [doi](https://doi.org/10.1145/3355089.3356497)

</details>
<a id="rigidbody"></a>
<details>
<summary><strong>Rigidbody (40)</strong></summary>

- [Efficient Differentiable Contact Model with Long-range Influence](https://arxiv.org/abs/2509.20917) *ICLR 2026* categories: `Differentiable Simulation` [doi](https://doi.org/10.48550/arXiv.2509.20917)
- [Learning Object Properties Using Robot Proprioception via Differentiable Robot-Object Interaction](https://doi.org/10.1109/icra55743.2025.11127955) *ICRA 2025* categories: `Differentiable Simulation` `Embodied AI` [project](https://warpdiffrobot.github.io/) [doi](https://doi.org/10.1109/icra55743.2025.11127955)
- [Newton: An Open-Source, GPU-Accelerated Physics Simulation Engine Built upon NVIDIA Warp](https://github.com/newton-physics/newton) *2025* categories: `Engine` [paper](https://github.com/newton-physics/newton)
- [Painless Differentiable Rotation Dynamics](https://doi.org/10.1145/3730944) *TOG 2025* categories: `Differentiable Simulation` [project](https://mslab.es/projects/Painless/) [doi](https://doi.org/10.1145/3730944)
- [Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions](https://doi.org/10.1109/cvpr52734.2025.02101) *CVPR 2025* categories: `Embodied AI` [doi](https://doi.org/10.1109/cvpr52734.2025.02101)
- [Estimating Material Properties of Interacting Objects Using Sum-GP-UCB](https://doi.org/10.1109/icra57147.2024.10610129) *ICRA 2024* categories: `Embodied AI` [project](https://myunusseker.github.io/SumGP) [doi](https://doi.org/10.1109/icra57147.2024.10610129)
- [Jade: A Differentiable Physics Engine for Articulated Rigid Bodies with Intersection-Free Frictional Contact](https://sites.google.com/view/diffsim/) *ICRA 2024* categories: `Differentiable Simulation` `Engine` [paper](https://sites.google.com/view/diffsim/)
- [An Extensible, Data-Oriented Architecture for High-Performance, Many-World Simulation](https://madrona-engine.github.io/) *TOG 2023* categories: `Engine` tags: `Reinforcement Learning` [doi](https://doi.org/10.1145/3592427)
- [DefGraspNets: Grasp Planning on 3D Fields with Graph Neural Nets](https://doi.org/10.1109/icra48891.2023.10160986) *ICRA 2023* categories: `Neural Solver` `Embodied AI` [project](https://research.nvidia.com/publication/2023-05_defgraspnets-grasp-planning-3d-fields-graph-neural-nets) [doi](https://doi.org/10.1109/icra48891.2023.10160986)
- [Differentiable Dynamics Simulation Using Invariant Contact Mapping and Damped Contact Force](https://doi.org/10.1109/icra48891.2023.10161519) *ICRA 2023* categories: `Differentiable Simulation` `Embodied AI` [doi](https://doi.org/10.1109/icra48891.2023.10161519)
- [Differentiable Physics Simulation of Dynamics-Augmented Neural Objects](https://doi.org/10.1109/LRA.2023.3257707) *RA-L 2023* categories: `Differentiable Simulation` tags: `NeRF` [doi](https://doi.org/10.1109/LRA.2023.3257707)
- [DOC: Differentiable Optimal Control for Retargeting Motions onto Legged Robots](https://la.disneyresearch.com/publication/doc-differentiable-optimal-control-for-retargeting-motions-onto-legged-robots/) *TOG 2023* categories: `Control` `Embodied AI` [doi](https://doi.org/10.1145/3592454)
- [Dynamic-Resolution Model Learning for Object Pile Manipulation](https://doi.org/10.15607/rss.2023.xix.047) *RSS 2023* categories: `Embodied AI` [project](https://github.com/WangYixuan12/dyn-res-pile-manip) [doi](https://doi.org/10.15607/rss.2023.xix.047)
- [Fast-Grasp'D: Dexterous Multi-finger Grasp Generation Through Differentiable Simulation](https://doi.org/10.1109/icra48891.2023.10160314) *ICRA 2023* categories: `Differentiable Simulation` `Embodied AI` [doi](https://doi.org/10.1109/icra48891.2023.10160314)
- [Neural Collision Fields for Triangle Primitives](https://research.nvidia.com/labs/prl/publication/zesch2023ncf/) *Siggraph Asia 2023* categories: `Neural Representation` [doi](https://doi.org/10.1145/3610548.3618225)
- [SAM-RL: Sensing-Aware Model-Based Reinforcement Learning via Differentiable Physics-Based Simulation and Rendering](https://doi.org/10.15607/rss.2023.xix.040) *RSS 2023* categories: `Differentiable Simulation` tags: `Reinforcement Learning` [doi](https://doi.org/10.15607/rss.2023.xix.040)
- [Vr-handnet: A visually and physically plausible hand manipulation system in virtual reality](https://ieeexplore.ieee.org/abstract/document/10066837) *TVCG 2023* tags: `User Interaction` [paper](https://ieeexplore.ieee.org/abstract/document/10066837)
- [Accelerated Policy Learning with Parallel Differentiable Simulation](https://arxiv.org/abs/2204.07137) *Conference on Robot Learning (CoRL) 2022* categories: `Differentiable Simulation` tags: `Reinforcement Learning` [project](https://short-horizon-actor-critic.github.io/) [doi](https://doi.org/10.48550/arXiv.2204.07137)
- [Dojo: A Differentiable Physics Engine for Robotics](https://sites.google.com/view/dojo-sim) *Arxiv 2022* categories: `Differentiable Simulation` `Engine` [paper](https://sites.google.com/view/dojo-sim)
- [Learning Object Relations with Graph Neural Networks for Target-Driven Grasping in Dense Clutter](https://doi.org/10.1109/icra46639.2022.9811601) *ICRA 2022* categories: `Embodied AI` [doi](https://doi.org/10.1109/icra46639.2022.9811601)
- [Learning physical dynamics with subequivariant graph neural networks](https://hanjq17.github.io/SGNN/) *NeurIPS 2022* [paper](https://hanjq17.github.io/SGNN/)
- [Learning physics constrained dynamics using autoencoders](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6d5e035724687454549b97d6c805dc84-Abstract-Conference.html) *NeurIPS 2022* [paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6d5e035724687454549b97d6c805dc84-Abstract-Conference.html)
- [Probabilistic Inference of Simulation Parameters via Parallel Differentiable Simulation](https://doi.org/10.1109/icra46639.2022.9812293) *ICRA 2022* categories: `Differentiable Simulation` `Embodied AI` [project](https://uscresl.github.io/prob-diff-sim) [doi](https://doi.org/10.1109/icra46639.2022.9812293)
- [SAGCI-System: Towards Sample-Efficient, Generalizable, Compositional, and Incremental Robot Learning](https://doi.org/10.1109/icra46639.2022.9811859) *ICRA 2022* categories: `Differentiable Simulation` `Embodied AI` [doi](https://doi.org/10.1109/icra46639.2022.9811859)
- [Brax - A Differentiable Physics Engine for Large Scale Rigid Body Simulation](https://github.com/google/brax) *NeurIPS 2021* categories: `Differentiable Simulation` `Engine` [paper](https://github.com/google/brax)
- [Efficient Differentiable Simulation of Articulated Bodies](https://github.com/YilingQiao/diffarticulated) *ICML 2021* categories: `Differentiable Simulation` [paper](https://github.com/YilingQiao/diffarticulated)
- [Fast and Feature-Complete Differentiable Physics Engine for Articulated Rigid Bodies with Contact Constraints](https://arxiv.org/abs/2103.16021) *RSS 2021* categories: `Differentiable Simulation` `Engine` [doi](https://doi.org/10.15607/RSS.2021.XVII.034)
- [Learning to Propagate Interaction Effects for Modeling Deformable Linear Objects Dynamics](https://doi.org/10.1109/icra48506.2021.9561636) *ICRA 2021* categories: `Embodied AI` [project](https://amm.aass.oru.se/icra2021-learning-dlo) [doi](https://doi.org/10.1109/icra48506.2021.9561636)
- [NeuralSim: Augmenting Differentiable Simulators with Neural Networks](https://doi.org/10.1109/icra48506.2021.9560935) *ICRA 2021* categories: `Neural Solver` [project](https://uscresl.org/publication/neuralsim-augmenting-differentiable-simulators-with-neural-networks) [doi](https://doi.org/10.1109/icra48506.2021.9560935)
- [PyBullet, a Python module for physics simulation for games, robotics and machine learning](http://pybullet.org) *2016--2021* categories: `Engine` [paper](http://pybullet.org)
- [Single-view robot pose and joint angle estimation via render & compare](https://www.di.ens.fr/willow/research/robopose/) *CVPR 2021* [paper](https://www.di.ens.fr/willow/research/robopose/)
- [The Role of Physics-Based Simulators in Robotics](https://doi.org/10.1146/annurev-control-072220-093055) *ARCRAS 2021* categories: `Survey` [doi](https://doi.org/10.1146/annurev-control-072220-093055)
- [ADD: analytically differentiable dynamics for multi-body systems with frictional contact](https://arxiv.org/abs/2007.00987) *TOG 2020* categories: `Differentiable Simulation` [doi](https://doi.org/10.1145/3414685.3417766)
- [Rl-cyclegan: Reinforcement learning aware simulation-to-real](https://arxiv.org/abs/2006.09001) *CVPR 2020* tags: `Reinforcement Learning` [paper](https://arxiv.org/abs/2006.09001)
- [Scalable Differentiable Physics for Learning and Control](https://github.com/YilingQiao/diffsim) *ICML 2020* categories: `Differentiable Simulation` [paper](https://github.com/YilingQiao/diffsim)
- [Use the force, luke! learning to predict physical forces by simulating effects](https://ehsanik.github.io/forcecvpr2020/) *CVPR 2020* [paper](https://ehsanik.github.io/forcecvpr2020/)
- [Drake: Model-based design and verification for robotics](https://drake.mit.edu) *2019* categories: `Engine` [paper](https://drake.mit.edu)
- [Learning to fly: computational controller design for hybrid UAVs with reinforcement learning](https://people.csail.mit.edu/jiex/papers/LearningToFly/index.html) *TOG 2019* categories: `Control` tags: `Reinforcement Learning` [doi](https://doi.org/10.1145/3306346.3322940)
- [Shapestacks: Learning vision-based physical intuition for generalised object stacking](https://arxiv.org/abs/1804.08018) *ECCV 2018* [paper](https://arxiv.org/abs/1804.08018)
- [MuJoCo: A physics engine for model-based control](https://mujoco.org/) *IROS 2012* categories: `Engine` [doi](https://doi.org/10.1109/IROS.2012.6386109)

</details>
<a id="multiphys"></a>
<details>
<summary><strong>Multiphys (17)</strong></summary>

- [Multiphysics Simulation Methods in Computer Graphics](https://doi.org/10.1111/cgf.70082) *CGF 2025* categories: `Survey` [project](https://multi.physics-simulation.org/) [doi](https://doi.org/10.1111/cgf.70082)
- [Stabilizing Reinforcement Learning in Differentiable Multiphysics Simulation](https://arxiv.org/abs/2412.12089) *ICLR 2025* categories: `Differentiable Simulation` tags: `Reinforcement Learning` [project](https://rewarped.github.io/) [paper](https://arxiv.org/abs/2412.12089)
- [A Review of Differentiable Simulators](https://doi.org/10.1109/ACCESS.2024.3425448) *IEEE Access 2024* categories: `Differentiable Simulation` `Survey` [project](https://rhys-newbury.github.io/projects/DiffSim) [doi](https://doi.org/10.1109/ACCESS.2024.3425448)
- [Neural Physical Simulation with Multi-Resolution Hash Grid Encoding](https://ojs.aaai.org/index.php/AAAI/article/view/28349) *AAAI 2024* [paper](https://ojs.aaai.org/index.php/AAAI/article/view/28349)
- [SoftMAC: Differentiable Soft Body Simulation with Forecast-based Contact Model and Two-way Coupling with Articulated Rigid Bodies and Clothes](https://doi.org/10.1109/IROS58592.2024.10801308) *IROS 2024* categories: `Differentiable Simulation` `Engine` [project](https://minliu01.github.io/SoftMAC/) [doi](https://doi.org/10.1109/IROS58592.2024.10801308)
- [A generalized constitutive model for versatile mpm simulation and inverse learning with differentiable physics](https://xuan-li.github.io/publication/su2023generalized/) *PACMCGIT 2023* categories: `Differentiable Simulation` [paper](https://xuan-li.github.io/publication/su2023generalized/)
- [Dynamic mesh-aware radiance fields](https://mesh-aware-rf.github.io/) *ICCV 2023* [paper](https://mesh-aware-rf.github.io/)
- [Learning neural constitutive laws from motion observations for generalizable pde dynamics](https://sites.google.com/view/nclaw) *ICML 2023* categories: `Differentiable Simulation` tags: `Neural Material` [paper](https://sites.google.com/view/nclaw)
- [MPMNet: A data-driven MPM framework for dynamic fluid-solid interaction](https://ieeexplore.ieee.org/document/10113697) *TVCG 2023* [paper](https://ieeexplore.ieee.org/document/10113697)
- [PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification](https://sites.google.com/view/PAC-NeRF) *ICLR 2023* categories: `Reconstruction` tags: `NeRF` [paper](https://sites.google.com/view/PAC-NeRF)
- [PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics](https://xpandora.github.io/PhysGaussian/) *Arxiv 2023* tags: `3DGS` [paper](https://xpandora.github.io/PhysGaussian/)
- [Differentiable Simulation](https://doi.org/10.1145/3476117.3483433) *Siggraph Asia 2021* categories: `Survey` `Differentiable Simulation` [doi](https://doi.org/10.1145/3476117.3483433)
- [gradSim: Differentiable Simulation for System Identification and Visuomotor Control](https://openreview.net/forum?id=c_E8kFWfhp0) *ICLR 2021* categories: `Differentiable Simulation` `Control` [project](https://gradsim.github.io/) [paper](https://openreview.net/forum?id=c_E8kFWfhp0)
- [NeuralSim: Augmenting Differentiable Simulators with Neural Networks](https://github.com/erwincoumans/tiny-differentiable-simulator) *ICRA 2021* [paper](https://github.com/erwincoumans/tiny-differentiable-simulator)
- [NVIDIA SimNetTM: An AI-Accelerated Multi-Physics Simulation Framework](https://arxiv.org/abs/2012.07938) *ICCS 2021* [paper](https://arxiv.org/abs/2012.07938)
- [Learning Mesh-Based Simulation with Graph Networks](http://arxiv.org/abs/2010.03409) *ICLR 2020* categories: `Neural Solver` [project](https://sites.google.com/view/meshgraphnets) [doi](https://doi.org/10.48550/arxiv.2010.03409)
- [Learning to simulate complex physics with graph networks](https://sites.google.com/view/learning-to-simulate) *ICML 2020* [paper](https://sites.google.com/view/learning-to-simulate)

</details>
<a id="category-guide"></a>
<a id="tag-guide"></a>
<details>
<summary><strong>Category Guide</strong></summary>

The guide documents the stable categories. Paper-specific tags stay inline and remain open-ended.

| Category | Meaning |
| --- | --- |
| `Differentiable Simulation` | Pipelines whose forward pass is an explicit physical simulator, with gradients propagated through that simulator. |
| `Neural Representation` | Physics-aware neural state, field, or latent representations used to model physical processes. |
| `Neural Solver` | Works where the solve, update, or simulation computation is replaced or driven by a learned solver. |
| `Reconstruction` | Recovering geometry, motion, state, or parameters from observations. |
| `Control` | Control-centered methods such as policy design, MPC, or action optimization for physical systems. |
| `Embodied AI` | Validation in robotic or embodied settings such as manipulation, locomotion, or embodied interaction. |
| `Engine` | Clearly reusable engines, frameworks, or toolkits rather than one-off task-specific methods. |
| `Fracture` | Fracture, crack propagation, or material failure is a central simulation phenomenon. |
| `Avatar` | Human-avatar-centric settings such as clothed humans or body-driven garment dynamics. |
| `Survey` | Survey or review papers. |

</details>
<a id="keyword-guide"></a>
<details>
<summary><strong>Keyword Guide</strong></summary>

Keywords are the reader-facing, open-ended descriptors used for quick understanding and search.

| Keyword | Count |
| --- | --- |
| `Reinforcement Learning` | 11 |
| `3DGS` | 8 |
| `User Interaction` | 8 |
| `NeRF` | 6 |
| `Super Resolution` | 6 |
| `Neural Material` | 4 |
| `Style Transfer` | 4 |
| `Real2Sim` | 3 |

</details>
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
