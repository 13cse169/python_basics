from __future__ import annotations

import json
from collections import defaultdict, Counter
from typing import Dict, Any


def creation_and_access() -> None:
  print("--- creation_and_access ---")
  myDict: Dict[str, Any] = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
  }
  print("full dict:", myDict)
  print("direct access myDict['brand'] ->", myDict["brand"])
  # safe access
  print("get existing key myDict.get('model') ->", myDict.get("model"))
  print("get missing key with default myDict.get('color', 'unknown') ->", myDict.get("color", "unknown"))
  print("keys view ->", myDict.keys())
  print("values view ->", myDict.values())
  print("items view ->", myDict.items())


def set_and_update() -> None:
  print("--- set_and_update ---")
  d = {"a": 1, "b": 2}
  d["b"] = 20
  print("after d['b']=20 ->", d)
  d.update({"c": 3, "b": 200})
  print("after update ->", d)

  # setdefault: returns existing value or sets and returns default
  v = d.setdefault("d", 4)
  print("setdefault('d',4) ->", v, ", d ->", d)

  # fromkeys creates a new dict from keys with a single value
  keys = ["x", "y", "z"]
  fk = dict.fromkeys(keys, 0)
  print("fromkeys ->", fk)


def merging_and_copying() -> None:
  print("--- merging_and_copying ---")
  x = {"a": 1, "b": 2}
  y = {"b": 20, "c": 3}
  print("x ->", x)
  print("y ->", y)
  # Python 3.9+: dict union operator
  try:
    merged = x | y
    print("merged (x | y) ->", merged)
  except TypeError:
    # older Python: use {**x, **y}
    merged = {**x, **y}
    print("merged (**x, **y) ->", merged)

  # copy vs clear
  z = merged.copy()
  print("copy z ->", z)
  z.clear()
  print("after z.clear() -> z:", z, " merged still:", merged)


def looping_and_removal() -> None:
  print("--- looping_and_removal ---")
  d = {"k1": 1, "k2": 2, "k3": 3}
  for key in d:
    print("key:", key)
  for key, val in d.items():
    print("item:", key, val)

  # removal
  val = d.pop("k3")
  print("popped k3 ->", val, ", d ->", d)
  d["new"] = 99
  print("after add new ->", d)
  popped_item = d.popitem()
  print("popitem() ->", popped_item, ", d ->", d)


def nested_and_comprehensions() -> None:
  print("--- nested_and_comprehensions ---")
  myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
  }
  print("nested dict ->", myfamily)
  print("access child2 name ->", myfamily["child2"]["name"])

  # dict comprehension
  squared_numbers = {x: x * x for x in range(6)}
  print("squared_numbers ->", squared_numbers)


def defaultdict_and_counter() -> None:
  print("--- defaultdict_and_counter ---")
  words = ["apple", "banana", "apple", "pear", "banana", "apple"]
  dd = defaultdict(int)
  for w in words:
    dd[w] += 1
  print("defaultdict counts ->", dict(dd))

  cnt = Counter(words)
  print("Counter ->", cnt)


def json_conversion() -> None:
  print("--- json_conversion ---")
  d = {"a": 1, "b": 2}
  s = json.dumps(d)
  print("json dumps ->", s)
  loaded = json.loads(s)
  print("json loads ->", loaded)


def main() -> None:
  creation_and_access()
  set_and_update()
  merging_and_copying()
  looping_and_removal()
  nested_and_comprehensions()
  defaultdict_and_counter()
  json_conversion()


if __name__ == "__main__":
  main()
