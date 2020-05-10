# kingsland university blockchain exercises
  
This REPO consist of several exercises.  MI01-Exercise 2 is documented below.
 
Build your own 
Blockchain 
 
MI01-Exercise 2
 
 
 	 




















  
 
 
www.kingslanduniversity.com	[updated 12 December 2018]
In this exercise, you will learn how Blockchain networks work by building a simple one in Python. Blockchain is an immutable, sequential chain of records called blocks. Blocks can hold transactions, documents, files or any data you like, really, but the important thing is that blocks are chained together using hashes. The blockchain networks consists of interconnected nodes which update the blocks together using a consensus algorithm (like proof-of-work).  
 
Original source: 
https://hackernoon.com/learn-blockchains-by-building-one-117428612f46. 
 
You will need Python 3.6+, Python IDE and HTTP client like Postman or cURL. Also, you will need to install the Flask and Requests Library for Python. 
 
1.	Install Python and Flask 
To install Python and all required libraries in Windows, use the steps below: 
 
1.	If you have installed Python, you can skip this step. If not, go to python website: https://www.python.org/downloads/ and download “Python 
3.6” (the x86 “executable installer” version). Then install it. 
 
2.	Choose the [Customize installation] link. 
  
3.	Check all the options and click [Next]. 
 
 
 
Check also the “Add Python to environment variables” (by default it is not checked) and click [Install]. 
  
4.	After completing open Command Line Interpreter and write the command: “python -V”. You should see the Python version. Note the capital “V”.
 
5.	Then install the “Flask” library using the command: 
pip install Flask==0.12.2 requests==2.18.4
 On GNU/Linux, you might have to use “pip3” instead.

2.	Install Postman 
We will need also Postman HTTP client as we mention it above. 
 
1.	Go to the official Postman web site: h ttps://www.getpostman.com, download and install Postman. 
  
 
2.	After installing it, you can sign up (it is free), or click “Take me straight to the app” at the bottom:
   
 
3.	After signing up you will see the following window. You can close the inner one. 
  
4.	Finally, you should see window like this one below: 
  
5.	Now we have all we need to start writing and testing the code. 
 
3.	Building Our Blockchain 
1.	Firstly, open your favorite text editor or Python IDE (e.g. PyCharm). 
2.	Create a new file, called “blockchain.py”.  
a.	If you are new to Python, remember to never mix tabs with spaces. 
b.	You may get errors like this “TabError: inconsistent use of tabs and spaces in indentation”. 
c.	Use 4 tabs for indenting code blocks. 
3.	We will create a Blockchain class whose constructor creates an initial empty list to store our blockchain, and another to store transactions. Here is how it will look like: 
  
4.	Let’s write some code so we can launch what we have so far, to see if it works. Note: those on the sides are two underscores each (double underscores).
 
If we open a command prompt now, navigate to the folder where we saved our blockchain.py file, and type python blockchain.py, we should see some output:
 
If instead you get an error message, check that you’ve typed everything correctly. 

5.	This is how a block looks like: 
  
 
Each Block has an index, a timestamp, a list of transactions, a proof and the hash of the previous Block. 
 
6.	Now we will define the method new_transaction() which will add new transactions to the block. Replace the code we currently have with:
  

After new_transaction() adds a transaction to the list, it returns the index of the block which the transaction will be added to: the next block to be mined. 
 
When our Blockchain is instantiated, we’ll need to seed it with a genesis block: a block with no predecessors. We’ll also need to add a “proof” to our genesis block which is the result of mining (or proof of work). 
 
  
 
7.	In addition to creating the genesis block in our constructor, we’ll also flesh out the methods for  
a.	new_block() 
b.	new_transaction() 
c.	hash() 
Now we will define the new_block() and hash() functions. 
 
8.	Firstly, we should import some libraries at the top of our file. 

  
9.	Then we will implement the new_block() function. 
  
10.	We now have blocks and we should implement last_block() function to be able to see the last block of our blockchain. 
  
 
11.	And the hash() function should look like this: 
  
 
12.	Let’s check if the code we have so far works. Change the if __name__ == “__main__” like this:
 
If everything went well, we should see two different hashes printed:
 
 
 
13.	Now the implementation of basic proof-of-work algorithm by adding the following methods to our Blockchain class: 
  
14.	Proof of work method has been implemented. Now we need a condition for validating the proof. To adjust the difficulty of the algorithm, we could modify the number of leading zeroes. But 4 is enough. You’ll find out that the addition of a single leading zero makes a huge difference to the time required to find a solution. 
  
15.	Let’s check if our “miner” is working. Change the bottom-most part of our program like this:
 
If everything went fine, the printed hash will now start with at least 4 zeroes:
 

 
 
Our class is almost complete, and we are ready to begin interacting with it using HTTP requests. 
 
