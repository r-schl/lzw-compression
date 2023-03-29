# Lempel–Ziv–Welch compression

### Overview

This is a simple console application that takes text as an argument and applies the LZW compression algorithm to it. It provides detailed information about the steps taken and the compression rate of the result. 

### Example interaction

```
python lzw.py mississippi
```
```
 LAST WORD    CURRENT CHAR    COMMENT                          ENTRIES      OUTPUT 
              m               pattern (last+curr) found                                  
 m            i               pattern (last+curr) not found    256 = mi     m       
 i            s               pattern (last+curr) not found    257 = is     i      
 s            s               pattern (last+curr) not found    258 = ss     s
 s            i               pattern (last+curr) not found    259 = si     s
 i            s               pattern (last+curr) found                            
 is           s               pattern (last+curr) not found    260 = iss    <257>   
 s            i               pattern (last+curr) found                
 si           p               pattern (last+curr) not found    261 = sip    <259>   
 p            p               pattern (last+curr) not found    262 = pp     p   
 p            i               pattern (last+curr) not found    263 = pi     p  
 i                                                                          i     
 
 input               mississippi    
 output              miss<257><259>ppi    
 storage             81.81818181818183%  
 compression rate    1.2222222222222223  
```

