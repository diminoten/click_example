# Click Example Project v1.0

###Installation:
```Bash
git clone https://github.com/diminoten/click_example.git
cd click_example
virtualenv env && env/bin/activate
pip install -e .
```

###Example usage:
```Bash
(ENV)diminoten-mbpr:click_example diminoten$ click_example blah bar fleeb floob
Main argument: blah
Main option 1: None
Bar argument 1: fleeb
Bar argument 2: floob
Bar option 1: None
Main argument 1 again: blah
(ENV)diminoten-mbpr:click_example diminoten$ click_example --option-one banana blah bar fleeb floob
Main argument: blah
Main option 1: banana
Bar argument 1: fleeb
Bar argument 2: floob
Bar option 1: None
Main argument 1 again: blah
(ENV)diminoten-mbpr:click_example diminoten$ click_example --option-one banana blah bar --option-one haha fleeb floob
Main argument: blah
Main option 1: banana
Bar argument 1: fleeb
Bar argument 2: floob
Bar option 1: haha
Main argument 1 again: blah
(ENV)diminoten-mbpr:click_example diminoten$ click_example blah foo bleeb
Main argument: blah
Main option 1: None
Foo argument: bleeb
Foo option 1: Default option
```

###Open questions:
* How to print the help text for subcommands?
