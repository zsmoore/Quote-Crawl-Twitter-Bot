# TweepyTest1.0
Getting familiar with Tweepy Library to use in other projects


Usage:

grabQuotes:
  input:  
    filename  
    tag to grab  
  
  Will grab every quote associated with that tag. Get the quote text.    
  Write to File specified with 'DELIM' between quotes for easy splitting.  
  
TweepyTest:  
  input:  
    auth_file with api keys  
    args for user reference  
    quote file to grab from  
         
  Will initialize api from auth_file.  
  Will grab random user from args file.  
  Will grab random quote from quote file.  
  Will Direct message a random quote to a random user.  
