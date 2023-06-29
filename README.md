# Real Time Action Detection Web App using YOWO Algorithm 
<p>This a repo for a real time action detection system. Through this web app anyone can detect what's happening at real time.The can detect through uploading video file or directly through Camera Also. This project uses YOWO Algorithm which the best algorithm till now because it is Fast & Accurate.</p>

#### See YOWO Algorithm Example :- 
<div>
  <img src='/examples/ava1.gif'>&nbsp; &nbsp; &nbsp;&nbsp;
  <img src='/examples/ava3.gif'>&nbsp; &nbsp; &nbsp;&nbsp;
  <img src='/examples/ava4.gif'>
</div>
<br>

#### See Web App Example :- 
<div style="display:flex;">
  <img src='/examples/frontpage.jpg' width=40%>&nbsp; &nbsp; &nbsp;&nbsp;
  <img src='/examples/dashboard.jpg' width="40%">&nbsp; &nbsp; &nbsp;&nbsp;
</div>


#### What we have used :-
<ol>
  <li><b>Flask, HTML, CSS, JS, BOOTSTRAP, Animated CSS</b> - For Frontend design</li>
  <li><b>SQLite, SQLAlchemy</b> - For database</li>
  <li><b>Python</b> - For Backend</li>
  <li><b>AVA Dataset</b> -  For dataset</li>
  <li><b>YOWO Algorithm</b> - For detection</li>
  <li><b>Docker</b> - For Deployment</li>
</ol>

## Installation

#### Clone this repo from the given Command 👇
```sh
$ git clone https://github.com/himanshu0072/Real-time-Action-Detection-using-YOWO
```
## Frontend - Setup 

#### Now Install the required libraries by the given command 👇
###### it will install all the library which is inside requirments.txt
```sh
$ pip install -r requirments.txt
```

Now you are able to run <b>app.py</b> and you can run it on localhost


## YOWO - Validating & Running


1. Install the required libraries which is imported inside of <b>test_video_ava.py file.</b><br>
2. Now install the torch with cuda enabled. You can visite official website of <a href="https://pytorch.org/" target="_blank">Pytorch</a> or use the following command 👇

```sh
$ pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```
<br>
3. All training configurations are given in <a href="https://github.com/himanshu0072/Real-time-Action-Detection-using-YOWO/blob/master/cfg/ava.yaml" target="_blank">ava.yaml</a><br>
4. Now to run and test the video in Yowo Algorithm use this command👇

```sh
$ python main.py --cfg cfg/ava.yaml
```

## Note :
This Project is using AVA Dataset. So to download the dataset and setup the file you can visit <a href="https://github.com/cvdfoundation/ava-dataset" target="_blank">AVA DATASET</a>

#### Team members:
<ul>
  <li>
    <a href="https://github.com/himanshu0072" target="_blank">Himanshu Prajapati</a></li>
  <li>
    <a href="https://github.com/aayushg2002" target="_blank">Ayush Gupta</a></li>
  <li>
     <a href="https://github.com/2002mayank" target="_blank">Mayank Patel</a>
  </li>
  </ul>
