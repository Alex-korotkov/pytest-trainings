import pytest
from hello_world import hello

def test_hello_world(capsys, monkeypatch, tmp_path): 
   monkeypatch.chdir(tmp_path)
   hello()
   with capsys.disabled():    
      print(tmp_path)
      with open("hello.txt") as f:
         out = f.readline()
   assert out == "Hello World!\n"
