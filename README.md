# CFBRecruits Module (In Progress - Please check back often for final product!)

*Making NCAA football recruiting data as easily accessible as possible*

## Table of Contents

1. Introduction
2. Installation

### 1. Introduction

The CFBRecruits module was created to gain access to NCAA football recruit data without having to pay for 3rd party API access (which is often sparse, inconsistent, or simply non-existant). Currently, the two largest websites tracking college football recruits are 247sports.com and Rivals.com. Each website ranks both overall university recruiting classes and individual recruits on a state- and nation-wide basis. The CFBRecruits module utilizes Selenium 2.0 to effecitively navigate ever-"shifting" DOM elements to deliver that data to your machine in a readable and easily iterable fashion.

**Currently, the CFBRecruits module will return the following data from both websites:**

1) Complete university recruiting class data by year
2) Average university recruit rating by year
3) The Top 50 recruiting classes by university, by year

### 2. Installation

The CFBRecruit module relies heavily on Selenium 2.0, and specifically Selenium's Google Chrome WebDriver. Later in these instructions we'll touch on all aspects of WebDrivers, but for now, you'll want to start by simply installing Selenium on your machine. (***NOTE:*** *While I'll cover the high-level specifics below, please be sure to brush on [Selenium's documentation!](https://selenium-python.readthedocs.io/installation.html)*)

