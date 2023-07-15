#!/usr/bin/python3                   
                                     
                                     
import subprocess                    
import cgi                           
                                     
print("Content-type: html/text")     
print()                              
                                     
                                     
cmd="date"                           
                                     
output=subprocess.getoutput(cmd)     
                                     
print("<pre>"+ output + "</pre>" )   