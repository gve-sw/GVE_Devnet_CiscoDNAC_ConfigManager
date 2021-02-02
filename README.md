# GVE_Devnet_CiscoDNAC_ConfigManager

| :exclamation:  External repository notice   |
|:---------------------------|
| This repository is now mirrored at "PLEASE UPDATE HERE - add External repo URL after code review is completed"  Please inform a https://github.com/gve-sw/ organization admin of any changes to mirror them to the external repo |
## Contacts
* Eda Akturk 

## Solution Components
*  Python 3.8
*  Cisco DNA Center 
    - [API Documentation](https://developer.cisco.com/docs/dna-center/#!cisco-dna-2-1-2-x-api-overview)

## Solution Overview
The solution checks the configuration for devices in DNA Center and allows you to find specific configurations and 
search for keywords in the device configurations. 

## Installation/Configuration

#### Clone the repo :
```$ git clone (link)```

#### *(Optional) Create Virtual Environment :*
Initialize a virtual environment 

```virtualenv venv```

Activate the virtual env

*Windows*   ``` venv\Scripts\activate```

*Linux* ``` source venv/bin/activate```

#### Install the libraries :

```$ pip install -r requirements.txt```


## Setup: 

*DNA Center*
1. Add the DNA Center Lab credentials in env_var.py
```
DNAC_URL = " "
DNAC_USER = " "
DNAC_PASS = " "
```

## Usage

1. Search for certain part of configuration in devices:
```
DNACenterLab.get_device_config(dev["id"], keyword)
```
For example you can get the "service" configuration ot the "name-server" configuration by imputing them as the keywords 
to get_device_config. 


2. Search for keywords in configurations:

```
DNACenterLab.check_config(dev["id"], "1.1.1.1")
```
For example you can add an ip address to see if exists in the device configuration such as 1.1.1.1. 


# Screenshots
![/IMAGES/output.PNG](/IMAGES/output.PNG)


### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
