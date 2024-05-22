# attach-to-pdf
Python script to attach files in a pdf based on borb

I know this has some bugs, i've fonund these ones, which looks depend on the underlying implementation.
* Trying to attach files to PDF/A files may cause `RecursionError: maximum recursion depth exceeded while calling a Python object` errors
* Attaching files to a pdf with already attached files may result in corrupting existing files.

## Installation
Just clone this somewhere, add the root directory to path and launch the tool with `attach-to-pdf [options]`, the script will generate automatically a venv and will install the required dependencies at first run.

That's it, enjoy!

## License
This program is offered under a commercial and under the AGPL license.
AGPL licensing: This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

Please, refer to [this page](https://www.gnu.org/licenses/) fot a copy od the GNU Affeo General Public License.
