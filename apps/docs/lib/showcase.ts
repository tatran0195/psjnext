import { Activity, Cog, Cpu, FileText, Layers, TrendingUp, Zap } from 'lucide-react';

export interface Solution {
    id: string;
    code: string;
    category: 'Fatigue' | 'AI' | 'Automation' | 'Reporting' | 'CFD' | 'Optimization';
    industry: string[];
    title: string;
    shortDesc: string;
    fullDesc: string;
    image: string;
    capabilities: string[];
    deliverables: string[];
    software: string[];
    duration: string;
    complexity: 'Standard' | 'Advanced' | 'Enterprise';
}

export const categoryConfig = {
    All: { color: '#0047AB', icon: Layers },
    Fatigue: { color: '#D4570D', icon: Activity },
    AI: { color: '#5B3BB8', icon: Cpu },
    Automation: { color: '#0047AB', icon: Cog },
    Reporting: { color: '#00875A', icon: FileText },
    CFD: { color: '#0099CC', icon: Zap },
    Optimization: { color: '#B86E00', icon: TrendingUp },
};

export const industries = [
    'All Industries',
    'Automotive',
    'Aerospace',
    'Marine',
    'Energy',
    'Materials',
    'Heavy Machinery',
    'Manufacturing',
    'Research',
];