4.	Exposing a Blockchain API 
We’re going to use the Python Flask Framework. It’s a micro-framework and it makes it easy to map endpoints to Python functions. This allows us talk to our Blockchain over the web using HTTP requests. 
 
We’ll create three API endpoints: 
●	/transactions/new – to create a new transaction to a block 
●	/mine – to tell our server to mine a new block. 
●	/chain – to return the full blockchain. 
 
Let’s set up the Flask framework. 
 
 
 
1.	We need the following new imports at the top: 
 
2.	Firstly, we instantiate our node. 
3.	Then create a random name for our node. 
4.	And instantiate the Blockchain class. 
  
5.	Create the /mine endpoint, which is a GET request. 
6.	Create the /transactions/new endpoint, which is a POST request, since we’ll be sending data to it. 
7.	Create the /chain endpoint, which returns the full blockchain.
8.	Run the server on port 5000. 
  
 
 Start the app from the command line, open a web browser, and navigate to http://localhost:5000/chain - if you see a JSON response, everything is fine.

9.	Next we will implement the new_transaction() endpoint: 
  
10.	It is time to implement the mine() function: 
  

(Re)start the application, and visit http://localhost:5000/mine - note it should take a while to open (if it’s still hard to notice, you might want to increase the difficulty, by changing the valid_proof() method to require more zeroes). Hit “refresh” a couple of times, and check if the index is increasing (meaning, new blocks are being added).
 
5.	Implementing a Consensus Algorithm 
So far, we've got a basic Blockchain that accepts transactions and allows us to mine new blocks. 
 
But the whole point of blockchains is that they should be decentralized. Now we’ll have to implement a Consensus Algorithm if we want more than one node in our network. 
1.	Each node on our network should keep a registry of other nodes on the network. Thus, we’ll need some more endpoints: 
a.	/nodes/register – to accept a list of new nodes in the form of 
URLs. 
b.	/nodes/resolve – to implement our Consensus Algorithm, which resolves any conflicts – to ensure a node has the correct chain. 
2.	We’ll need to modify our Blockchain’s constructor and provide a method for registering nodes: 
 
 
 
a.	We should add to the constructor (the __init__() method): 
 
b.	We should add another import: 
 
 
c.	 And add the register_node() method to our Blockchain class: 
  
 
3. We should import: 

  

We’ll make the rule that the longest valid chain is authoritative. In other words, the longest chain on the network is the de-facto one. Using this algorithm, we reach consensus amongst the nodes in our network. 
 
 
 
 
 
 
 
 
4.	The first method valid_chain() is responsible for checking if a chain is valid by looping through each block and verifying both the hash and the proof. 
 
 
5.	The method resolve_conflict() loops through all our neighboring nodes, downloads their chains and verifies them using the above method. 
a.	If a valid chain is found, whose length is bigger than ours, we replace our own chain with our neighbor’s chain. 
  
 
 
 
 
 
 
 
 
 
 
 
 
6.	Let’s register the two endpoints to our API, one for adding neighboring nodes and the another for resolving conflicts: 
a.	First the register_nodes() function (this connection is NOT bidirectional): 
  
b.	Then the consensus() function: 
 
 
7.	Finally, to be able to run several instances of the the app, you will need to change the part at the end of our code like this:
  

At this point you can grab a different machine if you like and spin up different nodes on your network. Or spin up processes using different ports on the same machine. 
●	It is easier to spin up another node on your machine, on a different port, and register it with your current node (using -p or --port switches and then the port number). 
●	Thus, you will have two nodes:  http://localhost:5000  and http://localhost:5001. 
 
6.	Interacting with our Blockchain 
1.	Now open command shell and go to your project file directory. 
2.	Start your first blockchain node: 
 
Run the command: 
python blockchain.py 
If everything is OK you will see the following result: 
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) 
   
 
 
3.	Now open Postman. 
4.	Let’s try mining a block by making a GET request to http://localhost:5000/mine. It should look like this:	 
  
5.	The result should be: 
  
6.	Let’s create a new transaction by making a POST request to http://localhost:5000/transactions/new with a body containing our transaction JSON structure: 
   
7.	The result should be: 
  
8.	Let’s inspect the full chain by requesting  http://localhost:5000/chain. 
  
9.	The result should be like this: 
  
 	 
 
10.	Register a new node: 
  
11.	Do not forget to run another node with port 5001 on your machine
12.	The result should be: 
  
13.	Finally resolve conflicts: 
  
 
14.	The result should be: 
  
 
15.	Let’s now send some commands to the second node (on port 5001):
    
16.	Ask it to check for a better chain: 
 
What to Submit? 
Create a zip file (e.g. your-name-own-blockchain-exercise.zip) holding the 
source code files like blockchain.py. 	 
Submit your zip file as homework at the course Web site.

** Notes

MI1OD: Blockchain Essentials - USA Self-paced Sept 2019
