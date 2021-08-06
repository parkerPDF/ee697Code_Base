# ee697Code_Base

submit_Files contains example files for how to submit any of the main_Worker_Files to have them run in parallel. The submit_Files are specific to CHTC and if you actually
  want to submit the main_Worker_Files to a server you'll likely need to change these to whatever you have access to uses.
  
main_Worker_Files contains all of the different ways that we've solved the ridge regression problem. Any of these are viable to submit and will solve a single memory parameter,
  lambda value, and CV fold per job submitted. They'll return MSE or the MSE per channel.

display_Results will take a file location and display the results. It's important to use No_Channel and Channel correctly. Some of the main_Worker_Files will output channel by
  channel MSE data, and some will output only subject wide data.
  normY.py and normY_hold_Hannel.py will output channel by channel data
  
The On_Computer files that are not in a folder are files that you can run and get results for on your local machine in a jupyter notebook.

Right away you'll only be able to run simulated_On_Computer as this is the only one that uses simulated data. It has a AR3 model and you can change the length (amount) of the data.
simulated_On_Computer has toggels for showing graphs for every channel and a toggel variable to choose between using the norm of Y or the length of Y in the regularization parameter.
