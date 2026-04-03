# Awesome Neural Physics

A curated list of papers on  the seamless fusion of neural models and physics simulation. It follows the field from injecting neural capabilities into classical solvers to embedding physical simulators directly within neural architectures.

> **Best browsing experience:** use the [interactive index](https://awesome-physics.github.io/awesome-neural-physics/) for search, filtering, tag lookup, and faster navigation.

<a id="categories"></a>
## Categories

[Fluid (75)](#fluid) | [Cloth (45)](#cloth) | [Softbody (58)](#softbody) | [Rigidbody (38)](#rigidbody) | [Multiphys (15)](#multiphys) | [Survey (5)](#survey)

<a id="fluid"></a>
<details open>
<summary><strong>Fluid (75)</strong></summary>

- A Neural Particle Level Set Method for Dynamic Interface Tracking. *TOG 2025*. `Neural Representation` [project](https://cdwj.github.io/projects/neural-pls-project-page/index.html) [doi](https://doi.org/10.1145/3730399)
- A Pioneering Neural Network Method for Efficient and Robust Fuel Sloshing Simulation in Aircraft. *AAAI 2025*. [project](https://github.com/chenyu-xjtu/A-Pioneering-Neural-Network-Method-for-Efficient-and-Robust-Fuel-Sloshing-Simulation-in-Aircraft) [doi](https://doi.org/10.1609/aaai.v39i15.33752)
- AMR-Transformer: Enabling Efficient Long-range Interaction for Complex Neural Fluid Simulation. *CVPR 2025*. `Neural Simulation` [project](https://github.com/JfanLiu/AMR_Transformer) [doi](https://doi.org/10.1109/cvpr52734.2025.00545)
- An Adjoint Method for Differentiable Fluid Simulation on Flow Maps. *Siggraph Asia 2025*. `Differentiable Simulation` [project](https://pearseven.github.io/DiffFMProject/) [doi](https://doi.org/10.1145/3757377.3763903)
- Learning an Implicit Physical Model for Image-based Fluid Simulation. *ICCV 2025*. `Reconstruction` `3DGS` [project](https://physfluid.github.io/) [paper](https://arxiv.org/abs/2508.08254)
- Neural Kinematic Bases for Fluids. *Siggraph Asia 2025*. `Neural Representation` [doi](https://doi.org/10.1145/3757377.3763925)
- Representing Flow Fields with Divergence-Free Kernels for Reconstruction. *PACMCGIT 2025*. `Neural Representation` `Reconstruction` [project](https://www.physicsbasedanimation.com/2025/08/10/representing-flow-fields-with-divergence-free-kernels-for-reconstruction) [doi](https://doi.org/10.1145/3747872)
- A Real-Time and Interactive Fluid Modeling System for Mixed Reality. *TVCG 2024*. `Reconstruction` `Interaction` [project](https://github.com/cenyc/Interactive-Fluid-Modeling) [doi](https://doi.org/10.1109/tvcg.2024.3456140)
- Differentiable Voronoi Diagrams for Simulation of Cell-Based Mechanical Systems. *TOG 2024*. [paper](https://github.com/lnumerow-ethz/VoronoiCellSim)
- Dynamic ocean inverse modeling based on differentiable rendering. *CVM 2024*. [paper](https://link.springer.com/article/10.1007/s41095-023-0338-4)
- Fluid Inverse Volumetric Modeling and Applications from Surface Motion. *TVCG 2024*. [paper](https://www.computer.org/csdl/journal/tg/5555/01/10452823/1UUuVAIPShy)
- Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting. *Arxiv 2024*. `3DGS` [paper](https://amysteriouscat.github.io/GaussianSplashing/)
- Laplacian Projection Based Global Physical Prior Smoke Reconstruction. *TVCG 2024*. `Differentiable Simulation` `Reconstruction` [paper](https://www.computer.org/csdl/journal/tg/5555/01/10414126/1TZIJbrBNo4)
- Learning Reduced Fluid Dynamics. *AAAI 2024*. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/29367)
- Neural Implicit Reduced Fluid Simulation. *Siggraph Asia 2024*. `Neural Simulation` `Neural Representation` [project](https://yuanyuantao.github.io/Neural-Implicit-Reduced-Fluid-Simulation/) [doi](https://doi.org/10.1145/3680528.3687628)
- Neural Monte Carlo Fluid Simulation. *Siggraph 2024*. `Neural Representation` [project](https://github.com/Pranav-Jain/Neural-Monte-Carlo-Fluid-Simulation) [doi](https://doi.org/10.1145/3641519.3657438)
- NeuralFluid: Neural Fluidic System Design and Control with Differentiable Simulation. *NeurIPS 2024*. `Differentiable Simulation` `Control` [project](https://people.csail.mit.edu/liyifei/publication/neuralfluid/) [paper](https://papers.nips.cc/paper_files/paper/2024/hash/9a379c1b05793d1c42dc832269834515-Abstract-Conference.html)
- NeuSmoke: Efficient Smoke Reconstruction and View Synthesis with Neural Transportation Fields. *Siggraph Asia 2024*. `Reconstruction` [project](https://github.com/JiaxiongQ/NeuSmoke) [doi](https://doi.org/10.1145/3680528.3687667)
- Physics-Informed Learning of Characteristic Trajectories for Smoke Reconstruction. *Siggraph 2024*. `Reconstruction` `NeRF` [project](https://github.com/19reborn/PICT_smoke) [doi](https://doi.org/10.1145/3641519.3657483)
- Reconstruction of implicit surfaces from fluid particles using convolutional neural networks. *CGF 2024*. `Reconstruction` [project](https://www.cs.ucr.edu/~craigs/research.html) [doi](https://doi.org/10.1111/cgf.15181)
- SNN-PDE: Learning Dynamic PDEs from Data with Simplicial Neural Networks. *AAAI 2024*. `Neural Simulation` [doi](https://doi.org/10.1609/aaai.v38i10.29038)
- Symmetric Basis Convolutions for Learning Lagrangian Fluid Mechanics. *ICLR 2024*. [paper](https://github.com/tum-pbs/SFBC)
- Aquarium: A Fully Differentiable Fluid-Structure Interaction Solver for Robotics Applications. *ICRA 2023*. `Differentiable Simulation` `Embodied AI` [project](https://github.com/RoboticExplorationLab/Aquarium.jl) [doi](https://doi.org/10.1109/icra48891.2023.10161494)
- Boundary Graph Neural Networks for 3D Simulations. *AAAI 2023*. `Neural Simulation` [project](https://ml-jku.github.io/bgnn) [doi](https://doi.org/10.1609/aaai.v37i8.26092)
- DiffFR: Differentiable SPH-Based Fluid-Rigid Coupling for Rigid Body Control. *TOG 2023*. `Differentiable Simulation` `Control` [doi](https://doi.org/10.1145/3618318)
- Fast fluid simulation via dynamic multi-scale gridding. *AAAI 2023*. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/25255)
- Fluid Simulation on Neural Flow Maps. *TOG 2023*. [paper](https://yitongdeng-projects.github.io/neural_flow_maps_webpage/)
- FluidLab: A Differentiable Environment for Benchmarking Complex Fluid Manipulation. *ICLR 2023*. `Differentiable Simulation` [paper](https://fluidlab2023.github.io/)
- Inferring Hybrid Neural Fluid Fields from Videos. *NeurIPS 2023*. `Reconstruction` `Neural Representation` [project](https://kovenyu.com/hyfluid/) [paper](https://papers.nips.cc/paper_files/paper/2023/hash/00feea0d4eea58fdda7151f7e7f76c72-Abstract-Conference.html)
- Interactive design of 2D car profiles with aerodynamic feedback. *CGF 2023*. `Neural Simulation` `Neural Representation` [project](https://hal.science/hal-03975369) [doi](https://doi.org/10.1111/cgf.14772)
- Learning to Estimate Single-View Volumetric Flow Motions without 3D Supervision. *ICLR 2023*. [paper](https://ge.in.tum.de/publications/2023-franz-neuralglobtrans/)
- Learning Vortex Dynamics for Fluid Inference and Prediction. *ICLR 2023*. [paper](https://github.com/yitongdeng-projects/learning_vortex_dynamics_code)
- Neural vortex method: From finite Lagrangian particles to infinite dimensional Eulerian dynamics. *Comput. Fluids 2023*. [doi](https://doi.org/10.1016/j.compfluid.2023.105811)
- Physics-Informed Neural Corrector for Deformation-based Fluid Control. *CGF 2023*. `Control` [doi](https://doi.org/10.1111/cgf.14751)
- Solving Inverse Physics Problems with Score Matching. *NeurIPS 2023*. [paper](https://github.com/tum-pbs/SMDP)
- SurfsUp: Learning Fluid Simulation for Novel Surfaces. *ICCV 2023*. `Neural Simulation` [project](https://surfsup.cs.columbia.edu/) [doi](https://doi.org/10.1109/ICCV51070.2023.01308)
- Deep Reconstruction of 3D Smoke Densities from Artist Sketches. *CGF 2022*. [doi](https://doi.org/10.1111/cgf.14461)
- Efficient Neural Style Transfer for Volumetric Simulations. *TOG 2022*. `Style Transfer` [doi](https://doi.org/10.1145/3550454.3555517)
- Fluidic Topology Optimization with an Anisotropic Mixture Model. *TOG 2022*. `Differentiable Simulation` [project](https://people.csail.mit.edu/liyifei/publication/anisotropicstokes) [doi](https://doi.org/10.1145/3550454.3555429)
- Guaranteed conservation of momentum for learning particle-based fluid dynamics. *NeurIPS 2022*. [paper](https://github.com/tum-pbs/DMCF)
- Half-Inverse Gradients for Physical Deep Learning. *ICLR 2022*. [paper](https://arxiv.org/abs/2203.10131)
- Neurofluid: Fluid dynamics grounding with particle-driven neural radiance fields. *ICML 2022*. [paper](https://syguan96.github.io/NeuroFluid/)
- Physics informed neural fields for smoke reconstruction with sparse data. *TOG 2022*. `Reconstruction` `NeRF` [doi](https://doi.org/10.1145/3528223.3530169)
- Transformer with implicit edges for particle-based physics simulation. *ECCV 2022*. [paper](https://www.mmlab-ntu.com/project/tie/index.html)
- Versatile Control of Fluid-directed Solid Objects Using Multi-task Reinforcement Learning. *TOG 2022*. `Control` `Reinforcement Learning` [doi](https://doi.org/10.1145/3554731)
- Data-driven simulation in fluids animation: A survey. *VRIH 2021*. `survey` [paper](https://www.sciencedirect.com/science/article/pii/S2096579621000139)
- Differentiable Fluids with Solid Coupling for Learning and Control. *AAAI 2021*. `Differentiable Simulation` `Control` [doi](https://doi.org/10.1609/aaai.v35i7.16764)
- Global transport for fluid reconstruction with learned self-supervision. *CVPR 2021*. [paper](https://ge.in.tum.de/publications/)
- Learning meaningful controls for fluids. *TOG 2021*. `Control` [paper](https://rachelcmy.github.io/den2vel/)
- Model-Predictive Control of Blood Suction for Surgical Hemostasis using Differentiable Fluid Simulations. *ICRA 2021*. `Control` `Embodied AI` [project](https://ucsdarclab.com/autopublication/model-predictive-control-of-blood-suction-for-surgical-hemostasis-using-differentiable-fluid-simulations) [doi](https://doi.org/10.1109/icra48506.2021.9561624)
- Neural upflow: A scene flow learning approach to increase the apparent resolution of particle-based liquids. *PACMCGIT 2021*. [paper](https://dl.acm.org/doi/abs/10.1145/3480147)
- Predicting high-resolution turbulence details in space and time. *TOG 2021*. `Super-Resolution` [paper](https://dl.acm.org/doi/abs/10.1145/3478513.3480492)
- Two-step Temporal Interpolation Network Using Forward Advection for Efficient Smoke Simulation. *CGF 2021*. [paper](https://onlinelibrary.wiley.com/doi/10.1111/cgf.142638)
- Volumetric appearance stylization with stylizing kernel prediction network. *TOG 2021*. `Style Transfer` [doi](https://doi.org/10.1145/3450626.3459799)
- A Novel CNN-Based Poisson Solver for Fluid Simulation. *TVCG 2020*. [doi](https://doi.org/10.1109/TVCG.2018.2873375)
- Dynamic fluid surface reconstruction using deep neural network. *CVPR 2020*. `Reconstruction` [paper](https://ivlab.cse.lsu.edu/FSRN_CVPR20.html)
- Dynamic Upsampling of Smoke through Dictionary-based Learning. *TOG 2020*. `Super-Resolution` [doi](https://doi.org/10.1145/3412360)
- Interactive liquid splash modeling by user sketches. *TOG 2020*. `Interaction` [paper](https://dl.acm.org/doi/abs/10.1145/3414685.3417832)
- Lagrangian neural style transfer for fluids. *TOG 2020*. `Style Transfer` [doi](https://doi.org/10.1145/3386569.3392473)
- Latent space subdivision: stable and controllable time predictions for fluid flow. *CGF 2020*. [paper](https://ge.in.tum.de/publications/2020-lssubdiv-wiewel/)
- Learning to Control PDEs with Differentiable Physics. *ICLR 2020*. `Differentiable Simulation` `Interaction` [project](https://github.com/p-holl/PDE-Control) [doi](https://doi.org/10.48550/arxiv.2001.07457)
- Machine learning for fluid mechanics. *ARFM 2020*. `survey` [paper](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-010719-060214)
- Tomofluid: Reconstructing dynamic fluid from sparse view videos. *CVPR 2020*. `Reconstruction` [paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Zang_TomoFluid_Reconstructing_Dynamic_Fluid_From_Sparse_View_Videos_CVPR_2020_paper.html)
- A CNN-based Flow Correction Method for Fast Preview. *CGF 2019*. `Super-Resolution` [paper](http://dalab.se.sjtu.edu.cn/www/home/?page_id=763)
- Lagrangian fluid simulation with continuous convolutions. *ICLR 2019*. [paper](https://ge.in.tum.de/publications/2020-ummenhofer-iclr/)
- ScalarFlow: a large-scale volumetric data set of real-world scalar transport flows for computer animation and machine learning. *TOG 2019*. [doi](https://doi.org/10.1145/3355089.3356545)
- Transport-based neural style transfer for smoke simulations. *TOG 2019*. `Style Transfer` [doi](https://doi.org/10.1145/3355089.3356560)
- Video-guided real-to-virtual parameter transfer for viscous fluids. *TOG 2019*. [doi](https://doi.org/10.1145/3355089.3356551)
- Deep dynamical modeling and control of unsteady fluid flows. *NeurIPS 2018*. `Control` [paper](https://github.com/sisl/deep_flow_control)
- Fluid directed rigid body control using deep reinforcement learning. *TOG 2018*. `Control` `Reinforcement Learning` [doi](https://doi.org/10.1145/3197517.3201334)
- tempoGAN: A temporally coherent, volumetric GAN for super-resolution fluid flow. *TOG 2018*. `Super-Resolution` [paper](https://ge.in.tum.de/publications/tempogan/)
- Accelerating eulerian fluid simulation with convolutional networks. *ICML 2017*. [paper](https://github.com/google/FluidNet)
- Data-driven synthesis of smoke flows with CNN-based feature descriptors. *TOG 2017*. [doi](https://doi.org/10.1145/3072959.3073643)
- Data-driven projection method in fluid simulation. *CAVW 2016*. [doi](https://doi.org/10.1002/cav.1695)
- Data-driven fluid simulations using regression forests. *TOG 2015*. [doi](https://doi.org/10.1145/2816795.2818129)

</details>
<a id="cloth"></a>
<details>
<summary><strong>Cloth (45)</strong></summary>

- Dress Anyone : Automatic Physically-Based Garment Pattern Refitting 56. *PACMCGIT 2025*. `Differentiable Simulation` [project](https://igl.ethz.ch/projects/dress_anyone) [doi](https://doi.org/10.1145/3747858)
- Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics. *TOG 2025*. `Differentiable Simulation` `Reconstruction` [project](https://dress-1-to-3.github.io/) [doi](https://doi.org/10.1145/3731177)
- Frequency-Divided Learning of Fine-Grained Clothing Behavior via Flexible Dynamic Graphs. *TVCG 2025*. `Neural Simulation` `Avatar` [project](https://shirui-homepage.com/publication/2025-freq-div-TVCG) [doi](https://doi.org/10.1109/tvcg.2025.3591816)
- PICA: Physics-Integrated Clothed Avatar. *TVCG 2025*. `3DGS` `Avatar` [project](https://ustc3dv.github.io/PICA) [doi](https://doi.org/10.1109/tvcg.2025.3614642)
- Self-Supervised Humidity-Controllable Garment Simulation via Capillary Bridge Modeling. *CGF 2025*. [doi](https://doi.org/10.1111/cgf.70236)
- Bayesian Differentiable Physics for Cloth Digitalization. *CVPR 2024*. `Differentiable Simulation` [paper](https://github.com/realcrane/Bayesian-Differentiable-Physics-for-Cloth-Digitalization)
- ContourCraft: Learning to Resolve Intersections in Neural Multi-Garment Simulations. *Siggraph 2024*. `Neural Simulation` [doi](https://doi.org/10.1145/3641519.3657408)
- DiffAvatar: Simulation-Ready Garment Optimization with Differentiable Simulation. *CVPR 2024*. `Differentiable Simulation` `Avatar` [paper](https://people.csail.mit.edu/liyifei/publication/diffavatar/)
- Efficient Deformation Learning of Varied Garments with a Structure-Preserving Multilevel Framework. *PACMCGIT 2024*. `Neural Simulation` [project](https://li-tianxing.github.io/publication/psdunet) [doi](https://doi.org/10.1145/3651286)
- Estimating Cloth Simulation Parameters From Tag Information and Cusick Drape Test. *CGF 2024*. [project](https://mingry.github.io/Fabrics5k) [doi](https://doi.org/10.1111/cgf.15027)
- Garment Animation NeRF with Color Editing. *CGF 2024*. `NeRF` `Avatar` [project](https://mengzephyr.com/Garment-Animation-NeRF-With-Color-Editing) [doi](https://doi.org/10.1111/cgf.15178)
- GarmentDreamer: 3DGS Guided Garment Synthesis with Diverse Geometry and Texture Details. *Arxiv 2024*. `3DGS` [paper](https://arxiv.org/abs/2405.12420)
- Neural Garment Dynamic Super-Resolution. *Siggraph Asia 2024*. `Super-Resolution` [project](https://mengzephyr.com/Neural-Garment-Dynamic-Super-Reslution) [doi](https://doi.org/10.1145/3680528.3687610)
- Neural Garment Dynamics via Manifold-Aware Transformers. *CGF 2024*. `Neural Simulation` `Avatar` [project](https://github.com/PeizhuoLi/manifold-aware-transformers) [doi](https://doi.org/10.1111/cgf.15028)
- NeuralClothSim: Neural Deformation Fields Meet the Thin Shell Theory. *NeurIPS 2024*. `Neural Simulation` `Neural Representation` [project](https://4dqv.mpi-inf.mpg.de/NeuralClothSim/) [paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c7649eeb93d2fad0ced9a3b974260710-Abstract-Conference.html)
- Parametric Linear Blend Skinning Model for Multiple-Shape 3D Garments. *TVCG 2024*. `Avatar` [project](https://www.sysu-hcp.net/projects/cv/126.html) [doi](https://doi.org/10.1109/tvcg.2024.3478852)
- Physics-guided Shape-from-Template: Monocular Video Perception through Neural Surrogate Models. *CVPR 2024*. `Neural Simulation` `Reconstruction` [project](https://github.com/vc-bonn/Physics-guided-Shape-from-Template) [doi](https://doi.org/10.1109/cvpr52733.2024.01130)
- Real-Time Neural Cloth Deformation Using a Compact Latent Space and a Latent Vector Predictor. *ECCV 2024*. `Neural Simulation` [doi](https://doi.org/10.1007/978-3-031-92387-6_25)
- ClothCombo: Modeling Inter-Cloth Interaction for Draping Multi-Layered Clothes. *TOG 2023*. [paper](https://dl.acm.org/doi/10.1145/3618376)
- D-Cloth: Skinning-based Cloth Dynamic Prediction with a Three-stage Network. *CGF 2023*. `Neural Simulation` [paper](https://min-tang.github.io/home/DCloth/)
- Detail-Aware Deep Clothing Animations Infused with Multi-Source Attributes. *CGF 2023*. `Avatar` [paper](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14651)
- DiffXPBD: Differentiable Position-Based Simulation of Compliant Constraint Dynamics. *PACMCGIT 2023*. `Differentiable Simulation` [doi](https://doi.org/10.1145/3606923)
- Elastic Context: Encoding Elasticity for Data-driven Models of Textiles Elastic Context: Encoding Elasticity for Data-driven Models of Textiles. *ICRA 2023*. `Neural Material` `Embodied AI` [doi](https://doi.org/10.1109/icra48891.2023.10160740)
- HOOD: Hierarchical Graphs for Generalized Modelling of Clothing Dynamics. *CVPR 2023*. `Neural Simulation` [project](https://dolorousrtur.github.io/hood/?trk=public_post_comment-text) [doi](https://doi.org/10.1109/cvpr52729.2023.01627)
- How Will It Drape Like? Capturing Fabric Mechanics from Depth Images. *CGF 2023*. `Sim2Real` [project](https://carlosrodriguezpardo.es/projects/MechFromDepth) [doi](https://doi.org/10.1111/cgf.14750)
- Learning Anchor Transformations for 3D Garment Animation. *CVPR 2023*. `Avatar` [project](https://semanticdh.github.io/AnchorDEF) [doi](https://doi.org/10.1109/cvpr52729.2023.00055)
- SwinGar: Spectrum-Inspired Neural Dynamic Deformation for Free-Swinging Garments. *TVCG 2023*. [doi](https://doi.org/10.1109/tvcg.2023.3346055)
- Towards Multi-Layered 3D Garments Animation. *ICCV 2023*. [project](https://mmlab-ntu.github.io/project/layersnet) [doi](https://doi.org/10.1109/iccv51070.2023.01321)
- DiffCloth: Differentiable Cloth Simulation with Dry Frictional Contact. *TOG 2022*. `Differentiable Simulation` [doi](https://doi.org/10.1145/3527660)
- Dressing avatars: Deep photorealistic appearance for physically simulated clothing. *TOG 2022*. `Avatar` [paper](https://research.facebook.com/publications/dressing-avatars-deep-photorealistic-appearance-for-physically-simulated-clothing/)
- Learning Latent Graph Dynamics for Visual Manipulation of Deformable Objects. *ICRA 2022*. `Neural Representation` `Embodied AI` [doi](https://doi.org/10.1109/icra46639.2022.9811597)
- Learning-based bending stiffness parameter estimation by a drape tester. *TOG 2022*. [paper](https://github.com/DrapeTester/ClothDrapeTester)
- Neural cloth simulation. *TOG 2022*. [paper](https://hbertiche.github.io/NeuralClothSim/)
- Pattern-based cloth registration and sparse-view animation. *TOG 2022*. [paper](https://dl.acm.org/doi/abs/10.1145/3550454.3555448)
- Predicting loose-fitting garment deformations using bone-driven motion networks. *Siggraph 2022*. `Neural Simulation` `Avatar` [paper](http://www.cad.zju.edu.cn/home/jin/SigCloth2022/SigCloth2022.htm)
- Snug: Self-supervised neural dynamic garments. *CVPR 2022*. `Neural Simulation` `Avatar` [paper](http://mslab.es/projects/SNUG/)
- Dynamic neural garments. *TOG 2021*. `Neural Simulation` `Avatar` [doi](https://doi.org/10.1145/3478513.3480497)
- Neural Implicit Surfaces for Efficient and Accurate Collisions in Physically Based Simulations. *Arxiv 2021*. `Neural Representation` [project](https://hbertiche.github.io/NeuralColliders/) [paper](https://arxiv.org/abs/2110.01614)
- PBNS: physically based neural simulation for unsupervised garment pose space deformation. *TOG 2021*. `Neural Simulation` `Avatar` [doi](https://doi.org/10.1145/3478513.3480479)
- Self-supervised collision handling via generative 3d garment models for virtual try-on. *CVPR 2021*. [paper](http://mslab.es/projects/SelfSupervisedGarmentCollisions/)
- Cloth in the wind: A case study of physical measurement through simulation. *CVPR 2020*. [paper](https://arxiv.org/abs/2003.05065)
- Learning to measure the static friction coefficient in cloth contact. *CVPR 2020*. [paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Rasheed_Learning_to_Measure_the_Static_Friction_Coefficient_in_Cloth_Contact_CVPR_2020_paper.html)
- Projective dynamics with dry frictional contact. *TOG 2020*. [doi](https://doi.org/10.1145/3386569.3392396)
- Differentiable Cloth Simulation for Inverse Problems. *NeurIPS 2019*. `Differentiable Simulation` [paper](https://gamma.umd.edu/researchdirections/virtualtryon/differentiablecloth)
- Learning an intrinsic garment space for interactive authoring of garment animation. *TOG 2019*. `Interaction` `Avatar` [doi](https://doi.org/10.1145/3355089.3356512)

</details>
<a id="softbody"></a>
<details>
<summary><strong>Softbody (58)</strong></summary>

- Neuralocks: Real-Time Dynamic Neural Hair Simulation. *CGF 2026*. `Neural Simulation` `Avatar` [doi](https://doi.org/10.1111/cgf.70407)
- A Differentiable Material Point Method Framework for Shape Morphing. *TVCG 2025*. `Differentiable Simulation` [project](https://chayo.oopy.io/1e7e3760-68e9-808e-b30a-f89ba08d6193) [doi](https://doi.org/10.1109/tvcg.2025.3591729)
- DeepFracture: A Generative Approach for Predicting Brittle Fractures with Neural Discrete Representation Learning. *CGF 2025*. `Neural Representation` `Fracture` [doi](https://doi.org/10.1111/cgf.70002)
- Elastic Locomotion with Mixed Second-order Differentiation. *Siggraph 2025*. `Differentiable Simulation` [doi](https://doi.org/10.1145/3721238.3730685)
- Inverse Design of Discrete Interlocking Materials with Desired Mechanical Behavior. *Siggraph 2025*. `Differentiable Simulation` [project](https://tangpengbin.github.io/publications/InverseDIM/index.html) [doi](https://doi.org/10.1145/3721238.3730675)
- PhysTwin: Physics-Informed Reconstruction and Simulation of Deformable Objects from Videos. *ICCV 2025*. `Real2Sim` `3DGS` [paper](https://jianghanxiao.github.io/phystwin-web/)
- Precise Gradient Discontinuities in Neural Fields for Subspace Physics. *Siggraph Asia 2025*. `Neural Representation` [project](https://www.dgp.toronto.edu/projects/discont_grad) [doi](https://doi.org/10.1145/3757377.3763810)
- Quaffure: Real-Time Quasi-Static Neural Hair Simulation. *CVPR 2025*. `Neural Simulation` `Avatar` [project](https://tuurstuyck.github.io/quaffure/quaffure.html) [doi](https://doi.org/10.1109/cvpr52734.2025.00031)
- Self-supervised Learning of Latent Space Dynamics. *PACMCGIT 2025*. `Neural Representation` [doi](https://doi.org/10.1145/3747854)
- Shape Space Spectra. *TOG 2025*. `Neural Representation` [project](https://www.dgp.toronto.edu/projects/sss) [doi](https://doi.org/10.1145/3731148)
- UniPhy: Learning a Unified Constitutive Model for Inverse Physics Simulation. *CVPR 2025*. `Differentiable Simulation` `Neural Material` [project](https://himangim.github.io/UniPhy) [doi](https://doi.org/10.1109/cvpr52734.2025.01511)
- Differentiable solver for time-dependent deformation problems with contact. *TOG 2024*. `Differentiable Simulation` [paper](https://dl.acm.org/doi/10.1145/3657648)
- DiffSound: Differentiable Modal Sound Rendering and Inverse Rendering for Diverse Inference Tasks. *Siggraph 2024*. `Differentiable Simulation` `Reconstruction` [project](https://hellojxt.github.io/DiffSound/) [doi](https://doi.org/10.1145/3641519.3657493)
- ElastoGen: 4D Generative Elastodynamics. *Arxiv 2024*. [paper](https://arxiv.org/abs/2405.15056)
- Feature Splatting: Language-Driven Physics-Based Scene Synthesis and Editing. *Arxiv 2024*. `Interaction` `3DGS` [paper](https://feature-splatting.github.io/)
- Near-realtime Facial Animation by Deep 3D Simulation Super-Resolution. *TOG 2024*. `Avatar` `Super-Resolution` [project](https://github.com/hjoonpark/3d-sim-super-res) [doi](https://doi.org/10.1145/3670687)
- Neural Modes: Self-supervised Learning of Nonlinear Modal Subspaces. *CVPR 2024*. `Neural Representation` [project](https://github.com/jiahong-w/neural-modes) [doi](https://doi.org/10.1109/cvpr52733.2024.02185)
- PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation. *Arxiv 2024*. [paper](https://physdreamer.github.io/)
- Pie-nerf: Physics-based interactive elastodynamics with nerf. *CVPR 2024*. `Interaction` `NeRF` [paper](https://fytalon.github.io/pienerf/)
- Real-time Wing Deformation Simulations for Flying Insects. *Siggraph 2024*. [project](https://graphics.cs.uh.edu/article/2024/2640/2024-siggraph-insectwingdeformation/) [doi](https://doi.org/10.1145/3641519.3657434)
- Soft Pneumatic Actuator Design using Differentiable Simulation. *Siggraph 2024*. `Differentiable Simulation` `Embodied AI` [project](https://la.disneyresearch.com/publication/soft-pneumatic-actuator-design-using-differentiable-simulation) [doi](https://doi.org/10.1145/3641519.3657467)
- VR-GS: A Physical Dynamics-Aware Interactive Gaussian Splatting System in Virtual Reality. *Arxiv 2024*. `Interaction` `3DGS` [paper](https://yingjiang96.github.io/VR-GS/)
- Beyond Chainmail: Computational Modeling of Discrete Interlocking Materials. *TOG 2023*. [doi](https://doi.org/10.1145/3592112)
- Data-Free Learning of Reduced-Order Kinematics. *Siggraph 2023*. [paper](https://nmwsharp.com/research/neural-physics-subspaces/)
- DiffVL: Scaling Up Soft Body Manipulation using Vision-Language Driven Differentiable Physics. *NeurIPS 2023*. `Differentiable Simulation` [paper](https://arxiv.org/abs/2312.06408)
- Learning Contact Deformations with General Collider Descriptors. *Siggraph Asia 2023*. [paper](https://dancasas.github.io/)
- LiCROM: Linear-Subspace Continuous Reduced Order Modeling with Neural Fields. *Siggraph Asia 2023*. [doi](https://doi.org/10.1145/3610548.3618158)
- Neural Metamaterial Networks for Nonlinear Material Design. *TOG 2023*. `Neural Material` [doi](https://doi.org/10.1145/3618325)
- Neural Stress Fields for Reduced-order Elastoplasticity and Fracture. *Siggraph Asia 2023*. `Neural Representation` `Fracture` [paper](https://zeshunzong.github.io/reduced-order-mpm/)
- Neuwigs: A neural dynamic model for volumetric hair capture and animation. *CVPR 2023*. `Neural Simulation` `Avatar` [paper](https://ziyanw1.github.io/neuwigs/)
- RoboNinja: Learning an Adaptive Cutting Policy for Multi-Material Objects. *RSS 2023*. `Control` `Embodied AI` [doi](https://doi.org/10.15607/rss.2023.xix.046)
- ACID: Action-Conditional Implicit Visual Dynamics for Deformable Object Manipulation. *RSS 2022*. `Neural Representation` `Embodied AI` [doi](https://doi.org/10.15607/rss.2022.xviii.001)
- Contact-centric deformation learning. *TOG 2022*. [paper](http://mslab.es/projects/ContactCentricLearning/)
- Differentiable Depth for Real2Sim Calibration of Soft Body Simulations. *CGF 2022*. `Differentiable Simulation` `Real2Sim` [project](https://researchprofiles.ku.dk/en/publications/differentiable-depth-for-real2sim-calibration-of-soft-body-simula) [doi](https://doi.org/10.1111/cgf.14720)
- Differentiable simulation of inertial musculotendons. *TOG 2022*. `Differentiable Simulation` [paper](https://dl.acm.org/doi/abs/10.1145/3550454.3555490)
- Implicit neural representation for physics-driven actuated soft bodies. *TOG 2022*. `Differentiable Simulation` [paper](https://people.inf.ethz.ch/zossg/publication/yang-2022/)
- Learning to Synthesize Volumetric Meshes from Vision-based Tactile Imprints. *ICRA 2022*. `Reconstruction` `Embodied AI` [doi](https://doi.org/10.1109/icra46639.2022.9812092)
- Neuphysics: Editable neural geometry and physics from monocular videos. *NeurIPS 2022*. `Differentiable Simulation` [paper](https://sites.google.com/view/neuphysics/home)
- RoboCraft: Learning to See, Simulate, and Shape Elasto-Plastic Objects with Graph Networks. *RSS 2022*. `Neural Simulation` `Embodied AI` [doi](https://doi.org/10.15607/rss.2022.xviii.008)
- Soft Robots Learn to Crawl: Jointly Optimizing Design and Control with Sim-to-Real Transfer. *RSS 2022*. `Control` `Sim2Real` [doi](https://doi.org/10.15607/rss.2022.xviii.062)
- Tracking Fast Trajectories with a Deformable Object using a Learned Model. *ICRA 2022*. `Neural Simulation` `Embodied AI` [project](https://uscresl.org/publication/tracking-fast-trajectories-with-a-deformable-object-using-a-learned-model) [doi](https://doi.org/10.1109/icra46639.2022.9812189)
- Virtual Elastic Objects. *CVPR 2022*. `Differentiable Simulation` [project](https://hsiaoyu.github.io/VEO) [doi](https://doi.org/10.1109/cvpr52688.2022.01537)
- A Deep Emulator for Secondary Motion of 3D Characters. *CVPR 2021*. `Neural Simulation` `Avatar` [project](https://github.com/ZhengMianlun/deep_emulator) [doi](https://doi.org/10.1109/cvpr46437.2021.00587)
- Accurately Solving Rod Dynamics with Graph Learning. *NeurIPS 2021*. `Neural Simulation` [project](https://computationalsciences.org/publications/shao-2021-physical-systems-graph-learning.html) [paper](http://hdl.handle.net/10754/679142)
- DiffAqua. *TOG 2021*. `Differentiable Simulation` [project](https://diffaqua.csail.mit.edu/) [doi](https://doi.org/10.1145/3450626.3459832)
- Differentiable simulation of soft multi-body systems. *NeurIPS 2021*. `Differentiable Simulation` [paper](https://github.com/YilingQiao/diff_fem)
- Diffpd: Differentiable projective dynamics. *TOG 2021*. `Differentiable Simulation` [paper](https://people.iiis.tsinghua.edu.cn/~taodu/)
- DiSECt: A Differentiable Simulation Engine for Autonomous Robotic Cutting. *RSS 2021*. `Differentiable Simulation` `Embodied AI` [project](https://eric-heiden.com/publication/2021-disect-rss) [doi](https://doi.org/10.15607/rss.2021.xvii.067)
- Efficient deformable shape correspondence via multiscale spectral manifold wavelets preservation. *CVPR 2021*. [paper](https://ieeexplore.ieee.org/document/9578652)
- High-order differentiable autoencoder for nonlinear model reduction. *TOG 2021*. [doi](https://doi.org/10.1145/3450626.3459754)
- Learning active quasistatic physics-based models from data. *TOG 2021*. `Differentiable Simulation` [paper](https://pages.cs.wisc.edu/~qisiw/SIG.html)
- Learning contact corrections for handle-based subspace dynamics. *TOG 2021*. [paper](http://mslab.es/projects/LearningContactCorrections/)
- Learning to manipulate amorphous materials. *TOG 2020*. `Reinforcement Learning` [doi](https://doi.org/10.1145/3414685.3417868)
- Real-time hair simulation with neural interpolation. *TVCG 2020*. `Neural Simulation` `Avatar` [paper](https://www.mlchai.com/publication/lyu2020real/)
- ChainQueen: A Real-Time Differentiable Physical Simulator for Soft Robotics. *ICRA 2019*. `Differentiable Simulation` [doi](https://doi.org/10.1109/ICRA.2019.8794333)
- Latent-space dynamics for reduced deformable simulation. *CGF 2019*. [paper](https://www.dgp.toronto.edu/projects/latent-space-dynamics/)
- Real2Sim: visco-elastic parameter estimation from dynamic motion. *TOG 2019*. `Differentiable Simulation` `Real2Sim` [doi](https://doi.org/10.1145/3355089.3356548)
- SoftCon: simulation and control of soft-bodied animals with biomimetic actuators. *TOG 2019*. `Control` `Reinforcement Learning` [doi](https://doi.org/10.1145/3355089.3356497)

</details>
<a id="rigidbody"></a>
<details>
<summary><strong>Rigidbody (38)</strong></summary>

- Learning Object Properties Using Robot Proprioception via Differentiable Robot-Object Interaction. *ICRA 2025*. `Differentiable Simulation` `Embodied AI` [project](https://warpdiffrobot.github.io/) [doi](https://doi.org/10.1109/icra55743.2025.11127955)
- Newton: An Open-Source, GPU-Accelerated Physics Simulation Engine Built upon NVIDIA Warp. *2025*. `Engine` [paper](https://github.com/newton-physics/newton)
- Painless Differentiable Rotation Dynamics. *TOG 2025*. `Differentiable Simulation` [project](https://mslab.es/projects/Painless/) [doi](https://doi.org/10.1145/3730944)
- Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions. *CVPR 2025*. `Embodied AI` [doi](https://doi.org/10.1109/cvpr52734.2025.02101)
- Estimating Material Properties of Interacting Objects Using Sum-GP-UCB. *ICRA 2024*. `Embodied AI` [project](https://myunusseker.github.io/SumGP) [doi](https://doi.org/10.1109/icra57147.2024.10610129)
- Jade: A Differentiable Physics Engine for Articulated Rigid Bodies with Intersection-Free Frictional Contact. *ICRA 2024*. `Differentiable Simulation` `Engine` [paper](https://sites.google.com/view/diffsim/)
- An Extensible, Data-Oriented Architecture for High-Performance, Many-World Simulation. *TOG 2023*. `Reinforcement Learning` `Engine` [doi](https://doi.org/10.1145/3592427)
- DefGraspNets: Grasp Planning on 3D Fields with Graph Neural Nets. *ICRA 2023*. `Neural Simulation` `Embodied AI` [project](https://research.nvidia.com/publication/2023-05_defgraspnets-grasp-planning-3d-fields-graph-neural-nets) [doi](https://doi.org/10.1109/icra48891.2023.10160986)
- Differentiable Dynamics Simulation Using Invariant Contact Mapping and Damped Contact Force. *ICRA 2023*. `Differentiable Simulation` `Embodied AI` [doi](https://doi.org/10.1109/icra48891.2023.10161519)
- Differentiable Physics Simulation of Dynamics-Augmented Neural Objects. *RA-L 2023*. `Differentiable Simulation` `NeRF` [doi](https://doi.org/10.1109/LRA.2023.3257707)
- DOC: Differentiable Optimal Control for Retargeting Motions onto Legged Robots. *TOG 2023*. `Control` `Embodied AI` [doi](https://doi.org/10.1145/3592454)
- Dynamic-Resolution Model Learning for Object Pile Manipulation. *RSS 2023*. `Embodied AI` [project](https://github.com/WangYixuan12/dyn-res-pile-manip) [doi](https://doi.org/10.15607/rss.2023.xix.047)
- Fast-Grasp'D: Dexterous Multi-finger Grasp Generation Through Differentiable Simulation. *ICRA 2023*. `Differentiable Simulation` `Embodied AI` [doi](https://doi.org/10.1109/icra48891.2023.10160314)
- Neural Collision Fields for Triangle Primitives. *Siggraph Asia 2023*. `Neural Representation` [doi](https://doi.org/10.1145/3610548.3618225)
- SAM-RL: Sensing-Aware Model-Based Reinforcement Learning via Differentiable Physics-Based Simulation and Rendering. *RSS 2023*. `Differentiable Simulation` `Reinforcement Learning` [doi](https://doi.org/10.15607/rss.2023.xix.040)
- Vr-handnet: A visually and physically plausible hand manipulation system in virtual reality. *TVCG 2023*. `Interaction` [paper](https://ieeexplore.ieee.org/abstract/document/10066837)
- Dojo: A Differentiable Physics Engine for Robotics. *Arxiv 2022*. `Differentiable Simulation` `Engine` [paper](https://sites.google.com/view/dojo-sim)
- Learning Object Relations with Graph Neural Networks for Target-Driven Grasping in Dense Clutter. *ICRA 2022*. `Embodied AI` [doi](https://doi.org/10.1109/icra46639.2022.9811601)
- Learning physical dynamics with subequivariant graph neural networks. *NeurIPS 2022*. [paper](https://hanjq17.github.io/SGNN/)
- Learning physics constrained dynamics using autoencoders. *NeurIPS 2022*. [paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6d5e035724687454549b97d6c805dc84-Abstract-Conference.html)
- Probabilistic Inference of Simulation Parameters via Parallel Differentiable Simulation. *ICRA 2022*. `Differentiable Simulation` `Embodied AI` [project](https://uscresl.github.io/prob-diff-sim) [doi](https://doi.org/10.1109/icra46639.2022.9812293)
- SAGCI-System: Towards Sample-Efficient, Generalizable, Compositional, and Incremental Robot Learning. *ICRA 2022*. `Differentiable Simulation` `Embodied AI` [doi](https://doi.org/10.1109/icra46639.2022.9811859)
- Brax - A Differentiable Physics Engine for Large Scale Rigid Body Simulation. *NeurIPS 2021*. `Differentiable Simulation` `Engine` [paper](https://github.com/google/brax)
- Efficient Differentiable Simulation of Articulated Bodies. *ICML 2021*. `Differentiable Simulation` [paper](https://github.com/YilingQiao/diffarticulated)
- Fast and Feature-Complete Differentiable Physics Engine for Articulated Rigid Bodies with Contact Constraints. *RSS 2021*. `Differentiable Simulation` `Engine` [doi](https://doi.org/10.15607/RSS.2021.XVII.034)
- Learning to Propagate Interaction Effects for Modeling Deformable Linear Objects Dynamics. *ICRA 2021*. `Embodied AI` [project](https://amm.aass.oru.se/icra2021-learning-dlo) [doi](https://doi.org/10.1109/icra48506.2021.9561636)
- NeuralSim: Augmenting Differentiable Simulators with Neural Networks. *ICRA 2021*. `Neural Simulation` `Sim2Real` [project](https://uscresl.org/publication/neuralsim-augmenting-differentiable-simulators-with-neural-networks) [doi](https://doi.org/10.1109/icra48506.2021.9560935)
- PyBullet, a Python module for physics simulation for games, robotics and machine learning. *2016--2021*. `Engine` [paper](http://pybullet.org)
- Single-view robot pose and joint angle estimation via render & compare. *CVPR 2021*. [paper](https://www.di.ens.fr/willow/research/robopose/)
- The Role of Physics-Based Simulators in Robotics. *ARCRAS 2021*. `survey` [doi](https://doi.org/10.1146/annurev-control-072220-093055)
- ADD: analytically differentiable dynamics for multi-body systems with frictional contact. *TOG 2020*. `Differentiable Simulation` [doi](https://doi.org/10.1145/3414685.3417766)
- Rl-cyclegan: Reinforcement learning aware simulation-to-real. *CVPR 2020*. `Reinforcement Learning` `Sim2Real` [paper](https://arxiv.org/abs/2006.09001)
- Scalable Differentiable Physics for Learning and Control. *ICML 2020*. `Differentiable Simulation` [paper](https://github.com/YilingQiao/diffsim)
- Use the force, luke! learning to predict physical forces by simulating effects. *CVPR 2020*. [paper](https://ehsanik.github.io/forcecvpr2020/)
- Drake: Model-based design and verification for robotics. *2019*. `Engine` [paper](https://drake.mit.edu)
- Learning to fly: computational controller design for hybrid UAVs with reinforcement learning. *TOG 2019*. `Control` `Reinforcement Learning` [doi](https://doi.org/10.1145/3306346.3322940)
- Shapestacks: Learning vision-based physical intuition for generalised object stacking. *ECCV 2018*. [paper](https://arxiv.org/abs/1804.08018)
- MuJoCo: A physics engine for model-based control. *IROS 2012*. `Engine` [doi](https://doi.org/10.1109/IROS.2012.6386109)

</details>
<a id="multiphys"></a>
<details>
<summary><strong>Multiphys (15)</strong></summary>

- Multiphysics Simulation Methods in Computer Graphics. *CGF 2025*. `survey` [project](https://multi.physics-simulation.org/) [doi](https://doi.org/10.1111/cgf.70082)
- Stabilizing Reinforcement Learning in Differentiable Multiphysics Simulation. *ICLR 2025*. `Differentiable Simulation` `Reinforcement Learning` [project](https://rewarped.github.io/) [paper](https://arxiv.org/abs/2412.12089)
- Neural Physical Simulation with Multi-Resolution Hash Grid Encoding. *AAAI 2024*. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/28349)
- A generalized constitutive model for versatile mpm simulation and inverse learning with differentiable physics. *PACMCGIT 2023*. `Differentiable Simulation` [paper](https://xuan-li.github.io/publication/su2023generalized/)
- Dynamic mesh-aware radiance fields. *ICCV 2023*. [paper](https://mesh-aware-rf.github.io/)
- Learning neural constitutive laws from motion observations for generalizable pde dynamics. *ICML 2023*. `Differentiable Simulation` `Neural Material` [paper](https://sites.google.com/view/nclaw)
- MPMNet: A data-driven MPM framework for dynamic fluid-solid interaction. *TVCG 2023*. [paper](https://ieeexplore.ieee.org/document/10113697)
- PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification. *ICLR 2023*. `Reconstruction` `NeRF` [paper](https://sites.google.com/view/PAC-NeRF)
- PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics. *Arxiv 2023*. `3DGS` [paper](https://xpandora.github.io/PhysGaussian/)
- Differentiable Simulation. *Siggraph Asia 2021*. `survey` `Differentiable Simulation` [doi](https://doi.org/10.1145/3476117.3483433)
- gradSim: Differentiable Simulation for System Identification and Visuomotor Control. *ICLR 2021*. `Differentiable Simulation` `Control` [project](https://gradsim.github.io/) [paper](https://openreview.net/forum?id=c_E8kFWfhp0)
- NeuralSim: Augmenting Differentiable Simulators with Neural Networks. *ICRA 2021*. [paper](https://github.com/erwincoumans/tiny-differentiable-simulator)
- NVIDIA SimNetTM: An AI-Accelerated Multi-Physics Simulation Framework. *ICCS 2021*. [paper](https://arxiv.org/abs/2012.07938)
- Learning Mesh-Based Simulation with Graph Networks. *ICLR 2020*. `Neural Simulation` [project](https://sites.google.com/view/meshgraphnets) [doi](https://doi.org/10.48550/arxiv.2010.03409)
- Learning to simulate complex physics with graph networks. *ICML 2020*. [paper](https://sites.google.com/view/learning-to-simulate)

</details>
<a id="survey"></a>
<details>
<summary><strong>Survey (5)</strong></summary>

- Multiphysics Simulation Methods in Computer Graphics. *CGF 2025*. `multiphys` [project](https://multi.physics-simulation.org/) [doi](https://doi.org/10.1111/cgf.70082)
- Data-driven simulation in fluids animation: A survey. *VRIH 2021*. `fluid` [paper](https://www.sciencedirect.com/science/article/pii/S2096579621000139)
- Differentiable Simulation. *Siggraph Asia 2021*. `multiphys` `Differentiable Simulation` [doi](https://doi.org/10.1145/3476117.3483433)
- The Role of Physics-Based Simulators in Robotics. *ARCRAS 2021*. `rigidbody` [doi](https://doi.org/10.1146/annurev-control-072220-093055)
- Machine learning for fluid mechanics. *ARFM 2020*. `fluid` [paper](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-010719-060214)

</details>
<a id="tag-guide"></a>
<details>
<summary><strong>Tag Guide</strong></summary>

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
