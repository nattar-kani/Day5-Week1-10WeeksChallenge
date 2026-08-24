import pytest 
import sys
from pathlib import Path
import argparse

sys.path.insert(0,str(Path(__file__).parent.parent/"src"))


from pyforge import analyze,clean,stats,config,version,main

@pytest.fixture
def args():
    return argparse.Namespace(file='test.py',verbose=False)

@pytest.mark.parametrize(
    "operation, expected",
    [
        (analyze,"Analyzing: test.py"),
        (clean, "Cleaning: test.py"),
        (stats, "Showing stats of test.py"),
        
    ]
        
)
def test_file_commands(operation, expected, args, capsys):
    operation(args)
    captured = capsys.readouterr()
    assert expected in captured.out

@pytest.mark.parametrize(
    "operation",
    [
        (analyze),
        (clean),
        (stats),
        (config),
        (version)
    ]
)
def test_verbose(operation,args,capsys):
    args.verbose = True
    operation(args)
    captured = capsys.readouterr()
    assert "Verbose mode enabled" in captured.out

@pytest.mark.parametrize(
    "command, expected",
    [
        (["analyze", "test.py"], "Analyzing: test.py"),
        (["clean", "test.py"], "Cleaning: test.py"),
        (["stats", "test.py"], "Showing stats of test.py"),
        (["config"], "PyForge configuration"),
        (["version"], "PyForge version 0.1.0")
    ]
)
def test_cli_commands(command,expected,monkeypatch,capsys):
    monkeypatch.setattr("sys.argv", ["pyforge"] + command)
    main()
    captured = capsys.readouterr()
    assert expected in captured.out