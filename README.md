# Flex Alert And Monitoring Documentation

This repo contains Flex Alert And Monitoring Documentation as well as tools to parse and process alert information.

### Getting Started

To setup the development environment first grab the python-venv you need. These instructions may be different
for your setup but are geared for an Ubuntu20.04 install. 

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.10 python3.10-venv
```

After that, within this repo create the venv..

```bash
python3.10 -m venv venv
```
Activate the environment

```bash
source venv/bin/activate
```

Now install the requirements...

```bash
pip install -r requirements.txt
```

Now you can serve the documents and begin developing on them...

```bash
python -m mkdocs serve
```

These documents depend on alerting rule definitions that are pulled from external sources. 
We must collect Prometheus Alerting Rules files and unzip them to a directory we can reach.

Once we have our rules files we can then parse them into a markdown document...

### Parse Prometheus Alert Outputs to alerts.md file...

```bash
python python parse.py /path/to/alerts/dir -o docs/alerts.md
```

The `/path/to/alerts/dir` is a set of yaml rules files produced by Prometheus configurations. 
This can be one or many files and the output will be a markdown formatted file with information
related to the alerts that can be viewed in a table format as part of the documentaiton.

