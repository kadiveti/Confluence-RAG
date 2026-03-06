# Confluence-RAG

# How to run?

### STEPS:


### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.11 -y
```

```bash
conda activate llmapp
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

> ⚠️ **Build tools required:** On Windows the `chroma-hnswlib` package
> (pulled in by `chromadb`) needs to compile a native extension. If you
> see an error like:
>
> ```
> error: Microsoft Visual C++ 14.0 or greater is required. Get it with
> "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
> ```
>
> install the Visual C++ Build Tools from the link above, or alternatively
> create the environment with Miniconda/Anaconda and install `chromadb`
> from conda-forge which provides pre‑built binaries:
>
> ```bash
> conda install -c conda-forge chromadb
> ```
>
> Removing `chroma-hnswlib` from `requirements.txt` is another option if
> you don't intend to use its HNSW index; in that case use a pure-Python
> backend such as `chromadb[sqlite]` or similar.
>
> Once the build tools are in place the normal `pip install` should
> complete successfully.
```

```bash
# Finally run the following command
python app/main.py
```