export const solutions: Solution[] = [
    {
        id: '01',
        code: 'PSJ-FAT-001',
        category: 'Fatigue',
        industry: ['Automotive', 'Heavy Machinery'],
        title: 'Shaft Fatigue Modeling Service',
        shortDesc: 'Excel-driven shaft parameter automation with full fatigue analysis pipeline.',
        fullDesc:
            'Custom Excel-based input system that automatically collects shaft geometry parameters and operating conditions. The system integrates with Jupiter and SunShine solvers to perform comprehensive fatigue lifecycle analysis with automated reporting.',
        image: '/showcase/fatigue.jpg',
        capabilities: [
            'Parametric geometry generation',
            'Multi-axial fatigue analysis',
            'S-N curve evaluation',
            'Damage accumulation',
        ],
        deliverables: [
            'Excel workbook',
            'Python automation scripts',
            'PDF/PPT reports',
            'Training materials',
        ],
        software: ['Jupiter', 'SunShine', 'MS Excel'],
        duration: '4-6 weeks',
        complexity: 'Standard',
    },
    {
        id: '02',
        code: 'PSJ-MBD-002',
        category: 'Fatigue',
        industry: ['Automotive'],
        title: 'Exhaust System MBD Automation',
        shortDesc: 'End-to-end multi-body dynamics fatigue analysis for exhaust systems.',
        fullDesc:
            'Complete automation pipeline from thermal stress analysis through modal decomposition and RFI (Random Frequency Input) analysis for exhaust system durability assessment.',
        image: '/images/workflow-dark.jpg',
        capabilities: [
            'Thermal stress mapping',
            'Modal analysis',
            'RFI evaluation',
            'Lifecycle prediction',
        ],
        deliverables: ['Automation framework', 'Analysis templates', 'Validation reports'],
        software: ['Jupiter', 'PSJ', 'SunShine'],
        duration: '6-8 weeks',
        complexity: 'Advanced',
    },
    {
        id: '03',
        code: 'PSJ-RPT-003',
        category: 'Reporting',
        industry: ['All Industries'],
        title: 'Automated PowerPoint Reporting',
        shortDesc: 'One-click export of analysis results to professional PowerPoint reports.',
        fullDesc:
            'Custom reporting system that automatically generates branded PowerPoint presentations including 3D visualizations, stress contour plots, animations, and quantitative result tables.',
        image: '/images/product-ui.jpg',
        capabilities: [
            'Template-driven reports',
            '3D visualization export',
            'Chart generation',
            'Multi-language support',
        ],
        deliverables: ['PPT templates', 'Python report engine', 'Documentation'],
        software: ['PSJ', 'MS PowerPoint'],
        duration: '3-4 weeks',
        complexity: 'Standard',
    },
    {
        id: '04',
        code: 'PSJ-AI-004',
        category: 'AI',
        industry: ['Marine', 'Aerospace'],
        title: 'AI-Powered Smart Dialog System',
        shortDesc: 'Machine learning system that predicts and pre-fills analysis parameters.',
        fullDesc:
            'Intelligent dialog system that learns from user operations and automatically populates parameters based on historical workflows. Reduces operation time by up to 60% for repetitive analysis tasks.',
        image: '/images/gui-builder.jpg',
        capabilities: [
            'Pattern recognition',
            'Parameter prediction',
            'User behavior learning',
            'Adaptive UI',
        ],
        deliverables: ['ML model', 'Integration plugin', 'Training dataset'],
        software: ['PSJ', 'Python ML stack'],
        duration: '8-12 weeks',
        complexity: 'Enterprise',
    },
    {
        id: '05',
        code: 'PSJ-AI-005',
        category: 'AI',
        industry: ['Marine'],
        title: 'Generative Ship Hull Design',
        shortDesc: 'Parametric morphing engine for AI training dataset generation.',
        fullDesc:
            'Automated ship hull variant generator that produces thousands of geometric variations for training neural networks in hydrodynamic prediction and design optimization.',
        image: '/showcase/ai-ship.jpg',
        capabilities: [
            'Parametric morphing',
            'Batch generation',
            'Quality validation',
            'Dataset curation',
        ],
        deliverables: ['Generation pipeline', 'Validated dataset', 'Quality metrics'],
        software: ['PSJ', 'Jupiter'],
        duration: '6-10 weeks',
        complexity: 'Advanced',
    },
    {
        id: '06',
        code: 'PSJ-AUT-006',
        category: 'Automation',
        industry: ['Materials', 'Research'],
        title: 'Voronoi Microstructure Generation',
        shortDesc: 'Automated polycrystalline microstructure modeling for metal analysis.',
        fullDesc:
            'Production-grade Voronoi tessellation engine for generating realistic metal microstructures. Used for crystal plasticity simulations and grain-level material behavior studies.',
        image: '/images/cae-model.jpg',
        capabilities: [
            'Voronoi tessellation',
            'Grain boundary modeling',
            'Crystal orientation',
            'Multi-scale coupling',
        ],
        deliverables: ['Generation tools', 'Mesh templates', 'Validation cases'],
        software: ['PSJ', 'Jupiter'],
        duration: '5-7 weeks',
        complexity: 'Advanced',
    },
    {
        id: '07',
        code: 'PSJ-CFD-007',
        category: 'CFD',
        industry: ['Energy', 'Manufacturing'],
        title: 'SunShine + OpenFOAM Coupling',
        shortDesc: 'Multi-physics coupling between thermal solver and CFD analysis.',
        fullDesc:
            'Bidirectional coupling system between OpenFOAM CFD solver and SunShine for iterative heat-flow and structural analysis until convergence. Enables true multi-physics simulations.',
        image: '/images/cae-analysis.jpg',
        capabilities: [
            'Solver coupling',
            'Iterative convergence',
            'Data interpolation',
            'Convergence monitoring',
        ],
        deliverables: ['Coupling interface', 'Workflow templates', 'Convergence tools'],
        software: ['OpenFOAM', 'SunShine', 'PSJ'],
        duration: '10-14 weeks',
        complexity: 'Enterprise',
    },
    {
        id: '08',
        code: 'PSJ-CFD-008',
        category: 'CFD',
        industry: ['Energy'],
        title: 'OpenFOAM Block Mesh Generation',
        shortDesc: 'Specialized structured mesh generation for high-fidelity CFD.',
        fullDesc:
            'Custom block mesh generator using OpenFOAM utilities for creating high-quality structured meshes optimized for specific CFD analysis requirements.',
        image: '/images/hero-mesh.jpg',
        capabilities: [
            'Structured meshing',
            'Quality control',
            'Boundary layer refinement',
            'Domain decomposition',
            'Mesh quality metrics',
        ],
        deliverables: ['Mesh generation scripts', 'Quality reports', 'Simulation templates'],
        software: ['OpenFOAM', 'PSJ'],
        duration: '4-6 weeks',
        complexity: 'Standard',
    },
    {
        id: '09',
        code: 'PSJ-AUT-009',
        category: 'Automation',
        industry: ['All Industries'],
        title: 'Automatic FE Model Generation',
        shortDesc: 'End-to-end FE model setup including mesh, BC, and materials.',
        fullDesc:
            'Complete automation of finite element model preparation including geometry meshing, boundary condition application, material assignment, and load case definition.',
        image: '/images/psj-workspace.jpg',
        capabilities: ['Auto-meshing', 'BC application', 'Material library', 'Quality validation'],
        deliverables: ['Automation scripts', 'Material library', 'Project templates'],
        software: ['PSJ', 'Jupiter'],
        duration: '6-8 weeks',
        complexity: 'Advanced',
    },
];
