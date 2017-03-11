# HackMerced 2017 Transition Site

This repository will store the transition website for HackMerced 2017F. It is written in Python with the Flask framewrork and will be used to server some basic files as well as enable a microservice to list jobs from our internal filesystem. This readme will be updated on the full uses of this website and how to use it.

[Website](http://hackmerced.com) |
[Sponsor Us!](http://hackmerced.com/sponsor)

## Installation

To run this website, you will need to have installed `python 2.7` or higher, `virtualenv`, and `npm` Once those programs have been installed, please enter the following:

1. Clone the respository
  ```bash
  $ git clone https://github.com/HackMerced/website-2017t.git
  ```

2. Establish your virtual environment
  ```bash
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

3. Install and build environment
  ```bash
  $ npm run setup
  ```

4. Run server
  To start the webserver type the following:
  ```bash
  $ npm start
  ```

  The website should run on [localhost:5000](http://localhost:5000)

5. Cleanup
  Remember to deactivate your virtual environment when you are done
  ```bash
  $ deactivate
  ```


## Development
There are no additional requirements for running a development instance of this website. For your sanity, we use `gulp` to compile our watch and compile our static data.

  ```bash
  $ npm run gulp
  ```
