# DelDash : Intelligent Deliveries Dashboard and analytics accelerator for Healthcare Providers

DelDash during its ideation and initial development  phase(in the GE Healthcare Hackathon)was envisioned as a layer over a traditional EMR that would help clinicians to prepare for child delivery better. <br>
### Features:
1. Frequency domain analysis of labor onset.
2. Prediction of True or False Labor Pain.
3. Recommendation of the administration of antenatal corticosteroid dosage.
4. Comparative analysis of vital parameter trends between two subjects.
5. Timeline: Provides a timeline of the change in trends of vitals over the days.[enhancement needed]
6. NTSV-C sections: keeps a record of the performance of the institute based on the NTSV-C sections.[enhancement needed]

NOTE: last page is a dummy page for an additional feature to be added which is under research.

### TODO:
- [ ] Make a light weight EMR to test DelDash
- [ ] Testing on EMR
- [ ] Make a wiki including roadmap
- [x] Add under a single organization
- [ ] Add incomplete functionalities(as mentioned in wiki)

### Contribution Guidelines
#### Why Contribute?
DelDash is an award winning idea prototype and we are constantly working to take it to production. You can contribute to be a part of this voluntarily. You may contribute for learning or if you are serious for this you can become the maintainer of this project and take part in decision making process of its future with us. Also, if you are a beginner and trying out with open source software development, its a great starting point!

#### How to Contribute:
##### 1. Setup development environment:
We assume you have python 3.0+ installed. <br>
1. Create a python virtual environment: <br>
  * `pip install virtualenv`<br>
  Then create a directory where you can keep all your virtual environments.(like venvs)
  then `cd` to that directory and:
  * `virtualenv deldash` : this will be your virtual enviroment for all DelDash related packages.
  * activate virtual environment:<br>
  `source deldash/bin/activate` : this will only work if you are in venvs directory.

##### 2. Setup DelDash
  * `git clone git@github.com:ShaswatLenka/DelDash.git`
  * `cd ` to the cloned repository
  * run `pip install requirements.txt`<br>
  NOTE: **activate** your virtual environment before this so that it gets installed in that environment.
  * run `python3 index.py` and DelDash will run in your browser locally.

![labor](https://github.com/ShaswatLenka/DelDash/blob/master/images/1.png)
![vitals](https://github.com/ShaswatLenka/DelDash/blob/master/images/2.png)
![timeline](https://github.com/ShaswatLenka/DelDash/blob/master/images/3.png)
![NTSV](https://github.com/ShaswatLenka/DelDash/blob/master/images/4.png)
![Performance](https://github.com/ShaswatLenka/DelDash/blob/master/images/5.png)
