# 🚀 AutoHF

**One-line AutoML: from idea to trained model using Hugging Face + AutoGluon.**

AutoHF is an autonomous machine learning pipeline that takes a natural language description of a task (e.g., "sentiment analysis") and automatically finds the best datasets on Hugging Face, ranks them by quality, and trains a state-of-the-art model using AutoGluon.

---

## ✨ Features

- **🔍 Intent-to-Task:** Automatically detects ML task types (classification, regression, etc.) and keywords from natural language.
- **📦 Autonomous Dataset Discovery:** Searches the Hugging Face Hub for relevant datasets using multi-strategy search.
- **🏆 Intelligent Ranking:** Ranks datasets based on quality signals like downloads, likes, and metadata completeness.
- **🏋️ Automated Training:** Leverages AutoGluon to train high-quality models with minimal configuration.
- **🧬 Agentic Architecture:** Inspired by patterns from **AutoGen**, **LangGraph**, and **OpenHands** for robust state management and collaboration.

---

## 🛠️ Internal Workflow

The following diagram shows how AutoHF orchestrates the pipeline from user input to a trained model:

```mermaid
graph TD
    User([User Input: 'sentiment analysis']) --> CLI[CLI / Python API]
    CLI --> Orchestrator[AutoHF Orchestrator]
    
    subgraph "Autonomous Pipeline (LangGraph-inspired States)"
        Orchestrator --> State1[Detecting Task]
        State1 --> TaskAgent[TaskAgent: Detects task type & keywords]
        
        TaskAgent --> State2[Searching Datasets]
        State2 --> DatasetAgent[DatasetAgent: Searches HF Hub]
        
        DatasetAgent --> State3[Ranking Datasets]
        State3 --> Ranker[DatasetRanker: Ranks by quality signals]
        
        Ranker --> State4[Loading & Profiling]
        State4 --> Loader[DatasetAgent: Loads best candidate & profiles]
        
        Loader --> State5[Training]
        State5 --> Trainer[AutoGluonTrainer: Trains & Optimizes]
    end
    
    Trainer --> State6[Completed]
    State6 --> Result[TrainResult: Model + Metrics]
    Result --> User
```

## 🏗️ Project Structure

The following diagram illustrates the static architecture and relationship between modules:

```mermaid
classDiagram
    class CLI {
        +main()
        +train(task)
        +search(task)
    }
    
    class AutoHF {
        -config: AutoHFConfig
        -task_agent: TaskAgent
        -dataset_agent: DatasetAgent
        +train(task_description)
        +search(task_description)
    }
    
    class TaskAgent {
        +detect_task(description)
    }
    
    class DatasetAgent {
        +search(task_type, keywords)
        +load(dataset_id)
    }
    
    class DatasetRanker {
        +rank_datasets(candidates)
    }
    
    class AutoGluonTrainer {
        +train_model(df, config)
    }
    
    class AutoHFConfig {
        +preset: str
        +time_limit: int
        +max_rows: int
    }

    CLI --> AutoHF : Uses
    AutoHF --> AutoHFConfig : Configures
    AutoHF --> TaskAgent : Orchestrates
    AutoHF --> DatasetAgent : Orchestrates
    AutoHF --> DatasetRanker : Uses
    AutoHF --> AutoGluonTrainer : Triggers
```

---

## 🚀 Quick Start

### Installation

```bash
# Basic installation
pip install autohf

# With training support (recommended)
pip install "autohf[train]"
```

### CLI Usage

Train a model with a single command:

```bash
# Quick prototype
autohf train "sentiment analysis"

# Higher quality training
autohf train "spam detection" --preset high_quality

# Just search for datasets
autohf search "question answering" --models
```

### Python API

```python
from autohf import AutoHF

# Initialize and train
hf = AutoHF.from_preset("medium_quality")
result = hf.train("customer review classification")

# Access results
print(f"Best model: {result.best_model_name}")
print(f"Accuracy: {result.metrics['accuracy']}")
print(f"Model saved at: {result.model_path}")
```

---

## 📋 Presets

AutoHF provides several presets inspired by AutoGluon to balance speed and quality:

| Preset | Time Limit | Focus |
| :--- | :--- | :--- |
| `quick_prototype` | 60s | Fast iteration, small datasets |
| `medium_quality` | 300s | **Default** - Good balance of speed/quality |
| `high_quality` | 600s | Better results, longer training |
| `best_quality` | 3600s | Maximum performance |
| `optimize_for_deployment` | 300s | Small model size, fast inference |

---

## 🏗️ Architecture & Patterns

AutoHF is built using modern software engineering patterns for AI:

- **State Management:** Uses a typed state machine (via `PipelineState`) inspired by **LangGraph** to track progress and handle transitions.
- **Agent Collaboration:** Employs specialized agents (**TaskAgent**, **DatasetAgent**) similar to **AutoGen** to separate concerns.
- **Autonomous Execution:** Implements retry logic and multi-strategy discovery patterns found in **OpenHands**.
- **Tabular Power:** Uses **AutoGluon** as the underlying engine for robust, automated model selection and hyperparameter tuning.

---

## 🗺️ Project Roadmap

Here is the planned development roadmap for AutoHF. Contributions and suggestions are welcome!

### Phase 1: Core Pipeline (Completed / In Progress)
- [x] Intent-to-Task detection with keyword extraction
- [x] Autonomous Hugging Face dataset search with multi-strategy discovery
- [x] Intelligent dataset ranking (downloads, likes, metadata)
- [x] AutoGluon-based automated training integration
- [x] CLI and Python API entry points
- [x] Configuration presets (quick/medium/high/best quality)
- [x] Agentic architecture with TaskAgent, DatasetAgent, and DatasetRanker

### Phase 2: Enhanced Model Hub
- [ ] Support for custom model fine-tuning (beyond AutoGluon tabular models)
- [ ] Integration with Hugging Face Model Hub for downloading pre-trained models
- [ ] Multi-modal support (image, audio, text classification)
- [ ] Model versioning and experiment tracking

### Phase 3: Advanced Dataset Management
- [ ] Dataset quality validation (missing values, class imbalance detection)
- [ ] Automatic dataset cleaning and preprocessing recommendations
- [ ] Train/validation/test split optimization
- [ ] Dataset caching and local mirror support

### Phase 4: Deployment & Serving
- [ ] Model export to ONNX, TorchScript, and CoreML formats
- [ ] REST API serving with FastAPI
- [ ] Docker containerization for easy deployment
- [ ] Batch prediction pipelines

### Phase 5: Observability & Collaboration
- [ ] Training metrics dashboard
- [ ] Pipeline execution logs and audit trails
- [ ] Team collaboration features (shared datasets, model registry)
- [ ] CI/CD integration for model retraining

### Phase 6: Enterprise Features
- [ ] Private Hugging Face Hub / AWS S3 / Azure Blob Storage support
- [ ] Role-based access control (RBAC)
- [ ] Scalable distributed training support
- [ ] Compliance and governance tooling

---

## 📜 License

MIT License. See `LICENSE` for details.
