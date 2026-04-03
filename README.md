# Awesome Neural Physics

A curated list of papers on **AI techniques for physics simulation** in computer graphics.

> `213` papers | `2012-2026` | `Fluid 67` | `Cloth 42` | `Softbody 56` | `Rigidbody 36` | `Multiphys 12`

This README is the compact browsing view. For search, filtering, and tag-based lookup, open [the interactive index](https://awesome-physics.github.io/awesome-neural-physics/).

**Browse:** [Recent Additions](#recent-additions) | [Tag Guide](#tag-guide) | [Categories](#categories) | [BibTeX](main.bib) | [Citation](#citation)

## Recent Additions

- **[Neuralocks: Real-Time Dynamic Neural Hair Simulation](https://doi.org/10.1111/cgf.70407)**. `Softbody / CGF 2026`. `Neural Simulation` `Avatar`
- **[A Differentiable Material Point Method Framework for Shape Morphing](https://doi.org/10.1109/tvcg.2025.3591729)**. `Softbody / TVCG 2025`. `Differentiable Simulation`
- **[A Neural Particle Level Set Method for Dynamic Interface Tracking](https://doi.org/10.1145/3730399)**. `Fluid / TOG 2025`. `Neural Representation`
- **[A Pioneering Neural Network Method for Efficient and Robust Fuel Sloshing Simulation in Aircraft](https://doi.org/10.1609/aaai.v39i15.33752)**. `Fluid / AAAI 2025`.
- **[DeepFracture: A Generative Approach for Predicting Brittle Fractures with Neural Discrete Representation Learning](https://nikoloside.graphics/deepfracture/)**. `Softbody / CGF 2025`. `Neural Representation` `Fracture`
- **[Dress Anyone : Automatic Physically-Based Garment Pattern Refitting 56](https://doi.org/10.1145/3747858)**. `Cloth / PACMCGIT 2025`. `Differentiable Simulation`
- **[Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics](https://doi.org/10.1145/3731177)**. `Cloth / TOG 2025`. `Differentiable Simulation` `Reconstruction`
- **[Elastic Locomotion with Mixed Second-order Differentiation](https://doi.org/10.1145/3721238.3730685)**. `Softbody / Siggraph 2025`. `Differentiable Simulation`

## Tag Guide

Inline tags only show secondary signals beyond the section label itself.

| Tag | Meaning |
| --- | --- |
| `Differentiable Simulation` | Pipelines whose forward pass is an explicit physical simulator, with differentiable gradients propagated through that simulator. |
| `Neural Simulation` | Learned forward simulators where part or all of the dynamics model is neural. |
| `Neural Representation` | Physics-aware neural state, field, or latent representations used to model dynamics. |
| `Neural Material` | Neural representations or neural constitutive models that explicitly encode material behavior. |
| `Reconstruction` | Recovering geometry, motion, or physical state from images, videos, or sparse observations. |
| `Interaction` | Interactive systems, authoring tools, editing workflows, or user-in-the-loop interfaces. |
| `Control` | Control, optimal control, MPC, or policy design for simulated physical systems. |
| `Reinforcement Learning` | Works that explicitly use reinforcement learning. |
| `Embodied AI` | Validation on robotic or embodied manipulation settings. |
| `Real2Sim` | Inferring simulation-ready models or parameters from real observations. |
| `Sim2Real` | Transfer from simulation-trained models or policies to the real world. |
| `NeRF` | Neural radiance fields or related volumetric neural rendering methods. |
| `3DGS` | 3D Gaussian splatting based modeling, rendering, or simulation pipelines. |
| `Engine` | Reusable simulation engines or general-purpose physics frameworks. |
| `Super-Resolution` | Increasing spatial or temporal detail beyond the native simulation resolution. |
| `Style Transfer` | Transferring appearance or motion style across simulations. |
| `Fracture` | Fracture, crack propagation, or failure phenomena in physical systems. |
| `Avatar` | Human or character-centric avatars, garments, or hair driven by body motion. |

## Categories

[Fluid (67)](#fluid) | [Cloth (42)](#cloth) | [Softbody (56)](#softbody) | [Rigidbody (36)](#rigidbody) | [Multiphys (12)](#multiphys) | [Survey (4)](#survey)

<a id="fluid"></a>
## Fluid (67)

- **[A Neural Particle Level Set Method for Dynamic Interface Tracking](https://doi.org/10.1145/3730399)**. `TOG 2025`. [project](https://cdwj.github.io/projects/neural-pls-project-page/index.html) `Neural Representation`
- **[A Pioneering Neural Network Method for Efficient and Robust Fuel Sloshing Simulation in Aircraft](https://doi.org/10.1609/aaai.v39i15.33752)**. `AAAI 2025`. [project](https://github.com/chenyu-xjtu/A-Pioneering-Neural-Network-Method-for-Efficient-and-Robust-Fuel-Sloshing-Simulation-in-Aircraft)
- **[Representing Flow Fields with Divergence-Free Kernels for Reconstruction](https://doi.org/10.1145/3747872)**. `PACMCGIT 2025`. [project](https://www.physicsbasedanimation.com/2025/08/10/representing-flow-fields-with-divergence-free-kernels-for-reconstruction) `Neural Representation` `Reconstruction`
- **[A Real-Time and Interactive Fluid Modeling System for Mixed Reality](https://doi.org/10.1109/tvcg.2024.3456140)**. `TVCG 2024`. [project](https://github.com/cenyc/Interactive-Fluid-Modeling) `Reconstruction` `Interaction`
- **[Differentiable Voronoi Diagrams for Simulation of Cell-Based Mechanical Systems](https://github.com/lnumerow-ethz/VoronoiCellSim)**. `TOG 2024`.
- **[Dynamic ocean inverse modeling based on differentiable rendering](https://link.springer.com/article/10.1007/s41095-023-0338-4)**. `CVM 2024`.
- **[Fluid Inverse Volumetric Modeling and Applications from Surface Motion](https://www.computer.org/csdl/journal/tg/5555/01/10452823/1UUuVAIPShy)**. `TVCG 2024`.
- **[Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting](https://amysteriouscat.github.io/GaussianSplashing/)**. `Arxiv 2024`. `3DGS`
- **[Inferring Hybrid Neural Fluid Fields from Videos](https://kovenyu.com/hyfluid/)**. `NeurIPS 2024`.
- **[Laplacian Projection Based Global Physical Prior Smoke Reconstruction](https://www.computer.org/csdl/journal/tg/5555/01/10414126/1TZIJbrBNo4)**. `TVCG 2024`. `Differentiable Simulation` `Reconstruction`
- **[Learning Reduced Fluid Dynamics](https://ojs.aaai.org/index.php/AAAI/article/view/29367)**. `AAAI 2024`.
- **[NeuSmoke: Efficient Smoke Reconstruction and View Synthesis with Neural Transportation Fields](https://doi.org/10.1145/3680528.3687667)**. `Siggraph Asia 2024`. [project](https://github.com/JiaxiongQ/NeuSmoke) `Reconstruction`
- **[Physics-Informed Learning of Characteristic Trajectories for Smoke Reconstruction](https://doi.org/10.1145/3641519.3657483)**. `Siggraph 2024`. [project](https://github.com/19reborn/PICT_smoke) `Reconstruction` `NeRF`
- **[Reconstruction of implicit surfaces from fluid particles using convolutional neural networks](https://doi.org/10.1111/cgf.15181)**. `CGF 2024`. [project](https://www.cs.ucr.edu/~craigs/research.html) `Reconstruction`
- **[SNN-PDE: Learning Dynamic PDEs from Data with Simplicial Neural Networks](http://dx.doi.org/10.1609/aaai.v38i10.29038)**. `AAAI 2024`. `Neural Simulation`
- **[Symmetric Basis Convolutions for Learning Lagrangian Fluid Mechanics](https://github.com/tum-pbs/SFBC)**. `ICLR 2024`.
- **[Aquarium: A Fully Differentiable Fluid-Structure Interaction Solver for Robotics Applications](https://doi.org/10.1109/icra48891.2023.10161494)**. `ICRA 2023`. [project](https://github.com/RoboticExplorationLab/Aquarium.jl) `Differentiable Simulation` `Embodied AI`
- **[Boundary Graph Neural Networks for 3D Simulations](https://doi.org/10.1609/aaai.v37i8.26092)**. `AAAI 2023`. [project](https://ml-jku.github.io/bgnn) `Neural Simulation`
- **[DiffFR: Differentiable SPH-Based Fluid-Rigid Coupling for Rigid Body Control](https://zhehaoli1999.github.io/DiffFR/)**. `TOG 2023`. `Differentiable Simulation` `Control`
- **[Fast fluid simulation via dynamic multi-scale gridding](https://ojs.aaai.org/index.php/AAAI/article/view/25255)**. `AAAI 2023`.
- **[Fluid Simulation on Neural Flow Maps](https://yitongdeng-projects.github.io/neural_flow_maps_webpage/)**. `TOG 2023`.
- **[FluidLab: A Differentiable Environment for Benchmarking Complex Fluid Manipulation](https://fluidlab2023.github.io/)**. `ICLR 2023`. `Differentiable Simulation`
- **[Interactive design of 2D car profiles with aerodynamic feedback](https://doi.org/10.1111/cgf.14772)**. `CGF 2023`. [project](https://hal.science/hal-03975369) `Neural Simulation` `Neural Representation`
- **[Learning to Estimate Single-View Volumetric Flow Motions without 3D Supervision](https://ge.in.tum.de/publications/2023-franz-neuralglobtrans/)**. `ICLR 2023`.
- **[Learning Vortex Dynamics for Fluid Inference and Prediction](https://github.com/yitongdeng-projects/learning_vortex_dynamics_code)**. `ICLR 2023`.
- **[Neural vortex method: From finite Lagrangian particles to infinite dimensional Eulerian dynamics](https://arxiv.org/abs/2006.04178)**. `Comput. Fluids 2023`.
- **[Physics-Informed Neural Corrector for Deformation-based Fluid Control](https://studios.disneyresearch.com/2023/05/07/physics-informed-neural-corrector-for-deformation-based-fluid-control/)**. `CGF 2023`. `Control`
- **[Solving Inverse Physics Problems with Score Matching](https://github.com/tum-pbs/SMDP)**. `NeurIPS 2023`.
- **[Deep Reconstruction of 3D Smoke Densities from Artist Sketches](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14461)**. `CGF 2022`.
- **[Efficient Neural Style Transfer for Volumetric Simulations](https://studios.disneyresearch.com/2022/11/30/efficient-neural-style-transfer-for-volumetric-simulations/)**. `TOG 2022`. `Style Transfer`
- **[Fluidic Topology Optimization with an Anisotropic Mixture Model](https://doi.org/10.1145/3550454.3555429)**. `TOG 2022`. [project](https://people.csail.mit.edu/liyifei/publication/anisotropicstokes) `Differentiable Simulation`
- **[Guaranteed conservation of momentum for learning particle-based fluid dynamics](https://github.com/tum-pbs/DMCF)**. `NeurIPS 2022`.
- **[Half-Inverse Gradients for Physical Deep Learning](https://arxiv.org/abs/2203.10131)**. `ICLR 2022`.
- **[Neurofluid: Fluid dynamics grounding with particle-driven neural radiance fields](https://syguan96.github.io/NeuroFluid/)**. `ICML 2022`.
- **[Physics informed neural fields for smoke reconstruction with sparse data](https://rachelcmy.github.io/pinf_smoke/)**. `TOG 2022`. `Reconstruction` `NeRF`
- **[Transformer with implicit edges for particle-based physics simulation](https://www.mmlab-ntu.com/project/tie/index.html)**. `ECCV 2022`.
- **[Versatile Control of Fluid-directed Solid Objects Using Multi-task Reinforcement Learning](https://dl.acm.org/doi/10.1145/3554731)**. `TOG 2022`. `Control` `Reinforcement Learning`
- **[Data-driven simulation in fluids animation: A survey](https://www.sciencedirect.com/science/article/pii/S2096579621000139)**. `VRIH 2021`. `survey`
- **[Differentiable Fluids with Solid Coupling for Learning and Control](https://ojs.aaai.org/index.php/AAAI/article/view/16764)**. `AAAI 2021`. `Differentiable Simulation` `Control`
- **[Global transport for fluid reconstruction with learned self-supervision](https://ge.in.tum.de/publications/)**. `CVPR 2021`.
- **[Learning meaningful controls for fluids](https://rachelcmy.github.io/den2vel/)**. `TOG 2021`. `Control`
- **[Model-Predictive Control of Blood Suction for Surgical Hemostasis using Differentiable Fluid Simulations](https://doi.org/10.1109/icra48506.2021.9561624)**. `ICRA 2021`. [project](https://ucsdarclab.com/autopublication/model-predictive-control-of-blood-suction-for-surgical-hemostasis-using-differentiable-fluid-simulations) `Control` `Embodied AI`
- **[Neural upflow: A scene flow learning approach to increase the apparent resolution of particle-based liquids](https://dl.acm.org/doi/abs/10.1145/3480147)**. `PACMCGIT 2021`.
- **[Predicting high-resolution turbulence details in space and time](https://dl.acm.org/doi/abs/10.1145/3478513.3480492)**. `TOG 2021`. `Super-Resolution`
- **[Two-step Temporal Interpolation Network Using Forward Advection for Efficient Smoke Simulation](https://onlinelibrary.wiley.com/doi/10.1111/cgf.142638)**. `CGF 2021`.
- **[Volumetric appearance stylization with stylizing kernel prediction network](https://dl.acm.org/doi/abs/10.1145/3450626.3459799)**. `TOG 2021`. `Style Transfer`
- **[A Novel CNN-Based Poisson Solver for Fluid Simulation](http://dalab.se.sjtu.edu.cn/www/home/?page_id=790)**. `TVCG 2020`.
- **[Dynamic fluid surface reconstruction using deep neural network](https://ivlab.cse.lsu.edu/FSRN_CVPR20.html)**. `CVPR 2020`. `Reconstruction`
- **[Dynamic Upsampling of Smoke through Dictionary-based Learning](https://faculty.sist.shanghaitech.edu.cn/faculty/liuxp/projects/ss_dbnn/index.htm)**. `TOG 2020`. `Super-Resolution`
- **[Interactive liquid splash modeling by user sketches](https://dl.acm.org/doi/abs/10.1145/3414685.3417832)**. `TOG 2020`. `Interaction`
- **[Lagrangian neural style transfer for fluids](https://github.com/byungsook/neural-flow-style)**. `TOG 2020`. `Style Transfer`
- **[Latent space subdivision: stable and controllable time predictions for fluid flow](https://ge.in.tum.de/publications/2020-lssubdiv-wiewel/)**. `CGF 2020`.
- **[Learning to Control PDEs with Differentiable Physics](http://arxiv.org/abs/2001.07457)**. `ICLR 2020`. [project](https://github.com/p-holl/PDE-Control) `Differentiable Simulation` `Interaction`
- **[Machine learning for fluid mechanics](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-010719-060214)**. `ARFM 2020`. `survey`
- **[Tomofluid: Reconstructing dynamic fluid from sparse view videos](https://openaccess.thecvf.com/content_CVPR_2020/html/Zang_TomoFluid_Reconstructing_Dynamic_Fluid_From_Sparse_View_Videos_CVPR_2020_paper.html)**. `CVPR 2020`. `Reconstruction`
- **[A CNN-based Flow Correction Method for Fast Preview](http://dalab.se.sjtu.edu.cn/www/home/?page_id=763)**. `CGF 2019`. `Super-Resolution`
- **[Lagrangian fluid simulation with continuous convolutions](https://ge.in.tum.de/publications/2020-ummenhofer-iclr/)**. `ICLR 2019`.
- **[ScalarFlow: a large-scale volumetric data set of real-world scalar transport flows for computer animation and machine learning](https://ge.in.tum.de/publications/2019-scalarflow-eckert/)**. `TOG 2019`.
- **[Transport-based neural style transfer for smoke simulations](https://dl.acm.org/doi/10.1145/3355089.3356560)**. `TOG 2019`. `Style Transfer`
- **[Video-guided real-to-virtual parameter transfer for viscous fluids](https://gamma.cs.unc.edu/ParameterTransfer/)**. `TOG 2019`.
- **[Deep dynamical modeling and control of unsteady fluid flows](https://github.com/sisl/deep_flow_control)**. `NeurIPS 2018`. `Control`
- **[Fluid directed rigid body control using deep reinforcement learning](https://gamma.cs.unc.edu/DRL_FluidRigid/)**. `TOG 2018`. `Control` `Reinforcement Learning`
- **[tempoGAN: A temporally coherent, volumetric GAN for super-resolution fluid flow](https://ge.in.tum.de/publications/tempogan/)**. `TOG 2018`. `Super-Resolution`
- **[Accelerating eulerian fluid simulation with convolutional networks](https://github.com/google/FluidNet)**. `ICML 2017`.
- **[Data-driven synthesis of smoke flows with CNN-based feature descriptors](https://ge.in.tum.de/publications/2017-sig-chu/)**. `TOG 2017`.
- **[Data-driven projection method in fluid simulation](http://dalab.se.sjtu.edu.cn/www/home/?page_id=911)**. `CAVW 2016`.
- **[Data-driven fluid simulations using regression forests](https://dl.acm.org/doi/10.1145/2816795.2818129)**. `TOG 2015`.

<a id="cloth"></a>
## Cloth (42)

- **[Dress Anyone : Automatic Physically-Based Garment Pattern Refitting 56](https://doi.org/10.1145/3747858)**. `PACMCGIT 2025`. [project](https://igl.ethz.ch/projects/dress_anyone) `Differentiable Simulation`
- **[Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics](https://doi.org/10.1145/3731177)**. `TOG 2025`. [project](https://dress-1-to-3.github.io/) `Differentiable Simulation` `Reconstruction`
- **[Frequency-Divided Learning of Fine-Grained Clothing Behavior via Flexible Dynamic Graphs](https://doi.org/10.1109/tvcg.2025.3591816)**. `TVCG 2025`. [project](https://shirui-homepage.com/publication/2025-freq-div-TVCG) `Neural Simulation` `Avatar`
- **[PICA: Physics-Integrated Clothed Avatar](https://doi.org/10.1109/tvcg.2025.3560241)**. `TVCG 2025`. [project](https://ustc3dv.github.io/PICA) `3DGS` `Avatar`
- **[Self-Supervised Humidity-Controllable Garment Simulation via Capillary Bridge Modeling](https://doi.org/10.1111/cgf.70236)**. `CGF 2025`.
- **[Bayesian Differentiable Physics for Cloth Digitalization](https://github.com/realcrane/Bayesian-Differentiable-Physics-for-Cloth-Digitalization)**. `CVPR 2024`. `Differentiable Simulation`
- **[ContourCraft: Learning to Resolve Intersections in Neural Multi-Garment Simulations](https://doi.org/10.1145/3641519.3657408)**. `Siggraph 2024`. `Neural Simulation`
- **[DiffAvatar: Simulation-Ready Garment Optimization with Differentiable Simulation](https://people.csail.mit.edu/liyifei/publication/diffavatar/)**. `CVPR 2024`. `Differentiable Simulation` `Avatar`
- **[Efficient Deformation Learning of Varied Garments with a Structure-Preserving Multilevel Framework](https://doi.org/10.1145/3651286)**. `PACMCGIT 2024`. [project](https://li-tianxing.github.io/publication/psdunet) `Neural Simulation`
- **[Estimating Cloth Simulation Parameters From Tag Information and Cusick Drape Test](https://doi.org/10.1111/cgf.15027)**. `CGF 2024`. [project](https://mingry.github.io/Fabrics5k)
- **[Garment Animation NeRF with Color Editing](https://doi.org/10.1111/cgf.15178)**. `CGF 2024`. [project](https://mengzephyr.com/Garment-Animation-NeRF-With-Color-Editing) `NeRF` `Avatar`
- **[GarmentDreamer: 3DGS Guided Garment Synthesis with Diverse Geometry and Texture Details](https://arxiv.org/abs/2405.12420)**. `Arxiv 2024`. `3DGS`
- **[Neural Garment Dynamic Super-Resolution](https://doi.org/10.1145/3680528.3687610)**. `Siggraph Asia 2024`. [project](https://mengzephyr.com/Neural-Garment-Dynamic-Super-Reslution) `Super-Resolution`
- **[Neural Garment Dynamics via Manifold-Aware Transformers](https://doi.org/10.1111/cgf.15028)**. `CGF 2024`. [project](https://github.com/PeizhuoLi/manifold-aware-transformers) `Neural Simulation` `Avatar`
- **[Parametric Linear Blend Skinning Model for Multiple-Shape 3D Garments](https://doi.org/10.1109/tvcg.2024.3478852)**. `TVCG 2024`. [project](https://www.sysu-hcp.net/projects/cv/126.html) `Avatar`
- **[Physics-guided Shape-from-Template: Monocular Video Perception through Neural Surrogate Models](https://doi.org/10.1109/cvpr52733.2024.01130)**. `CVPR 2024`. [project](https://github.com/vc-bonn/Physics-guided-Shape-from-Template) `Neural Simulation` `Reconstruction`
- **[ClothCombo: Modeling Inter-Cloth Interaction for Draping Multi-Layered Clothes](https://dl.acm.org/doi/10.1145/3618376)**. `TOG 2023`.
- **[D-Cloth: Skinning-based Cloth Dynamic Prediction with a Three-stage Network](https://min-tang.github.io/home/DCloth/)**. `CGF 2023`. `Neural Simulation`
- **[Detail-Aware Deep Clothing Animations Infused with Multi-Source Attributes](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14651)**. `CGF 2023`. `Avatar`
- **[DiffXPBD: Differentiable Position-Based Simulation of Compliant Constraint Dynamics](https://doi.org/10.1145/3606923)**. `PACMCGIT 2023`. `Differentiable Simulation`
- **[Elastic Context: Encoding Elasticity for Data-driven Models of Textiles Elastic Context: Encoding Elasticity for Data-driven Models of Textiles](https://doi.org/10.1109/icra48891.2023.10160740)**. `ICRA 2023`. `Neural Material` `Embodied AI`
- **[HOOD: Hierarchical Graphs for Generalized Modelling of Clothing Dynamics](https://doi.org/10.1109/cvpr52729.2023.01627)**. `CVPR 2023`. [project](https://dolorousrtur.github.io/hood/?trk=public_post_comment-text) `Neural Simulation`
- **[How Will It Drape Like? Capturing Fabric Mechanics from Depth Images](http://dx.doi.org/10.1111/cgf.14750)**. `CGF 2023`. [project](https://carlosrodriguezpardo.es/projects/MechFromDepth) `Sim2Real`
- **[Learning Anchor Transformations for 3D Garment Animation](https://doi.org/10.1109/cvpr52729.2023.00055)**. `CVPR 2023`. [project](https://semanticdh.github.io/AnchorDEF) `Avatar`
- **[SwinGar: Spectrum-Inspired Neural Dynamic Deformation for Free-Swinging Garments](https://doi.org/10.1109/tvcg.2023.3346055)**. `TVCG 2023`.
- **[Towards Multi-Layered 3D Garments Animation](https://doi.org/10.1109/iccv51070.2023.01321)**. `ICCV 2023`. [project](https://mmlab-ntu.github.io/project/layersnet)
- **[DiffCloth: Differentiable Cloth Simulation with Dry Frictional Contact](https://people.csail.mit.edu/liyifei/publication/diffcloth/)**. `TOG 2022`. `Differentiable Simulation`
- **[Dressing avatars: Deep photorealistic appearance for physically simulated clothing](https://research.facebook.com/publications/dressing-avatars-deep-photorealistic-appearance-for-physically-simulated-clothing/)**. `TOG 2022`. `Avatar`
- **[Learning Latent Graph Dynamics for Visual Manipulation of Deformable Objects](https://doi.org/10.1109/icra46639.2022.9811597)**. `ICRA 2022`. `Neural Representation` `Embodied AI`
- **[Learning-based bending stiffness parameter estimation by a drape tester](https://github.com/DrapeTester/ClothDrapeTester)**. `TOG 2022`.
- **[Neural cloth simulation](https://hbertiche.github.io/NeuralClothSim/)**. `TOG 2022`.
- **[Pattern-based cloth registration and sparse-view animation](https://dl.acm.org/doi/abs/10.1145/3550454.3555448)**. `TOG 2022`.
- **[Predicting loose-fitting garment deformations using bone-driven motion networks](http://www.cad.zju.edu.cn/home/jin/SigCloth2022/SigCloth2022.htm)**. `Siggraph 2022`. `Neural Simulation` `Avatar`
- **[Snug: Self-supervised neural dynamic garments](http://mslab.es/projects/SNUG/)**. `CVPR 2022`. `Neural Simulation` `Avatar`
- **[Dynamic neural garments](https://geometry.cs.ucl.ac.uk/projects/2021/DynamicNeuralGarments/)**. `TOG 2021`. `Neural Simulation` `Avatar`
- **[PBNS: physically based neural simulation for unsupervised garment pose space deformation](https://hbertiche.github.io/PBNS/)**. `TOG 2021`. `Neural Simulation` `Avatar`
- **[Self-supervised collision handling via generative 3d garment models for virtual try-on](http://mslab.es/projects/SelfSupervisedGarmentCollisions/)**. `CVPR 2021`.
- **[Cloth in the wind: A case study of physical measurement through simulation](https://arxiv.org/abs/2003.05065)**. `CVPR 2020`.
- **[Learning to measure the static friction coefficient in cloth contact](https://openaccess.thecvf.com/content_CVPR_2020/html/Rasheed_Learning_to_Measure_the_Static_Friction_Coefficient_in_Cloth_Contact_CVPR_2020_paper.html)**. `CVPR 2020`.
- **[Projective dynamics with dry frictional contact](https://astcort.github.io/)**. `TOG 2020`.
- **[Differentiable Cloth Simulation for Inverse Problems](https://gamma.umd.edu/researchdirections/virtualtryon/differentiablecloth)**. `NeurIPS 2019`. `Differentiable Simulation`
- **[Learning an intrinsic garment space for interactive authoring of garment animation](https://geometry.cs.ucl.ac.uk/projects/2019/garment_authoring/)**. `TOG 2019`. `Interaction` `Avatar`

<a id="softbody"></a>
## Softbody (56)

- **[Neuralocks: Real-Time Dynamic Neural Hair Simulation](https://doi.org/10.1111/cgf.70407)**. `CGF 2026`. `Neural Simulation` `Avatar`
- **[A Differentiable Material Point Method Framework for Shape Morphing](https://doi.org/10.1109/tvcg.2025.3591729)**. `TVCG 2025`. [project](https://chayo.oopy.io/1e7e3760-68e9-808e-b30a-f89ba08d6193) `Differentiable Simulation`
- **[DeepFracture: A Generative Approach for Predicting Brittle Fractures with Neural Discrete Representation Learning](https://nikoloside.graphics/deepfracture/)**. `CGF 2025`. `Neural Representation` `Fracture`
- **[Elastic Locomotion with Mixed Second-order Differentiation](https://doi.org/10.1145/3721238.3730685)**. `Siggraph 2025`. `Differentiable Simulation`
- **[Inverse Design of Discrete Interlocking Materials with Desired Mechanical Behavior](https://doi.org/10.1145/3721238.3730675)**. `Siggraph 2025`. [project](https://tangpengbin.github.io/publications/InverseDIM/index.html) `Differentiable Simulation`
- **[PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos](https://jianghanxiao.github.io/phystwin-web/)**. `ICCV 2025`. `Real2Sim` `3DGS`
- **[Precise Gradient Discontinuities in Neural Fields for Subspace Physics](https://doi.org/10.1145/3757377.3763810)**. `Siggraph Asia 2025`. [project](https://www.dgp.toronto.edu/projects/discont_grad) `Neural Representation`
- **[Quaffure: Real-Time Quasi-Static Neural Hair Simulation](https://doi.org/10.1109/cvpr52734.2025.00031)**. `CVPR 2025`. [project](https://tuurstuyck.github.io/quaffure/quaffure.html) `Neural Simulation` `Avatar`
- **[Self-supervised Learning of Latent Space Dynamics](https://doi.org/10.1145/3747854)**. `PACMCGIT 2025`. `Neural Representation`
- **[UniPhy: Learning a Unified Constitutive Model for Inverse Physics Simulation](https://doi.org/10.1109/cvpr52734.2025.01511)**. `CVPR 2025`. [project](https://himangim.github.io/UniPhy) `Differentiable Simulation` `Neural Material`
- **[Differentiable solver for time-dependent deformation problems with contact](https://dl.acm.org/doi/10.1145/3657648)**. `TOG 2024`. `Differentiable Simulation`
- **[DiffSound: Differentiable Modal Sound Rendering and Inverse Rendering for Diverse Inference Tasks](https://doi.org/10.1145/3641519.3657493)**. `Siggraph 2024`. [project](https://hellojxt.github.io/DiffSound/) `Differentiable Simulation` `Reconstruction`
- **[ElastoGen: 4D Generative Elastodynamics](https://arxiv.org/abs/2405.15056)**. `Arxiv 2024`.
- **[Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing](https://feature-splatting.github.io/)**. `Arxiv 2024`. `Interaction` `3DGS`
- **[Neural Modes: Self-supervised Learning of Nonlinear Modal Subspaces](https://doi.org/10.1109/cvpr52733.2024.02185)**. `CVPR 2024`. [project](https://github.com/jiahong-w/neural-modes) `Neural Representation`
- **[PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation](https://physdreamer.github.io/)**. `Arxiv 2024`.
- **[Pie-nerf: Physics-based interactive elastodynamics with nerf](https://fytalon.github.io/pienerf/)**. `CVPR 2024`. `Interaction` `NeRF`
- **[Real-time Wing Deformation Simulations for Flying Insects](https://doi.org/10.1145/3641519.3657434)**. `Siggraph 2024`. [project](https://graphics.cs.uh.edu/article/2024/2640/2024-siggraph-insectwingdeformation/)
- **[Soft Pneumatic Actuator Design using Differentiable Simulation](https://doi.org/10.1145/3641519.3657467)**. `Siggraph 2024`. [project](https://la.disneyresearch.com/publication/soft-pneumatic-actuator-design-using-differentiable-simulation) `Differentiable Simulation` `Embodied AI`
- **[VR-GS: A Physical Dynamics-Aware Interactive Gaussian Splatting System in Virtual Reality](https://yingjiang96.github.io/VR-GS/)**. `Arxiv 2024`. `Interaction` `3DGS`
- **[Beyond Chainmail: Computational Modeling of Discrete Interlocking Materials](https://doi.org/10.1145/3592112)**. `TOG 2023`.
- **[Data-Free Learning of Reduced-Order Kinematics](https://nmwsharp.com/research/neural-physics-subspaces/)**. `Siggraph 2023`.
- **[DiffVL: Scaling Up Soft Body Manipulation using Vision-Language Driven Differentiable Physics](https://arxiv.org/abs/2312.06408)**. `NeurIPS 2023`. `Differentiable Simulation`
- **[Learning Contact Deformations with General Collider Descriptors](https://dancasas.github.io/)**. `Siggraph Asia 2023`.
- **[LiCROM: Linear-Subspace Continuous Reduced Order Modeling with Neural Fields](https://arxiv.org/abs/2310.15907)**. `Siggraph Asia 2023`.
- **[Neural Metamaterial Networks for Nonlinear Material Design](https://github.com/liyuesolo/NeuralMetamaterialNetwork)**. `TOG 2023`. `Neural Material`
- **[Neural Stress Fields for Reduced-order Elastoplasticity and Fracture](https://zeshunzong.github.io/reduced-order-mpm/)**. `Siggraph Asia 2023`. `Neural Representation` `Fracture`
- **[Neuwigs: A neural dynamic model for volumetric hair capture and animation](https://ziyanw1.github.io/neuwigs/)**. `CVPR 2023`. `Neural Simulation` `Avatar`
- **[RoboNinja: Learning an Adaptive Cutting Policy for Multi-Material Objects](https://doi.org/10.15607/rss.2023.xix.046)**. `RSS 2023`. `Control` `Embodied AI`
- **[ACID: Action-Conditional Implicit Visual Dynamics for Deformable Object Manipulation](https://doi.org/10.15607/rss.2022.xviii.001)**. `RSS 2022`. `Neural Representation` `Embodied AI`
- **[Contact-centric deformation learning](http://mslab.es/projects/ContactCentricLearning/)**. `TOG 2022`.
- **[Differentiable Depth for Real2Sim Calibration of Soft Body Simulations](https://doi.org/10.1111/cgf.14720)**. `CGF 2022`. [project](https://researchprofiles.ku.dk/en/publications/differentiable-depth-for-real2sim-calibration-of-soft-body-simula) `Differentiable Simulation` `Real2Sim`
- **[Differentiable simulation of inertial musculotendons](https://dl.acm.org/doi/abs/10.1145/3550454.3555490)**. `TOG 2022`. `Differentiable Simulation`
- **[Implicit neural representation for physics-driven actuated soft bodies](https://people.inf.ethz.ch/zossg/publication/yang-2022/)**. `TOG 2022`. `Differentiable Simulation`
- **[Learning to Synthesize Volumetric Meshes from Vision-based Tactile Imprints](https://doi.org/10.1109/icra46639.2022.9812092)**. `ICRA 2022`. `Reconstruction` `Embodied AI`
- **[Neuphysics: Editable neural geometry and physics from monocular videos](https://sites.google.com/view/neuphysics/home)**. `NeurIPS 2022`. `Differentiable Simulation`
- **[RoboCraft: Learning to See, Simulate, and Shape Elasto-Plastic Objects with Graph Networks](https://doi.org/10.15607/rss.2022.xviii.008)**. `RSS 2022`. `Neural Simulation` `Embodied AI`
- **[Soft Robots Learn to Crawl: Jointly Optimizing Design and Control with Sim-to-Real Transfer](https://doi.org/10.15607/rss.2022.xviii.062)**. `RSS 2022`. `Control` `Sim2Real`
- **[Tracking Fast Trajectories with a Deformable Object using a Learned Model](https://doi.org/10.1109/icra46639.2022.9812189)**. `ICRA 2022`. [project](https://uscresl.org/publication/tracking-fast-trajectories-with-a-deformable-object-using-a-learned-model) `Neural Simulation` `Embodied AI`
- **[Virtual Elastic Objects](https://doi.org/10.1109/cvpr52688.2022.01537)**. `CVPR 2022`. [project](https://hsiaoyu.github.io/VEO) `Differentiable Simulation`
- **[A Deep Emulator for Secondary Motion of 3D Characters](https://doi.org/10.1109/cvpr46437.2021.00587)**. `CVPR 2021`. [project](https://github.com/ZhengMianlun/deep_emulator) `Neural Simulation` `Avatar`
- **[Accurately Solving Rod Dynamics with Graph Learning](http://hdl.handle.net/10754/679142)**. `NeurIPS 2021`. [project](https://computationalsciences.org/publications/shao-2021-physical-systems-graph-learning.html) `Neural Simulation`
- **[DiffAqua](https://doi.org/10.1145/3450626.3459832)**. `TOG 2021`. [project](https://diffaqua.csail.mit.edu/) `Differentiable Simulation`
- **[Differentiable simulation of soft multi-body systems](https://github.com/YilingQiao/diff_fem)**. `NeurIPS 2021`. `Differentiable Simulation`
- **[Diffpd: Differentiable projective dynamics](https://people.iiis.tsinghua.edu.cn/~taodu/)**. `TOG 2021`. `Differentiable Simulation`
- **[DiSECt: A Differentiable Simulation Engine for Autonomous Robotic Cutting](https://doi.org/10.15607/rss.2021.xvii.067)**. `RSS 2021`. [project](https://eric-heiden.com/publication/2021-disect-rss) `Differentiable Simulation` `Embodied AI`
- **[Efficient deformable shape correspondence via multiscale spectral manifold wavelets preservation](https://ieeexplore.ieee.org/document/9578652)**. `CVPR 2021`.
- **[High-order differentiable autoencoder for nonlinear model reduction](https://dl.acm.org/doi/10.1145/3450626.3459754)**. `TOG 2021`.
- **[Learning active quasistatic physics-based models from data](https://pages.cs.wisc.edu/~qisiw/SIG.html)**. `TOG 2021`. `Differentiable Simulation`
- **[Learning contact corrections for handle-based subspace dynamics](http://mslab.es/projects/LearningContactCorrections/)**. `TOG 2021`.
- **[Learning to manipulate amorphous materials](https://tml.stanford.edu/publications/2020/learning-manipulate-amorphous-materials)**. `TOG 2020`. `Reinforcement Learning`
- **[Real-time hair simulation with neural interpolation](https://www.mlchai.com/publication/lyu2020real/)**. `TVCG 2020`. `Neural Simulation` `Avatar`
- **[ChainQueen: A Real-Time Differentiable Physical Simulator for Soft Robotics](https://github.com/yuanming-hu/ChainQueen)**. `ICRA 2019`. `Differentiable Simulation`
- **[Latent-space dynamics for reduced deformable simulation](https://www.dgp.toronto.edu/projects/latent-space-dynamics/)**. `CGF 2019`.
- **[Real2Sim: visco-elastic parameter estimation from dynamic motion](https://dl.acm.org/doi/10.1145/3355089.3356548)**. `TOG 2019`. `Differentiable Simulation` `Real2Sim`
- **[SoftCon: simulation and control of soft-bodied animals with biomimetic actuators](https://mrl.snu.ac.kr/publications/ProjectSoftCon/SoftCon.html?utm_campaign=Artificial%2BIntelligence%2BWeekly&utm_medium=rss&utm_source=Artificial_Intelligence_Weekly_153)**. `TOG 2019`. `Control` `Reinforcement Learning`

<a id="rigidbody"></a>
## Rigidbody (36)

- **[Learning Object Properties Using Robot Proprioception via Differentiable Robot-Object Interaction](https://doi.org/10.1109/icra55743.2025.11127955)**. `ICRA 2025`. [project](https://warpdiffrobot.github.io/) `Differentiable Simulation` `Embodied AI`
- **[Painless Differentiable Rotation Dynamics](https://doi.org/10.1145/3730944)**. `TOG 2025`. [project](https://mslab.es/projects/Painless/) `Differentiable Simulation`
- **[Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions](https://doi.org/10.1109/cvpr52734.2025.02101)**. `CVPR 2025`. `Embodied AI`
- **[Estimating Material Properties of Interacting Objects Using Sum-GP-UCB](https://doi.org/10.1109/icra57147.2024.10610129)**. `ICRA 2024`. [project](https://myunusseker.github.io/SumGP) `Embodied AI`
- **[Jade: A Differentiable Physics Engine for Articulated Rigid Bodies with Intersection-Free Frictional Contact](https://sites.google.com/view/diffsim/)**. `ICRA 2024`. `Differentiable Simulation` `Engine`
- **[An Extensible, Data-Oriented Architecture for High-Performance, Many-World Simulation](https://madrona-engine.github.io/)**. `TOG 2023`. `Reinforcement Learning` `Engine`
- **[DefGraspNets: Grasp Planning on 3D Fields with Graph Neural Nets](https://doi.org/10.1109/icra48891.2023.10160986)**. `ICRA 2023`. [project](https://research.nvidia.com/publication/2023-05_defgraspnets-grasp-planning-3d-fields-graph-neural-nets) `Neural Simulation` `Embodied AI`
- **[Differentiable Dynamics Simulation Using Invariant Contact Mapping and Damped Contact Force](https://doi.org/10.1109/icra48891.2023.10161519)**. `ICRA 2023`. `Differentiable Simulation` `Embodied AI`
- **[DOC: Differentiable Optimal Control for Retargeting Motions onto Legged Robots](https://la.disneyresearch.com/publication/doc-differentiable-optimal-control-for-retargeting-motions-onto-legged-robots/)**. `TOG 2023`. `Control` `Embodied AI`
- **[Dynamic-Resolution Model Learning for Object Pile Manipulation](https://doi.org/10.15607/rss.2023.xix.047)**. `RSS 2023`. [project](https://github.com/WangYixuan12/dyn-res-pile-manip) `Embodied AI`
- **[Fast-Grasp'D: Dexterous Multi-finger Grasp Generation Through Differentiable Simulation](https://doi.org/10.1109/icra48891.2023.10160314)**. `ICRA 2023`. `Differentiable Simulation` `Embodied AI`
- **[Neural Collision Fields for Triangle Primitives](https://research.nvidia.com/labs/prl/publication/zesch2023ncf/)**. `Siggraph Asia 2023`. `Neural Representation`
- **[SAM-RL: Sensing-Aware Model-Based Reinforcement Learning via Differentiable Physics-Based Simulation and Rendering](https://doi.org/10.15607/rss.2023.xix.040)**. `RSS 2023`. `Differentiable Simulation` `Reinforcement Learning`
- **[Vr-handnet: A visually and physically plausible hand manipulation system in virtual reality](https://ieeexplore.ieee.org/abstract/document/10066837)**. `TVCG 2023`. `Interaction`
- **[Dojo: A Differentiable Physics Engine for Robotics](https://sites.google.com/view/dojo-sim)**. `Arxiv 2022`. `Differentiable Simulation` `Engine`
- **[Learning Object Relations with Graph Neural Networks for Target-Driven Grasping in Dense Clutter](https://doi.org/10.1109/icra46639.2022.9811601)**. `ICRA 2022`. `Embodied AI`
- **[Learning physical dynamics with subequivariant graph neural networks](https://hanjq17.github.io/SGNN/)**. `NeurIPS 2022`.
- **[Learning physics constrained dynamics using autoencoders](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6d5e035724687454549b97d6c805dc84-Abstract-Conference.html)**. `NeurIPS 2022`.
- **[Probabilistic Inference of Simulation Parameters via Parallel Differentiable Simulation](https://doi.org/10.1109/icra46639.2022.9812293)**. `ICRA 2022`. [project](https://uscresl.github.io/prob-diff-sim) `Differentiable Simulation` `Embodied AI`
- **[SAGCI-System: Towards Sample-Efficient, Generalizable, Compositional, and Incremental Robot Learning](https://doi.org/10.1109/icra46639.2022.9811859)**. `ICRA 2022`. `Differentiable Simulation` `Embodied AI`
- **[Brax - A Differentiable Physics Engine for Large Scale Rigid Body Simulation](https://github.com/google/brax)**. `NeurIPS 2021`. `Differentiable Simulation` `Engine`
- **[Efficient Differentiable Simulation of Articulated Bodies](https://github.com/YilingQiao/diffarticulated)**. `ICML 2021`. `Differentiable Simulation`
- **[Fast and Feature-Complete Differentiable Physics Engine for Articulated Rigid Bodies with Contact Constraints](https://arxiv.org/abs/2103.16021)**. `RSS 2021`. `Differentiable Simulation` `Engine`
- **[Learning to Propagate Interaction Effects for Modeling Deformable Linear Objects Dynamics](https://doi.org/10.1109/icra48506.2021.9561636)**. `ICRA 2021`. [project](https://amm.aass.oru.se/icra2021-learning-dlo) `Embodied AI`
- **[NeuralSim: Augmenting Differentiable Simulators with Neural Networks](https://doi.org/10.1109/icra48506.2021.9560935)**. `ICRA 2021`. [project](https://uscresl.org/publication/neuralsim-augmenting-differentiable-simulators-with-neural-networks) `Neural Simulation` `Sim2Real`
- **[PyBullet, a Python module for physics simulation for games, robotics and machine learning](http://pybullet.org)**. `2016--2021`. `Engine`
- **[Single-view robot pose and joint angle estimation via render & compare](https://www.di.ens.fr/willow/research/robopose/)**. `CVPR 2021`.
- **[The Role of Physics-Based Simulators in Robotics](https://doi.org/10.1146/annurev-control-072220-093055)**. `ARCRAS 2021`. `survey`
- **[ADD: analytically differentiable dynamics for multi-body systems with frictional contact](https://arxiv.org/abs/2007.00987)**. `TOG 2020`. `Differentiable Simulation`
- **[Rl-cyclegan: Reinforcement learning aware simulation-to-real](https://arxiv.org/abs/2006.09001)**. `CVPR 2020`. `Reinforcement Learning` `Sim2Real`
- **[Scalable Differentiable Physics for Learning and Control](https://github.com/YilingQiao/diffsim)**. `ICML 2020`. `Differentiable Simulation`
- **[Use the force, luke! learning to predict physical forces by simulating effects](https://ehsanik.github.io/forcecvpr2020/)**. `CVPR 2020`.
- **[Drake: Model-based design and verification for robotics](https://drake.mit.edu)**. `2019`. `Engine`
- **[Learning to fly: computational controller design for hybrid UAVs with reinforcement learning](https://people.csail.mit.edu/jiex/papers/LearningToFly/index.html)**. `TOG 2019`. `Control` `Reinforcement Learning`
- **[Shapestacks: Learning vision-based physical intuition for generalised object stacking](https://arxiv.org/abs/1804.08018)**. `ECCV 2018`.
- **[MuJoCo: A physics engine for model-based control](https://mujoco.org/)**. `IROS 2012`. `Engine`

<a id="multiphys"></a>
## Multiphys (12)

- **[Multiphysics Simulation Methods in Computer Graphics](https://doi.org/10.1111/cgf.70082)**. `CGF 2025`. [project](https://multi.physics-simulation.org/) `survey`
- **[Neural Physical Simulation with Multi-Resolution Hash Grid Encoding](https://ojs.aaai.org/index.php/AAAI/article/view/28349)**. `AAAI 2024`.
- **[A generalized constitutive model for versatile mpm simulation and inverse learning with differentiable physics](https://xuan-li.github.io/publication/su2023generalized/)**. `PACMCGIT 2023`. `Differentiable Simulation`
- **[Dynamic mesh-aware radiance fields](https://mesh-aware-rf.github.io/)**. `ICCV 2023`.
- **[Learning neural constitutive laws from motion observations for generalizable pde dynamics](https://sites.google.com/view/nclaw)**. `ICML 2023`. `Differentiable Simulation` `Neural Material`
- **[MPMNet: A data-driven MPM framework for dynamic fluid-solid interaction](https://ieeexplore.ieee.org/document/10113697)**. `TVCG 2023`.
- **[PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification](https://sites.google.com/view/PAC-NeRF)**. `ICLR 2023`. `Reconstruction` `NeRF`
- **[PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics](https://xpandora.github.io/PhysGaussian/)**. `Arxiv 2023`. `3DGS`
- **[NeuralSim: Augmenting Differentiable Simulators with Neural Networks](https://github.com/erwincoumans/tiny-differentiable-simulator)**. `ICRA 2021`.
- **[NVIDIA SimNetTM: An AI-Accelerated Multi-Physics Simulation Framework](https://arxiv.org/abs/2012.07938)**. `ICCS 2021`.
- **[Learning Mesh-Based Simulation with Graph Networks](http://arxiv.org/abs/2010.03409)**. `ICLR 2020`. [project](https://sites.google.com/view/meshgraphnets) `Neural Simulation`
- **[Learning to simulate complex physics with graph networks](https://sites.google.com/view/learning-to-simulate)**. `ICML 2020`.

<a id="survey"></a>
## Survey (4)

- **[Multiphysics Simulation Methods in Computer Graphics](https://doi.org/10.1111/cgf.70082)**. `CGF 2025`. [project](https://multi.physics-simulation.org/) `multiphys`
- **[Data-driven simulation in fluids animation: A survey](https://www.sciencedirect.com/science/article/pii/S2096579621000139)**. `VRIH 2021`. `fluid`
- **[The Role of Physics-Based Simulators in Robotics](https://doi.org/10.1146/annurev-control-072220-093055)**. `ARCRAS 2021`. `rigidbody`
- **[Machine learning for fluid mechanics](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-010719-060214)**. `ARFM 2020`. `fluid`

## Citation

If you find this repository helpful, please consider citing it!

```
@misc{wang2024awesomelist,
  title = {Awesome Neural Physics - A Curated List of Papers on AI Techniques for Physics Simulation in Computer Graphics},
  author = {Hui Wang},
  journal = {GitHub repository},
  url = {https://github.com/awesome-physics/awesome-neural-physics},
  year = {2023},
}
```
