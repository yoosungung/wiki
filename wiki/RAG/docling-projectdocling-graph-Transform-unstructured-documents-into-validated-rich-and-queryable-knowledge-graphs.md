---
title: "docling-projectdocling-graph Transform unstructured documents into validated, rich and queryable knowledge graphs."
related_raw: ["[[raw/docling-projectdocling-graph Transform unstructured documents into validated, rich and queryable knowledge graphs..md]]"]
tags: ['#inbox']
type: "wiki"
status: "published"
last_updated: "2026-08-23"
updated: "2026-08-23"
---

# docling-projectdocling-graph Transform unstructured documents into validated, rich and queryable knowledge graphs.

[![Docling Graph](https://github.com/docling-project/docling-graph/raw/main/docs/assets/logo.png)](https://github.com/docling-project/docling-graph)

## Docling Graph

[![Docs](https://camo.githubusercontent.com/89648943131f785f7950a481c1bd1edae64c1d1fbf64f7bd79dd2a454f5d4e9a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d6c6976652d627269676874677265656e)](https://docling-project.github.io/docling-graph/) [![PyPI version](https://camo.githubusercontent.com/eccb1b9b1a6563156c3a817d57f9f3468ed2d1759c747824772bc682dcae1627/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f646f636c696e672d67726170683f63616368655365636f6e64733d333030)](https://pypi.org/project/docling-graph/) [![Python 3.10 | 3.11 | 3.12](https://camo.githubusercontent.com/65fd04ee202ebfcda865a52f36120cc2fd8dd2b7f1fd9141cd64cb7bbfadb9e0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e3130253230253743253230332e3131253230253743253230332e31322d626c7565)](https://www.python.org/downloads/) [![uv](https://camo.githubusercontent.com/bec95721f735c7ba951b338419fcb6a4810be2f3c0fc50b2e0b322f7dcd65bc9/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f61737472616c2d73682f75762f6d61696e2f6173736574732f62616467652f76302e6a736f6e)](https://github.com/astral-sh/uv) [![Ruff](https://camo.githubusercontent.com/d6c7524504b7d886a9d34c11f44b9d31b2de1a579325b42e932744c4575a063b/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f61737472616c2d73682f727566662f6d61696e2f6173736574732f62616467652f76322e6a736f6e)](https://github.com/astral-sh/ruff) [![License MIT](https://camo.githubusercontent.com/f79d111bbde33b517af0f42a44cd4d766e2ad0e26bad8aba8d7855eafd6a6f60/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f646f636c696e672d70726f6a6563742f646f636c696e672d6772617068)](https://opensource.org/licenses/MIT) [![Pydantic v2](https://camo.githubusercontent.com/225cfe67be4e841d9763753ec947434ef7a9469f9723474322e3818d3272e333/68747470733a2f2f696d672e736869656c64732e696f2f656e64706f696e743f75726c3d68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f707964616e7469632f707964616e7469632f6d61696e2f646f63732f62616467652f76322e6a736f6e)](https://pydantic.dev/) [![NetworkX](https://camo.githubusercontent.com/ee513d2c75e623d04a0b1df39c0583e7b37dd155496dfec732ceba084eb4b77a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e6574776f726b582d332e302b2d726564)](https://networkx.org/) [![Typer](https://camo.githubusercontent.com/ad570d431426493dd969e22b4bb61ac6821fb68d685e969ce36b3a322edf76c4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54797065722d434c492d707572706c65)](https://typer.tiangolo.com/) [![Rich](https://camo.githubusercontent.com/a8712fa3d54afb909a01b280b5f10a992b38739b04516c4c5f3cb89c2b9e684c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f526963682d7465726d696e616c2d707572706c65)](https://github.com/Textualize/rich) [![vLLM](https://camo.githubusercontent.com/f95b0424fbad24b128b148a7d12756cde91122059abe67c033ca14706a2a9f47/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f764c4c4d2d636f6d70617469626c652d627269676874677265656e)](https://vllm.ai/) [![Ollama](https://camo.githubusercontent.com/246808381f2ef11fee6723deb099bd76ec71980e91ad6317d50d4777c72aa6e2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f6c6c616d612d636f6d70617469626c652d627269676874677265656e)](https://ollama.ai/) [![OpenSSF Best Practices](https://camo.githubusercontent.com/6d618d364d1b9f12dcd4c6c22e3c927a0b6ddcca01661a8a8bc1842d029436dc/68747470733a2f2f7777772e626573747072616374696365732e6465762f70726f6a656374732f31313539382f6261646765)](https://www.bestpractices.dev/projects/11598) [![LF AI & Data](https://camo.githubusercontent.com/45367c8427d91508a8d1d0ab00ef3ce951e04cd64366153b130d09e32e5d92af/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c462532304149253230253236253230446174612d3030333737383f6c6f676f3d6c696e7578666f756e646174696f6e266c6f676f436f6c6f723d66666626636f6c6f723d303039346666266c6162656c436f6c6f723d303033373738)](https://lfaidata.foundation/projects/)

Docling-Graph turns documents into validated **Pydantic** objects, then builds a **directed knowledge graph** with explicit semantic relationships.

This transformation enables high-precision use cases in **chemistry, finance, and legal** domains, where AI must capture exact entity connections (compounds and reactions, instruments and dependencies, properties and measurements) **rather than rely on approximate text embeddings**.

This toolkit supports two extraction paths: **local VLM extraction** via Docling, and **LLM-based extraction** routed through **LiteLLM** for local runtimes (vLLM, Ollama) and API providers (OpenAI, Gemini, IBM watsonx, Mistral and more), all orchestrated through a flexible, config-driven pipeline.

## Key Capabilities

- **✍🏻 Input formats:** [Docling](https://docling-project.github.io/docling/usage/supported_formats/) ’s supported inputs: PDF, images, DocLang, markdown, Office and more.
- **🧠 Extraction:** [LLM](https://docling-project.github.io/docling-graph/fundamentals/pipeline-configuration/backend-selection/) or [VLM](https://docling-project.github.io/docling-graph/fundamentals/pipeline-configuration/backend-selection/) backends, with [chunking](https://docling-project.github.io/docling-graph/fundamentals/extraction-process/chunking-strategies/) and [processing modes](https://docling-project.github.io/docling-graph/fundamentals/pipeline-configuration/processing-modes/).
- **💎 Graphs:** Pydantic to [NetworkX](https://docling-project.github.io/docling-graph/fundamentals/graph-management/graph-conversion/) directed graphs with stable IDs, edge and [provenance](https://docling-project.github.io/docling-graph/fundamentals/graph-management/provenance/) metadata.
- **📦 Export:** [CSV](https://docling-project.github.io/docling-graph/fundamentals/graph-management/export-formats/#csv-export), [Cypher](https://docling-project.github.io/docling-graph/fundamentals/graph-management/export-formats/#cypher-export), and other KG-friendly formats.
- **🔍 Visualization:** [Interactive HTML](https://docling-project.github.io/docling-graph/fundamentals/graph-management/visualization/) and Markdown reports.
- **🐛 Trace capture:** [Debug exports](https://docling-project.github.io/docling-graph/usage/advanced/trace-data-debugging/) for extraction and fallback diagnostics.

### Latest Changes

- **🔗 Graph fusion:** [Merge](https://docling-project.github.io/docling-graph/usage/cli/merge-command/) multiple knowledge graphs into one. Fully audited, deterministic, and no LLM calls.
- **🧩 Template generation:** [Generate](https://docling-project.github.io/docling-graph/usage/cli/template-command/) Pydantic templates from example documents or ontologies (OWL/RDFS...).
- **🦆 DocLang support:** Parse `.dclg` /`.dclx` inputs, and [optionally serialize](https://docling-project.github.io/docling-graph/fundamentals/extraction-process/document-conversion/#llm-input-serialization) document as [DocLang](https://github.com/doclang-project/doclang) for the LLM.
- **📍 Data grounding:** Deterministic [provenance](https://docling-project.github.io/docling-graph/fundamentals/graph-management/provenance/) ledger with bounding-box geometry and no extra LLM calls.
- **✨ Dense extraction:** Advanced [skeleton-then-flesh](https://docling-project.github.io/docling-graph/fundamentals/extraction-process/dense-extraction/) extraction mode for complex documents.
- **🚀 Docling Serve support:** Offload [document conversion](https://docling-project.github.io/docling-graph/fundamentals/pipeline-configuration/docling-serve/) to a remote [docling-serve](https://github.com/docling-project/docling-serve) instance.

## Quick Start

### Requirements

- Python 3.10 or higher

### Installation

```
pip install docling-graph
```

This installs the core package with LiteLLM for remote and local LLM providers.

VLM backend support requires the `vlm` extra:

```
pip install "docling-graph[vlm]
```

For detailed installation instructions (including optional extras and GPU setup), see [Installation Guide](https://docling-project.github.io/docling-graph/fundamentals/installation/).

### API Key Setup (Remote Inference)

Copy [`.env.example`](https://github.com/docling-project/docling-graph/blob/main/.env.example) to `.env` and fill in the values for the provider(s) you use:

```
cp .env.example .env
```

See [API Keys Setup](https://docling-project.github.io/docling-graph/fundamentals/installation/api-keys/) for provider-specific instructions (including Amazon Bedrock's AWS credential chain).

### Basic Usage

#### CLI

```
# Initialize configuration
docling-graph init

# Convert document from URL (each line except the last must end with \)
docling-graph convert "https://arxiv.org/pdf/2207.02720" \
    --template "docs.examples.templates.rheology_research.ScholarlyRheologyPaper" \
    --processing-mode "many-to-one" \
    --extraction-contract "dense" \
    --debug

# Visualize results
docling-graph inspect outputs
```

#### Python API - Default Behavior

```
from docling_graph import run_pipeline, PipelineContext
from docs.examples.templates.rheology_research import ScholarlyRheologyPaper

# Create configuration
config = {
    "source": "https://arxiv.org/pdf/2207.02720",
    "template": ScholarlyRheologyPaper,
    "backend": "llm",
    "inference": "remote",
    "processing_mode": "many-to-one",
    "extraction_contract": "auto",
    "provider_override": "mistral",
    "model_override": "mistral-medium-latest",
    "structured_output": True,  # default
    "use_chunking": True,
}

# Run pipeline - returns data directly, no files written to disk
context: PipelineContext = run_pipeline(config)

# Access results
graph = context.knowledge_graph
models = context.extracted_models
metadata = context.graph_metadata

print(f"Extracted {len(models)} model(s)")
print(f"Graph: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges")
```

Every node above also carries a deterministic `__provenance__` attribute by default (`provenance="standard"`), pointing back to the source chunk and page it was extracted from — no extra LLM calls involved. See [Data Grounding & Provenance](https://docling-project.github.io/docling-graph/fundamentals/graph-management/provenance/).

For debugging, use `--debug` with the CLI to save intermediate artifacts to disk; see [Trace Data & Debugging](https://docling-project.github.io/docling-graph/usage/advanced/trace-data-debugging/). For more examples, see [Examples](https://docling-project.github.io/docling-graph/usage/examples/).

## Pydantic Templates

Templates define both the **extraction schema** and the resulting **graph structure**.

```
from pydantic import BaseModel, Field
from docling_graph.utils import edge

class Person(BaseModel):
    """Person entity with stable ID."""
    model_config = {
        'is_entity': True,
        'graph_id_fields': ['last_name', 'date_of_birth']
    }
    
    first_name: str = Field(description="Person's first name")
    last_name: str = Field(description="Person's last name")
    date_of_birth: str = Field(description="Date of birth (YYYY-MM-DD)")

class Organization(BaseModel):
    """Organization entity."""
    model_config = {'is_entity': True}
    
    name: str = Field(description="Organization name")
    employees: list[Person] = edge("EMPLOYS", description="List of employees")
```

### Generating a template from documents

Instead of writing the template by hand, you can induce one from a few example documents:

```
docling-graph template from-docs invoice1.pdf invoice2.pdf \
    --output templates/invoices.py \
    --name InvoiceDocument \
    --trial-run
```

The documents are converted with Docling, then LLM passes propose classes, fields, and relationships **as structured data** — a deterministic renderer turns that into the Python module, so no LLM ever writes code. Candidates are filtered by deterministic gates (every identity example must appear verbatim in the source) and merged across documents. `--trial-run` then runs a real extraction on the first document and prints an advisory quality report.

Each generator also writes an editable SPEC YAML next to the template (`templates/invoices.spec.yaml`). Rename an edge or flip an entity to a component with a one-line YAML edit and re-render, rather than hand-patching generated code:

```
docling-graph template from-spec templates/invoices.spec.yaml -o templates/invoices.py
```

Templates can also be compiled from an existing ontology — OWL/RDFS/SKOS, LinkML, or JSON Schema — with no LLM involved at all (needs the `templategen` extra: `pip install 'docling-graph[templategen]'`). Any template, generated or hand-written, can be checked against the rulebook:

```
docling-graph template from-ontology schema.ttl --root ex:InsurancePolicy -o templates/policy.py
docling-graph template lint templates.invoices.InvoiceDocument
```

For complete guidance, see:

- [template Command](https://docling-project.github.io/docling-graph/usage/cli/template-command/) — generating, linting, and evaluating templates
- [Schema Definition Guide](https://docling-project.github.io/docling-graph/fundamentals/schema-definition/)
- [Template Basics](https://docling-project.github.io/docling-graph/fundamentals/schema-definition/template-basics/)
- [Example Templates](https://github.com/docling-project/docling-graph/blob/main/docs/examples/README.md)

## Documentation

Comprehensive documentation can be found on [Docling Graph's Page](https://docling-project.github.io/docling-graph/).

### Documentation Structure

The documentation follows the docling-graph pipeline stages:

1. [Introduction](https://docling-project.github.io/docling-graph/introduction/) - Overview and core concepts
2. [Installation](https://docling-project.github.io/docling-graph/fundamentals/installation/) - Setup and environment configuration
3. [Schema Definition](https://docling-project.github.io/docling-graph/fundamentals/schema-definition/) - Creating Pydantic templates
4. [Pipeline Configuration](https://docling-project.github.io/docling-graph/fundamentals/pipeline-configuration/) - Configuring the extraction pipeline
5. [Extraction Process](https://docling-project.github.io/docling-graph/fundamentals/extraction-process/) - Document conversion and extraction
6. [Graph Management](https://docling-project.github.io/docling-graph/fundamentals/graph-management/) - Converting, grounding, exporting, and visualizing graphs
7. [CLI Reference](https://docling-project.github.io/docling-graph/usage/cli/) - Command-line interface guide
8. [Python API](https://docling-project.github.io/docling-graph/usage/api/) - Programmatic usage
9. [Examples](https://docling-project.github.io/docling-graph/usage/examples/) - Working code examples
10. [Advanced Topics](https://docling-project.github.io/docling-graph/usage/advanced/) - Performance, testing, error handling
11. [API Reference](https://docling-project.github.io/docling-graph/reference/) - Detailed API documentation
12. [Community](https://docling-project.github.io/docling-graph/community/) - Contributing and development guide

## Contributing

We welcome contributions! Please see:

- [Contributing Guidelines](https://github.com/docling-project/docling-graph/blob/main/.github/CONTRIBUTING.md) - How to contribute
- [Development Guide](https://docling-project.github.io/docling-graph/community/) - Development setup

### Development Setup

```
# Clone and setup
git clone https://github.com/docling-project/docling-graph
cd docling-graph

# Install with dev dependencies
uv sync --extra dev

# Run Execute pre-commit checks
uv run pre-commit run --all-files
```

## License

MIT License - see [LICENSE](https://github.com/docling-project/docling-graph/blob/main/LICENSE) for details.

## Acknowledgments

Docling Graph builds on outstanding open-source projects:

- [Docling](https://github.com/docling-project/docling) - document conversion and VLM extraction
- [Pydantic](https://pydantic.dev/) - schema definition and validation
- [NetworkX](https://networkx.org/) - graph construction and analysis
- [LiteLLM](https://github.com/BerriAI/litellm) - unified LLM provider interface
- [Cytoscape](https://js.cytoscape.org/) - interactive graph visualization

---
- **Source:** Unknown
