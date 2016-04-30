# Cloud Control Assessment Framework
An extensible framework for performing and reporting on automated end user control tests of Cloud IaaS platforms.


## Installation

Clone repository: `git clone https://github.com/wjwoodson/cloud-control-assessment-framework.git`

Initialize database: `./database-setup.sh`

### Requirements
- Python 2.7
-  bottle (packaged)
-  sqlalchemy
-  jinja2
- sqlite3

## Usage

Run the application: `python ccaf.py`

Browse to `http://localhost:8300/`

### Assessment Frameworks

### Providers 

### Control Tests

### Running an Assessment

#### Reporting


## API

### Control Tests

#### Custom Modules
Custom modules for performing Control Tests against a given Provider can be added in the `modules` directory. These modules must have the following properties:

- Each module must be placed in its own subdirectory in `modules`
- filename: `__init__.py`
- `name = <modulename>` (This is the resource identifier under /control_test/)
- minimum of two functions: `match` (criteria that request must match to execute module) and `run` (module execution)
- Only PUT requests to the module resource (/api/1/control_test/name) will be routed by the ccaf application to the module for `match`ing.

A sample is provided in: `modules/sample_module/__init__.py`.

You can test it with `curl -XPUT http://localhost:8300/api/1/control_test/sample_module`

