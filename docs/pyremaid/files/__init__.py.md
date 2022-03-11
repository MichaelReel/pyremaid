# ./src/pyremaid/files/__init__.py

### Imports


---
```mermaid
flowchart TB
  _f81_n373["If"]
  _f81_n374["not os.path.isdir(output_path)"]
  _f81_n375["Expr"]
  _f81_n376["os.makedirs(output_path)"]
  _f82_n377["Expr"]
  _f82_n378["create_output_folder(output_path=output_path)"]
  _f82_l83["(root, dirs, files)"]
  _f82_l83_l84_n379["Expr"]
  _f82_l83_l84_n380["os.remove(os.path.join(root, name))"]
  _f82_l83_l85["name"]
  _f82_l83_l85_n381["Expr"]
  _f82_l83_l85_n382["os.rmdir(os.path.join(root, name))"]
  _f82_l83_l84["name"]
  _f87_n384["If"]
  _f87_n385["not os.path.isdir(os.path.dirname(output_file))"]
  _f87_n386["Expr"]
  _f87_n387["os.makedirs(os.path.dirname(output_file))"]
  _f87_n388["With"]
  _f87_n389["withitem"]
  _f87_n390["open(output_file, 'w')"]
  _f87_n391["Name"]
  _f87_n392["Store"]
  _f87_n393["Expr"]
  _f87_n394["md_file.write(content)"]

  subgraph _create_output_folder
    direction TB
    _f81_n373 --> _f81_n374
    _f81_n374 --> _f81_n375
    _f81_n375 --> _f81_n376
  end
  subgraph _create_cleared_output_folder
    direction TB
    _f82_n377 --> _f82_n378
    _f82_n378 --> _f82_l83
    %% loop (root, dirs, files)
      %% loop name
        _f82_l83_l84_n379 --> _f82_l83_l84_n380
      %% end name
      _f82_l83_l84_n380 --> _f82_l83_l84_n379
      _f82_l83_l84_n379 --> _f82_l83_l85
      %% loop name
        _f82_l83_l85_n381 --> _f82_l83_l85_n382
      %% end name
      _f82_l83_l85_n382 --> _f82_l83_l85_n381
    %% end (root, dirs, files)
    _f82_l83_l85_n381 --> _f82_l83_l84
  end
  subgraph _get_output_file_path_for_input_file
    direction TB
  end
  subgraph _update_output_file
    direction TB
    _f87_n384 --> _f87_n385
    _f87_n385 --> _f87_n386
    _f87_n386 --> _f87_n387
    _f87_n387 --> _f87_n388
    _f87_n388 --> _f87_n389
    _f87_n389 --> _f87_n390
    _f87_n390 --> _f87_n391
    _f87_n391 --> _f87_n392
    _f87_n392 --> _f87_n393
    _f87_n393 --> _f87_n394
  end

```
---

<details>
<summary>Debug AST model dump</summary>

```

```
</details>

