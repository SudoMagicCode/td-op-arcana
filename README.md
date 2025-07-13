# TD Operator Arcana

A compendium of TouchDesigner operator examples. Pulls all examples from Op Snippets and from other TD Community Resources into a single reference.

Python translation project:

`td-op-arcana\python-translation`

**Requirements**

* Python 3.11

### Setup

Install Python `3.13`  

We'll be using a special sub directory as the location for any python virtual environment elements that TouchDesigner will use. In your terminal navigate to `td-op-arcana\python-translation`.  

Create your virtual environment:  

```pwsh
uv venv --python 3.13 
```

Activate the virtual environment

```pwsh
.venv\Scripts\activate
```

Fetch all dependencies

```base
uv pip install -r requirements.txt
```
