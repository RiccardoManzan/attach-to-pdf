# attach-to-pdf
Python script to attach files in a pdf based on borb

I know this has some bugs, i've fonund these ones, which looks depend on the underlying implementation.
* Trying to attach files to PDF/A files may cause `RecursionError: maximum recursion depth exceeded while calling a Python object` errors
* Attaching files to a pdf with already attached files may result in corrupting existing files.

## Installation
Just clone this somewhere, register this to the `.bashrc` or `.profile` script by using the command:

```bash
source ~/path/to/folder/index.bash
```
That's it, enjoy!

## Usage
Launch the tool with `attach-to-pdf [options]`, the script will generate automatically a venv and will install the required dependencies at first run.

See cmd help for details regarding the options.

## License
See the [LICENSE file](./LICENSE)
