rows = 10
space = 0
for i in range(1, rows): 
    print(" " * space, end = "")
    space += 1
    print("* " * (rows - i))

'''
Inverted Triangle

* * * * * * * * * 
 * * * * * * * * 
  * * * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * 
'''